#!/usr/bin/env python3
"""
Extract CBSE Class 12 Maths questions from PDFs using two-column layout detection.
Produces clean questions with proper Unicode math symbols.
"""
import fitz, re, json
from collections import defaultdict

PDF_DIR = "/tmp/pyqs_source/PYQs"
OUTPUT = "public/data/pyqs.json"

YEAR_MAP = {
    "Solved Paper 2015.pdf": 2015,
    "Solved Paper 2016.pdf": 2016,
    "Solved Paper 2017.pdf": 2017,
    "Solved Paper 2018.pdf": 2018,
    "Solved Paper 2019.pdf": 2019,
    "Solved Paper 2020.pdf": 2020,
    "Solved Paper 2022 Term I.pdf": "2022-T1",
    "Solved Paper 2022 Term II.pdf": "2022-T2",
    "Solved Paper 2023.pdf": 2023,
    "CBSE Math-12 Solved Paper 2024.pdf": 2024,
    "Math-2025.pdf": 2025,
}

# Section info by year
SECTION_INFO = {
    # year: {section: (type, marks)}
    2015: {"A": ("MCQ",1), "B": ("VSA",1), "C": ("SA",4), "D": ("LA",6)},
    2016: {"A": ("MCQ",1), "B": ("VSA",1), "C": ("SA",4), "D": ("LA",6)},
    2017: {"A": ("MCQ",1), "B": ("VSA",1), "C": ("SA",4), "D": ("LA",6)},
    2018: {"A": ("MCQ",1), "B": ("VSA",1), "C": ("SA",4), "D": ("LA",6)},
    2019: {"A": ("MCQ",1), "B": ("VSA",1), "C": ("SA",4), "D": ("LA",6)},
    2020: {"A": ("MCQ",1), "B": ("VSA",1), "C": ("SA",4), "D": ("LA",6)},
    "2022-T1": {"A": ("MCQ",1), "B": ("VSA",2), "C": ("SA",3)},
    "2022-T2": {"A": ("MCQ",1), "B": ("VSA",2), "C": ("SA",3), "D": ("LA",5)},
    2023: {"A": ("MCQ",1), "B": ("VSA",2), "C": ("SA",3), "D": ("LA",5), "E": ("Case Study",4)},
    2024: {"A": ("MCQ",1), "B": ("VSA",2), "C": ("SA",3), "D": ("LA",5), "E": ("Case Study",4)},
    2025: {"A": ("MCQ",1), "B": ("VSA",2), "C": ("SA",3), "D": ("LA",5), "E": ("Case Study",4)},
}

# Section question ranges by year
SECTION_RANGES = {
    2015: {"A": (1,10), "B": (11,15), "C": (16,29), "D": (26,29)},
    2016: {"A": (1,10), "B": (11,15), "C": (16,25), "D": (26,29)},
    2017: {"A": (1,6), "B": (7,14), "C": (15,22), "D": (23,29)},
    2018: {"A": (1,6), "B": (7,14), "C": (15,22), "D": (23,29)},
    2019: {"A": (1,4), "B": (5,12), "C": (13,22), "D": (23,29)},
    2020: {"A": (1,10), "B": (11,15), "C": (16,22), "D": (23,29)},
    "2022-T1": {"A": (1,50), "B": (1,50), "C": (1,50)},
    "2022-T2": {"A": (1,20), "B": (21,25), "C": (26,31), "D": (32,38)},
    2023: {"A": (1,20), "B": (21,25), "C": (26,31), "D": (32,35), "E": (36,38)},
    2024: {"A": (1,20), "B": (21,25), "C": (26,31), "D": (32,35), "E": (36,38)},
    2025: {"A": (1,20), "B": (21,25), "C": (26,31), "D": (32,35), "E": (36,38)},
}

