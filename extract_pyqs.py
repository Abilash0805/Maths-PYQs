#!/usr/bin/env python3
"""
Improved CBSE Class 12 Maths PYQ extractor.
Reads PDFs and extracts Q&A with chapter classification.
"""

import json
import re
import os
import PyPDF2
from collections import Counter

PDF_DIR = "./pdfs/PYQs"
OUTPUT = "./public/data/pyqs.json"

CHAPTERS = [
    "Relations and Functions",
    "Inverse Trigonometric Functions",
    "Matrices",
    "Determinants",
    "Continuity and Differentiability",
    "Application of Derivatives",
    "Integrals",
    "Differential Equations",
    "Vector Algebra",
    "Three Dimensional Geometry",
    "Linear Programming",
    "Probability",
]

CHAPTER_KEYWORDS = {
    "Relations and Functions": [
        "function", "injective", "surjective", "bijective", "relation", "one-one", "onto",
        "one one", "domain", "range", "codomain", "equivalence relation", "identity function",
        "f(x)", "f :r", "f:r", "reflexive", "symmetric", "transitive", "partition",
        "binary operation", "composition"
    ],
    "Inverse Trigonometric Functions": [
        "sin-1", "cos-1", "tan-1", "sin–1", "cos–1", "tan–1",
        "sin^{-1}", "cos^{-1}", "tan^{-1}", "cot-1", "sec-1", "cosec-1",
        "inverse trigonometric", "principal value", "arcsin", "arccos", "arctan",
        "sin^-1", "cos^-1", "tan^-1", "cot–1", "sec–1", "cosec–1"
    ],
    "Matrices": [
        "matrix", "matrices", "transpose", "symmetric matrix", "skew-symmetric",
        "skew symmetric", "row matrix", "column matrix", "square matrix", "diagonal matrix",
        "identity matrix", "null matrix", "scalar matrix", "order of matrix",
        "matrix equation", "a = [", "b = ["
    ],
    "Determinants": [
        "determinant", "cofactor", "adjoint", "singular", "non-singular",
        "cramer", "minor", "adj a", "inverse of matrix",
        "system of equations using matrix", "det", "expand"
    ],
    "Continuity and Differentiability": [
        "continuous", "continuity", "differentiable", "differentiability",
        "left hand limit", "right hand limit", "rolle", "lagrange",
        "mean value theorem", "mvt", "chain rule", "implicit differentiation",
        "lhd", "rhd", "lhl", "rhl"
    ],
    "Application of Derivatives": [
        "increasing", "decreasing", "maxima", "minima", "maximum value", "minimum value",
        "tangent", "normal to", "rate of change", "slope of curve", "critical point",
        "stationary point", "optimiz", "optimis", "rate at which",
        "local maximum", "local minimum", "absolute maximum", "absolute minimum",
        "inflection", "approximation", "error", "approximate value"
    ],
    "Integrals": [
        "integral", "integrate", "integration", "evaluate the integral",
        "area under", "area bounded", "definite integral", "indefinite integral",
        "partial fraction", "substitution", "by parts", "reduction formula",
        "find the value of", "sec x", "tan x", "sin x dx", "cos x dx",
        "e^x", "log x dx"
    ],
    "Differential Equations": [
        "differential equation", "d²y", "d2y", "dy/dx", "dy dx",
        "order of", "degree of", "general solution", "particular solution",
        "homogeneous", "linear differential", "variable separable", "integrating factor",
        "formation of", "orthogonal trajectory", "d.e.", "ode"
    ],
    "Vector Algebra": [
        "position vector", "unit vector", "collinear vector", "coplanar vector",
        "scalar product", "dot product", "cross product", "magnitude of",
        "direction of vector", "resultant vector", "scalar triple product",
        "vector triple product", "parallelogram", "triangle law",
        "components of vector"
    ],
    "Three Dimensional Geometry": [
        "direction cosines", "direction ratios", "line in 3", "plane",
        "distance from plane", "distance between lines", "angle between plane",
        "angle between line", "cartesian equation", "vector equation of line",
        "vector equation of plane", "skew lines", "three dimensional",
        "foot of perpendicular", "image of point", "x/a = y/b", "x-x1"
    ],
    "Linear Programming": [
        "linear programming", "objective function", "constraint", "feasible region",
        "corner point", "maximize", "minimize", "lpp", "linear programming problem",
        "bounded", "unbounded", "optimal solution", "iso-profit", "iso-cost",
        "vertices of feasible", "graphical method"
    ],
    "Probability": [
        "probability", "bayes", "conditional probability", "random variable",
        "p(a)", "p(b)", "p(e)", "independent event", "mutually exclusive",
        "binomial distribution", "probability distribution", "expected value",
        "sample space", "favourable outcome", "bernoulli", "binomial",
        "at least", "at most", "getting a head", "dice", "card", "ball"
    ],
}


def extract_pdf_text(pdf_path):
    texts = []
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
    return "\n".join(texts)


def get_year_term(filename):
    name = filename.lower()
    if "2025" in name:
        return 2025, None
    elif "2024" in name:
        return 2024, None
    elif "2023" in name:
        return 2023, None
    elif "2022 term ii" in name:
        return 2022, "Term II"
    elif "2022 term i" in name or "2022 term" in name:
        return 2022, "Term I"
    elif "2022" in name:
        return 2022, None
    elif "2020" in name:
        return 2020, None
    elif "2019" in name:
        return 2019, None
    elif "2018" in name:
        return 2018, None
    elif "2017" in name:
        return 2017, None
    elif "2016" in name:
        return 2016, None
    elif "2015" in name:
        return 2015, None
    return 0, None


