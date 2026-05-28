#!/usr/bin/env python3
"""
Extract questions and answers from CBSE Class 12 Mathematics PDFs.
Reads pre-extracted text from /tmp/pdf_texts.json and outputs structured JSON.

Handles multiple paper formats:
  - 2015-2019: Interleaved Q + Sol./Ans. in older section structure (A/B/C or A/B/C/D)
  - 2020:      Interleaved Ans. with MCQ options in section A
  - 2022 T1:   All MCQ, interleaved Sol. immediately after each question
  - 2022 T2:   Interleaved Ans., sections A (2mk) / B (3mk) / C (4mk)
  - 2023-2025: Separate questions block + ANSWERS block, multi-set papers
"""

import json
import re
import os
import sys
from collections import defaultdict
from pathlib import Path


# ─── Chapter classification ─────────────────────────────────────────────────────

CHAPTER_KEYWORDS = {
    "Relations and Functions": [
        "injective", "surjective", "bijective", "one-one", "onto",
        "reflexive relation", "symmetric relation", "transitive",
        "equivalence relation", "domain", "range", "codomain",
        "composite function", "many-one", "into function",
        r"\brelation\b", r"\bfunction\b", "f : ", "f:",
    ],
    "Inverse Trigonometric Functions": [
        "sin-1", "cos-1", "tan-1", "sin-1", "cos-1", "tan-1",
        "sin-1", "cos-1", "tan-1",
        "arcsin", "arccos", "arctan",
        "inverse trigonometric", "principal value",
    ],
    "Matrices": [
        r"\bmatri[cx]\b", r"\bmatrices\b",
        "transpose", "symmetric matrix", "skew-symmetric", "skew symmetric",
        r"order \d+\s*[x]\s*\d+",
        "identity matrix", "null matrix", "zero matrix",
    ],
    "Determinants": [
        r"\bdeterminant\b", r"\|A\|", r"\|adj",
        "cofactor", "adjoint", "singular matrix", "non-singular",
        "|adj A|", "adj A",
        r"det\s*[\(\|]",
    ],
    "Continuity and Differentiability": [
        r"\bcontinuous\b", r"\bcontinuity\b",
        r"\bdifferentiable\b", r"\bdifferentiability\b",
        "rolle's theorem", "mean value theorem", "lagrange",
        "dy/dx", "d2y",
        "implicit differentiation", "logarithmic differentiation",
    ],
    "Application of Derivatives": [
        r"\bincreasing\b", r"\bdecreasing\b",
        r"\bmaxima\b", r"\bminima\b", r"\bmaximum\b", r"\bminimum\b",
        r"\btangent\b", r"\bnormal to\b",
        "rate of change", r"\bslope\b",
        "optimiz", "stationary point", "critical point",
        "local maximum", "local minimum", "absolute maximum",
        "point of inflection",
    ],
    "Integrals": [
        r"\bintegral\b", r"\bintegrate\b", r"\bintegration\b",
        "antiderivative", "area under",
        "definite integral", "indefinite integral",
        "by parts", "partial fractions",
    ],
    "Differential Equations": [
        "differential equation",
        "d2y", "dy/dx",
        "general solution", "particular solution",
        "variable separable", "homogeneous equation",
        "linear differential", "integrating factor",
    ],
    "Vector Algebra": [
        r"\bvector\b", r"\bvectors\b",
        "scalar product", "cross product", "dot product",
        r"\bcollinear\b", r"\bcoplanar\b",
        "unit vector", "position vector", "magnitude of",
        "scalar triple product", "vector triple product",
    ],
    "Three Dimensional Geometry": [
        "direction cosines", "direction ratios",
        "distance from", "three dimensional", "3-d geometry",
        "equation of plane", "equation of line",
        "skew lines", "shortest distance", "perpendicular distance",
    ],
    "Linear Programming": [
        "linear programming", "objective function",
        r"\bconstraint\b", r"\bfeasible\b",
        "corner point", "feasible region",
        r"\bmaximize\b", r"\bminimize\b",
        "lpp", "optimal solution",
    ],
    "Probability": [
        r"\bprobability\b", r"\bbayes\b",
        r"\bconditional\b", "random variable",
        r"\bP\(", r"\bevent\b", "independent events", "mutually exclusive",
        "binomial distribution",
        "sample space",
    ],
}


def classify_chapter(text):
    text_lower = text.lower()
    scores = defaultdict(int)
    for chapter, patterns in CHAPTER_KEYWORDS.items():
        for pattern in patterns:
            try:
                if re.search(pattern, text_lower, re.IGNORECASE):
                    scores[chapter] += 1
            except re.error:
                if pattern.lower() in text_lower:
                    scores[chapter] += 1
    if not scores:
        return "General"
    return max(scores, key=lambda c: (scores[c], list(CHAPTER_KEYWORDS.keys()).index(c)))


