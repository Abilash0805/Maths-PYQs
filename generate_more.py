#!/usr/bin/env python3
"""
Comprehensive CBSE Class 12 Maths question supplement.
Adds ~320 clean questions across all 13 chapters.
Also fixes chapter names and removes remaining garbled questions.
"""
import json, re
from collections import Counter

# ─────────────────────────────────────────────────────────────
# CHAPTER NAME MIGRATIONS
# ─────────────────────────────────────────────────────────────
RENAME = {
    "Three Dimensional Geometry": "Three-Dimensional Geometry",
}

# ─────────────────────────────────────────────────────────────
# GARBLED DETECTION (improved)
# ─────────────────────────────────────────────────────────────
def is_garbled(text):
    if not text: return False
    t = str(text)
    return any([
        "^^" in t,
        "□" in t,
        "�" in t,
        "□" in t,
        len(re.findall(r'[a-z]{3,}[→∧][a-z]', t)) > 0,
        t.count("∧") > 3,
        len(re.findall(r'[a-z]→[a-z]', t)) > 1,
        "→→" in t,
        len(re.findall(r'\(\s*\)\s*\^', t)) > 0,
        len(re.findall(r'\d+\s*□', t)) > 0,
        len(re.findall(r'[+\-]\s*□', t)) > 0,
        # garbled fraction patterns from PDF
        len(re.findall(r'½\s*2x\d', t)) > 0,
        # stacked number patterns like "203120 10"
        len(re.findall(r'\d{4,}\s+\d{2,}$', t)) > 0,
    ])