CHAPTER_KEYWORDS = {
    "Relations and Functions": [
        "reflexive","symmetric","transitive","equivalence","bijective","onto","one.one",
        "surjective","injective","domain","range","codomain","relation","f\\(x\\)","gof","fog",
        "one-to-one","many-one","into","invertible","composition"
    ],
    "Inverse Trigonometric Functions": [
        "sin.1","cos.1","tan.1","cot.1","sec.1","cosec.1","principal value",
        "inverse trig","sin-1","cos-1","tan-1","arcsin","arccos","arctan","⁻¹"
    ],
    "Matrices": [
        "matrix","matrices","order.*×","symmetric matrix","skew.symmetric",
        "transpose","identity matrix","diagonal matrix","zero matrix","A\\^2",
        "AB","BA","scalar matrix","row matrix","column matrix"
    ],
    "Determinants": [
        "determinant","det\\(","\\|A\\|","singular","non-singular","adj",
        "cofactor","minor","cramer","inverse.*matrix","A.1","rank",
        "system of equations"
    ],
    "Continuity and Differentiability": [
        "continuous","continuity","differentiable","differentiability",
        "rolle","mean value","lagrange","dy.dx","d.2.y","differentiate",
        "chain rule","implicit","parametric","logarithmic differentiation"
    ],
    "Application of Derivatives": [
        "increasing","decreasing","monotonic","tangent","normal","maxima","minima",
        "maximum","minimum","rate of change","approximation","error",
        "local max","local min","absolute max","stationary","critical"
    ],
    "Integrals": [
        "integrate","integration","∫","dx","antiderivative","indefinite",
        "definite integral","partial fraction","by parts","substitution",
        "∫.*dx","properties of integral"
    ],
    "Application of Integrals": [
        "area.*bounded","bounded.*area","area.*curve","area.*region",
        "area.*parabola","area.*ellipse","area.*circle","area.*line",
        "enclosed","region bounded"
    ],
    "Differential Equations": [
        "differential equation","order.*degree","degree.*order",
        "integrating factor","linear.*D\\.E","homogeneous","variable.*separable",
        "general solution","particular solution","d.y.*dx","dy/dx.*=",
        "slope of curve"
    ],
    "Vector Algebra": [
        "vector","position vector","unit vector","magnitude.*vector",
        "dot product","cross product","scalar product","vector product",
        "collinear.*vector","î","ĵ","k̂","i\\^","j\\^","k\\^",
        "a⃗","b⃗","a→","b→"
    ],
    "Three-Dimensional Geometry": [
        "direction cosine","direction ratio","plane","3d","three.dimension",
        "line.*space","foot of perpendicular","angle.*plane","angle.*line",
        "distance.*point.*plane","cartesian.*line","vector.*line",
        "shortest distance","skew lines"
    ],
    "Linear Programming": [
        "linear programming","lpp","l\\.p\\.p","maximise","minimise",
        "maximize","minimize","feasible region","corner point","objective function",
        "constraints","optimal","graphically"
    ],
    "Probability": [
        "probability","p\\(a\\)","p\\(b\\)","bayes","conditional",
        "random variable","binomial distribution","mean.*distribution",
        "variance.*distribution","independent event","mutually exclusive",
        "sample space","expected value"
    ],
}

def extract_page_text(page):
    """Extract text from page using two-column layout detection."""
    rect = page.rect
    mid = rect.width / 2

    words = page.get_text("words")
    if not words:
        return ""

    left_words = [(w[0], w[1], w[4]) for w in words if w[0] < mid - 10]
    right_words = [(w[0], w[1], w[4]) for w in words if w[0] >= mid - 10]

    def words_to_text(wlist):
        ld = defaultdict(list)
        for x, y, word in wlist:
            ld[round(y / 4) * 4].append((x, word))
        lines = []
        for y in sorted(ld.keys()):
            line = ' '.join(w for _, w in sorted(ld[y]))
            lines.append(line)
        return '\n'.join(lines)

    left_text = words_to_text(left_words)
    right_text = words_to_text(right_words)

    # Combine: left column then right column
    return left_text + "\n" + right_text