# ─── Year extraction ────────────────────────────────────────────────────────────

def extract_year(filename):
    """Return year label. Check 'Term II' BEFORE 'Term I' to avoid substring match."""
    if "2022" in filename:
        name_lower = filename.lower()
        if "term ii" in name_lower:
            return "2022-T2"
        if "term i" in name_lower:
            return "2022-T1"
    m = re.search(r"(20\d{2})", filename)
    if m:
        return int(m.group(1))
    return 0


def year_to_int(year):
    if isinstance(year, int):
        return year
    return int(str(year)[:4])


# ─── Section metadata ──────────────────────────────────────────────────────────

def get_section_meta(section_letter, year):
    yr = year_to_int(year)
    year_str = str(year)
    s = section_letter.upper()
    if "T2" in year_str:
        return {"A": (2, "SA"), "B": (3, "SA"), "C": (4, "LA")}.get(s, (2, "SA"))
    if "T1" in year_str:
        return (1, "MCQ")
    if yr >= 2021:
        return {"A": (1, "MCQ"), "B": (2, "VSA"), "C": (3, "SA"),
                "D": (5, "LA"), "E": (4, "Case Study")}.get(s, (1, "General"))
    if yr == 2020:
        return {"A": (1, "MCQ"), "B": (2, "VSA"), "C": (4, "SA"), "D": (6, "LA")}.get(s, (1, "General"))
    # 2015-2019
    return {"A": (1, "VSA"), "B": (4, "LA-I"), "C": (6, "LA-II"), "D": (6, "LA-II")}.get(s, (1, "General"))