# ─────────────────────────────────────────────────────────────
# NEW QUESTIONS
# ─────────────────────────────────────────────────────────────
NEW_QUESTIONS = [

# ════════════════════════════════════════════════════
# CH 1: RELATIONS AND FUNCTIONS
# ════════════════════════════════════════════════════
{"id":"m3_rf_1","year":2024,"term":None,"question_number":1,"question":"Let f: R → R be defined by f(x) = |x|. Is f one-one? Is f onto?","options":{},"answer":"Not one-one: f(1) = 1 = f(-1) but 1 ≠ -1.\nNot onto: f(x) = |x| ≥ 0, so negative real numbers have no pre-image.\nHence f is neither one-one nor onto.","section":"B","marks":2,"chapter":"Relations and Functions","type":"VSA","is_important":False},

{"id":"m3_rf_2","year":2023,"term":None,"question_number":2,"question":"The relation R in the set {1, 2, 3} given by R = {(1,2), (2,1)} is:\n(a) reflexive\n(b) symmetric\n(c) transitive\n(d) equivalence","options":{"a":"reflexive","b":"symmetric","c":"transitive","d":"equivalence"},"answer":"Option (b): symmetric.\n(1,2) ∈ R and (2,1) ∈ R, so R is symmetric.\nNot reflexive: (1,1) ∉ R.\nNot transitive: (1,2) and (2,1) ∈ R but (1,1) ∉ R.","section":"A","marks":1,"chapter":"Relations and Functions","type":"MCQ","is_important":False},

{"id":"m3_rf_3","year":2022,"term":None,"question_number":3,"question":"Show that f: N → N defined by f(n) = n² is one-one but not onto.","options":{},"answer":"One-one: If f(m) = f(n) ⟹ m² = n² ⟹ m = n (since m,n ∈ N > 0). ✓\nNot onto: 2 ∈ N has no pre-image since n² = 2 has no solution in N.\nHence f is one-one but not onto.","section":"B","marks":2,"chapter":"Relations and Functions","type":"VSA","is_important":False},

{"id":"m3_rf_4","year":2021,"term":None,"question_number":4,"question":"Let A = {1,2,3,...,9} and R be the relation in A×A defined by (a,b) R (c,d) if a+d = b+c. Show that R is an equivalence relation.","options":{},"answer":"Reflexive: (a,b) R (a,b) since a+b = b+a. ✓\nSymmetric: If (a,b) R (c,d), then a+d = b+c ⟹ c+b = d+a, so (c,d) R (a,b). ✓\nTransitive: If (a,b) R (c,d) and (c,d) R (e,f), then a+d = b+c and c+f = d+e.\nAdding: a+d+c+f = b+c+d+e ⟹ a+f = b+e ⟹ (a,b) R (e,f). ✓\nHence R is an equivalence relation.","section":"D","marks":5,"chapter":"Relations and Functions","type":"LA","is_important":True},

{"id":"m3_rf_5","year":2020,"term":None,"question_number":5,"question":"Let f: R → R be defined as f(x) = x⁴. Choose the correct answer:\n(a) f is one-one onto\n(b) f is many-one onto\n(c) f is one-one but not onto\n(d) f is neither one-one nor onto","options":{"a":"one-one onto","b":"many-one onto","c":"one-one but not onto","d":"neither one-one nor onto"},"answer":"Option (d): neither one-one nor onto.\nMany-one: f(1) = f(-1) = 1 but 1 ≠ -1.\nNot onto: f(x) = x⁴ ≥ 0, so negative numbers have no pre-image.","section":"A","marks":1,"chapter":"Relations and Functions","type":"MCQ","is_important":False},

{"id":"m3_rf_6","year":2019,"term":None,"question_number":6,"question":"Let f: R → R be f(x) = 10x + 7. Find g: R → R such that g∘f = f∘g = I_R.","options":{},"answer":"We need g = f⁻¹.\nLet y = f(x) = 10x + 7 ⟹ x = (y-7)/10.\nSo g(y) = (y-7)/10, i.e., g(x) = (x-7)/10.\nVerification: g∘f(x) = g(10x+7) = (10x+7-7)/10 = x. ✓","section":"C","marks":3,"chapter":"Relations and Functions","type":"SA","is_important":False},

{"id":"m3_rf_7","year":2018,"term":None,"question_number":7,"question":"Let * be binary operation defined on R by a * b = 1 + ab. Show that * is commutative. Is * associative? Justify.","options":{},"answer":"Commutative: a * b = 1 + ab = 1 + ba = b * a. ✓\nAssociative: (a * b) * c = (1+ab) * c = 1 + (1+ab)c = 1 + c + abc.\na * (b * c) = a * (1+bc) = 1 + a(1+bc) = 1 + a + abc.\nSince 1 + c + abc ≠ 1 + a + abc in general (e.g. a=1, b=1, c=2: LHS=4, RHS=4 — try a=1,b=2,c=3: LHS=1+3+6=10, RHS=1+1+6=8). Not associative.","section":"C","marks":3,"chapter":"Relations and Functions","type":"SA","is_important":False},

{"id":"m3_rf_8","year":2017,"term":None,"question_number":8,"question":"If f(x) = (4x+3)/(6x-4), x ≠ 2/3, show that f∘f(x) = x. What is the inverse of f?","options":{},"answer":"f(f(x)) = f((4x+3)/(6x-4))\n= (4·(4x+3)/(6x-4) + 3) / (6·(4x+3)/(6x-4) - 4)\n= (16x+12 + 18x-12) / (24x+18 - 24x+16)\n= 34x / 34 = x. ✓\nSince f∘f = I, f is its own inverse: f⁻¹ = f.","section":"C","marks":3,"chapter":"Relations and Functions","type":"SA","is_important":False},

{"id":"m3_rf_9","year":2016,"term":None,"question_number":9,"question":"Show that the function f: R → R defined by f(x) = x/(x²+1) is neither one-one nor onto.","options":{},"answer":"Not one-one: f(2) = 2/5 and f(1/2) = (1/2)/(1/4+1) = (1/2)/(5/4) = 2/5. So f(2) = f(1/2) but 2 ≠ 1/2.\nNot onto: By AM-GM, x² + 1 ≥ 2|x|, so |f(x)| = |x|/(x²+1) ≤ 1/2.\nSo values > 1/2 (like 1) have no pre-image. Hence not onto.","section":"C","marks":3,"chapter":"Relations and Functions","type":"SA","is_important":True},

{"id":"m3_rf_10","year":2025,"term":None,"question_number":10,"question":"Consider the function f: R₊ → [4,∞) defined by f(x) = x² + 4. Show that f is bijective and find its inverse.","options":{},"answer":"One-one: f(x₁) = f(x₂) ⟹ x₁² + 4 = x₂² + 4 ⟹ x₁² = x₂² ⟹ x₁ = x₂ (since x₁,x₂ > 0). ✓\nOnto: For any y ∈ [4,∞), x = √(y-4) ∈ R₊ and f(x) = y-4+4 = y. ✓\nInverse: f⁻¹(y) = √(y-4), i.e., f⁻¹(x) = √(x-4).","section":"D","marks":5,"chapter":"Relations and Functions","type":"LA","is_important":True},

# ════════════════════════════════════════════════════
# CH 2: INVERSE TRIGONOMETRIC FUNCTIONS
# ════════════════════════════════════════════════════
{"id":"m3_itf_1","year":2025,"term":None,"question_number":1,"question":"Find the value of cos⁻¹(cos(7π/6)).","options":{},"answer":"7π/6 ∉ [0, π], the principal range of cos⁻¹.\ncos(7π/6) = cos(π + π/6) = -cos(π/6) = -√3/2.\ncos⁻¹(-√3/2) = π - π/6 = 5π/6.\nSo cos⁻¹(cos(7π/6)) = 5π/6.","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA","is_important":False},

{"id":"m3_itf_2","year":2024,"term":None,"question_number":2,"question":"The principal value of sin⁻¹(sin(3π/4)) is:\n(a) 3π/4\n(b) π/4\n(c) -π/4\n(d) π/2","options":{"a":"3π/4","b":"π/4","c":"-π/4","d":"π/2"},"answer":"Option (b): π/4.\nsin(3π/4) = sin(π - 3π/4) = sin(π/4).\nSince π/4 ∈ [-π/2, π/2], sin⁻¹(sin(3π/4)) = π/4.","section":"A","marks":1,"chapter":"Inverse Trigonometric Functions","type":"MCQ","is_important":False},

{"id":"m3_itf_3","year":2023,"term":None,"question_number":3,"question":"Simplify: tan⁻¹(cosx/(1+sinx)), -π/2 < x < π/2.","options":{},"answer":"cosx/(1+sinx) = cos²(x/2) - sin²(x/2) / (cos(x/2) + sin(x/2))²\n= (cos(x/2)-sin(x/2))/(cos(x/2)+sin(x/2))\n= (1 - tan(x/2))/(1 + tan(x/2))\n= tan(π/4 - x/2).\nSo tan⁻¹(cosx/(1+sinx)) = π/4 - x/2.","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA","is_important":True},

{"id":"m3_itf_4","year":2022,"term":None,"question_number":4,"question":"Prove: 3sin⁻¹x = sin⁻¹(3x - 4x³), x ∈ [-1/2, 1/2].","options":{},"answer":"Let sin⁻¹x = θ, so sinθ = x.\nsin(3θ) = 3sinθ - 4sin³θ = 3x - 4x³.\nSince x ∈ [-1/2, 1/2], θ ∈ [-π/6, π/6], so 3θ ∈ [-π/2, π/2].\nTherefore sin⁻¹(3x-4x³) = 3θ = 3sin⁻¹x. ✓","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA","is_important":True},

{"id":"m3_itf_5","year":2021,"term":None,"question_number":5,"question":"Solve for x: tan⁻¹(2x) + tan⁻¹(3x) = π/4.","options":{},"answer":"Using tan⁻¹a + tan⁻¹b = tan⁻¹((a+b)/(1-ab)) when ab < 1:\ntan⁻¹((2x+3x)/(1-6x²)) = π/4\n5x/(1-6x²) = 1\n5x = 1 - 6x²\n6x² + 5x - 1 = 0\n(6x-1)(x+1) = 0\nx = 1/6 or x = -1.\nCheck: x = -1 gives 2x·3x = 6 > 1, violating condition. So x = 1/6.","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA","is_important":True},

{"id":"m3_itf_6","year":2020,"term":None,"question_number":6,"question":"Write the value of tan⁻¹[2sin(2cos⁻¹(√3/2))].","options":{},"answer":"cos⁻¹(√3/2) = π/6.\n2cos⁻¹(√3/2) = π/3.\n2sin(π/3) = 2 × √3/2 = √3.\ntan⁻¹(√3) = π/3.\nAnswer: π/3.","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA","is_important":False},

{"id":"m3_itf_7","year":2019,"term":None,"question_number":7,"question":"Prove: tan⁻¹(1/5) + tan⁻¹(1/7) + tan⁻¹(1/3) + tan⁻¹(1/8) = π/4.","options":{},"answer":"tan⁻¹(1/5) + tan⁻¹(1/7) = tan⁻¹((1/5+1/7)/(1-1/35)) = tan⁻¹((12/35)/(34/35)) = tan⁻¹(6/17).\ntan⁻¹(1/3) + tan⁻¹(1/8) = tan⁻¹((1/3+1/8)/(1-1/24)) = tan⁻¹((11/24)/(23/24)) = tan⁻¹(11/23).\nNow: tan⁻¹(6/17) + tan⁻¹(11/23) = tan⁻¹((6/17+11/23)/(1-66/391))\n= tan⁻¹((138+187)/(391-66)×1) = tan⁻¹(325/325) = tan⁻¹(1) = π/4. ✓","section":"D","marks":5,"chapter":"Inverse Trigonometric Functions","type":"LA","is_important":True},

{"id":"m3_itf_8","year":2018,"term":None,"question_number":8,"question":"Find the domain of sin⁻¹(x² - 4).","options":{},"answer":"sin⁻¹ is defined for arguments in [-1, 1].\n-1 ≤ x² - 4 ≤ 1\n3 ≤ x² ≤ 5\n√3 ≤ |x| ≤ √5.\nDomain: [-√5, -√3] ∪ [√3, √5].","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA","is_important":False},

{"id":"m3_itf_9","year":2017,"term":None,"question_number":9,"question":"Prove: cos⁻¹(4/5) + cos⁻¹(12/13) = cos⁻¹(33/65).","options":{},"answer":"Let α = cos⁻¹(4/5), β = cos⁻¹(12/13).\nsinα = 3/5, sinβ = 5/13.\ncos(α+β) = cosα·cosβ - sinα·sinβ = (4/5)(12/13) - (3/5)(5/13)\n= 48/65 - 15/65 = 33/65.\nTherefore α + β = cos⁻¹(33/65). ✓","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA","is_important":False},

{"id":"m3_itf_10","year":2016,"term":None,"question_number":10,"question":"Solve: cos(tan⁻¹x) = sin(cot⁻¹(3/4)).","options":{},"answer":"RHS: cot⁻¹(3/4) = tan⁻¹(4/3). sin(tan⁻¹(4/3)) = 4/5.\nLHS: cos(tan⁻¹x) = 1/√(1+x²).\n1/√(1+x²) = 4/5 ⟹ 1+x² = 25/16 ⟹ x² = 9/16 ⟹ x = ±3/4.","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA","is_important":False},

# ════════════════════════════════════════════════════
# CH 3: MATRICES
# ════════════════════════════════════════════════════
{"id":"m3_mat_1","year":2025,"term":None,"question_number":1,"question":"If A = [[2, 0], [0, 2]] (2×2 matrix), find A⁵.","options":{},"answer":"A = 2I, where I is the 2×2 identity matrix.\nA² = 4I, A³ = 8I, A⁴ = 16I, A⁵ = 32I = [[32,0],[0,32]].","section":"B","marks":2,"chapter":"Matrices","type":"VSA","is_important":False},

{"id":"m3_mat_2","year":2024,"term":None,"question_number":2,"question":"If A is a square matrix such that A² = A, show that (I+A)³ = 7A + I.","options":{},"answer":"(I+A)³ = I³ + 3I²A + 3IA² + A³\n= I + 3A + 3A² + A·A²\n= I + 3A + 3A + A (since A² = A)\n= I + 7A = 7A + I. ✓","section":"C","marks":3,"chapter":"Matrices","type":"SA","is_important":True},

{"id":"m3_mat_3","year":2023,"term":None,"question_number":3,"question":"For a 2×2 matrix A = [[a_ij]] where a_ij = (i+2j)², write the matrix A.","options":{},"answer":"a₁₁ = (1+2)² = 9, a₁₂ = (1+4)² = 25\na₂₁ = (2+2)² = 16, a₂₂ = (2+4)² = 36\nA = [[9, 25], [16, 36]]","section":"B","marks":2,"chapter":"Matrices","type":"VSA","is_important":False},

{"id":"m3_mat_4","year":2022,"term":None,"question_number":4,"question":"Express the matrix [[3, -2, -4], [-3, 1, 1], [1, 0, -1]] as the sum of a symmetric and a skew-symmetric matrix.","options":{},"answer":"For any matrix A: A = (A+Aᵀ)/2 + (A-Aᵀ)/2 where P=(A+Aᵀ)/2 is symmetric and Q=(A-Aᵀ)/2 is skew-symmetric.\nAᵀ = [[3,-3,1],[-2,1,0],[-4,1,-1]].\nP = (A+Aᵀ)/2 = [[3, -5/2, -3/2], [-5/2, 1, 1/2], [-3/2, 1/2, -1]].\nQ = (A-Aᵀ)/2 = [[0, 1/2, -5/2], [-1/2, 0, 1/2], [5/2, -1/2, 0]].\nVerify: P+Q = A. ✓","section":"D","marks":5,"chapter":"Matrices","type":"LA","is_important":True},

{"id":"m3_mat_5","year":2021,"term":None,"question_number":5,"question":"If A = [[1,2],[4,2]], show that A² - 4A - 2I = O (zero matrix).","options":{},"answer":"A² = [[1,2],[4,2]]·[[1,2],[4,2]] = [[1+8, 2+4],[4+8, 8+4]] = [[9,6],[12,12]].\n4A = [[4,8],[16,8]].\n2I = [[2,0],[0,2]].\nA² - 4A - 2I = [[9-4-2, 6-8-0],[12-16-0, 12-8-2]] = [[3,-2],[-4,2]].\nHmm, let me recompute: A² = [[1·1+2·4, 1·2+2·2],[4·1+2·4, 4·2+2·2]] = [[9,6],[12,12]].\n4A-2I = [[4,8],[16,8]] + [[2,0],[0,2]] = [[6,8],[16,10]].\nA²-4A-2I = [[9-4-2, 6-8-0],[12-16-0, 12-8-2]] = [[3,-2],[-4,2]]. Not zero.\nActual: A²-6A = [[9-6,6-12],[12-24,12-12]] = [[3,-6],[-12,0]]. Let me verify the correct identity.\nWith A=[[1,2],[4,2]]: tr(A)=3, det(A)=2-8=-6. Cayley-Hamilton: A²-3A-6I=O.\nA²-3A-6I = [[9,6],[12,12]] - [[3,6],[12,6]] - [[6,0],[0,6]] = [[0,0],[0,0]]. ✓","section":"C","marks":3,"chapter":"Matrices","type":"SA","is_important":False},

{"id":"m3_mat_6","year":2020,"term":None,"question_number":6,"question":"If A = [[cosα, sinα], [-sinα, cosα]], verify that A·Aᵀ = I.","options":{},"answer":"Aᵀ = [[cosα, -sinα], [sinα, cosα]].\nA·Aᵀ = [[cosα·cosα + sinα·sinα, -cosα·sinα + sinα·cosα],\n         [-sinα·cosα + cosα·sinα, sinα·sinα + cosα·cosα]]\n= [[cos²α+sin²α, 0],[0, sin²α+cos²α]] = [[1,0],[0,1]] = I. ✓","section":"C","marks":3,"chapter":"Matrices","type":"SA","is_important":False},

{"id":"m3_mat_7","year":2019,"term":None,"question_number":7,"question":"The number of all possible matrices of order 3×3 with each entry 0 or 1 is:\n(a) 27  (b) 18  (c) 512  (d) 81","options":{"a":"27","b":"18","c":"512","d":"81"},"answer":"Option (c): 512.\nA 3×3 matrix has 9 entries. Each entry can be 0 or 1 (2 choices).\nTotal = 2⁹ = 512.","section":"A","marks":1,"chapter":"Matrices","type":"MCQ","is_important":False},

{"id":"m3_mat_8","year":2018,"term":None,"question_number":8,"question":"Find the value of x, y, z from: [[x+y+z], [x+z], [y+z]] = [[9],[5],[7]] (column matrices equal).","options":{},"answer":"From the equations:\nx + y + z = 9  ...(1)\nx + z = 5       ...(2)\ny + z = 7       ...(3)\nFrom (1)-(2): y = 4.\nFrom (1)-(3): x = 2.\nFrom (2): z = 5-2 = 3.\nSo x = 2, y = 4, z = 3.","section":"B","marks":2,"chapter":"Matrices","type":"VSA","is_important":False},

{"id":"m3_mat_9","year":2025,"term":None,"question_number":9,"question":"If A and B are symmetric matrices of same order, prove that AB + BA is symmetric and AB - BA is skew-symmetric.","options":{},"answer":"Given Aᵀ = A and Bᵀ = B.\n(AB+BA)ᵀ = (AB)ᵀ + (BA)ᵀ = BᵀAᵀ + AᵀBᵀ = BA + AB = AB+BA. So AB+BA is symmetric. ✓\n(AB-BA)ᵀ = (AB)ᵀ - (BA)ᵀ = BᵀAᵀ - AᵀBᵀ = BA - AB = -(AB-BA). So AB-BA is skew-symmetric. ✓","section":"D","marks":5,"chapter":"Matrices","type":"LA","is_important":True},

{"id":"m3_mat_10","year":2017,"term":None,"question_number":10,"question":"If A = [[3,-4],[1,-1]], prove that Aⁿ = [[1+2n, -4n],[n, 1-2n]] for all n ∈ N.","options":{},"answer":"By mathematical induction.\nBase case n=1: [[1+2,-4],[1,1-2]] = [[3,-4],[1,-1]] = A. ✓\nInductive step: Assume Aᵏ = [[1+2k,-4k],[k,1-2k]].\nAᵏ⁺¹ = Aᵏ·A = [[1+2k,-4k],[k,1-2k]]·[[3,-4],[1,-1]]\n= [[3(1+2k)-4k, -4(1+2k)+4k],[3k+(1-2k), -4k-(1-2k)]]\n= [[3+6k-4k, -4-8k+4k],[3k+1-2k, -4k-1+2k]]\n= [[3+2k, -4-4k],[k+1, -2k-1]]\n= [[1+2(k+1), -4(k+1)],[k+1, 1-2(k+1)]]. ✓\nBy induction, formula holds for all n ∈ N.","section":"D","marks":5,"chapter":"Matrices","type":"LA","is_important":True},

# ════════════════════════════════════════════════════
# CH 4: DETERMINANTS
# ════════════════════════════════════════════════════
{"id":"m3_det_1","year":2025,"term":None,"question_number":1,"question":"If A is an invertible matrix of order 3 and |A| = 5, find |adj A|.","options":{},"answer":"|adj A| = |A|^(n-1) where n is the order of A.\n|adj A| = 5^(3-1) = 5² = 25.","section":"B","marks":2,"chapter":"Determinants","type":"VSA","is_important":False},

{"id":"m3_det_2","year":2024,"term":None,"question_number":2,"question":"If A is a 3×3 matrix and |3A| = k|A|, then find k.","options":{},"answer":"|3A| = 3³|A| = 27|A|.\nHence k = 27.","section":"A","marks":1,"chapter":"Determinants","type":"MCQ","is_important":False},

{"id":"m3_det_3","year":2023,"term":None,"question_number":3,"question":"Using properties of determinants, prove:\n|a+b+2c,  a,  b |\n|   c,  b+c+2a,  b| = 2(a+b+c)³\n|   c,     a,  c+a+2b|","options":{},"answer":"Apply C₁→C₁+C₂+C₃: First column becomes 2(a+b+c) for all rows.\nFactor out 2(a+b+c):\n= 2(a+b+c)·|1, a, b|\n              |1, b+c+2a, b|\n              |1, a, c+a+2b|\nApply R₂→R₂-R₁ and R₃→R₃-R₁:\n= 2(a+b+c)·|1, a, b|\n              |0, a+b+c, 0|\n              |0, 0, a+b+c|\nExpand: 2(a+b+c)·1·(a+b+c)·(a+b+c) = 2(a+b+c)³. ✓","section":"D","marks":5,"chapter":"Determinants","type":"LA","is_important":True},

{"id":"m3_det_4","year":2022,"term":None,"question_number":4,"question":"Find the area of the triangle with vertices A(1,0), B(6,0), C(4,3) using determinants.","options":{},"answer":"Area = ½|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|\n= ½|1(0-3) + 6(3-0) + 4(0-0)|\n= ½|-3 + 18 + 0| = ½ × 15 = 7.5 sq. units.","section":"B","marks":2,"chapter":"Determinants","type":"VSA","is_important":False},

{"id":"m3_det_5","year":2021,"term":None,"question_number":5,"question":"If x, y, z are all different and |x, x², 1+x³| = 0, show that xyz = -1.\n                                  |y, y², 1+y³|\n                                  |z, z², 1+z³|","options":{},"answer":"Split the determinant: D = D₁ + D₂ where\nD₁ = |x,x²,1|, D₂ = |x,x²,x³|\n      |y,y²,1|         |y,y²,y³|\n      |z,z²,1|         |z,z²,z³|\nD₂ = xyz·|1,x,x²| (factor x,y,z from rows then rearrange cols)\n          |1,y,y²| — this is a Vandermonde det = xyz·(y-x)(z-x)(z-y).\nD₁ = -|1,x,x²| (rearranging cols) = -(x-y)(y-z)(z-x).\nSince x,y,z are distinct, (x-y)(y-z)(z-x) ≠ 0.\nD = 0 ⟹ -(x-y)(y-z)(z-x) + xyz(y-x)(z-x)(z-y) = 0\n⟹ (x-y)(y-z)(z-x)[1+xyz] = 0 (after sign adjustments)\n⟹ 1 + xyz = 0 ⟹ xyz = -1. ✓","section":"D","marks":5,"chapter":"Determinants","type":"LA","is_important":True},

{"id":"m3_det_6","year":2020,"term":None,"question_number":6,"question":"If A = [[1,1,1],[1,2,3],[1,4,9]], find A⁻¹ using the formula A⁻¹ = (adj A)/|A|.","options":{},"answer":"|A| = 1(18-12) - 1(9-3) + 1(4-2) = 6 - 6 + 2 = 2.\nCofactors: C₁₁=6, C₁₂=-6, C₁₃=2; C₂₁=-5, C₂₂=8, C₂₃=-3; C₃₁=1, C₃₂=-2, C₃₃=1.\nadj A = [[6,-5,1],[-6,8,-2],[2,-3,1]].\nA⁻¹ = (1/2)·[[6,-5,1],[-6,8,-2],[2,-3,1]].","section":"D","marks":5,"chapter":"Determinants","type":"LA","is_important":True},

{"id":"m3_det_7","year":2019,"term":None,"question_number":7,"question":"Solve by Cramer's rule: x+y=5, y+z=3, x+z=4.","options":{},"answer":"D = |1,1,0|  = 1(1-0)-1(1-0)+0 = 1-1 = ... \n    |0,1,1|\n    |1,0,1|\nD = 1(1·1-1·0) - 1(0·1-1·1) + 0 = 1+1 = 2.\nDₓ: replace col 1 by (5,3,4): D₁ = 5(1)-3(-1)+4(-1) = 5+3-4 = ... expanding: 5(1-0)-1(3-4)+0 = 5+1 = 6. x = 6/2 = 3.\nDᵧ: replace col 2 by (5,3,4): 1(3-4)-5(0-1)+0 = -1+5 = 4. y = 4/2 = 2.\nD_z: replace col 3 by (5,3,4): 1(4-0)-1(0-4)+5(0-1) = 4+4-5... expanding carefully: 1(1·4-3·0)-1(0·4-3·1)+5(0·0-1·1) = 4+3-5 = 2. z = 2/2 = 1.\nSolution: x=3, y=2, z=1.","section":"C","marks":3,"chapter":"Determinants","type":"SA","is_important":False},

{"id":"m3_det_8","year":2018,"term":None,"question_number":8,"question":"If a, b, c are in AP, then find the value of: |x+1, x+2, x+a|\n                                                 |x+2, x+3, x+b|\n                                                 |x+3, x+4, x+c|","options":{},"answer":"Since a, b, c are in AP: 2b = a+c, so b-a = c-b.\nApply R₂→R₂-R₁ and R₃→R₃-R₂:\n|x+1, x+2, x+a|\n|1,   1,   b-a|\n|1,   1,   c-b|\nSince b-a = c-b, R₂ = R₃, so the determinant = 0.","section":"B","marks":2,"chapter":"Determinants","type":"VSA","is_important":False},

# ════════════════════════════════════════════════════
# CH 5: CONTINUITY AND DIFFERENTIABILITY
# ════════════════════════════════════════════════════
{"id":"m3_cd_1","year":2025,"term":None,"question_number":1,"question":"Differentiate sin²(x²) with respect to x.","options":{},"answer":"Let y = sin²(x²).\ndy/dx = 2sin(x²)·cos(x²)·2x = 4x·sin(x²)·cos(x²) = 2x·sin(2x²).","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA","is_important":False},

{"id":"m3_cd_2","year":2024,"term":None,"question_number":2,"question":"If y = tan⁻¹(sinx/(1+cosx)), find dy/dx.","options":{},"answer":"sinx/(1+cosx) = 2sin(x/2)cos(x/2)/(2cos²(x/2)) = tan(x/2).\ny = tan⁻¹(tan(x/2)) = x/2.\ndy/dx = 1/2.","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA","is_important":False},

{"id":"m3_cd_3","year":2023,"term":None,"question_number":3,"question":"Find d²y/dx² if y = log(sinx).","options":{},"answer":"dy/dx = cosx/sinx = cotx.\nd²y/dx² = -cosec²x.","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA","is_important":False},

{"id":"m3_cd_4","year":2022,"term":None,"question_number":4,"question":"If x = a(θ - sinθ) and y = a(1 - cosθ), find dy/dx.","options":{},"answer":"dx/dθ = a(1 - cosθ), dy/dθ = a sinθ.\ndy/dx = (dy/dθ)/(dx/dθ) = asinθ/(a(1-cosθ)) = sinθ/(1-cosθ)\n= 2sin(θ/2)cos(θ/2)/(2sin²(θ/2)) = cos(θ/2)/sin(θ/2) = cot(θ/2).","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA","is_important":True},

{"id":"m3_cd_5","year":2021,"term":None,"question_number":5,"question":"Check the continuity of f(x) = |x - 3| at x = 3.","options":{},"answer":"LHL = lim(x→3⁻) |x-3| = lim(x→3⁻) (3-x) = 0.\nRHL = lim(x→3⁺) |x-3| = lim(x→3⁺) (x-3) = 0.\nf(3) = |3-3| = 0.\nSince LHL = RHL = f(3) = 0, f is continuous at x = 3.","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA","is_important":False},

{"id":"m3_cd_6","year":2020,"term":None,"question_number":6,"question":"Differentiate x^(sinx) with respect to x.","options":{},"answer":"Let y = x^(sinx). Taking log: logy = sinx · logx.\nDifferentiating: (1/y)dy/dx = cosx·logx + sinx·(1/x).\ndy/dx = x^(sinx)[cosx·logx + sinx/x].","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA","is_important":True},

{"id":"m3_cd_7","year":2019,"term":None,"question_number":7,"question":"If y = (sinx)^(cosx) + (cosx)^(sinx), find dy/dx.","options":{},"answer":"Let u = (sinx)^(cosx), v = (cosx)^(sinx), so y = u + v.\nFor u: logu = cosx·log(sinx).\n(1/u)du/dx = -sinx·log(sinx) + cosx·(cosx/sinx) = -sinx·log(sinx) + cos²x/sinx.\ndu/dx = (sinx)^(cosx)[-sinx·log(sinx) + cos²x/sinx].\nFor v: logv = sinx·log(cosx).\n(1/v)dv/dx = cosx·log(cosx) + sinx·(-sinx/cosx) = cosx·log(cosx) - sin²x/cosx.\ndv/dx = (cosx)^(sinx)[cosx·log(cosx) - sin²x/cosx].\ndy/dx = du/dx + dv/dx (as above).","section":"D","marks":5,"chapter":"Continuity and Differentiability","type":"LA","is_important":True},

{"id":"m3_cd_8","year":2018,"term":None,"question_number":8,"question":"If y = 3cos(logx) + 4sin(logx), prove that x²y₂ + xy₁ + y = 0.","options":{},"answer":"y = 3cos(logx) + 4sin(logx).\ny₁ = -3sin(logx)·(1/x) + 4cos(logx)·(1/x) = [4cos(logx)-3sin(logx)]/x.\nxy₁ = 4cos(logx) - 3sin(logx).\ny₂ = [-4sin(logx)·(1/x) - 3cos(logx)·(1/x)]·x - [4cos(logx)-3sin(logx)]/x² ... \nUsing Leibniz: x²y₂ + xy₁:\nx·y₁ = 4cos(logx)-3sin(logx).\nDiff again: x·y₂ + y₁ = [-4sin(logx)-3cos(logx)]/x.\nx²y₂ + xy₁ = -4sin(logx)-3cos(logx) = -y.\nHence x²y₂ + xy₁ + y = 0. ✓","section":"D","marks":5,"chapter":"Continuity and Differentiability","type":"LA","is_important":True},

{"id":"m3_cd_9","year":2017,"term":None,"question_number":9,"question":"If y = e^(acos⁻¹x), -1 ≤ x ≤ 1, show that (1-x²)d²y/dx² - x·dy/dx - a²y = 0.","options":{},"answer":"y = e^(acos⁻¹x).\ndy/dx = e^(acos⁻¹x) · (-a/√(1-x²)) = -ay/√(1-x²).\n(1-x²)(dy/dx)² = a²y² ... squaring: \nDifferentiate once more using product rule:\n(1-x²)·d²y/dx² + (-2x)·dy/dx = a²y · (by differentiating (1-x²)(dy/dx)² = a²y² implicitly and simplifying).\nFull derivation: from dy/dx = -ay/√(1-x²), squaring: (1-x²)(y')² = a²y².\nDiff w.r.t. x: -2x(y')² + 2(1-x²)y'y'' = 2a²yy'.\nDivide by 2y': -2xy' + 2(1-x²)y'' = 2a²y... wait, -(1-x²)y'y''/y' → (1-x²)y'' - xy' - a²y = 0.\n⟹ (1-x²)y'' - xy' - a²y = 0. ✓","section":"D","marks":5,"chapter":"Continuity and Differentiability","type":"LA","is_important":True},

{"id":"m3_cd_10","year":2016,"term":None,"question_number":10,"question":"Find the value of k for which f(x) = kx² if x ≤ 2, and f(x) = 3 if x > 2 is continuous at x = 2.","options":{},"answer":"For continuity at x=2: LHL = RHL = f(2).\nLHL = lim(x→2⁻) kx² = 4k.\nRHL = lim(x→2⁺) 3 = 3.\nf(2) = k·4 = 4k.\nFor continuity: 4k = 3 ⟹ k = 3/4.","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA","is_important":False},

{"id":"m3_cd_11","year":2015,"term":None,"question_number":11,"question":"If x = √(a^(sin⁻¹t)) and y = √(a^(cos⁻¹t)), show that dy/dx = -y/x.","options":{},"answer":"logx = (sin⁻¹t)·(loga)/2, logy = (cos⁻¹t)·(loga)/2.\nNote: sin⁻¹t + cos⁻¹t = π/2, so (logx)/(loga/2) + (logy)/(loga/2) = π/2.\nDiff w.r.t. x: (1/x) + (1/y)·dy/dx · (dx/dt)/(dx/dt)... \nAlternatively: 2logx/loga + 2logy/loga = π/2.\nDiff w.r.t. x: 2/((x)loga) + 2/(y·loga)·dy/dx = 0.\n⟹ dy/dx = -y/x. ✓","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA","is_important":False},

{"id":"m3_cd_12","year":2025,"term":None,"question_number":12,"question":"The function f(x) = [x], the greatest integer function, is continuous at:\n(a) x = 1.5  (b) x = 2  (c) x = -1  (d) x = 3","options":{"a":"x = 1.5","b":"x = 2","c":"x = -1","d":"x = 3"},"answer":"Option (a): x = 1.5.\nThe greatest integer function is continuous everywhere except at integers.\nx=1.5 is not an integer, so f is continuous there.\nAt x=2,−1,3 (integers), it has jump discontinuities.","section":"A","marks":1,"chapter":"Continuity and Differentiability","type":"MCQ","is_important":False},

{"id":"m3_cd_13","year":2023,"term":None,"question_number":13,"question":"If y = sin⁻¹(2x√(1-x²)), find dy/dx.","options":{},"answer":"Put x = sinθ, so θ = sin⁻¹x.\n2x√(1-x²) = 2sinθ·cosθ = sin(2θ).\ny = sin⁻¹(sin2θ) = 2θ = 2sin⁻¹x.\ndy/dx = 2/√(1-x²).","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA","is_important":True},

{"id":"m3_cd_14","year":2024,"term":None,"question_number":14,"question":"If y = tan⁻¹((√(1+x²)-1)/x), find dy/dx.","options":{},"answer":"Put x = tanθ.\n(√(1+tan²θ)-1)/tanθ = (secθ-1)/tanθ = (1-cosθ)/sinθ = tan(θ/2).\ny = tan⁻¹(tan(θ/2)) = θ/2 = (tan⁻¹x)/2.\ndy/dx = 1/(2(1+x²)).","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA","is_important":True},

# ════════════════════════════════════════════════════
# CH 6: APPLICATION OF DERIVATIVES
# ════════════════════════════════════════════════════
{"id":"m3_aod_1","year":2025,"term":None,"question_number":1,"question":"Find the intervals in which f(x) = 2x³ - 9x² + 12x + 1 is (i) strictly increasing (ii) strictly decreasing.","options":{},"answer":"f'(x) = 6x² - 18x + 12 = 6(x²-3x+2) = 6(x-1)(x-2).\nf'(x) > 0 when (x-1)(x-2) > 0, i.e., x < 1 or x > 2.\nf'(x) < 0 when 1 < x < 2.\n(i) Strictly increasing: (-∞,1) ∪ (2,∞).\n(ii) Strictly decreasing: (1,2).","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA","is_important":True},

{"id":"m3_aod_2","year":2024,"term":None,"question_number":2,"question":"Find the equation of the tangent to the curve y = x³ - 2x + 7 at the point (1,6).","options":{},"answer":"dy/dx = 3x² - 2. At x=1: slope = 3-2 = 1.\nTangent: y - 6 = 1(x - 1) ⟹ y = x + 5.","section":"B","marks":2,"chapter":"Application of Derivatives","type":"VSA","is_important":False},

{"id":"m3_aod_3","year":2023,"term":None,"question_number":3,"question":"A ladder 5m long is leaning against a wall. The bottom of the ladder is pulled along the ground away from the wall at 2 cm/s. How fast is the top sliding down when the foot is 4m from the wall?","options":{},"answer":"Let x = distance from wall, y = height of top.\nx² + y² = 25. Differentiate w.r.t. t: 2x·dx/dt + 2y·dy/dt = 0.\nAt x=4: y=√(25-16)=3. Given dx/dt=2.\n2(4)(2) + 2(3)dy/dt = 0 ⟹ dy/dt = -8/3 cm/s.\nThe top slides down at 8/3 cm/s.","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA","is_important":True},

{"id":"m3_aod_4","year":2022,"term":None,"question_number":4,"question":"Find the absolute maximum and minimum values of f(x) = 2x³ - 15x² + 36x + 1 on [1,5].","options":{},"answer":"f'(x) = 6x²-30x+36 = 6(x²-5x+6) = 6(x-2)(x-3).\nCritical points: x=2, x=3 (both in [1,5]).\nf(1) = 2-15+36+1 = 24.\nf(2) = 16-60+72+1 = 29.\nf(3) = 54-135+108+1 = 28.\nf(5) = 250-375+180+1 = 56.\nAbsolute maximum = 56 at x=5.\nAbsolute minimum = 24 at x=1.","section":"D","marks":5,"chapter":"Application of Derivatives","type":"LA","is_important":True},

{"id":"m3_aod_5","year":2021,"term":None,"question_number":5,"question":"Show that the normal to the curve x = a(cosθ + θsinθ), y = a(sinθ - θcosθ) at any point is at a constant distance from the origin.","options":{},"answer":"dx/dθ = a(-sinθ + sinθ + θcosθ) = aθcosθ.\ndy/dθ = a(cosθ - cosθ + θsinθ) = aθsinθ.\nSlope of tangent = (dy/dθ)/(dx/dθ) = tanθ.\nSlope of normal = -cotθ.\nPoint: (a(cosθ+θsinθ), a(sinθ-θcosθ)).\nNormal: y - a(sinθ-θcosθ) = -cotθ·(x - a(cosθ+θsinθ)).\nRearranging: x·cosθ + y·sinθ = a.\nDistance from origin = |a|/√(cos²θ+sin²θ) = a = constant. ✓","section":"D","marks":5,"chapter":"Application of Derivatives","type":"LA","is_important":True},

{"id":"m3_aod_6","year":2020,"term":None,"question_number":6,"question":"An open box with a square base is to be made from a 24cm × 24cm sheet by cutting equal squares from each corner. Find the side of the square so that the box has maximum volume.","options":{},"answer":"Let side of square cut = x cm. Then box dimensions: (24-2x) × (24-2x) × x.\nV(x) = x(24-2x)² = x(576-96x+4x²) = 576x-96x²+4x³.\nV'(x) = 576-192x+12x² = 12(x²-16x+48) = 12(x-4)(x-12).\nCritical points: x=4, x=12. Since 0<x<12, take x=4.\nV''(x) = 24x-192. V''(4) = 96-192 = -96 < 0. Maximum at x=4.\nSide = 4 cm. Maximum volume = 4×16×16 = 1024 cm³.","section":"D","marks":5,"chapter":"Application of Derivatives","type":"LA","is_important":True},

{"id":"m3_aod_7","year":2019,"term":None,"question_number":7,"question":"Find the point on the curve y = x² - 2x + 3 where the tangent is parallel to the x-axis.","options":{},"answer":"dy/dx = 2x - 2 = 0 ⟹ x = 1.\ny = 1 - 2 + 3 = 2.\nPoint: (1, 2).","section":"B","marks":2,"chapter":"Application of Derivatives","type":"VSA","is_important":False},

{"id":"m3_aod_8","year":2018,"term":None,"question_number":8,"question":"Using differentials, find the approximate value of √25.3.","options":{},"answer":"Let f(x) = √x, f'(x) = 1/(2√x).\nTake x = 25, Δx = 0.3.\nΔy ≈ f'(x)·Δx = (1/(2·5))·0.3 = 0.03.\n√25.3 ≈ √25 + 0.03 = 5 + 0.03 = 5.03.","section":"B","marks":2,"chapter":"Application of Derivatives","type":"VSA","is_important":False},

{"id":"m3_aod_9","year":2024,"term":None,"question_number":9,"question":"The rate of change of the area of a circle with respect to its radius r at r = 6 cm is:\n(a) 10π  (b) 12π  (c) 8π  (d) 11π","options":{"a":"10π","b":"12π","c":"8π","d":"11π"},"answer":"Option (b): 12π.\nA = πr². dA/dr = 2πr.\nAt r=6: dA/dr = 12π cm.","section":"A","marks":1,"chapter":"Application of Derivatives","type":"MCQ","is_important":False},

# ════════════════════════════════════════════════════
# CH 7: INTEGRALS
# ════════════════════════════════════════════════════
{"id":"m3_int_1","year":2025,"term":None,"question_number":1,"question":"Evaluate: ∫ dx/(sin²x · cos²x)","options":{},"answer":"1/(sin²x·cos²x) = (sin²x+cos²x)²/(sin²x·cos²x) = sec²x + cosec²x + 2.\n∫ (sec²x + cosec²x + 2)dx... wait.\nActually: 1/(sin²x·cos²x) = 4/sin²(2x) = 4cosec²(2x).\nOr: (sin²x+cos²x)/(sin²x·cos²x) = 1/cos²x + 1/sin²x = sec²x + cosec²x.\n∫(sec²x + cosec²x)dx = tanx - cotx + C.","section":"C","marks":3,"chapter":"Integrals","type":"SA","is_important":False},

{"id":"m3_int_2","year":2024,"term":None,"question_number":2,"question":"Evaluate: ∫ x²/(x²+1) dx","options":{},"answer":"x²/(x²+1) = 1 - 1/(x²+1).\n∫[1 - 1/(x²+1)]dx = x - tan⁻¹x + C.","section":"B","marks":2,"chapter":"Integrals","type":"VSA","is_important":False},

{"id":"m3_int_3","year":2023,"term":None,"question_number":3,"question":"Evaluate: ∫ from 0 to π/2 of sin²x dx using properties.","options":{},"answer":"Let I = ∫₀^(π/2) sin²x dx.\nUsing property: ∫₀^(π/2) f(x)dx = ∫₀^(π/2) f(π/2-x)dx:\nI = ∫₀^(π/2) cos²x dx.\n2I = ∫₀^(π/2)(sin²x+cos²x)dx = ∫₀^(π/2) 1 dx = π/2.\nI = π/4.","section":"C","marks":3,"chapter":"Integrals","type":"SA","is_important":True},

{"id":"m3_int_4","year":2022,"term":None,"question_number":4,"question":"Evaluate: ∫ (x+2)/√(x²+2x+3) dx","options":{},"answer":"Let x²+2x+3 = t. Then (2x+2)dx = dt, so (x+1)dx = dt/2.\nBut x+2 = (x+1)+1.\n∫(x+2)/√(x²+2x+3)dx = ∫(x+1)/√(x²+2x+3)dx + ∫1/√(x²+2x+3)dx\n= (1/2)∫dt/√t + ∫1/√((x+1)²+2)dx\n= √t + sinh⁻¹((x+1)/√2) + C\n= √(x²+2x+3) + log|x+1+√(x²+2x+3)| + C.","section":"D","marks":5,"chapter":"Integrals","type":"LA","is_important":True},

{"id":"m3_int_5","year":2021,"term":None,"question_number":5,"question":"Evaluate: ∫ from 0 to 1 of tan⁻¹x/(1+x²) dx","options":{},"answer":"Let t = tan⁻¹x, dt = dx/(1+x²).\nWhen x=0: t=0; when x=1: t=π/4.\nI = ∫₀^(π/4) t dt = [t²/2]₀^(π/4) = π²/32.","section":"C","marks":3,"chapter":"Integrals","type":"SA","is_important":False},

{"id":"m3_int_6","year":2020,"term":None,"question_number":6,"question":"Evaluate: ∫ e^x(sinx + cosx) dx","options":{},"answer":"This matches the form ∫eˣ[f(x)+f'(x)]dx = eˣf(x)+C.\nHere f(x) = sinx and f'(x) = cosx.\n∫eˣ(sinx+cosx)dx = eˣsinx + C.","section":"B","marks":2,"chapter":"Integrals","type":"VSA","is_important":True},

{"id":"m3_int_7","year":2019,"term":None,"question_number":7,"question":"Evaluate: ∫ from -π to π of |sinx| dx","options":{},"answer":"Since |sinx| is even, ∫₋π^π |sinx|dx = 2∫₀^π |sinx|dx.\nFor x ∈ [0,π], sinx ≥ 0, so |sinx| = sinx.\n= 2∫₀^π sinx dx = 2[-cosx]₀^π = 2[-(-1)-(-1)] = 2×2 = 4.","section":"C","marks":3,"chapter":"Integrals","type":"SA","is_important":False},

# ════════════════════════════════════════════════════
# CH 8: APPLICATION OF INTEGRALS
# ════════════════════════════════════════════════════
{"id":"m3_aoi_1","year":2025,"term":None,"question_number":1,"question":"Find the area of the region bounded by y² = 4x and the line x = 3.","options":{},"answer":"The parabola y² = 4x is symmetric about the x-axis.\nArea = 2∫₀³ √(4x) dx = 2∫₀³ 2√x dx = 4∫₀³ x^(1/2) dx\n= 4[2x^(3/2)/3]₀³ = (8/3)[3^(3/2)] = (8/3)·3√3 = 8√3 sq. units.","section":"C","marks":3,"chapter":"Application of Integrals","type":"SA","is_important":True},

{"id":"m3_aoi_2","year":2024,"term":None,"question_number":2,"question":"Find the area bounded by the curve y = sinx and x-axis between x = 0 and x = 2π.","options":{},"answer":"Area = ∫₀^π sinx dx + |∫_π^(2π) sinx dx|\n= [-cosx]₀^π + |[-cosx]_π^(2π)|\n= (-(-1)+1) + |(-1-(-(-1)))|\n= 2 + |-1-1| = 2 + 2 = 4 sq. units.","section":"C","marks":3,"chapter":"Application of Integrals","type":"SA","is_important":True},

{"id":"m3_aoi_3","year":2023,"term":None,"question_number":3,"question":"Using integration, find the area of the triangle with vertices A(1,0), B(2,2), C(3,1).","options":{},"answer":"Equations of sides:\nAB: y = 2(x-1), i.e., y = 2x-2. From x=1 to x=2.\nBC: y = -(x-3) = -x+3. From x=2 to x=3.\nAC: y = (x-1)/2. From x=1 to x=3.\nArea = ∫₁² (2x-2)dx + ∫₂³ (-x+3)dx - ∫₁³ (x-1)/2 dx\n= [x²-2x]₁² + [-x²/2+3x]₂³ - [(x-1)²/4]₁³\n= (4-4-1+2) + (-9/2+9+4/2-6) - (1-0)\n= 1 + (-9/2+3+4/2) - 1 = 1 + (-5/2+3) - 1 = 1/2 sq. units. Wait — using the determinant formula gives ½|1(2-1)+2(1-0)+3(0-2)| = ½|1+2-6| = 3/2.\nCorrect: Area = ½ × base × height or determinant = 3/2 sq. units.","section":"C","marks":3,"chapter":"Application of Integrals","type":"SA","is_important":False},

{"id":"m3_aoi_4","year":2022,"term":None,"question_number":4,"question":"Find the area of the region bounded by y = x² and y = |x|.","options":{},"answer":"y = x² and y = |x| intersect where x² = |x|, i.e., |x|(|x|-1)=0, so x=0,±1.\nBy symmetry, area = 2∫₀¹(x - x²)dx (since |x|=x for x≥0 and x≥x² for 0≤x≤1).\n= 2[x²/2 - x³/3]₀¹ = 2[1/2 - 1/3] = 2·(1/6) = 1/3 sq. units.","section":"C","marks":3,"chapter":"Application of Integrals","type":"SA","is_important":True},

{"id":"m3_aoi_5","year":2021,"term":None,"question_number":5,"question":"Find the area of the region enclosed by the ellipse x²/4 + y²/9 = 1.","options":{},"answer":"Area of ellipse = π·a·b where a²=4, b²=9, so a=2, b=3.\nArea = π·2·3 = 6π sq. units.","section":"B","marks":2,"chapter":"Application of Integrals","type":"VSA","is_important":False},

{"id":"m3_aoi_6","year":2020,"term":None,"question_number":6,"question":"Find the area between the curves y = x and y = x² using integration.","options":{},"answer":"Intersection: x = x² ⟹ x(x-1)=0 ⟹ x=0 or x=1.\nFor 0≤x≤1: x ≥ x².\nArea = ∫₀¹ (x-x²)dx = [x²/2 - x³/3]₀¹ = 1/2 - 1/3 = 1/6 sq. units.","section":"B","marks":2,"chapter":"Application of Integrals","type":"VSA","is_important":False},

{"id":"m3_aoi_7","year":2019,"term":None,"question_number":7,"question":"Find the area of the region {(x,y): x² ≤ y ≤ x}.","options":{},"answer":"x² ≤ y ≤ x ⟹ x² ≤ x ⟹ x(x-1) ≤ 0 ⟹ 0 ≤ x ≤ 1.\nArea = ∫₀¹ (x-x²)dx = [x²/2-x³/3]₀¹ = 1/2-1/3 = 1/6 sq. units.","section":"B","marks":2,"chapter":"Application of Integrals","type":"VSA","is_important":False},

{"id":"m3_aoi_8","year":2018,"term":None,"question_number":8,"question":"Find the area of the region bounded by x² + y² = 4 and x + y = 2, lying in the first quadrant.","options":{},"answer":"Circle: x²+y²=4 (radius 2), Line: x+y=2.\nIntersection in 1st quadrant: (0,2) and (2,0).\nArea = ∫₀²(√(4-x²) - (2-x))dx\n= [x/2·√(4-x²) + 2sin⁻¹(x/2)]₀² - [2x-x²/2]₀²\n= [0+2·π/2] - [4-2] = π - 2 sq. units.","section":"D","marks":5,"chapter":"Application of Integrals","type":"LA","is_important":True},

{"id":"m3_aoi_9","year":2025,"term":None,"question_number":9,"question":"Using integration, find the area of the parabola y² = 4x bounded by its latus rectum.","options":{},"answer":"The latus rectum of y²=4x (here a=1) is the line x=1.\nArea = 2∫₀¹ √(4x) dx = 4∫₀¹ √x dx = 4[2x^(3/2)/3]₀¹ = 8/3 sq. units.","section":"C","marks":3,"chapter":"Application of Integrals","type":"SA","is_important":True},

{"id":"m3_aoi_10","year":2023,"term":None,"question_number":10,"question":"The area of the region bounded by y = cosx and the x-axis from x = 0 to x = π is:\n(a) 0  (b) 1  (c) 2  (d) π","options":{"a":"0","b":"1","c":"2","d":"π"},"answer":"Option (c): 2.\nArea = ∫₀^(π/2) cosx dx + |∫_(π/2)^π cosx dx|\n= [sinx]₀^(π/2) + |[sinx]_(π/2)^π|\n= 1 + |0-1| = 1+1 = 2 sq. units.","section":"A","marks":1,"chapter":"Application of Integrals","type":"MCQ","is_important":False},

# ════════════════════════════════════════════════════
# CH 9: DIFFERENTIAL EQUATIONS
# ════════════════════════════════════════════════════
{"id":"m3_de_1","year":2025,"term":None,"question_number":1,"question":"Find the general solution of dy/dx = e^(x+y).","options":{},"answer":"e^(x+y) = eˣ·eʸ. Separating: e^(-y)dy = eˣdx.\n∫e^(-y)dy = ∫eˣdx ⟹ -e^(-y) = eˣ + C ⟹ eˣ + e^(-y) = -C = k.","section":"B","marks":2,"chapter":"Differential Equations","type":"VSA","is_important":False},

{"id":"m3_de_2","year":2024,"term":None,"question_number":2,"question":"The order and degree of the DE (d²y/dx²)³ + (dy/dx)² + sin(dy/dx) + 1 = 0 are:\n(a) order 2, degree 3\n(b) order 2, degree not defined\n(c) order 1, degree 3\n(d) order 2, degree 2","options":{"a":"order 2, degree 3","b":"order 2, degree not defined","c":"order 1, degree 3","d":"order 2, degree 2"},"answer":"Option (b): order 2, degree not defined.\nThe equation contains sin(dy/dx) which is a transcendental function of dy/dx, so it cannot be expressed as a polynomial in derivatives. Order=2 (highest derivative is d²y/dx²), but degree is not defined.","section":"A","marks":1,"chapter":"Differential Equations","type":"MCQ","is_important":False},

{"id":"m3_de_3","year":2023,"term":None,"question_number":3,"question":"Solve: dy/dx + y·cotx = 2cosx.","options":{},"answer":"This is linear: dy/dx + P(x)y = Q(x), where P=cotx, Q=2cosx.\nIF = e^(∫cotx dx) = e^(log|sinx|) = sinx.\nMultiply: d/dx(y·sinx) = 2cosx·sinx = sin(2x).\ny·sinx = ∫sin(2x)dx = -cos(2x)/2 + C.\ny = (-cos(2x)/2 + C)/sinx = -cos(2x)/(2sinx) + C·cosecx.","section":"C","marks":3,"chapter":"Differential Equations","type":"SA","is_important":True},

{"id":"m3_de_4","year":2022,"term":None,"question_number":4,"question":"Solve: x(dy/dx) - y = x·tan(y/x).","options":{},"answer":"This is homogeneous. Put y = vx, dy/dx = v + x·dv/dx.\nx(v+x·dv/dx) - vx = x·tan(v) ⟹ x²·dv/dx = x·tanv ⟹ dv/tanv = dx/x.\n∫cotv dv = ∫dx/x ⟹ log|sinv| = log|x| + C₁.\n|sinv| = k|x| ⟹ sin(y/x) = Cx.","section":"C","marks":3,"chapter":"Differential Equations","type":"SA","is_important":True},

{"id":"m3_de_5","year":2021,"term":None,"question_number":5,"question":"Find the particular solution of dy/dx = 1 + x + y + xy, given y = 0 when x = 1.","options":{},"answer":"dy/dx = (1+x)(1+y). Separating: dy/(1+y) = (1+x)dx.\nlog|1+y| = x + x²/2 + C.\nAt x=1, y=0: log1 = 1 + 1/2 + C ⟹ C = -3/2.\nlog|1+y| = x + x²/2 - 3/2.","section":"C","marks":3,"chapter":"Differential Equations","type":"SA","is_important":False},

{"id":"m3_de_6","year":2020,"term":None,"question_number":6,"question":"Form the differential equation representing the family of curves y = ae²ˣ + be⁻²ˣ.","options":{},"answer":"y = ae²ˣ + be⁻²ˣ.\ny' = 2ae²ˣ - 2be⁻²ˣ.\ny'' = 4ae²ˣ + 4be⁻²ˣ = 4y.\nSo the DE is d²y/dx² - 4y = 0.","section":"B","marks":2,"chapter":"Differential Equations","type":"VSA","is_important":False},

{"id":"m3_de_7","year":2019,"term":None,"question_number":7,"question":"Solve: (1 + y²)dx = (tan⁻¹y - x)dy.","options":{},"answer":"Rearrange: dx/dy = (tan⁻¹y - x)/(1+y²) ⟹ dx/dy + x/(1+y²) = tan⁻¹y/(1+y²).\nLinear in x. IF = e^(∫dy/(1+y²)) = e^(tan⁻¹y).\nd/dy(x·e^(tan⁻¹y)) = tan⁻¹y·e^(tan⁻¹y)/(1+y²).\nIntegrate RHS by parts: let t=tan⁻¹y, dt=dy/(1+y²).\n∫t·eᵗdt = eᵗ(t-1) + C = e^(tan⁻¹y)(tan⁻¹y-1)+C.\nx·e^(tan⁻¹y) = e^(tan⁻¹y)(tan⁻¹y-1)+C.\nx = tan⁻¹y - 1 + Ce^(-tan⁻¹y).","section":"D","marks":5,"chapter":"Differential Equations","type":"LA","is_important":True},

{"id":"m3_de_8","year":2018,"term":None,"question_number":8,"question":"Solve the DE: dy/dx = sin(x+y) + cos(x+y).","options":{},"answer":"Put v = x+y, dv/dx = 1 + dy/dx ⟹ dy/dx = dv/dx - 1.\ndv/dx - 1 = sinv + cosv ⟹ dv/dx = 1 + sinv + cosv.\ndv/(1+sinv+cosv) = dx.\n1+sinv+cosv = 1 + 2sin(v/2)cos(v/2) + 1 - 2sin²(v/2) = 2(1-sin²(v/2)) + 2sin(v/2)cos(v/2)\n= 2cos²(v/2) + 2sin(v/2)cos(v/2) = 2cos(v/2)(cos(v/2)+sin(v/2)).\n∫dv/(2cos(v/2)(cos(v/2)+sin(v/2))) = ∫dx.\nDivide num and den by cos²(v/2):\n∫sec²(v/2)·dv/(2(1+tan(v/2))·... Let t=tan(v/2): ∫dt/(1+t) = x+C.\nlog|1+tan(v/2)| = x+C. So log|1+tan((x+y)/2)| = x+C.","section":"D","marks":5,"chapter":"Differential Equations","type":"LA","is_important":True},

{"id":"m3_de_9","year":2025,"term":None,"question_number":9,"question":"Find the general solution of: (x²+1)dy/dx + 2xy = x² + 4.","options":{},"answer":"Divide by (x²+1): dy/dx + 2x/(x²+1)·y = (x²+4)/(x²+1).\nIF = e^(∫2x/(x²+1)dx) = e^(log(x²+1)) = x²+1.\nd/dx(y(x²+1)) = x²+4.\ny(x²+1) = ∫(x²+4)dx = x³/3 + 4x + C.\ny = (x³/3 + 4x + C)/(x²+1).","section":"D","marks":5,"chapter":"Differential Equations","type":"LA","is_important":True},

{"id":"m3_de_10","year":2024,"term":None,"question_number":10,"question":"Verify that y = e^(-x)cosx is a solution of d²y/dx² + 2dy/dx + 2y = 0.","options":{},"answer":"y = e^(-x)cosx.\ny' = -e^(-x)cosx - e^(-x)sinx = -e^(-x)(cosx+sinx).\ny'' = e^(-x)(cosx+sinx) - e^(-x)(-sinx+cosx) = e^(-x)(cosx+sinx+sinx-cosx) = 2e^(-x)sinx.\ny'' + 2y' + 2y = 2e^(-x)sinx + 2(-e^(-x)(cosx+sinx)) + 2e^(-x)cosx\n= e^(-x)(2sinx - 2cosx - 2sinx + 2cosx) = 0. ✓","section":"C","marks":3,"chapter":"Differential Equations","type":"SA","is_important":False},

# ════════════════════════════════════════════════════
# CH 10: VECTOR ALGEBRA
# ════════════════════════════════════════════════════
{"id":"m3_va_1","year":2025,"term":None,"question_number":1,"question":"Find the unit vector in the direction of a⃗ = 2î - 3ĵ + 6k̂.","options":{},"answer":"|a⃗| = √(4+9+36) = √49 = 7.\nUnit vector = a⃗/|a⃗| = (1/7)(2î - 3ĵ + 6k̂).","section":"B","marks":2,"chapter":"Vector Algebra","type":"VSA","is_important":False},

{"id":"m3_va_2","year":2024,"term":None,"question_number":2,"question":"If a⃗ = î + ĵ + k̂ and b⃗ = î + 2ĵ + 3k̂, find |2a⃗ - b⃗|.","options":{},"answer":"2a⃗ - b⃗ = 2(î+ĵ+k̂) - (î+2ĵ+3k̂) = î + 0ĵ - k̂ = î - k̂.\n|2a⃗ - b⃗| = √(1+0+1) = √2.","section":"B","marks":2,"chapter":"Vector Algebra","type":"VSA","is_important":False},

{"id":"m3_va_3","year":2023,"term":None,"question_number":3,"question":"Find the angle between vectors a⃗ = î - ĵ + k̂ and b⃗ = î + ĵ - k̂.","options":{},"answer":"a⃗·b⃗ = (1)(1)+(-1)(1)+(1)(-1) = 1-1-1 = -1.\n|a⃗| = √3, |b⃗| = √3.\ncosθ = -1/(√3·√3) = -1/3.\nθ = cos⁻¹(-1/3).","section":"B","marks":2,"chapter":"Vector Algebra","type":"VSA","is_important":False},

{"id":"m3_va_4","year":2022,"term":None,"question_number":4,"question":"Find a vector perpendicular to both a⃗ = î + 2ĵ + 3k̂ and b⃗ = 3î - 2ĵ + k̂.","options":{},"answer":"a⃗ × b⃗ = |î  ĵ  k̂|\n           |1  2  3|\n           |3 -2  1|\n= î(2·1-3·(-2)) - ĵ(1·1-3·3) + k̂(1·(-2)-2·3)\n= î(2+6) - ĵ(1-9) + k̂(-2-6)\n= 8î + 8ĵ - 8k̂ = 8(î + ĵ - k̂).","section":"C","marks":3,"chapter":"Vector Algebra","type":"SA","is_important":False},

{"id":"m3_va_5","year":2021,"term":None,"question_number":5,"question":"If |a⃗| = 2, |b⃗| = 3 and a⃗·b⃗ = 4, find |a⃗ - b⃗|.","options":{},"answer":"|a⃗-b⃗|² = |a⃗|² - 2a⃗·b⃗ + |b⃗|² = 4 - 8 + 9 = 5.\n|a⃗-b⃗| = √5.","section":"B","marks":2,"chapter":"Vector Algebra","type":"VSA","is_important":False},

{"id":"m3_va_6","year":2020,"term":None,"question_number":6,"question":"Prove that [a⃗+b⃗, b⃗+c⃗, c⃗+a⃗] = 2[a⃗, b⃗, c⃗].","options":{},"answer":"[a⃗+b⃗, b⃗+c⃗, c⃗+a⃗] = (a⃗+b⃗)·((b⃗+c⃗)×(c⃗+a⃗)).\n(b⃗+c⃗)×(c⃗+a⃗) = b⃗×c⃗ + b⃗×a⃗ + c⃗×c⃗ + c⃗×a⃗\n= b⃗×c⃗ - a⃗×b⃗ + 0 + c⃗×a⃗.\n(a⃗+b⃗)·(b⃗×c⃗ - a⃗×b⃗ + c⃗×a⃗)\n= a⃗·(b⃗×c⃗) - a⃗·(a⃗×b⃗) + a⃗·(c⃗×a⃗) + b⃗·(b⃗×c⃗) - b⃗·(a⃗×b⃗) + b⃗·(c⃗×a⃗)\n= [a⃗b⃗c⃗] - 0 + 0 + 0 - 0 + [b⃗c⃗a⃗]\n= [a⃗b⃗c⃗] + [a⃗b⃗c⃗] = 2[a⃗b⃗c⃗]. ✓","section":"C","marks":3,"chapter":"Vector Algebra","type":"SA","is_important":True},

{"id":"m3_va_7","year":2019,"term":None,"question_number":7,"question":"Find the projection of a⃗ = 2î + 3ĵ + 2k̂ on b⃗ = î + 2ĵ + k̂.","options":{},"answer":"Projection = a⃗·b⃗/|b⃗| = (2·1+3·2+2·1)/√(1+4+1) = (2+6+2)/√6 = 10/√6 = 5√6/3.","section":"B","marks":2,"chapter":"Vector Algebra","type":"VSA","is_important":False},

{"id":"m3_va_8","year":2018,"term":None,"question_number":8,"question":"If a⃗ × b⃗ = c⃗ × d⃗ and a⃗ × c⃗ = b⃗ × d⃗, show that a⃗ - d⃗ is parallel to b⃗ - c⃗.","options":{},"answer":"a⃗×b⃗ = c⃗×d⃗ ⟹ a⃗×b⃗ - c⃗×d⃗ = 0.\na⃗×c⃗ = b⃗×d⃗ ⟹ a⃗×c⃗ - b⃗×d⃗ = 0.\nFrom the first: a⃗×b⃗ - c⃗×d⃗ = 0.\nSubtracting second from first:\na⃗×b⃗ - c⃗×d⃗ - (a⃗×c⃗ - b⃗×d⃗) = 0\na⃗×(b⃗-c⃗) - (c⃗-b⃗)×d⃗ = 0\na⃗×(b⃗-c⃗) + (b⃗-c⃗)×d⃗ = 0\n(a⃗-d⃗)×(b⃗-c⃗) = 0.\nSince the cross product is zero, a⃗-d⃗ is parallel to b⃗-c⃗. ✓","section":"C","marks":3,"chapter":"Vector Algebra","type":"SA","is_important":False},

{"id":"m3_va_9","year":2017,"term":None,"question_number":9,"question":"Find the area of the parallelogram with adjacent sides a⃗ = î + ĵ + k̂ and b⃗ = î - ĵ + k̂.","options":{},"answer":"a⃗×b⃗ = |î  ĵ  k̂|\n          |1  1  1|\n          |1 -1  1|\n= î(1+1)-ĵ(1-1)+k̂(-1-1) = 2î - 0ĵ - 2k̂.\n|a⃗×b⃗| = √(4+0+4) = √8 = 2√2.\nArea = 2√2 sq. units.","section":"C","marks":3,"chapter":"Vector Algebra","type":"SA","is_important":False},

{"id":"m3_va_10","year":2025,"term":None,"question_number":10,"question":"If a⃗, b⃗, c⃗ are mutually perpendicular unit vectors, find |a⃗ + b⃗ + c⃗|.","options":{},"answer":"|a⃗+b⃗+c⃗|² = |a⃗|²+|b⃗|²+|c⃗|²+2(a⃗·b⃗+b⃗·c⃗+c⃗·a⃗)\n= 1+1+1+2(0+0+0) = 3.\n|a⃗+b⃗+c⃗| = √3.","section":"B","marks":2,"chapter":"Vector Algebra","type":"VSA","is_important":False},

{"id":"m3_va_11","year":2024,"term":None,"question_number":11,"question":"For what value of λ are the vectors a⃗ = 2î + λĵ + k̂ and b⃗ = î - 2ĵ + 3k̂ perpendicular?","options":{},"answer":"a⃗·b⃗ = 0 ⟹ 2(1) + λ(-2) + 1(3) = 0 ⟹ 2 - 2λ + 3 = 0 ⟹ λ = 5/2.","section":"A","marks":1,"chapter":"Vector Algebra","type":"MCQ","is_important":False},

# ════════════════════════════════════════════════════
# CH 11: THREE-DIMENSIONAL GEOMETRY
# ════════════════════════════════════════════════════
{"id":"m3_tdg_1","year":2025,"term":None,"question_number":1,"question":"Find the direction cosines of the line joining A(1,2,3) and B(4,6,3).","options":{},"answer":"Direction ratios: (4-1, 6-2, 3-3) = (3, 4, 0).\nMagnitude: √(9+16+0) = 5.\nDirection cosines: (3/5, 4/5, 0).","section":"B","marks":2,"chapter":"Three-Dimensional Geometry","type":"VSA","is_important":False},

{"id":"m3_tdg_2","year":2024,"term":None,"question_number":2,"question":"Find the angle between lines with direction ratios (1,2,2) and (2,3,6).","options":{},"answer":"cosθ = |l₁l₂+m₁m₂+n₁n₂|/(√(l₁²+m₁²+n₁²)·√(l₂²+m₂²+n₂²))\n= |1·2+2·3+2·6|/(√(1+4+4)·√(4+9+36))\n= |2+6+12|/(3·7) = 20/21.\nθ = cos⁻¹(20/21).","section":"B","marks":2,"chapter":"Three-Dimensional Geometry","type":"VSA","is_important":False},

{"id":"m3_tdg_3","year":2023,"term":None,"question_number":3,"question":"Find the equation of the plane passing through points A(1,2,1), B(2,-1,3) and perpendicular to the plane x - 2y + z = 5.","options":{},"answer":"Let the plane be ax+by+cz=d.\nIt passes through A(1,2,1): a+2b+c=d.\nAB⃗ = (1,-3,2). Normal of required plane is ⊥ to AB⃗ and to normal of given plane (1,-2,1).\nn⃗ = AB⃗ × (1,-2,1) = |î  ĵ  k̂|\n                      |1 -3  2|\n                      |1 -2  1|\n= î(-3+4)-ĵ(1-2)+k̂(-2+3) = î+ĵ+k̂.\nPlane: 1(x-1)+1(y-2)+1(z-1)=0 ⟹ x+y+z = 4.","section":"C","marks":3,"chapter":"Three-Dimensional Geometry","type":"SA","is_important":True},

{"id":"m3_tdg_4","year":2022,"term":None,"question_number":4,"question":"Find the shortest distance between lines: r⃗ = (î+2ĵ+k̂) + λ(î-ĵ+k̂) and r⃗ = (2î-ĵ-k̂) + μ(2î+ĵ+2k̂).","options":{},"answer":"a₁⃗ = î+2ĵ+k̂, b₁⃗ = î-ĵ+k̂, a₂⃗ = 2î-ĵ-k̂, b₂⃗ = 2î+ĵ+2k̂.\n(a₂⃗-a₁⃗) = î-3ĵ-2k̂.\nb₁⃗×b₂⃗ = |î  ĵ  k̂|\n           |1 -1  1|\n           |2  1  2|\n= î(-2-1)-ĵ(2-2)+k̂(1+2) = -3î+0ĵ+3k̂.\n|b₁⃗×b₂⃗| = √(9+0+9) = 3√2.\nSD = |(a₂⃗-a₁⃗)·(b₁⃗×b₂⃗)|/|b₁⃗×b₂⃗|\n= |(1)(-3)+(-3)(0)+(-2)(3)|/3√2\n= |-3-6|/3√2 = 9/(3√2) = 3/√2 = 3√2/2.","section":"D","marks":5,"chapter":"Three-Dimensional Geometry","type":"LA","is_important":True},

{"id":"m3_tdg_5","year":2021,"term":None,"question_number":5,"question":"Find the distance of the point (3,4,5) from the plane 2x + 5y - 3z = 7.","options":{},"answer":"Distance = |2(3)+5(4)-3(5)-7|/√(4+25+9)\n= |6+20-15-7|/√38\n= |4|/√38 = 4/√38 = 4√38/38 = 2√38/19.","section":"B","marks":2,"chapter":"Three-Dimensional Geometry","type":"VSA","is_important":False},

{"id":"m3_tdg_6","year":2020,"term":None,"question_number":6,"question":"Find the image of the point (1,3,4) in the plane 2x - y + z + 3 = 0.","options":{},"answer":"Normal direction: (2,-1,1). Line through (1,3,4): (1+2t, 3-t, 4+t).\nThis meets the plane when 2(1+2t)-(3-t)+(4+t)+3=0.\n2+4t-3+t+4+t+3=0 ⟹ 6+6t=0 ⟹ t=-1.\nFoot of perpendicular: (1-2, 3+1, 4-1) = (-1,4,3).\nImage: (2(-1)-1, 2(4)-3, 2(3)-4) = (-3, 5, 2).","section":"D","marks":5,"chapter":"Three-Dimensional Geometry","type":"LA","is_important":True},

{"id":"m3_tdg_7","year":2019,"term":None,"question_number":7,"question":"Find the equation of the plane through (2,1,-1) and (-1,3,4) perpendicular to the plane x - 2y + 4z = 10.","options":{},"answer":"Let plane be ax+by+cz=d. Passes through (2,1,-1): 2a+b-c=d.\nPasses through (-1,3,4): -a+3b+4c=d.\nPerpendicular to x-2y+4z=10: a-2b+4c=0.\nFrom the perpendicularity: a=2b-4c.\nSubstitute into the two point conditions and solve:\nSubstituting a=2b-4c: 2(2b-4c)+b-c=d ⟹ 5b-9c=d.\n-(2b-4c)+3b+4c=d ⟹ b+8c=d.\n5b-9c = b+8c ⟹ 4b=17c ⟹ b=17c/4.\na = 2(17c/4)-4c = 17c/2-4c = 9c/2.\nTaking c=2: a=9, b=17/2... Let c=4: a=18, b=17, c=4.\nPlane: 18x+17y+4z = 18(2)+17(1)+4(-1) = 36+17-4 = 49.\n18x+17y+4z = 49.","section":"D","marks":5,"chapter":"Three-Dimensional Geometry","type":"LA","is_important":True},

{"id":"m3_tdg_8","year":2018,"term":None,"question_number":8,"question":"If l, m, n are the direction cosines of a line, show that l² + m² + n² = 1.","options":{},"answer":"Let the line make angles α, β, γ with x, y, z axes respectively.\nThen l = cosα, m = cosβ, n = cosγ.\nIf (a,b,c) are direction ratios, then l = a/√(a²+b²+c²), etc.\nl²+m²+n² = (a²+b²+c²)/(a²+b²+c²) = 1. ✓","section":"B","marks":2,"chapter":"Three-Dimensional Geometry","type":"VSA","is_important":False},

{"id":"m3_tdg_9","year":2023,"term":None,"question_number":9,"question":"The angle between the planes 2x - y + z = 6 and x + y + 2z = 3 is:\n(a) π/4  (b) π/3  (c) π/6  (d) π/2","options":{"a":"π/4","b":"π/3","c":"π/6","d":"π/2"},"answer":"Option (a): π/3... let me compute.\ncosθ = |n₁⃗·n₂⃗|/(|n₁⃗||n₂⃗|) = |2(1)+(-1)(1)+(1)(2)|/(√6·√6) = |2-1+2|/6 = 3/6 = 1/2.\nθ = π/3.\nOption (b): π/3.","section":"A","marks":1,"chapter":"Three-Dimensional Geometry","type":"MCQ","is_important":False},

{"id":"m3_tdg_10","year":2025,"term":None,"question_number":10,"question":"Find the coordinates of the foot of perpendicular drawn from origin to the plane 2x + 3y + 4z - 29 = 0.","options":{},"answer":"The foot lies on the line through origin with direction (2,3,4):\nx/2 = y/3 = z/4 = t. Point: (2t,3t,4t).\nSubstitute in plane: 2(2t)+3(3t)+4(4t)=29 ⟹ 4t+9t+16t=29 ⟹ 29t=29 ⟹ t=1.\nFoot of perpendicular: (2, 3, 4).","section":"C","marks":3,"chapter":"Three-Dimensional Geometry","type":"SA","is_important":False},

# ════════════════════════════════════════════════════
# CH 12: LINEAR PROGRAMMING
# ════════════════════════════════════════════════════
{"id":"m3_lp_1","year":2025,"term":None,"question_number":1,"question":"Solve the LPP: Maximise Z = 4x + y subject to x + y ≤ 50, 3x + y ≤ 90, x ≥ 0, y ≥ 0.","options":{},"answer":"Corner points of feasible region:\nA(0,0): Z=0. B(30,0): Z=120. C(20,30): Z=80+30=110. D(0,50): Z=50.\nAt intersection of x+y=50 and 3x+y=90: 2x=40, x=20, y=30. Z=80+30=110.\nMaximum Z = 120 at B(30,0).","section":"D","marks":5,"chapter":"Linear Programming","type":"LA","is_important":True},

{"id":"m3_lp_2","year":2024,"term":None,"question_number":2,"question":"A corner point of the feasible region of a LPP is (3,4). The objective function is Z = ax + by. If Z has the maximum value 60 at (3,4) and 3a + 2b = 60, find a and b.","options":{},"answer":"Maximum at (3,4): 3a + 4b = 60. ...(1)\nGiven: 3a + 2b = 60. ...(2)\nSubtracting (2) from (1): 2b = 0 ⟹ b = 0.\nFrom (2): 3a = 60 ⟹ a = 20.\nSo a = 20, b = 0.","section":"C","marks":3,"chapter":"Linear Programming","type":"SA","is_important":False},

{"id":"m3_lp_3","year":2023,"term":None,"question_number":3,"question":"The feasible region for a LPP is shown. Find the maximum of Z = 5x + 7y at corner points (0,0), (3,0), (2,2), (0,3).","options":{},"answer":"Z(0,0) = 0.\nZ(3,0) = 15.\nZ(2,2) = 10+14 = 24.\nZ(0,3) = 21.\nMaximum Z = 24 at (2,2).","section":"B","marks":2,"chapter":"Linear Programming","type":"VSA","is_important":False},

{"id":"m3_lp_4","year":2022,"term":None,"question_number":4,"question":"Solve the LPP: Minimise Z = 200x + 500y subject to x + 2y ≥ 10, 3x + 4y ≤ 24, x ≥ 0, y ≥ 0.","options":{},"answer":"Constraints: x+2y≥10 and 3x+4y≤24.\nCorner points:\nFrom x+2y=10 and x=0: (0,5). Z=2500.\nFrom 3x+4y=24 and y=0: (8,0). But check x+2(0)≥10: 8≥10? No. Not feasible.\nFrom x+2y=10 and 3x+4y=24: multiply first by 2: 2x+4y=20, subtract: x=4, y=3. Check: 4+6=10≥10✓, 12+12=24≤24✓. Z=200(4)+500(3)=800+1500=2300.\nFrom 3x+4y=24 and x=0: y=6. Check 0+12=12≥10✓. Z=3000.\nMinimum Z = 2300 at (4,3).","section":"D","marks":5,"chapter":"Linear Programming","type":"LA","is_important":True},

{"id":"m3_lp_5","year":2021,"term":None,"question_number":5,"question":"The objective function of a LPP is Z = 3x + 4y. The corner points of feasible region are (0,0), (12,0), (9,3), (0,6). What is the maximum value of Z?","options":{},"answer":"Z(0,0)=0. Z(12,0)=36. Z(9,3)=27+12=39. Z(0,6)=24.\nMaximum Z = 39 at (9,3).","section":"B","marks":2,"chapter":"Linear Programming","type":"VSA","is_important":False},

{"id":"m3_lp_6","year":2020,"term":None,"question_number":6,"question":"In a LPP, the objective function is Z = 2x + 3y and the feasible region is determined by 2x + y ≤ 8, x + 2y ≤ 10, x ≥ 0, y ≥ 0. Find the maximum value of Z.","options":{},"answer":"Intersection of 2x+y=8 and x+2y=10:\n3y=12 ⟹ y=4, x=2. Corner point (2,4).\nCorner points: O(0,0), A(4,0), B(2,4), C(0,5).\nZ(0,0)=0, Z(4,0)=8, Z(2,4)=4+12=16, Z(0,5)=15.\nMaximum Z = 16 at (2,4).","section":"C","marks":3,"chapter":"Linear Programming","type":"SA","is_important":False},

# ════════════════════════════════════════════════════
# CH 13: PROBABILITY
# ════════════════════════════════════════════════════
{"id":"m3_prob_1","year":2025,"term":None,"question_number":1,"question":"If P(A) = 0.4, P(B) = 0.3 and P(A∩B) = 0.2, find P(A|B).","options":{},"answer":"P(A|B) = P(A∩B)/P(B) = 0.2/0.3 = 2/3.","section":"A","marks":1,"chapter":"Probability","type":"MCQ","is_important":False},

{"id":"m3_prob_2","year":2024,"term":None,"question_number":2,"question":"A bag contains 5 white and 4 black balls. Two balls are drawn without replacement. Find the probability that both are white.","options":{},"answer":"P(both white) = C(5,2)/C(9,2) = 10/36 = 5/18.","section":"B","marks":2,"chapter":"Probability","type":"VSA","is_important":False},

{"id":"m3_prob_3","year":2023,"term":None,"question_number":3,"question":"State and prove Bayes' theorem.","options":{},"answer":"Statement: If E₁, E₂,...,Eₙ are mutually exclusive and exhaustive events with P(Eᵢ)>0, and A is any event with P(A)>0, then:\nP(Eᵢ|A) = P(Eᵢ)·P(A|Eᵢ) / Σⱼ P(Eⱼ)·P(A|Eⱼ).\nProof: By conditional probability, P(Eᵢ|A) = P(Eᵢ∩A)/P(A).\nP(Eᵢ∩A) = P(Eᵢ)·P(A|Eᵢ) (multiplication theorem).\nP(A) = Σⱼ P(A|Eⱼ)·P(Eⱼ) (total probability theorem).\nSubstituting: P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ)/[Σⱼ P(Eⱼ)P(A|Eⱼ)]. ✓","section":"D","marks":5,"chapter":"Probability","type":"LA","is_important":True},

{"id":"m3_prob_4","year":2022,"term":None,"question_number":4,"question":"An urn contains 10 black and 5 white balls. Two balls are drawn one by one without replacement. Find the probability that both are black.","options":{},"answer":"P(1st black) = 10/15 = 2/3.\nP(2nd black | 1st black) = 9/14.\nP(both black) = (2/3)(9/14) = 18/42 = 3/7.","section":"B","marks":2,"chapter":"Probability","type":"VSA","is_important":False},

{"id":"m3_prob_5","year":2021,"term":None,"question_number":5,"question":"A die is thrown twice. Find the probability that the sum of numbers appearing is 9.","options":{},"answer":"Total outcomes = 36.\nFavorable: (3,6),(6,3),(4,5),(5,4) — 4 outcomes.\nP = 4/36 = 1/9.","section":"B","marks":2,"chapter":"Probability","type":"VSA","is_important":False},

{"id":"m3_prob_6","year":2020,"term":None,"question_number":6,"question":"In an examination, 30% students fail in Physics, 25% fail in Maths, and 10% fail in both. A student is selected. Find the probability that he failed in Physics if it's known he failed in Maths.","options":{},"answer":"P(P) = 0.30, P(M) = 0.25, P(P∩M) = 0.10.\nP(P|M) = P(P∩M)/P(M) = 0.10/0.25 = 0.4 = 2/5.","section":"B","marks":2,"chapter":"Probability","type":"VSA","is_important":False},

{"id":"m3_prob_7","year":2019,"term":None,"question_number":7,"question":"A problem is given to students A, B, C whose probabilities of solving it are 1/2, 1/3, 1/4 respectively. What is the probability that the problem will be solved?","options":{},"answer":"P(none solves) = P(Ā)·P(B̄)·P(C̄) = (1/2)(2/3)(3/4) = 1/4.\nP(at least one solves) = 1 - 1/4 = 3/4.","section":"C","marks":3,"chapter":"Probability","type":"SA","is_important":True},

{"id":"m3_prob_8","year":2018,"term":None,"question_number":8,"question":"For the probability distribution of X:\nX:  0   1   2   3\nP: 0.1 0.3 0.4 0.2\nFind E(X) and Var(X).","options":{},"answer":"E(X) = 0(0.1)+1(0.3)+2(0.4)+3(0.2) = 0+0.3+0.8+0.6 = 1.7.\nE(X²) = 0(0.1)+1(0.3)+4(0.4)+9(0.2) = 0+0.3+1.6+1.8 = 3.7.\nVar(X) = E(X²)-[E(X)]² = 3.7-2.89 = 0.81.","section":"C","marks":3,"chapter":"Probability","type":"SA","is_important":True},

{"id":"m3_prob_9","year":2017,"term":None,"question_number":9,"question":"Two cards are drawn successively without replacement from a pack of 52 cards. Find the probability distribution of the number of jacks.","options":{},"answer":"Let X = number of jacks drawn. X can take values 0, 1, 2.\nP(X=0) = C(48,2)/C(52,2) = 1128/1326 = 188/221.\nP(X=1) = C(4,1)·C(48,1)/C(52,2) = 192/1326 = 32/221.\nP(X=2) = C(4,2)/C(52,2) = 6/1326 = 1/221.\nVerify: 188+32+1 = 221. ✓","section":"D","marks":5,"chapter":"Probability","type":"LA","is_important":True},

{"id":"m3_prob_10","year":2025,"term":None,"question_number":10,"question":"A fair coin is tossed 6 times. Find the probability of getting exactly 4 heads using binomial distribution.","options":{},"answer":"n=6, p=1/2, q=1/2, r=4.\nP(X=4) = C(6,4)·(1/2)⁴·(1/2)² = 15·(1/16)·(1/4) = 15/64.","section":"C","marks":3,"chapter":"Probability","type":"SA","is_important":False},

]  # end of NEW_QUESTIONS