def classify_chapter(text):
    text_lower = text.lower()
    scores = {}
    for chapter, keywords in CHAPTER_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in text_lower)
        if score > 0:
            scores[chapter] = score
    if not scores:
        return "General"
    return max(scores, key=scores.get)


def clean_text(t):
    """Clean extracted text."""
    if not t:
        return ""
    # Fix common PDF extraction artifacts
    t = re.sub(r'\s+', ' ', t)
    t = t.strip()
    return t


def parse_questions_from_text(text, year, term):
    questions = []

    # Normalize
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Try to find Q&A blocks
    # Pattern: number followed by text, then Sol.
    # Works for standard CBSE solved papers format

    # Split into blocks by question numbers
    # Question numbers appear as: "1.", "2.", etc at start of line or after whitespace
    # But NOT inside math expressions

    # Strategy: scan line by line, collect blocks
    lines = text.split('\n')
    blocks = []  # (q_num, block_text)
    current_num = None
    current_block = []

    for line in lines:
        # Check if this line starts a new question
        m = re.match(r'^\s{0,3}(\d{1,2})\.\s+(.+)', line)
        if m:
            num = int(m.group(1))
            if 1 <= num <= 38:
                if current_num is not None:
                    blocks.append((current_num, '\n'.join(current_block)))
                current_num = num
                current_block = [m.group(2)]
                continue

        if current_num is not None:
            current_block.append(line)

    if current_num is not None:
        blocks.append((current_num, '\n'.join(current_block)))

    year_str = str(year) + (f"_{term.replace(' ', '')}" if term else "")

    for q_num, block in blocks:
        # Determine section and marks
        if q_num <= 20:
            section, marks, q_type = "A", 1, "MCQ"
        elif q_num <= 25:
            section, marks, q_type = "B", 2, "VSA"
        elif q_num <= 31:
            section, marks, q_type = "C", 3, "SA"
        elif q_num <= 35:
            section, marks, q_type = "D", 5, "LA"
        else:
            section, marks, q_type = "E", 4, "Case Study"

        # Split question from answer
        # Sol. appears after the question
        sol_patterns = [
            r'\nSol\.\s*',
            r'\n\s*Sol\.\s*',
            r'\nSol\s*\.\s*',
            r'Sol\.\s*Option',
            r'Sol\.\s*\(',
        ]

        question_text = block
        answer_text = ""

        for pat in sol_patterns:
            parts = re.split(pat, block, maxsplit=1, flags=re.IGNORECASE)
            if len(parts) == 2:
                question_text = parts[0]
                answer_text = parts[1]
                break

        question_text = clean_text(question_text)
        answer_text = clean_text(answer_text)

        if not question_text or len(question_text) < 8:
            continue

        # Extract MCQ options
        options = {}
        if q_type == "MCQ" or marks == 1:
            option_matches = list(re.finditer(
                r'\(([abcdABCD])\)\s*([^(]{2,80}?)(?=\s*\([abcdABCD]\)|\s*Sol\.|\s*$)',
                question_text + " " + answer_text[:200]
            ))
            for om in option_matches:
                key = om.group(1).lower()
                val = clean_text(om.group(2))
                if val:
                    options[key] = val

            # Remove options from question text
            if options:
                for key in 'abcd':
                    idx = question_text.find(f'({key})')
                    if idx == -1:
                        idx = question_text.find(f'({key.upper()})')
                    if idx > 10:
                        question_text = question_text[:idx].strip()
                        break

        # Classify chapter
        combined = question_text + " " + answer_text
        chapter = classify_chapter(combined)
        if chapter == "General":
            chapter = "Relations and Functions"

        is_important = marks == 5

        qid = f"{year_str}_{q_num}"

        questions.append({
            "id": qid,
            "year": year,
            "term": term,
            "question_number": q_num,
            "question": question_text,
            "options": options,
            "answer": answer_text,
            "section": section,
            "marks": marks,
            "chapter": chapter,
            "type": q_type,
            "is_important": is_important,
        })

    return questions


def main():
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    all_questions = []

    for pdf_name in sorted(os.listdir(PDF_DIR)):
        if not pdf_name.endswith('.pdf'):
            continue

        year, term = get_year_term(pdf_name)
        if year == 0:
            print(f"WARNING: Skipping {pdf_name} (unknown year)")
            continue

        print(f"\nProcessing {pdf_name} → {year}{' ' + term if term else ''}")
        text = extract_pdf_text(os.path.join(PDF_DIR, pdf_name))
        questions = parse_questions_from_text(text, year, term)
        print(f"  → {len(questions)} questions")

        chap_dist = Counter(q['chapter'] for q in questions)
        for ch, cnt in chap_dist.most_common(5):
            print(f"    {ch}: {cnt}")

        all_questions.extend(questions)

    # Deduplicate
    seen = set()
    unique = []
    for q in all_questions:
        if q['id'] not in seen:
            seen.add(q['id'])
            unique.append(q)

    print(f"\n{'='*60}")
    print(f"Total: {len(unique)} questions")

    year_dist = Counter(
        str(q['year']) + (' ' + q['term'] if q.get('term') else '')
        for q in unique
    )
    for yr, cnt in sorted(year_dist.items()):
        print(f"  {yr}: {cnt}")

    chapter_dist = Counter(q['chapter'] for q in unique)
    print("\nBy chapter:")
    for ch, cnt in sorted(chapter_dist.items(), key=lambda x: -x[1]):
        print(f"  {ch}: {cnt}")

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)

    print(f"\nSaved to {OUTPUT}")


if __name__ == "__main__":
    main()