# ─── Text cleaning ─────────────────────────────────────────────────────────────

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'/[a-z]+nosp', '', text)
    text = re.sub(r'/arrowleftnosp|/arrowrightnosp|/combarrowextender', '', text)
    text = re.sub(r'/circumflexnosp', '^', text)
    text = re.sub(r'/g\d+', '', text)
    text = re.sub(r'Oswaal CBSE[^\n]*\n?', '', text)
    text = re.sub(r'OSWAAL CBSE[^\n]*\n?', '', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# ─── MCQ option parsing ─────────────────────────────────────────────────────────

def parse_options(text):
    options = {}
    pattern = re.compile(
        r'\(([aAbBcCdD])\)\s*([^\n(]+?)(?=\s*\([aAbBcCdD]\)|\s*Sol\.|\s*Ans\.|\n\s*\d+\.|\s*$)',
        re.DOTALL
    )
    matches = pattern.findall(text)
    if len(matches) >= 2:
        for letter, val in matches:
            clean = val.strip().rstrip(',;').strip()
            if clean:
                options[letter.lower()] = clean
        if len(options) >= 2:
            return options
    # line-by-line fallback
    lines = text.split('\n')
    current, current_val = None, []
    for line in lines:
        stripped = line.strip()
        m = re.match(r'^\(([aAbBcCdD])\)\s*(.*)', stripped)
        if m:
            if current is not None:
                v = ' '.join(current_val).strip()
                if v:
                    options[current] = v
            current = m.group(1).lower()
            current_val = [m.group(2).strip()]
        elif current is not None and stripped and not re.match(r'^\d+\.', stripped):
            current_val.append(stripped)
    if current is not None:
        v = ' '.join(current_val).strip()
        if v:
            options[current] = v
    return options


def remove_option_lines(text):
    lines = text.split('\n')
    result = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if re.match(r'^\([aAbBcCdD]\)', stripped):
            skip = True
        elif skip and not re.match(r'^\([aAbBcCdD]\)', stripped):
            skip = False
            result.append(line)
        else:
            result.append(line)
    return '\n'.join(result).strip()


# ─── Q + Sol split ─────────────────────────────────────────────────────────────

_SOL_RE = re.compile(r'\n\s*(?:Sol\.|Ans\.|Solution\s*:|Answer\s*:)', re.IGNORECASE)


def split_q_sol(block):
    m = _SOL_RE.search(block)
    if m:
        return block[:m.start()].strip(), block[m.start():].strip()
    return block.strip(), ""


# ─── Question-number pattern ───────────────────────────────────────────────────

# Match ' 1. ' or '  12. ' at line start followed by word char or '('
# The lookahead avoids matching standalone digit references in equations
_Q_NUM_RE = re.compile(r'(?:^|\n)\s{0,4}\*?\s*(\d{1,2})\. +(?=[A-Za-z\(])', re.MULTILINE)


def parse_section_block(sec_text, section, marks, qtype):
    questions = []
    matches = list(_Q_NUM_RE.finditer(sec_text))
    if not matches:
        return questions

    for i, match in enumerate(matches):
        q_num = int(match.group(1))
        if q_num > 60:
            continue
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(sec_text)
        block = sec_text[start:end].strip()
        block_body = re.sub(r'^\s*\*?\s*\d{1,2}\.\s*', '', block, count=1).strip()

        q_text, sol_text = split_q_sol(block_body)
        q_text = clean_text(q_text)
        sol_text = clean_text(sol_text)

        if len(q_text) < 8:
            continue

        options = {}
        if marks == 1 or qtype == "MCQ":
            options = parse_options(q_text)
            if options:
                q_text = remove_option_lines(q_text)

        questions.append({
            "question_number": q_num,
            "question": q_text,
            "options": options,
            "answer": sol_text,
            "section": section,
            "marks": marks,
            "type": qtype,
        })
    return questions


# ─── Section finding ───────────────────────────────────────────────────────────

def find_sections(text, min_pos=0):
    pat = re.compile(
        r'(?:^|\n)\s*(?:SECTION|SeCTIon|Section)\s*[-]*\s*([A-Ea-e])\b',
        re.MULTILINE
    )
    return [(m.start(), m.group(1).upper()) for m in pat.finditer(text, min_pos)]


# ─── Answers-block parser ──────────────────────────────────────────────────────

def parse_answers_block(ans_text):
    answers = {}
    pat = re.compile(
        r'(?:^|\n)\s*(\d{1,2})\.\s+(.+?)(?=(?:\n\s*\d{1,2}\.\s)|$)',
        re.DOTALL
    )
    for m in pat.finditer(ans_text):
        q_num = m.group(1)
        body = clean_text(m.group(2))
        if len(body) > 3:
            if q_num not in answers or len(body) > len(answers[q_num]):
                answers[q_num] = body
    return answers


# ─── Detect preamble end ──────────────────────────────────────────────────────

def find_preamble_end(text):
    m = re.search(r'(?:Delhi|Outside\s+Delhi)\s+Set', text)
    if m:
        return m.start()
    m = re.search(r'Code\s+No\s*[:.]?\s*\d', text)
    if m:
        return m.start()
    m = re.search(r'Series\s*:\s*\S+\s+\d+/\d+/\d+', text)
    if m:
        return m.start()
    return min(800, len(text) // 4)


# ─── Multi-set paper parser (2023, 2024, 2025) ─────────────────────────────────

def parse_multiset_paper(text, year):
    """Parse papers with separate Q blocks and ANSWERS blocks (multiple sets)."""
    ans_m = re.search(r'\n[^\n]*?ANSWERS\n', text)
    if ans_m:
        q_portion = text[:ans_m.start()]
        a_portion = text[ans_m.start():]
    else:
        q_portion = text
        a_portion = ""

    preamble_end = find_preamble_end(q_portion)
    sections = find_sections(q_portion, preamble_end)

    all_qs = []
    for i, (sec_pos, sec_letter) in enumerate(sections):
        sec_end = sections[i + 1][0] if i + 1 < len(sections) else len(q_portion)
        sec_text = q_portion[sec_pos:sec_end]
        marks, qtype = get_section_meta(sec_letter, year)
        if "multiple choice" in sec_text[:300].lower():
            qtype = "MCQ"
            marks = 1
        parsed = parse_section_block(sec_text, sec_letter, marks, qtype)
        all_qs.extend(parsed)

    answers_by_num = {}
    if a_portion:
        a_sections = find_sections(a_portion, 0)
        for i, (sec_pos, sec_letter) in enumerate(a_sections):
            sec_end = a_sections[i + 1][0] if i + 1 < len(a_sections) else len(a_portion)
            sec_ans_text = a_portion[sec_pos:sec_end]
            sec_answers = parse_answers_block(sec_ans_text)
            for num, ans in sec_answers.items():
                if num not in answers_by_num or len(ans) > len(answers_by_num[num]):
                    answers_by_num[num] = ans

    # Dedup questions (multiple sets may repeat same Q numbers)
    best_qs = {}
    for q in all_qs:
        k = q["question_number"]
        score = len(q["question"]) + len(q["answer"])
        if k not in best_qs or score > (len(best_qs[k]["question"]) + len(best_qs[k]["answer"])):
            best_qs[k] = q

    result = []
    for q_num, q in sorted(best_qs.items()):
        key = str(q_num)
        if key in answers_by_num:
            if not q["answer"] or len(answers_by_num[key]) > len(q["answer"]):
                q["answer"] = answers_by_num[key]
        result.append(q)
    return result


# ─── Interleaved Q+A parser (2015-2022) ───────────────────────────────────────

def parse_interleaved_paper(text, year):
    """Parse papers where each question is immediately followed by its Sol./Ans."""
    preamble_end = find_preamble_end(text)
    sections = find_sections(text, preamble_end)
    if not sections:
        return []

    all_qs = []
    for i, (sec_pos, sec_letter) in enumerate(sections):
        sec_end = sections[i + 1][0] if i + 1 < len(sections) else len(text)
        sec_text = text[sec_pos:sec_end]
        marks, qtype = get_section_meta(sec_letter, year)
        if "multiple choice" in sec_text[:300].lower():
            qtype = "MCQ"
            marks = 1
        parsed = parse_section_block(sec_text, sec_letter, marks, qtype)
        all_qs.extend(parsed)

    # Dedup by (section, question_number)
    best = {}
    for q in all_qs:
        k = (q["section"], q["question_number"])
        score = len(q["question"]) + len(q["answer"])
        if k not in best or score > (len(best[k]["question"]) + len(best[k]["answer"])):
            best[k] = q
    return list(best.values())


# ─── Top-level paper dispatcher ────────────────────────────────────────────────

def parse_paper(filename, raw_text):
    year = extract_year(filename)
    text = clean_text(raw_text)
    yr_int = year_to_int(year)

    if yr_int >= 2023:
        questions = parse_multiset_paper(text, year)
    else:
        questions = parse_interleaved_paper(text, year)

    result = []
    for q in questions:
        q["year"] = year
        q["chapter"] = classify_chapter(q["question"] + " " + q["answer"])
        q["id"] = f"{year}_{q['question_number']}"
        result.append(q)
    return result


# ─── Global deduplication ──────────────────────────────────────────────────────

def deduplicate_global(questions):
    seen = {}
    for q in questions:
        qid = q["id"]
        score = len(q["question"]) + len(q["answer"])
        if qid not in seen or score > (len(seen[qid]["question"]) + len(seen[qid]["answer"])):
            seen[qid] = q
    return list(seen.values())


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    input_path = "/tmp/pdf_texts.json"
    output_dir = Path("/home/user/Maths-PYQs/public/data")
    output_path = output_dir / "pyqs.json"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {input_path}...")
    with open(input_path, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)
    print(f"Found {len(pdf_texts)} papers.\n")

    all_questions = []
    stats_by_year = defaultdict(int)
    parse_errors = []

    for filename, raw_text in sorted(pdf_texts.items()):
        year = extract_year(filename)
        print(f"Processing: {filename}  (year={year}, chars={len(raw_text)})")
        try:
            questions = parse_paper(filename, raw_text)
            print(f"  -> {len(questions)} questions")
            stats_by_year[year] += len(questions)
            all_questions.extend(questions)
        except Exception as exc:
            import traceback
            msg = f"{filename}: {exc}"
            print(f"  ERROR: {exc}", file=sys.stderr)
            parse_errors.append(msg)
            traceback.print_exc()

    before = len(all_questions)
    all_questions = deduplicate_global(all_questions)
    after = len(all_questions)
    if before != after:
        print(f"\nDeduplication: {before} -> {after} questions")

    all_questions.sort(key=lambda q: (str(q["year"]), q["question_number"]))

    output = [
        {
            "id": q["id"],
            "year": q["year"],
            "question_number": q["question_number"],
            "question": q["question"],
            "options": q["options"],
            "answer": q["answer"],
            "section": q["section"],
            "marks": q["marks"],
            "chapter": q["chapter"],
            "type": q["type"],
        }
        for q in all_questions
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"OUTPUT: {output_path}")
    print(f"{'='*60}")
    print(f"\nTOTAL QUESTIONS EXTRACTED: {len(output)}")

    print("\nQuestions per year:")
    for yr in sorted(stats_by_year.keys(), key=lambda y: str(y)):
        print(f"  {yr}: {stats_by_year[yr]}")

    chapter_stats = defaultdict(int)
    for q in output:
        chapter_stats[q["chapter"]] += 1
    print("\nQuestions per chapter:")
    for ch, cnt in sorted(chapter_stats.items(), key=lambda x: -x[1]):
        print(f"  {ch}: {cnt}")

    type_stats = defaultdict(int)
    for q in output:
        type_stats[q["type"]] += 1
    print("\nQuestions by type:")
    for t, cnt in sorted(type_stats.items()):
        print(f"  {t}: {cnt}")

    with_answer = sum(1 for q in output if q["answer"])
    pct = (100 * with_answer // len(output)) if output else 0
    print(f"\nAnswer coverage: {with_answer}/{len(output)} ({pct}%)")

    if parse_errors:
        print(f"\nParsing issues ({len(parse_errors)}):")
        for e in parse_errors:
            print(f"  - {e}")
    else:
        print("\nNo parsing errors.")

    print(f"\nDone. JSON written to {output_path}")
    return output


if __name__ == "__main__":
    main()