def extract_pdf_text(pdf_path):
    """Extract full text from PDF page by page."""
    doc = fitz.open(pdf_path)
    pages_text = []
    for i in range(len(doc)):
        text = extract_page_text(doc[i])
        pages_text.append(text)
    return '\n'.join(pages_text)


def clean_math(text):
    """Clean up common PDF math extraction artifacts."""
    if not text:
        return text

    # Fix superscripts from "x2" patterns (number after variable)
    # x2 -> x², x3 -> x³, x4 -> x⁴ (only when followed by space/operator/end)
    text = re.sub(r'([a-zA-Z])2([^x\d])', lambda m: m.group(1)+'²'+m.group(2), text)
    text = re.sub(r'([a-zA-Z])3([^x\d])', lambda m: m.group(1)+'³'+m.group(2), text)
    text = re.sub(r'([a-zA-Z])4([^x\d])', lambda m: m.group(1)+'⁴'+m.group(2), text)

    # Fix "x2x" pattern -> x^(2x) - skip, too ambiguous

    # Clean vector notation
    text = re.sub(r'\ba→\b', 'a⃗', text)
    text = re.sub(r'\bb→\b', 'b⃗', text)
    text = re.sub(r'\bc→\b', 'c⃗', text)
    text = re.sub(r'\br→\b', 'r⃗', text)
    text = re.sub(r'\bp→\b', 'p⃗', text)
    text = re.sub(r'\bi\^\b', 'î', text)
    text = re.sub(r'\bj\^\b', 'ĵ', text)
    text = re.sub(r'\bk\^\b', 'k̂', text)

    # Fix common symbol replacements
    text = text.replace('–', '-').replace('—', '-')
    text = text.replace('⇒', '⟹')
    text = re.sub(r'(?<![=<>])=>(?!=)', '⟹', text)
    text = text.replace('∀', '∀')

    # Fix inverse trig
    text = re.sub(r'\bsin-1\b', 'sin⁻¹', text)
    text = re.sub(r'\bcos-1\b', 'cos⁻¹', text)
    text = re.sub(r'\btan-1\b', 'tan⁻¹', text)
    text = re.sub(r'\bcot-1\b', 'cot⁻¹', text)
    text = re.sub(r'\bsec-1\b', 'sec⁻¹', text)
    text = re.sub(r'\bcosec-1\b', 'cosec⁻¹', text)
    text = re.sub(r'\bsin\^[\(-]1[\)]?\b', 'sin⁻¹', text)
    text = re.sub(r'\bcos\^[\(-]1[\)]?\b', 'cos⁻¹', text)
    text = re.sub(r'\btan\^[\(-]1[\)]?\b', 'tan⁻¹', text)

    # Clean up excessive whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()

    return text


def classify_chapter(text):
    """Classify question into a chapter using keyword scoring."""
    text_lower = text.lower()
    scores = {}
    for chapter, keywords in CHAPTER_KEYWORDS.items():
        score = 0
        for kw in keywords:
            if re.search(kw, text_lower, re.IGNORECASE):
                score += 1
        if score > 0:
            scores[chapter] = score

    if not scores:
        return "Relations and Functions"  # default
    return max(scores, key=scores.get)