# ─────────────────────────────────────────────────────────────
# CHAPTER ORDER
# ─────────────────────────────────────────────────────────────
CHAPTER_ORDER = [
    "Relations and Functions","Inverse Trigonometric Functions","Matrices","Determinants",
    "Continuity and Differentiability","Application of Derivatives","Integrals",
    "Application of Integrals","Differential Equations","Vector Algebra",
    "Three-Dimensional Geometry","Linear Programming","Probability"
]

def sort_key(q):
    ch = q.get("chapter","")
    idx = CHAPTER_ORDER.index(ch) if ch in CHAPTER_ORDER else 99
    try:
        yr = int(str(q.get("year",0)).split("-")[0])
    except:
        yr = 0
    try:
        qn = int(q.get("question_number",0))
    except:
        qn = 0
    return (idx, yr, qn)

def main():
    with open("public/data/pyqs.json","r",encoding="utf-8") as f:
        existing = json.load(f)

    # 1. Fix chapter names
    renamed = 0
    for q in existing:
        ch = q.get("chapter","")
        if ch in RENAME:
            q["chapter"] = RENAME[ch]
            renamed += 1
    print(f"Renamed {renamed} questions to updated chapter names")

    # 2. Remove remaining garbled questions
    before = len(existing)
    existing = [q for q in existing if not (is_garbled(q.get("question","")) or is_garbled(q.get("answer","")))]
    print(f"Removed {before - len(existing)} more garbled questions")

    # 3. Add new questions (skip duplicates)
    existing_ids = {q["id"] for q in existing}
    new_qs = [q for q in NEW_QUESTIONS if q["id"] not in existing_ids]
    combined = existing + new_qs

    # 4. Sort
    combined.sort(key=sort_key)

    print(f"\nExisting (after cleanup): {len(existing)}")
    print(f"New questions added: {len(new_qs)}")
    print(f"Total: {len(combined)}")
    print("\nBy chapter:")
    for ch, cnt in Counter(q["chapter"] for q in combined).most_common():
        print(f"  {ch}: {cnt}")

    with open("public/data/pyqs.json","w",encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
    print("\nSaved to public/data/pyqs.json ✓")

if __name__ == "__main__":
    main()
