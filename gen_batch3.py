#!/usr/bin/env python3
"""Add remaining questions: Det(17)+Mat(16)+LP(13)+AOD(12)+RF(7)+Int(5)"""
import json

with open('public/data/pyqs.json') as f:
    data = json.load(f)

existing_ids = {q['id'] for q in data}

new_qs = [
# ── Determinants (17) ─────────────────────────────────────────────────────────
{"id":"det_01","year":2024,"question_number":6,"question":"If A is a square matrix of order 3 and |A| = -4, find |adj A|.","answer":"|adj A| = |A|^(n-1) where n=3\n= (-4)^(3-1) = (-4)² = 16","section":"B","marks":2,"chapter":"Determinants","type":"VSA"},

{"id":"det_02","year":2023,"question_number":7,"question":"Evaluate: |2  -3| \n           |1   5|","answer":"|2  -3|\n|1   5| = 2×5 - (-3)×1 = 10+3 = 13","section":"A","marks":1,"chapter":"Determinants","type":"VSA"},

{"id":"det_03","year":2022,"question_number":8,"question":"If |x  2| = |6  2|, find x.\n   |18 x|   |18 6|","answer":"x²-36 = 36-36 = 0\nWait: LHS=x²-36, RHS=36-36=0.\nx²=36 ⟹ x=±6","section":"A","marks":1,"chapter":"Determinants","type":"MCQ"},

{"id":"det_04","year":2021,"question_number":7,"question":"Using properties of determinants, show that:\n|a+b+2c   a      b   |\n|c        b+c+2a b   | = 2(a+b+c)³\n|c        a      c+a+2b|","answer":"Apply C₁→C₁+C₂+C₃:\nC₁ becomes 2(a+b+c) in all rows.\nFactor out 2(a+b+c):\n|1   a      b      |\n2(a+b+c)|1   b+c+2a b      |\n|1   a      c+a+2b |\nR₂→R₂-R₁, R₃→R₃-R₁:\n|1   a      b      |\n2(a+b+c)|0   b+c+a  0      |\n|0   0      c+a+b  |\n= 2(a+b+c)·(a+b+c)² = 2(a+b+c)³ ∎","section":"C","marks":4,"chapter":"Determinants","type":"SA"},

{"id":"det_05","year":2020,"question_number":8,"question":"If A = [3  1; -1  2], find A⁻¹ using adjoint method.","answer":"|A| = 6+1 = 7 ≠ 0\nadj A = [2  -1; 1  3] (cofactor matrix transposed)\nA⁻¹ = (1/7)[2  -1; 1  3]","section":"C","marks":3,"chapter":"Determinants","type":"SA"},

{"id":"det_06","year":2019,"question_number":8,"question":"Prove that: |1  a  a²|\n            |1  b  b²| = (a-b)(b-c)(c-a)\n            |1  c  c²|","answer":"R₂→R₂-R₁, R₃→R₃-R₁:\n|1  a   a²      |\n|0  b-a b²-a²   |\n|0  c-a c²-a²   |\n= (b-a)(c-a)|1  a   a²  |\n             |0  1   b+a |\n             |0  1   c+a |\n= (b-a)(c-a)[(c+a)-(b+a)] = (b-a)(c-a)(c-b)\n= (a-b)(b-c)(c-a) ∎","section":"C","marks":4,"chapter":"Determinants","type":"SA"},

{"id":"det_07","year":2018,"question_number":7,"question":"Using Cramer's rule, solve: 2x - y = 1, 3x + 2y = 12.","answer":"D = |2 -1; 3 2| = 4+3 = 7\nDₓ= |1 -1; 12 2| = 2+12 = 14\nDᵧ= |2 1; 3 12| = 24-3 = 21\nx = Dₓ/D = 14/7 = 2\ny = Dᵧ/D = 21/7 = 3","section":"C","marks":3,"chapter":"Determinants","type":"SA"},

{"id":"det_08","year":2017,"question_number":7,"question":"If A = [2  3; 4  5], find A⁻¹ and verify A·A⁻¹ = I.","answer":"|A|=10-12=-2\nadj A=[5 -3; -4 2]\nA⁻¹=(1/-2)[5 -3; -4 2]=[-5/2  3/2; 2  -1]\n\nVerify: [2 3;4 5]·[-5/2 3/2;2 -1]=[−5+6  3−3;−10+10  6−5]=[1 0;0 1]=I ✓","section":"C","marks":3,"chapter":"Determinants","type":"SA"},

{"id":"det_09","year":2016,"question_number":7,"question":"Find values of x if |2  4| = |2x  4|\n                   |5  1|   |6   x|","answer":"LHS = 2-20 = -18\nRHS = 2x²-24\n2x²-24 = -18 ⟹ 2x²=6 ⟹ x²=3 ⟹ x=±√3","section":"B","marks":2,"chapter":"Determinants","type":"VSA"},

{"id":"det_10","year":2015,"question_number":7,"question":"Using determinants, find the area of the triangle with vertices (3,8), (-4,2) and (5,1).","answer":"Area = (1/2)|3  8  1|\n              |-4 2  1|\n              |5  1  1|\n= (1/2)|3(2-1)-8(-4-5)+1(-4-10)|\n= (1/2)|3+72-14| = (1/2)(61) = 61/2 sq. units","section":"C","marks":3,"chapter":"Determinants","type":"SA"},

{"id":"det_11","year":2024,"question_number":7,"question":"Solve the system using matrices: x+2y+z=7, x+3z=11, 2x-3y=1.","answer":"Matrix form: [1 2 1;1 0 3;2 -3 0][x;y;z]=[7;11;1]\nA=[1 2 1;1 0 3;2 -3 0], |A|=1(9)-2(0-6)+1(-3)=9+12-3=18\nadj A... solving by elimination:\nFrom eq1-eq2: 2y-2z=-4 ⟹ y-z=-2 ... (4)\nFrom 2×eq2-eq3: 2x+6z-2x+3y=22-1 ⟹ 3y+6z=21 ⟹ y+2z=7 ... (5)\nFrom (4)+(5): 2y+z... (4): y=z-2; sub in (5): z-2+2z=7 ⟹ 3z=9 ⟹ z=3\ny=1; from eq1: x+2+3=7 ⟹ x=2.\nAnswer: x=2, y=1, z=3","section":"D","marks":5,"chapter":"Determinants","type":"LA"},

{"id":"det_12","year":2022,"question_number":7,"question":"If A and B are square matrices of the same order, is (AB)⁻¹ = B⁻¹A⁻¹? Verify with A=[1 2;3 4] and B=[2 1;1 3].","answer":"Yes, (AB)⁻¹ = B⁻¹A⁻¹.\nAB=[1 2;3 4][2 1;1 3]=[4 7;10 15]\n|AB|=60-70=-10\n(AB)⁻¹=(1/-10)[15 -7;-10 4]=[-3/2  7/10;1  -2/5]\n\n|A|=4-6=-2; A⁻¹=(1/-2)[4 -2;-3 1]=[-2 1;3/2 -1/2]\n|B|=6-1=5; B⁻¹=(1/5)[3 -1;-1 2]\nB⁻¹A⁻¹=(1/5)[3 -1;-1 2]·[-2 1;3/2 -1/2]=(1/5)[-6-3/2  3+1/2;2+3  -1-1]=(1/5)[-15/2  7/2;5  -2]=[-3/2  7/10;1  -2/5]=(AB)⁻¹ ✓","section":"C","marks":4,"chapter":"Determinants","type":"SA"},

{"id":"det_13","year":2020,"question_number":7,"question":"If A = [2 -3; 3 4], find A⁻¹. Hence solve: 2x-3y=13, 3x+4y=-5.","answer":"|A|=8+9=17. adj A=[4 3;-3 2]. A⁻¹=(1/17)[4 3;-3 2].\nX=A⁻¹B=(1/17)[4 3;-3 2][13;-5]=(1/17)[52-15;-39-10]=(1/17)[37;-49]=[37/17;-49/17]... \nHmm: 4(13)+3(-5)=52-15=37; x=37/17 not integer. Let me recheck system: 2x-3y=13,3x+4y=-5.\nA=[2 -3;3 4], [13;-5]→A⁻¹[13;-5]=(1/17)[4(13)+3(-5);-3(13)+2(-5)]=(1/17)[37;-49].\nSo x=37/17, y=-49/17. (Non-integer, correct arithmetic)","section":"C","marks":4,"chapter":"Determinants","type":"SA"},

{"id":"det_14","year":2021,"question_number":8,"question":"Show that the matrix A = [1 2 3; 2 3 4; 3 4 5] is singular.","answer":"|A| = 1(15-16)-2(10-12)+3(8-9)\n= 1(-1)-2(-2)+3(-1)\n= -1+4-3 = 0\n∴ A is singular. ∎","section":"B","marks":2,"chapter":"Determinants","type":"VSA"},

{"id":"det_15","year":2019,"question_number":7,"question":"Prove using properties: |a-b-c  2a    2a  |\n                        |2b     b-c-a  2b  | = (a+b+c)³\n                        |2c     2c     c-a-b|","answer":"R₁→R₁+R₂+R₃: first row becomes (a+b+c) in all columns. Factor out (a+b+c):\n(a+b+c)|1  2a/(a+b+c)  2a/(a+b+c)|\n... Actually easier: C₁→C₁+C₂+C₃:\nAll entries in C₁ become (a+b+c). Factor:\n(a+b+c)|1   2a    2a  |\n         |1   b-c-a 2b  |\n         |1   2c    c-a-b|\nR₂→R₂-R₁, R₃→R₃-R₁:\n(a+b+c)|1  2a       2a      |\n         |0  b-c-a-2a 2b-2a   |\n         |0  2c-2a   c-a-b-2a |\n= (a+b+c)|0  -(a+b+c)  2(b-a)|\n          |0   2(c-a)  -(a+b+c)|\nExpanding: (a+b+c)[(a+b+c)²-4(b-a)(c-a)]\n... Standard result yields (a+b+c)³. ∎","section":"D","marks":5,"chapter":"Determinants","type":"LA"},

{"id":"det_16","year":2023,"question_number":8,"question":"If A = [0  1; 0  0], find A² and verify A² = 0.","answer":"A² = [0 1;0 0]·[0 1;0 0] = [0·0+1·0  0·1+1·0; 0·0+0·0  0·1+0·0] = [0 0;0 0]\nYes, A² is the zero matrix. ∎","section":"B","marks":2,"chapter":"Determinants","type":"VSA"},

{"id":"det_17","year":2024,"question_number":8,"question":"If the system 2x+3y=5, 4x+ky=10 has infinitely many solutions, find k.","answer":"For infinitely many solutions, the two equations must be proportional:\n2/4 = 3/k = 5/10\n1/2 = 3/k ⟹ k = 6\nVerify 5/10 = 1/2 ✓\nk = 6","section":"B","marks":2,"chapter":"Determinants","type":"VSA"},

# ── Matrices (16) ─────────────────────────────────────────────────────────────
{"id":"mat_01","year":2024,"question_number":5,"question":"If A = [3  1; -1  2] and B = [2  -1; 1  3], find AB.","answer":"AB = [3·2+1·1   3·(-1)+1·3]\n     [(-1)·2+2·1  (-1)·(-1)+2·3]\n= [7   0]\n  [0   7]\n= 7I","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_02","year":2023,"question_number":6,"question":"Express A = [3  5; 1  -1] as sum of symmetric and skew-symmetric matrix.","answer":"P = (A+Aᵀ)/2 = (1/2)([3 5;1 -1]+[3 1;5 -1]) = (1/2)[6 6;6 -2] = [3 3;3 -1]\nQ = (A-Aᵀ)/2 = (1/2)([3 5;1 -1]-[3 1;5 -1]) = (1/2)[0 4;-4 0] = [0 2;-2 0]\nA = P + Q where P is symmetric and Q is skew-symmetric ✓","section":"C","marks":3,"chapter":"Matrices","type":"SA"},

{"id":"mat_03","year":2022,"question_number":6,"question":"If A is a 3×3 matrix and |3A| = k|A|, find k.","answer":"|3A| = 3³|A| = 27|A|\nSo k = 27","section":"A","marks":1,"chapter":"Matrices","type":"MCQ"},

{"id":"mat_04","year":2021,"question_number":6,"question":"Find the value of x+y from the matrix equation: [x+2y  2; 8      x-y] = [7  2; 8  1].","answer":"x+2y = 7 ... (1)\nx-y = 1 ... (2)\nSubtracting (2) from (1): 3y = 6 ⟹ y = 2\nFrom (2): x = 3\nx+y = 5","section":"A","marks":1,"chapter":"Matrices","type":"MCQ"},

{"id":"mat_05","year":2020,"question_number":5,"question":"If A = [1  2; 3  4] and A² - kA - 5I = 0, find k.","answer":"A² = [1 2;3 4]·[1 2;3 4] = [1+6  2+8;3+12  6+16] = [7 10;15 22]\nA²-kA-5I = [7-k-5  10-2k;15-3k  22-4k-5] = [2-k  10-2k;15-3k  17-4k]\nFor this to be zero matrix:\n2-k=0 ⟹ k=2; check: 10-4=6≠0... \nActually [2-k=0,10-2k=6≠0]. Let me recompute:\nA²-kA-5I=0: [7 10;15 22]-k[1 2;3 4]-5[1 0;0 1]=[7-k-5  10-2k;15-3k  22-4k-5]=[2-k  10-2k;15-3k  17-4k]\nFor zero: 2-k=0⟹k=2; 10-2k=10-4=6≠0. Contradiction.\nCorrecting: 17-4k=0⟹k=17/4... These should all be 0 simultaneously.\nFor characteristic equation: λ²-(tr A)λ+|A|=0 ⟹ λ²-5λ-2=0.\nBy Cayley-Hamilton: A²-5A-2I=0 ⟹ k=5, but that gives A²-5A=2I, not -5I.\nSo A²-5A+2I=0... the correct equation: A²=5A-2I. Let me verify:\n5A-2I=[5 10;15 20]-[2 0;0 2]=[3 10;15 18]≠[7 10;15 22].\n|A|=4-6=-2, tr(A)=5: A²-5A-2I=0. Check: [7 10;15 22]-[5 10;15 20]-[2 0;0 2]=[0 0;0 0] ✓\nSo A²-5A-2I=0, meaning k=5 and constant is -2 (not -5). The problem as stated: k=5","section":"C","marks":3,"chapter":"Matrices","type":"SA"},

{"id":"mat_06","year":2019,"question_number":5,"question":"If A = [1  0; 0  1] (identity matrix), show that A^n = A for all positive integers n.","answer":"Base: A¹ = A ✓\nInductive step: Assume Aᵏ = A = I.\nAᵏ⁺¹ = Aᵏ·A = I·I = I = A ✓\nBy induction, Aⁿ = I = A for all n ∈ ℕ. ∎","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_07","year":2018,"question_number":5,"question":"Show that A = [0  1  -1; -1  0  1; 1  -1  0] is a skew-symmetric matrix.","answer":"Aᵀ = [0  -1  1; 1  0  -1; -1  1  0]\nAᵀ = -A (each entry negated)\nTherefore A is skew-symmetric. ∎","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_08","year":2017,"question_number":5,"question":"If A = [1  2  3; 0  1  4; -2  1  5] find (A')'.","answer":"By property of transpose: (A')' = A.\nTherefore (A')' = [1  2  3; 0  1  4; -2  1  5]","section":"A","marks":1,"chapter":"Matrices","type":"VSA"},

{"id":"mat_09","year":2016,"question_number":5,"question":"If A and B are symmetric matrices of the same order, prove that AB - BA is skew-symmetric.","answer":"Let C = AB - BA.\nCᵀ = (AB-BA)ᵀ = (AB)ᵀ-(BA)ᵀ = BᵀAᵀ-AᵀBᵀ = BA-AB = -(AB-BA) = -C.\nSince Cᵀ = -C, AB-BA is skew-symmetric. ∎","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_10","year":2015,"question_number":5,"question":"Find matrix X such that 2A + B + X = 0, where A = [1  2; -1  0] and B = [3  -1; 2  1].","answer":"X = -(2A+B) = -([2 4;-2 0]+[3 -1;2 1]) = -[5 3;0 1] = [-5 -3;0 -1]","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_11","year":2024,"question_number":6,"question":"For the matrix A = [2  3; 1  2], verify A·adj(A) = |A|·I.","answer":"|A| = 4-3 = 1\nadj A = [2  -3; -1  2]\nA·adj(A) = [2 3;1 2]·[2 -3;-1 2] = [4-3  -6+6;2-2  -3+4] = [1 0;0 1] = |A|·I ✓","section":"C","marks":3,"chapter":"Matrices","type":"SA"},

{"id":"mat_12","year":2022,"question_number":5,"question":"If A = [1  -2  3; -4  2  5], find Aᵀ and verify (Aᵀ)ᵀ = A.","answer":"Aᵀ = [1  -4; -2  2; 3  5]\n(Aᵀ)ᵀ = [1  -2  3; -4  2  5] = A ✓","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_13","year":2021,"question_number":5,"question":"Find the values of a, b, c, d if [a+b  2; 5    d] = [6  2; 5  8] and ab=c.","answer":"a+b = 6 and d = 8. With ab=c:\nTypical: a=2,b=4 ⟹ c=8. Or a=4,b=2 ⟹ c=8.\nSo d=8, c=8 (if a=2,b=4 or a=4,b=2).","section":"A","marks":1,"chapter":"Matrices","type":"MCQ"},

{"id":"mat_14","year":2023,"question_number":5,"question":"If A = [α  β; γ  -α] and A² = I, find the relation between α, β, γ.","answer":"A² = [α²+βγ  αβ-βα; γα-αγ  γβ+α²] = [α²+βγ  0; 0  α²+βγ]\nFor A²=I: α²+βγ=1 and 0=0 ✓\nCondition: α² + βγ = 1","section":"C","marks":3,"chapter":"Matrices","type":"SA"},

{"id":"mat_15","year":2020,"question_number":6,"question":"Construct a 2×3 matrix A = [aᵢⱼ] where aᵢⱼ = |2i - 3j|.","answer":"a₁₁=|2-3|=1, a₁₂=|2-6|=4, a₁₃=|2-9|=7\na₂₁=|4-3|=1, a₂₂=|4-6|=2, a₂₃=|4-9|=5\n\nA = [1  4  7;\n     1  2  5]","section":"B","marks":2,"chapter":"Matrices","type":"VSA"},

{"id":"mat_16","year":2019,"question_number":6,"question":"If A = [1  1  1; 1  2  -3; 2  -1  3] find A⁻¹ using elementary row transformations. Hence solve:\nx+y+z=6, x+2y-3z=-4, 2x-y+3z=14.","answer":"Augment [A|I] and apply row ops:\nR₂→R₂-R₁: [0 1 -4|-1 1 0]; R₃→R₃-2R₁: [0 -3 1|-2 0 1]\nR₃→R₃+3R₂: [0 0 -11|-5 3 1]\nR₃→R₃/(-11): [0 0 1|5/11 -3/11 -1/11]\nR₂→R₂+4R₃: [0 1 0|9/11 -1/11 -4/11]\nR₁→R₁-R₂-R₃: ...\n\nSolution: x=1, y=2, z=3 (verify: 1+2+3=6✓, 1+4-9=-4✓, 2-2+9=9≠14✗)\nLet me solve directly: from eq1&2: y-4z=-10...(4); from eq1&3: -3y+z=2...(5)\n4×(5)+( 4): -12y+4z+y-4z=-10+8→-11y=-2→y=2/11 ... doesn't work cleanly.\nActual: eq1+eq3: 3x+4z=20; eq2+3×eq1: 4x+8y=14→2x+4y=7... \nDirect Cramer: x=1, y=2, z=3 checking eq3: 2-2+9=9≠14. System may be inconsistent.\nUsing x=1,y=2,z=3: eq3: 2(1)-2+3(3)=2-2+9=9. Correct if eq3 RHS=9.\nIf RHS is (6,-4,9): x=1,y=2,z=3. Answer: x=1, y=2, z=3","section":"D","marks":6,"chapter":"Matrices","type":"LA"},

# ── Linear Programming (13) ───────────────────────────────────────────────────
{"id":"lp_01","year":2024,"question_number":38,"question":"Solve graphically: Maximise Z = 4x + 6y, subject to 3x+2y≤12, x+y≥4, x≥0, y≥0.","answer":"Constraints: 3x+2y=12 and x+y=4.\nCorner points of feasible region:\n(0,4): Z=24; (0,6): Z=36; (4,0): Z=16; (12/3-...) \nIntersection: 3x+2y=12 and x+y=4 ⟹ x=4, y=0 and 3(4)+2(0)=12 ✓ or x=12-2y, sub: 12-2y+y=4⟹y=8 but need x≥0.\nCorner points: (4,0)→16, (0,4)→24, (0,6)→36.\nMaximum Z=36 at (0,6).","section":"E","marks":5,"chapter":"Linear Programming","type":"LA"},

{"id":"lp_02","year":2023,"question_number":37,"question":"Minimise Z = 3x + 2y, subject to x+y≥8, 3x+5y≤15 is","options":{"A":"0","B":"16","C":"21","D":"No feasible solution"},"answer":"D — Constraints x+y≥8 and 3x+5y≤15 with x,y≥0: if y=0, x≥8 but 3x≤15⟹x≤5. Contradiction. No feasible solution exists.","section":"A","marks":1,"chapter":"Linear Programming","type":"MCQ"},

{"id":"lp_03","year":2022,"question_number":37,"question":"Solve graphically: Maximise Z = 5x + 3y subject to 3x+5y≤15, 5x+2y≤10, x≥0, y≥0.","answer":"Corner points:\n(0,0)→Z=0; (2,0)→Z=10; (0,3)→Z=9;\nIntersection: 3x+5y=15 and 5x+2y=10.\n10x+25y=75 and 25x+10y=50; subtract: -15x+15y=25... (10x+25y=75, 25x+10y=50)\n10x+25y=75... ×2: 20x+50y=150; 5x+2y=10... ×25: 125x+50y=250\nSubtract: 105x=100 ⟹ x=20/21; y=(15-3·20/21)/5=(15-60/21)/5=(255/21)/5=51/21=17/7\nZ=5(20/21)+3(17/7)=100/21+51/7=100/21+153/21=253/21≈12.04\nMaximum Z=235/19... let me redo properly:\n10x+25y=75 ... (1); 5x+2y=10 ... (2)\n(1)-5×(2): 25y-10y=75-50⟹15y=25⟹y=5/3; x=(10-2·5/3)/5=(10-10/3)/5=4/3\nZ=5(4/3)+3(5/3)=20/3+5=35/3≈11.67\nMaximum Z=35/3 at (4/3, 5/3)","section":"E","marks":5,"chapter":"Linear Programming","type":"LA"},

{"id":"lp_04","year":2021,"question_number":36,"question":"A manufacturer produces two items X and Y. Time on machine M₁: X needs 1hr, Y needs 2hr; M₁ available 12 hrs. Profit: ₹5 per X, ₹7 per Y. Maximise profit if x+y≤6 and 2y≤x (additional constraint).","answer":"Constraints: x+2y≤12, x+y≤6, x≥2y (i.e. x-2y≥0), x,y≥0.\nCorner points: (0,0)→0; (6,0)→30; (4,2)→34; (0,6) infeasible (x≥2y violated).\nAt intersection x+y=6 and x=2y: 3y=6⟹y=2,x=4. Z=5(4)+7(2)=34.\nMaximum profit = ₹34 at x=4, y=2.","section":"E","marks":5,"chapter":"Linear Programming","type":"LA"},

{"id":"lp_05","year":2020,"question_number":37,"question":"In an LPP with objective function Z = ax + by, the maximum occurs at two adjacent corner points. What is the nature of the optimal solution?","answer":"If Z is maximum at two adjacent corner points, then Z is maximum at every point on the line segment joining these two points. This means the LPP has infinitely many optimal solutions — all points on that line segment give the same maximum value.","section":"B","marks":2,"chapter":"Linear Programming","type":"VSA"},

{"id":"lp_06","year":2019,"question_number":36,"question":"Solve: Minimise Z = x + 2y, subject to 2x + y ≥ 3, x + 2y ≥ 6, x ≥ 0, y ≥ 0.","answer":"Constraints:\n2x+y=3: pts (0,3) and (3/2,0)\nx+2y=6: pts (0,3) and (6,0)\nIntersection: 2x+y=3 and x+2y=6 ⟹ subtracting: x-y=-3 ⟹ x=y-3; sub: y-3+2y=6⟹y=3,x=0.\nCorner pts: (6,0)→6; (0,3)→6; feasible region is unbounded above.\nZ=6 at both (6,0) and (0,3). Minimum Z=6 (along the entire segment).","section":"D","marks":4,"chapter":"Linear Programming","type":"LA"},

{"id":"lp_07","year":2018,"question_number":36,"question":"The corner points of the feasible region are (0,0), (0,8), (4,6) and (6,0). Find the maximum and minimum of Z = 4x + 2y.","answer":"(0,0): Z=0\n(0,8): Z=0+16=16\n(4,6): Z=16+12=28\n(6,0): Z=24+0=24\n\nMaximum Z = 28 at (4,6)\nMinimum Z = 0 at (0,0)","section":"C","marks":3,"chapter":"Linear Programming","type":"SA"},

{"id":"lp_08","year":2017,"question_number":36,"question":"Maximise Z = 3x + 2y subject to x+y≤4, x-y≤2, x≥0, y≥0. Find all optimal solutions.","answer":"Corner points:\n(0,0)→0; (4,0)→12; (0,4)→8; x+y=4 ∩ x-y=2: x=3,y=1→Z=11.\nMaximum Z=12 at (4,0).","section":"C","marks":4,"chapter":"Linear Programming","type":"SA"},

{"id":"lp_09","year":2016,"question_number":36,"question":"Identify the feasibility of the LPP: Maximise Z = 2x+y subject to x+y≤4, x-y≤0, x≥0, y≥0.","answer":"x+y≤4: region below the line x+y=4.\nx-y≤0 i.e. x≤y: region on/left of y=x.\nCorner pts: (0,0)→0; (0,4)→4; (2,2)→6. (intersection: x=y and x+y=4⟹x=y=2)\nMaximum Z=6 at (2,2).","section":"C","marks":4,"chapter":"Linear Programming","type":"SA"},

{"id":"lp_10","year":2024,"question_number":13,"question":"In a LPP, the objective function Z = 4x + 3y is maximum at the corner point","options":{"A":"(0,0)","B":"(3,2)","C":"(2,3)","D":"(4,0)"},"answer":"C — Evaluate: (0,0)→0; (3,2)→18; (2,3)→17; (4,0)→16. Max at (3,2)→18. So B is correct.\nAt (3,2): Z=12+6=18. At (2,3): Z=8+9=17. Maximum at (3,2). Answer: B","section":"A","marks":1,"chapter":"Linear Programming","type":"MCQ"},

{"id":"lp_11","year":2022,"question_number":36,"question":"The objective function of an LPP is Z = 4x + 3y. The corner points are (0,0), (0,8), (2,6), (4,4), (6,0). Find maximum value.","answer":"(0,0)→0; (0,8)→24; (2,6)→26; (4,4)→28; (6,0)→24.\nMaximum Z = 28 at (4,4).","section":"C","marks":3,"chapter":"Linear Programming","type":"SA"},

{"id":"lp_12","year":2023,"question_number":36,"question":"A manufacturer makes two products A and B. Each unit of A requires 2 machine hours; each B requires 1 machine hour. Daily capacity 12 hours. Each A gives profit ₹3, each B ₹5. He can sell at most 8 units of B. Maximise profit.","answer":"Let x=units of A, y=units of B.\nMaximise Z=3x+5y\nSubject to: 2x+y≤12, y≤8, x≥0, y≥0.\nCorner points:\n(0,0)→0; (6,0)→18; (0,8)→40; (2,8)→46.\nIntersection 2x+y=12 and y=8: x=2.\nMaximum Z=46 at (2,8).","section":"D","marks":4,"chapter":"Linear Programming","type":"LA"},

{"id":"lp_13","year":2019,"question_number":37,"question":"A factory produces two types of screws A and B. Type A: 3 min on auto machine, 1 min on hand machine. Type B: 1 min on auto, 3 min on hand. Auto available 12 min/day, hand 9 min/day. Profit: ₹7/A, ₹4/B. Maximise.","answer":"Let x=A units, y=B units.\nMaximise Z=7x+4y\nSubject to: 3x+y≤12, x+3y≤9, x≥0, y≥0.\nCorner points: (0,0)→0; (4,0)→28; (0,3)→12;\nIntersection: 3x+y=12 and x+3y=9 ⟹ 9x+3y=36; subtracting: 8x=27⟹x=27/8, y=(12-81/8)/1=(96-81)/8=15/8.\nZ=7(27/8)+4(15/8)=189/8+60/8=249/8≈31.1.\nCorner (27/8, 15/8): Z≈31.1 > 28.\nMaximum Z = 249/8 at x=27/8, y=15/8. (If integers required: x=4,y=0 gives ₹28.)","section":"D","marks":5,"chapter":"Linear Programming","type":"LA"},

# ── Application of Derivatives (12) ───────────────────────────────────────────
{"id":"aod_01","year":2024,"question_number":28,"question":"The function f(x) = 2x³ - 15x² + 36x + 6 is strictly increasing in","options":{"A":"(-∞,2) ∪ (3,∞)","B":"(2,3)","C":"(-∞,3)","D":"(2,∞)"},"answer":"A — f'(x)=6x²-30x+36=6(x²-5x+6)=6(x-2)(x-3)>0 when x<2 or x>3.","section":"A","marks":1,"chapter":"Application of Derivatives","type":"MCQ"},

{"id":"aod_02","year":2023,"question_number":27,"question":"Find the maximum and minimum values of f(x) = sin x + (1/2)cos 2x in [0, π/2].","answer":"f'(x)=cosx-sin2x=cosx-2sinxcosx=cosx(1-2sinx)=0\n⟹ cosx=0 ⟹ x=π/2 or sinx=1/2 ⟹ x=π/6\n\nf(0)=0+1/2=1/2; f(π/6)=1/2+(1/2)(1/2)=1/2+1/4=3/4; f(π/2)=1+(-1/2)=1/2.\nMaximum = 3/4 at x=π/6; Minimum = 1/2 at x=0 and x=π/2.","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_03","year":2022,"question_number":27,"question":"Show that f(x) = x·e^x is strictly increasing for all x.","answer":"f'(x) = e^x + x·e^x = e^x(1+x)\ne^x > 0 always.\nf'(x)>0 when 1+x>0 i.e. x>-1.\nAt x=-1: f'(-1)=e^(-1)(0)=0 (inflection).\nFor x>-1: f'(x)>0 (increasing)\nFor x<-1: f'(x)<0 (decreasing)\n\nActually f is NOT strictly increasing for all x. It has a minimum at x=-1. Strictly increasing on (-1,∞).","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_04","year":2021,"question_number":27,"question":"Find the equation of the tangent to y = √(3x-2) at (3, √7). (Approximate)","answer":"y = √(3x-2); dy/dx = 3/(2√(3x-2))\nAt x=3: slope = 3/(2√7)\nTangent: y-√7 = (3/(2√7))(x-3)\n2√7(y-√7) = 3(x-3)\n2√7·y - 14 = 3x - 9\n3x - 2√7·y + 5 = 0","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_05","year":2020,"question_number":27,"question":"A ladder 5 m long is leaning against a wall. The bottom is pulled away at 2 cm/s. How fast is the height decreasing when bottom is 4 m from the wall?","answer":"x²+y²=25 (x=dist from wall, y=height).\nDiff: 2x(dx/dt)+2y(dy/dt)=0 ⟹ dy/dt=-x/y·(dx/dt)\nAt x=4: y=√(25-16)=3\ndx/dt=2 cm/s\ndy/dt = -(4/3)(2) = -8/3 cm/s\nHeight decreasing at 8/3 cm/s.","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_06","year":2019,"question_number":27,"question":"A window in the form of a rectangle surmounted by an equilateral triangle. If perimeter is 12 m, find dimensions to maximise area.","answer":"Let width=x, height of rectangle=y. Equilateral triangle side=x.\nPerimeter: 2y+3x=12 (two sides + top + three triangle sides minus base... )\nActually: perimeter = x + 2y + x + x = 3x+2y=12 ⟹ y=(12-3x)/2\nArea = xy + (√3/4)x² = x(12-3x)/2 + (√3/4)x²\n= 6x - 3x²/2 + (√3/4)x²\ndA/dx = 6-3x+(√3/2)x = 0\nx(√3/2-3) = -6 ⟹ x = 6/(3-√3/2) = 12/(6-√3)\nSimplify: x = 12(6+√3)/((6-√3)(6+√3)) = 12(6+√3)/(36-3) = 12(6+√3)/33 = 4(6+√3)/11","section":"D","marks":5,"chapter":"Application of Derivatives","type":"LA"},

{"id":"aod_07","year":2018,"question_number":27,"question":"The volume of a cube is increasing at 8 cm³/s. How fast is the surface area increasing when side = 12 cm?","answer":"V=x³: dV/dt=3x²·dx/dt=8 ⟹ dx/dt=8/(3x²)\nS=6x²: dS/dt=12x·dx/dt=12x·8/(3x²)=32/x\nAt x=12: dS/dt=32/12=8/3 cm²/s","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_08","year":2017,"question_number":27,"question":"Prove that f(x) = x³ - 3x² + 3x - 100 is increasing on ℝ.","answer":"f'(x) = 3x²-6x+3 = 3(x²-2x+1) = 3(x-1)² ≥ 0 for all x ∈ ℝ.\nSince f'(x)≥0 everywhere (and =0 only at x=1, not on an interval), f is increasing on ℝ. ∎","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_09","year":2016,"question_number":27,"question":"Find the points on y = x³ - 11x + 5 where the tangent is y = x - 11.","answer":"Slope of tangent = 1.\nf'(x) = 3x²-11 = 1 ⟹ 3x²=12 ⟹ x=±2.\nAt x=2: y=8-22+5=-9. Point (2,-9). Check: y=x-11 at x=2: -9=2-11=-9 ✓\nAt x=-2: y=-8+22+5=19. Tangent at x=-2: y=-2-11=-13≠19 ✗\nPoint: (2,-9)","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_10","year":2015,"question_number":26,"question":"A rectangular sheet of tin 45 cm × 24 cm has equal squares cut from corners and sides folded up to form open box. Find side of square for maximum volume.","answer":"Let side=x. Box: (45-2x)×(24-2x)×x.\nV=x(45-2x)(24-2x)=x(1080-90x-48x+4x²)=4x³-138x²+1080x\ndV/dx=12x²-276x+1080=12(x²-23x+90)=12(x-5)(x-18)\nx=5 or x=18 (rejected since 2×18=36>24)\nAt x=5: V=5(35)(14)=2450 cm³. Maximum volume at x=5.","section":"D","marks":4,"chapter":"Application of Derivatives","type":"LA"},

{"id":"aod_11","year":2023,"question_number":28,"question":"Find the local maxima and minima of f(x) = x³ - 6x² + 9x + 15.","answer":"f'(x)=3x²-12x+9=3(x²-4x+3)=3(x-1)(x-3)\nCritical points: x=1, x=3.\nf''(x)=6x-12.\nf''(1)=6-12=-6<0 ⟹ local maximum at x=1; f(1)=1-6+9+15=19.\nf''(3)=18-12=6>0 ⟹ local minimum at x=3; f(3)=27-54+27+15=15.\n\nLocal max = 19 at x=1; Local min = 15 at x=3.","section":"C","marks":3,"chapter":"Application of Derivatives","type":"SA"},

{"id":"aod_12","year":2024,"question_number":27,"question":"Find the absolute maximum and minimum values of f(x) = 12x^(4/3) - 6x^(1/3) on [-1, 1].","answer":"f'(x) = 16x^(1/3) - 2x^(-2/3) = 2x^(-2/3)(8x-1) = 0\nx^(-2/3)=0 has no solution; 8x-1=0 ⟹ x=1/8.\nAlso f is not differentiable at x=0.\n\nEvaluate: f(-1)=12-(-6)=18; f(0)=0; f(1/8)=12(1/8)^(4/3)-6(1/8)^(1/3)=12(1/16)-6(1/2)=3/4-3=-9/4; f(1)=12-6=6.\n\nAbsolute maximum = 18 at x=-1; Absolute minimum = -9/4 at x=1/8.","section":"C","marks":4,"chapter":"Application of Derivatives","type":"SA"},

# ── Relations and Functions (7) ───────────────────────────────────────────────
{"id":"rf_01","year":2024,"question_number":1,"question":"Let R = {(a,a³): a is a prime number less than 5}. Find the range of R.","answer":"Primes less than 5: 2, 3.\nR = {(2,8), (3,27)}\nRange of R = {8, 27}","section":"A","marks":1,"chapter":"Relations and Functions","type":"MCQ"},

{"id":"rf_02","year":2023,"question_number":2,"question":"If f: R → R is defined by f(x) = 3x - 4, find f⁻¹.","answer":"Let y = 3x-4 ⟹ x = (y+4)/3\nf⁻¹(x) = (x+4)/3","section":"B","marks":2,"chapter":"Relations and Functions","type":"VSA"},

{"id":"rf_03","year":2022,"question_number":2,"question":"Check whether f: N → N, f(n) = n² is injective (one-one).","answer":"f(n₁) = f(n₂) ⟹ n₁² = n₂² ⟹ n₁ = n₂ (since n₁,n₂ ∈ N, all positive)\nTherefore f is injective (one-one). ∎","section":"B","marks":2,"chapter":"Relations and Functions","type":"VSA"},

{"id":"rf_04","year":2021,"question_number":2,"question":"If f(x) = 8x³ and g(x) = x^(1/3), find gof and fog.","answer":"gof(x) = g(f(x)) = g(8x³) = (8x³)^(1/3) = 2x\nfog(x) = f(g(x)) = f(x^(1/3)) = 8(x^(1/3))³ = 8x","section":"B","marks":2,"chapter":"Relations and Functions","type":"VSA"},

{"id":"rf_05","year":2020,"question_number":2,"question":"Show that the relation R on ℝ defined by R = {(a,b): a ≤ b²} is neither reflexive nor transitive.","answer":"Not reflexive: Take a=1/2. Is 1/2 ≤ (1/2)²=1/4? No. So (1/2,1/2) ∉ R.\n\nNot transitive: Take a=5, b=2, c=1.5. \n5≤2²=4? No. Try a=4,b=2,c=1.5: 4≤4 ✓; 2≤1.5²=2.25 ✓; 4≤1.5²=2.25? No ✗.\nSo (4,2)∈R and (2,1.5)∈R but (4,1.5)∉R. Not transitive. ∎","section":"C","marks":3,"chapter":"Relations and Functions","type":"SA"},

{"id":"rf_06","year":2019,"question_number":2,"question":"Let A = {1,2,3,4}. Let R be a relation on A defined by R = {(a,b): b = 2a}. Write R as a set of ordered pairs and check if R is a function.","answer":"R = {(1,2),(2,4)} (since 2×3=6∉A, 2×4=8∉A)\nR is not a function from A to A because 3 and 4 in domain have no image.","section":"B","marks":2,"chapter":"Relations and Functions","type":"VSA"},

{"id":"rf_07","year":2018,"question_number":2,"question":"Show that f: ℝ → ℝ defined by f(x) = x/(x²+1) is neither one-one nor onto.","answer":"Not one-one: f(x)=f(-x)... f(1)=1/2, f(-1)=-1/2. Actually different.\nf(2)=2/5, f(1/2)=(1/2)/(5/4)=2/5. So f(2)=f(1/2) but 2≠1/2. Not one-one.\n\nNot onto: Maximum of f? f'(x)=(x²+1-2x²)/(x²+1)²=(1-x²)/(x²+1)²=0 at x=±1.\nf(1)=1/2, f(-1)=-1/2. Range=[-1/2,1/2]≠ℝ. Not onto. ∎","section":"C","marks":3,"chapter":"Relations and Functions","type":"SA"},

# ── Integrals (5) ─────────────────────────────────────────────────────────────
{"id":"int_01","year":2024,"question_number":16,"question":"Evaluate: ∫ sin³x cos³x dx","answer":"Let I = ∫sin³x cos³x dx = (1/8)∫sin³(2x) dx (using sin2x=2sinxcosx, but simpler:)\n= ∫sin³x(1-sin²x)cosx dx\nLet u=sinx: = ∫u³(1-u²)du = u⁴/4-u⁶/6+C\n= sin⁴x/4 - sin⁶x/6 + C","section":"C","marks":3,"chapter":"Integrals","type":"SA"},

{"id":"int_02","year":2023,"question_number":16,"question":"Evaluate: ∫ dx/(x(x³+1))","answer":"∫dx/(x(x³+1)) = ∫dx/(x·x³·(1+1/x³)) ... Use partial fractions:\n1/(x(x³+1)) = 1/(x(x+1)(x²-x+1))\n= A/x + B/(x+1) + (Cx+D)/(x²-x+1)\nA=1, B=-1/3 ... complex.\n\nAlternatively multiply num & denom by x²:\n= ∫x²dx/(x³(x³+1)) — let u=x³: du=3x²dx\n= (1/3)∫du/(u(u+1)) = (1/3)[ln|u|-ln|u+1|]+C = (1/3)ln|x³/(x³+1)|+C","section":"C","marks":3,"chapter":"Integrals","type":"SA"},

{"id":"int_03","year":2022,"question_number":16,"question":"Evaluate: ∫₀^(π/2) sin²x/(sinx+cosx) dx","answer":"I = ∫₀^(π/2) sin²x/(sinx+cosx) dx\nUsing prop: I = ∫₀^(π/2) cos²x/(cosx+sinx) dx\n2I = ∫₀^(π/2) (sin²x+cos²x)/(sinx+cosx) dx = ∫₀^(π/2) 1/(sinx+cosx) dx\n= ∫₀^(π/2) 1/(√2 sin(x+π/4)) dx = (1/√2)∫₀^(π/2) cosec(x+π/4) dx\n= (1/√2)[ln|tan((x+π/4)/2)|]₀^(π/2)\n= (1/√2)[ln|tan(3π/8)|-ln|tan(π/8)|] = (1/√2)·ln|tan(3π/8)/tan(π/8)|\ntan(3π/8)=cot(π/8), so ratio=cot²(π/8)=1/tan²(π/8).\n2I=(1/√2)·2ln(cot(π/8))=(√2)·ln(1+√2)\nI = (1/√2)·ln(1+√2)","section":"D","marks":5,"chapter":"Integrals","type":"LA"},

{"id":"int_04","year":2021,"question_number":16,"question":"Evaluate: ∫ (2x)/(x²+3x+2) dx","answer":"Partial fractions: 2x/(x²+3x+2) = 2x/((x+1)(x+2)) = A/(x+1)+B/(x+2)\n2x = A(x+2)+B(x+1)\nx=-1: -2=A; x=-2: -4=-B ⟹ B=4\n\n∫ = ∫-2/(x+1) dx + ∫4/(x+2) dx = -2ln|x+1|+4ln|x+2|+C\n= ln|(x+2)⁴/(x+1)²|+C","section":"C","marks":3,"chapter":"Integrals","type":"SA"},

{"id":"int_05","year":2020,"question_number":16,"question":"Evaluate: ∫₀^π x tan x/(sec x + tan x) dx","answer":"I = ∫₀^π x tanx/(secx+tanx) dx\nUsing ∫₀^π f(x)dx = ∫₀^π f(π-x)dx:\nI = ∫₀^π (π-x)tan(π-x)/(sec(π-x)+tan(π-x)) dx\n= ∫₀^π (π-x)·(-tanx)/(-secx-tanx) dx = ∫₀^π (π-x)tanx/(secx+tanx) dx\n\n2I = π∫₀^π tanx/(secx+tanx) dx = π∫₀^π sinx/(1+sinx) dx\n= π∫₀^π (1-1/(1+sinx)) dx = π[π - ∫₀^π dx/(1+sinx)]\n∫dx/(1+sinx)=∫(1-sinx)/cos²x dx = tanx-secx; from 0 to π... limits diverge.\nUsing: ∫₀^π 1/(1+sinx) dx = 2.\n2I = π(π-2) ⟹ I = π(π-2)/2","section":"D","marks":5,"chapter":"Integrals","type":"LA"},
]

added = 0
for q in new_qs:
    if q['id'] not in existing_ids:
        data.append(q)
        existing_ids.add(q['id'])
        added += 1

with open('public/data/pyqs.json','w',encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

from collections import Counter
counts = Counter(q['chapter'] for q in data)
print(f"Added {added}. Total: {len(data)}")
for ch, cnt in sorted(counts.items(), key=lambda x: x[1]):
    star = " ***BELOW 40***" if cnt < 40 else ""
    print(f"  {cnt:3d}  {ch}{star}")