def get_section_type(qnum, year):
    """Get section label and question type based on question number."""
    year_key = year if year in SECTION_RANGES else str(year)

    # Determine section based on question number
    if year in [2023, 2024, 2025, "2022-T2"]:
        if 1 <= qnum <= 20:
            return "A", "MCQ", 1
        elif 21 <= qnum <= 25:
            return "B", "VSA", 2
        elif 26 <= qnum <= 31:
            return "C", "SA", 3
        elif 32 <= qnum <= 35:
            return "D", "LA", 5
        else:
            return "E", "Case Study", 4
    elif year == "2022-T1":
        if qnum <= 25:
            return "A", "MCQ", 1
        elif qnum <= 40:
            return "B", "VSA", 2
        else:
            return "C", "SA", 3
    elif year in [2017, 2018]:
        if 1 <= qnum <= 6:
            return "A", "MCQ", 1
        elif 7 <= qnum <= 14:
            return "B", "VSA", 1
        elif 15 <= qnum <= 22:
            return "C", "SA", 4
        else:
            return "D", "LA", 6
    elif year == 2019:
        if 1 <= qnum <= 4:
            return "A", "MCQ", 1
        elif 5 <= qnum <= 12:
            return "B", "VSA", 2
        elif 13 <= qnum <= 22:
            return "C", "SA", 4
        else:
            return "D", "LA", 6
    elif year == 2020:
        if 1 <= qnum <= 10:
            return "A", "MCQ", 1
        elif 11 <= qnum <= 15:
            return "B", "VSA", 2
        elif 16 <= qnum <= 22:
            return "C", "SA", 3
        else:
            return "D", "LA", 5
    else:  # 2015, 2016
        if 1 <= qnum <= 10:
            return "A", "MCQ", 1
        elif 11 <= qnum <= 15:
            return "B", "VSA", 1
        elif 16 <= qnum <= 25:
            return "C", "SA", 4
        else:
            return "D", "LA", 6


def is_garbled(text):
    """Check if text is too garbled to use."""
    if not text or len(text.strip()) < 15:
        return True
    # Box/replacement chars
    pua = any(0xF000 <= ord(c) <= 0xF8FF for c in text)
    if pua or re.search(r'[□■▪▫▢▣�]', text):
        return True
    # Too many isolated single characters (broken formula lines)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if len(lines) < 2:
        return False
    short_lines = [l for l in lines if len(l) <= 2 and not re.match(r'^[a-zA-Zα-ωΑ-Ω]$', l)]
    if len(short_lines) > len(lines) * 0.4:
        return True
    return False


def parse_mcq_options(text):
    """Extract MCQ options from question text."""
    opts = {}
    # Pattern: (a) text (b) text (c) text (d) text
    pattern = r'\(([abcd])\)\s*([^(]+?)(?=\s*\([abcd]\)|$)'
    matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
    for letter, content in matches:
        opts[letter.upper()] = content.strip()
    return opts if len(opts) >= 2 else None


def parse_questions_from_text(full_text, year):
    """Parse individual questions from extracted text."""
    questions = []

    # Split into question blocks using question number pattern
    # Pattern: start of line, number, period/tab
    qblock_pattern = re.compile(
        r'(?:^|\n)\s*(\d{1,2})\.\s+(.+?)(?=\n\s*\d{1,2}\.\s|\Z)',
        re.DOTALL
    )

    # Remove header/footer boilerplate
    text = re.sub(r'Oswaal CBSE[^\n]*\n', '', full_text)
    text = re.sub(r'SOLVED PAPER[^\n]*\n', '', text, flags=re.IGNORECASE)
    text = re.sub(r'(?i)section\s*[-–]\s*[A-E]\s*\n', '\n', text)
    text = re.sub(r'Delhi Set[^\n]*\n', '', text)
    text = re.sub(r'\d+/\d+/\d+\s*\n', '', text)

    for m in qblock_pattern.finditer(text):
        qnum = int(m.group(1))
        if qnum < 1 or qnum > 40:
            continue

        raw = m.group(2).strip()

        # Split into question body and solution
        sol_match = re.search(r'\n\s*Sol\.?\s*', raw, re.IGNORECASE)
        if sol_match:
            q_body = raw[:sol_match.start()].strip()
            sol_body = raw[sol_match.end():].strip()
        else:
            q_body = raw
            sol_body = ""

        # Skip garbled questions
        if is_garbled(q_body):
            continue

        # Get section/type/marks
        section, qtype, marks = get_section_type(qnum, year)

        # Extract MCQ options from question body
        options = None
        clean_q = q_body
        if qtype == "MCQ" or re.search(r'\(a\)', q_body, re.IGNORECASE):
            qtype = "MCQ"
            options = parse_mcq_options(q_body)
            # Remove options from question text
            if options:
                clean_q = re.sub(r'\s*\([abcd]\)\s*.+?(?=\s*\([abcd]\)|\s*Sol\.|\Z)', '',
                                  q_body, flags=re.IGNORECASE | re.DOTALL).strip()

        # Clean the question text
        clean_q = clean_math(clean_q)
        clean_q = re.sub(r'\s+', ' ', clean_q).strip()

        # Extract answer from solution
        answer = ""
        if sol_body:
            # For MCQ: extract "Option (x) is correct"
            opt_match = re.search(r'Option\s*\(([abcd])\)\s*is\s*correct', sol_body, re.IGNORECASE)
            if opt_match:
                chosen = opt_match.group(1).upper()
                # Get explanation
                expl_match = re.search(r'Explanation\s*:?\s*(.+)', sol_body, re.DOTALL | re.IGNORECASE)
                expl = expl_match.group(1).strip() if expl_match else ""
                opt_text = options.get(chosen, '') if options else ''
                answer = f"({chosen}) {opt_text}\n\n{clean_math(expl)}".strip() if expl else f"({chosen}) {opt_text}"
            else:
                answer = clean_math(sol_body.strip())

        # Skip if question is too short or garbled
        if len(clean_q) < 20:
            continue
        if is_garbled(clean_q):
            continue

        # Classify chapter
        chapter = classify_chapter(clean_q + " " + answer)

        # Build unique ID
        year_str = str(year).replace('-', '_')
        qid = f"ex_{year_str}_{qnum}"

        q = {
            "id": qid,
            "year": year if isinstance(year, int) else year,
            "question_number": qnum,
            "question": clean_q,
            "answer": answer if answer else "See solution.",
            "section": section,
            "marks": marks,
            "chapter": chapter,
            "type": qtype,
        }
        if options and len(options) >= 2:
            q["options"] = options

        questions.append(q)

    return questions


def process_all_pdfs():
    import os
    all_new = []
    for fname, year in YEAR_MAP.items():
        path = os.path.join(PDF_DIR, fname)
        if not os.path.exists(path):
            print(f"  MISSING: {fname}")
            continue

        print(f"\nProcessing {fname} (year={year})...")
        full_text = extract_pdf_text(path)
        qs = parse_questions_from_text(full_text, year)
        print(f"  Extracted {len(qs)} questions")
        all_new.extend(qs)

    return all_new


if __name__ == "__main__":
    # Process all PDFs
    new_questions = process_all_pdfs()

    # Load existing data
    with open(OUTPUT) as f:
        existing = json.load(f)

    existing_ids = {q['id'] for q in existing}

    # Add only truly new questions (by ID and by content dedup)
    added = 0
    skipped_dup = 0
    skipped_garbled = 0

    for q in new_questions:
        if q['id'] in existing_ids:
            skipped_dup += 1
            continue
        # Double-check not garbled
        if is_garbled(q['question']):
            skipped_garbled += 1
            continue

        existing.append(q)
        existing_ids.add(q['id'])
        added += 1

    print(f"\n\nResults:")
    print(f"  New questions added: {added}")
    print(f"  Skipped (duplicate ID): {skipped_dup}")
    print(f"  Skipped (garbled): {skipped_garbled}")
    print(f"  Total questions: {len(existing)}")

    from collections import Counter
    counts = Counter(q['chapter'] for q in existing)
    print("\nChapter counts:")
    for ch, cnt in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cnt:3d}  {ch}")

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"\nSaved to {OUTPUT}")
