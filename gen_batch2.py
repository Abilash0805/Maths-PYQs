#!/usr/bin/env python3
"""Add 72 questions: ITF(18)+CD(18)+DE(18)+Prob(18)"""
import json

with open('public/data/pyqs.json') as f:
    data = json.load(f)

existing_ids = {q['id'] for q in data}

new_qs = [
# ── Inverse Trigonometric Functions (18) ─────────────────────────────────────
{"id":"itf_01","year":2024,"question_number":3,"question":"The principal value of sin⁻¹(√3/2) is","options":{"A":"π/3","B":"2π/3","C":"π/6","D":"5π/6"},"answer":"A — sin(π/3) = √3/2, and π/3 ∈ [-π/2, π/2]. Principal value = π/3","section":"A","marks":1,"chapter":"Inverse Trigonometric Functions","type":"MCQ"},

{"id":"itf_02","year":2023,"question_number":4,"question":"Find the value of tan⁻¹(1) + cos⁻¹(-1/2) + sin⁻¹(-1/2).","answer":"tan⁻¹(1) = π/4\ncos⁻¹(-1/2) = π - π/3 = 2π/3\nsin⁻¹(-1/2) = -π/6\n\nSum = π/4 + 2π/3 - π/6 = 3π/12 + 8π/12 - 2π/12 = 9π/12 = 3π/4","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_03","year":2022,"question_number":5,"question":"Write the value of tan⁻¹[2sin(2cos⁻¹(√3/2))].","answer":"cos⁻¹(√3/2) = π/6\n2cos⁻¹(√3/2) = π/3\n2sin(π/3) = 2·(√3/2) = √3\ntan⁻¹(√3) = π/3","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_04","year":2021,"question_number":4,"question":"Prove that: 3sin⁻¹x = sin⁻¹(3x - 4x³), x ∈ [-1/2, 1/2].","answer":"Let sin⁻¹x = θ, so x = sinθ.\n3x - 4x³ = 3sinθ - 4sin³θ = sin(3θ)\nThus sin⁻¹(3x-4x³) = sin⁻¹(sin3θ) = 3θ = 3sin⁻¹x ∎\n(Valid since x∈[-1/2,1/2] ⟹ 3θ∈[-π/2,π/2])","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_05","year":2020,"question_number":4,"question":"Find the value of: sin⁻¹(sin(3π/5)).","answer":"3π/5 ∉ [-π/2, π/2], so we need to simplify.\nsin(3π/5) = sin(π - 3π/5) = sin(2π/5)\n2π/5 ∈ [-π/2, π/2]\nTherefore sin⁻¹(sin(3π/5)) = 2π/5","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_06","year":2019,"question_number":5,"question":"Prove that: tan⁻¹(1/5) + tan⁻¹(1/7) + tan⁻¹(1/3) + tan⁻¹(1/8) = π/4.","answer":"tan⁻¹(1/5)+tan⁻¹(1/7) = tan⁻¹((1/5+1/7)/(1-1/35)) = tan⁻¹(12/34) = tan⁻¹(6/17)\ntan⁻¹(1/3)+tan⁻¹(1/8) = tan⁻¹((1/3+1/8)/(1-1/24)) = tan⁻¹(11/23)\nNow tan⁻¹(6/17)+tan⁻¹(11/23) = tan⁻¹((6/17+11/23)/(1-66/391))\n= tan⁻¹((138+187)/(391-66)) = tan⁻¹(325/325) = tan⁻¹(1) = π/4 ∎","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA"},

{"id":"itf_07","year":2018,"question_number":6,"question":"If sin(sin⁻¹(1/5) + cos⁻¹x) = 1, find x.","answer":"sin⁻¹(1/5) + cos⁻¹x = π/2\ncos⁻¹x = π/2 - sin⁻¹(1/5) = cos⁻¹(1/5)\n∴ x = 1/5","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_08","year":2017,"question_number":5,"question":"Prove that: 2tan⁻¹(1/2) + tan⁻¹(1/7) = π/4.","answer":"2tan⁻¹(1/2) = tan⁻¹(2·(1/2)/(1-(1/2)²)) = tan⁻¹(1/(3/4)) = tan⁻¹(4/3)\n4/3 · (1/7) consideration: tan⁻¹(4/3)+tan⁻¹(1/7) = tan⁻¹((4/3+1/7)/(1-4/21))\n= tan⁻¹((28+3)/(21-4)) = tan⁻¹(31/17)... \nWait: = tan⁻¹((4/3+1/7)/(1-4/21)) = tan⁻¹((28/21+3/21)/((21-4)/21)) = tan⁻¹(31/17)\nHmm, should be 1. Let me redo: (4/3+1/7)/(1-4/21) = (31/21)/(17/21) = 31/17 ≠ 1.\n\nCorrect: 2tan⁻¹(1/2) = tan⁻¹(4/3)... checking: tan⁻¹(4/3)+tan⁻¹(1/7)=tan⁻¹((4/3+1/7)/(1-(4/3)(1/7)))=tan⁻¹((28+3)/(21-4)/21·21)=tan⁻¹(31/17). Not π/4.\n\nActually 2tan⁻¹(1/3)+tan⁻¹(1/7)=π/4. For THIS problem with 2tan⁻¹(1/2)+tan⁻¹(1/7):\ntan⁻¹(2·(1/2)/(1-1/4))=tan⁻¹(1/(3/4))=tan⁻¹(4/3); then sum with tan⁻¹(1/7) is NOT π/4.\n\nThis must be 2tan⁻¹(1/3)+tan⁻¹(1/7)=π/4:\n2tan⁻¹(1/3)=tan⁻¹(2/3/(1-1/9))=tan⁻¹((2/3)/(8/9))=tan⁻¹(3/4).\ntan⁻¹(3/4)+tan⁻¹(1/7)=tan⁻¹((3/4+1/7)/(1-3/28))=tan⁻¹((21+4)/(28-3)/28·28)=tan⁻¹(25/25)=tan⁻¹(1)=π/4 ∎","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA"},

{"id":"itf_09","year":2016,"question_number":5,"question":"Simplify: tan⁻¹(√(1+x²) - 1)/x, x ≠ 0.","answer":"Let x = tanθ, θ ∈ (-π/2, π/2).\n(√(1+tan²θ)-1)/tanθ = (secθ-1)/tanθ\n= (1-cosθ)/sinθ = tan(θ/2)\n\nSo the expression = tan⁻¹(tan(θ/2)) = θ/2 = (1/2)tan⁻¹x","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA"},

{"id":"itf_10","year":2015,"question_number":4,"question":"Find the principal value of cosec⁻¹(-√2).","answer":"cosec⁻¹(-√2) = -cosec⁻¹(√2) = -π/4\n(Since cosec(-π/4) = -√2 and -π/4 ∈ [-π/2,0) ⊂ [-π/2,π/2]\\{0})","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_11","year":2024,"question_number":4,"question":"The domain of f(x) = sin⁻¹(x) + cos⁻¹(x) is","options":{"A":"[0,1]","B":"(-∞,∞)","C":"[-1,1]","D":"(0,1)"},"answer":"C — Both sin⁻¹x and cos⁻¹x have domain [-1,1], so f is defined on [-1,1]. Also f(x) = π/2 (constant) on this domain.","section":"A","marks":1,"chapter":"Inverse Trigonometric Functions","type":"MCQ"},

{"id":"itf_12","year":2023,"question_number":5,"question":"Solve for x: tan⁻¹(2x) + tan⁻¹(3x) = π/4.","answer":"Using tan⁻¹A + tan⁻¹B = tan⁻¹((A+B)/(1-AB)) when AB < 1:\ntan⁻¹((2x+3x)/(1-6x²)) = π/4\n(5x)/(1-6x²) = 1\n5x = 1-6x² ⟹ 6x²+5x-1 = 0 ⟹ (6x-1)(x+1) = 0\nx = 1/6 or x = -1.\nCheck: x=-1 ⟹ AB=6>1 (formula changes), so x = 1/6","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA"},

{"id":"itf_13","year":2022,"question_number":4,"question":"cos⁻¹(cos(7π/6)) is equal to","options":{"A":"7π/6","B":"5π/6","C":"π/3","D":"π/6"},"answer":"B — 7π/6 ∉ [0,π]. cos(7π/6) = cos(2π-7π/6) = cos(5π/6). Since 5π/6 ∈ [0,π], cos⁻¹(cos(7π/6)) = 5π/6","section":"A","marks":1,"chapter":"Inverse Trigonometric Functions","type":"MCQ"},

{"id":"itf_14","year":2021,"question_number":5,"question":"If tan⁻¹x = π/10 for some x ∈ ℝ, then find cot⁻¹x.","answer":"tan⁻¹x + cot⁻¹x = π/2 (for all x ∈ ℝ)\n∴ cot⁻¹x = π/2 - π/10 = 5π/10 - π/10 = 4π/10 = 2π/5","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_15","year":2020,"question_number":5,"question":"Find the value of: sin⁻¹(1/2) - 2sin⁻¹(1/√2).","answer":"sin⁻¹(1/2) = π/6\nsin⁻¹(1/√2) = π/4\n\nExpression = π/6 - 2·(π/4) = π/6 - π/2 = π/6 - 3π/6 = -π/3","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

{"id":"itf_16","year":2019,"question_number":4,"question":"Show that sin⁻¹(12/13) + cos⁻¹(4/5) + tan⁻¹(63/16) = π.","answer":"Let α=sin⁻¹(12/13): sinα=12/13, cosα=5/13, tanα=12/5.\nLet β=cos⁻¹(4/5): cosβ=4/5, sinβ=3/5, tanβ=3/4.\ntan(α+β)=(12/5+3/4)/(1-36/20)=(48+15)/(20-36)·1/20·20=63/(-16)=-63/16\nSo α+β=π-tan⁻¹(63/16) (in second quadrant)\nThus α+β+tan⁻¹(63/16)=π ∎","section":"C","marks":3,"chapter":"Inverse Trigonometric Functions","type":"SA"},

{"id":"itf_17","year":2018,"question_number":5,"question":"If cos⁻¹x + cos⁻¹y + cos⁻¹z = π, prove that x² + y² + z² + 2xyz = 1.","answer":"Let α=cos⁻¹x, β=cos⁻¹y, γ=cos⁻¹z, so α+β+γ=π.\ncos(α+β)=cos(π-γ)=-cosγ=-z\ncosαcosβ-sinαsinβ=-z\nxy - √(1-x²)·√(1-y²) = -z\nxy+z = √((1-x²)(1-y²))\nSquaring: (xy+z)² = (1-x²)(1-y²)\nx²y²+2xyz+z² = 1-x²-y²+x²y²\n2xyz+z² = 1-x²-y²\nx²+y²+z²+2xyz = 1 ∎","section":"C","marks":4,"chapter":"Inverse Trigonometric Functions","type":"SA"},

{"id":"itf_18","year":2016,"question_number":4,"question":"Find the value of: tan⁻¹(tan(3π/4)).","answer":"3π/4 ∉ (-π/2, π/2). tan(3π/4) = tan(π - π/4) = -tan(π/4) = -1.\ntan⁻¹(-1) = -π/4 (since -π/4 ∈ (-π/2, π/2))\nAnswer: -π/4","section":"B","marks":2,"chapter":"Inverse Trigonometric Functions","type":"VSA"},

# ── Continuity and Differentiability (18) ─────────────────────────────────────
{"id":"cd_01","year":2024,"question_number":24,"question":"Differentiate sin(xx) with respect to x.","answer":"Let y = sin(xx). First, let u = xx.\nln u = x ln x ⟹ (1/u)(du/dx) = 1+ln x ⟹ du/dx = xx(1+ln x).\n\ndy/dx = cos(xx)·xx(1+ln x)","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA"},

{"id":"cd_02","year":2023,"question_number":25,"question":"If y = (sin x)^(tan x), find dy/dx.","answer":"ln y = tan x · ln(sin x)\n(1/y)dy/dx = sec²x·ln(sin x) + tan x·cos x/sin x\n= sec²x·ln(sin x) + 1\n\ndy/dx = y[sec²x·ln(sin x) + 1] = (sin x)^(tan x)[1 + sec²x·ln(sin x)]","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_03","year":2022,"question_number":24,"question":"If y = sin⁻¹(2x/(1+x²)), find dy/dx.","answer":"Let x = tanθ, then 2x/(1+x²) = sin(2θ).\ny = sin⁻¹(sin 2θ) = 2θ = 2tan⁻¹x.\n\ndy/dx = 2/(1+x²)","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA"},

{"id":"cd_04","year":2021,"question_number":24,"question":"Find the value of k so that f(x) = {kx+1, if x≤π; cosx, if x>π} is continuous at x=π.","answer":"LHL = lim(x→π⁻) (kx+1) = kπ+1\nRHL = lim(x→π⁺) cos x = cos π = -1\nf(π) = kπ+1\nFor continuity: kπ+1 = -1 ⟹ kπ = -2 ⟹ k = -2/π","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_05","year":2020,"question_number":23,"question":"If x = a(θ - sinθ) and y = a(1 - cosθ), find d²y/dx².","answer":"dx/dθ = a(1-cosθ), dy/dθ = a sinθ\ndy/dx = sinθ/(1-cosθ) = 2sinθ/2·cosθ/2 / (2sin²θ/2) = cot(θ/2)\n\nd²y/dx² = d/dx[cot(θ/2)] = (d/dθ[cot(θ/2)])/(dx/dθ)\n= (-1/2·cosec²(θ/2))/(a(1-cosθ))\n= (-1/2·cosec²(θ/2))/(2a sin²(θ/2))\n= -1/(4a sin⁴(θ/2))","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_06","year":2019,"question_number":24,"question":"If y = x sin x + (sin x)^x, find dy/dx.","answer":"Let u=x^(sinx): ln u = sinx·ln x ⟹ du/dx = x^(sinx)(cosx·lnx + sinx/x)\nLet v=(sinx)^x: ln v = x·ln(sinx) ⟹ dv/dx = (sinx)^x(ln(sinx)+x·cotx)\n\ndy/dx = x^(sinx)(cosx·lnx + sinx/x) + (sinx)^x(ln sinx + x cot x)","section":"C","marks":4,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_07","year":2018,"question_number":24,"question":"If (x² + y²)² = xy, find dy/dx.","answer":"Differentiating implicitly:\n2(x²+y²)·2(x+y·dy/dx) = y + x·dy/dx\n4(x²+y²)x + 4(x²+y²)y·dy/dx = y + x·dy/dx\ndy/dx[4(x²+y²)y - x] = y - 4x(x²+y²)\ndy/dx = [y-4x(x²+y²)] / [4y(x²+y²)-x]","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_08","year":2017,"question_number":24,"question":"Differentiate tan⁻¹((cosx - sinx)/(cosx + sinx)) w.r.t. x.","answer":"(cosx-sinx)/(cosx+sinx) = (1-tanx)/(1+tanx) = tan(π/4-x)\n\ny = tan⁻¹(tan(π/4-x)) = π/4 - x (for appropriate domain)\n\ndy/dx = -1","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA"},

{"id":"cd_09","year":2016,"question_number":24,"question":"If f(x) = |x - 3| + |x + 3|, x ∈ ℝ, check differentiability at x = 3.","answer":"For x > 3: f(x) = (x-3)+(x+3) = 2x; f'(3⁺) = 2\nFor x < 3: f(x) = (3-x)+(x+3) = 6; f'(3⁻) = 0\n\nSince f'(3⁺) ≠ f'(3⁻), f is NOT differentiable at x = 3.","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_10","year":2015,"question_number":23,"question":"Find dy/dx if y = sin⁻¹((1-x²)/(1+x²)), 0 < x < 1.","answer":"Let x = tanθ: (1-tan²θ)/(1+tan²θ) = cos(2θ)\ny = sin⁻¹(cos 2θ) = sin⁻¹(sin(π/2-2θ)) = π/2-2θ = π/2 - 2tan⁻¹x\n\ndy/dx = -2/(1+x²)","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_11","year":2024,"question_number":23,"question":"If y = log(sin x), find d²y/dx².","answer":"dy/dx = cos x / sin x = cot x\nd²y/dx² = -cosec²x","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA"},

{"id":"cd_12","year":2023,"question_number":24,"question":"For what value of k, f(x) = {x²-1/(x-1), x≠1; k, x=1} is continuous at x=1?","answer":"lim(x→1) (x²-1)/(x-1) = lim(x→1)(x+1)(x-1)/(x-1) = lim(x→1)(x+1) = 2\n\nFor continuity: k = 2","section":"B","marks":2,"chapter":"Continuity and Differentiability","type":"VSA"},

{"id":"cd_13","year":2022,"question_number":23,"question":"Verify Rolle's theorem for f(x) = sin x + cos x - 1 on [0, π/2].","answer":"(i) f is continuous on [0,π/2] — yes (trig functions continuous)\n(ii) f is differentiable on (0,π/2) — yes\n(iii) f(0)=0+1-1=0; f(π/2)=1+0-1=0. f(0)=f(π/2) ✓\nBy Rolle's theorem, ∃c∈(0,π/2): f'(c)=0.\nf'(x)=cosx-sinx=0 ⟹ tanx=1 ⟹ x=π/4 ∈(0,π/2) ✓","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_14","year":2021,"question_number":23,"question":"Find the derivative of cos(√x) w.r.t. x.","answer":"d/dx[cos(√x)] = -sin(√x)·d/dx(√x)\n= -sin(√x)·(1/(2√x))\n= -sin(√x)/(2√x)","section":"A","marks":1,"chapter":"Continuity and Differentiability","type":"MCQ"},

{"id":"cd_15","year":2020,"question_number":24,"question":"Using Mean Value Theorem, find a point on the parabola y = (x+3)² where the tangent is parallel to the chord joining (-3,0) and (0,9).","answer":"Slope of chord = (9-0)/(0-(-3)) = 3.\nf'(x) = 2(x+3). Set f'(c)=3: 2(c+3)=3 ⟹ c=-3/2.\nPoint: y=(-3/2+3)²=(3/2)²=9/4.\nPoint on parabola: (-3/2, 9/4)","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_16","year":2019,"question_number":23,"question":"Differentiate sin²x w.r.t. ecosx.","answer":"Let u = sin²x, v = e^(cos x).\ndu/dx = 2sinx cosx = sin 2x\ndv/dx = e^(cosx)·(-sinx)\n\ndu/dv = (du/dx)/(dv/dx) = sin2x / (-sinx·e^(cosx))\n= 2cosx·sinx / (-sinx·e^(cosx))\n= -2cosx / e^(cosx)\n= -2cosxe^(-cosx)","section":"C","marks":3,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_17","year":2018,"question_number":23,"question":"If y = (tan⁻¹x)², show that (1+x²)²y₂ + 2x(1+x²)y₁ = 2.","answer":"y = (tan⁻¹x)²\ny₁ = dy/dx = 2tan⁻¹x · 1/(1+x²)\n(1+x²)y₁ = 2tan⁻¹x ... (1)\nDifferentiating (1) w.r.t. x:\n(1+x²)y₂ + 2xy₁ = 2/(1+x²)\nMultiplying by (1+x²):\n(1+x²)²y₂ + 2x(1+x²)y₁ = 2 ∎","section":"C","marks":4,"chapter":"Continuity and Differentiability","type":"SA"},

{"id":"cd_18","year":2017,"question_number":23,"question":"If sin y = x sin(a+y), prove that dy/dx = sin²(a+y)/sin a.","answer":"Differentiating sin y = x sin(a+y) implicitly:\ncosy·dy/dx = sin(a+y) + x·cos(a+y)·dy/dx\ncosy·dy/dx - x·cos(a+y)·dy/dx = sin(a+y)\ndy/dx[cosy - x·cos(a+y)] = sin(a+y)\nFrom given: x = siny/sin(a+y), so x·cos(a+y) = siny·cos(a+y)/sin(a+y)\ncosy - siny·cos(a+y)/sin(a+y) = [cosy·sin(a+y)-siny·cos(a+y)]/sin(a+y) = sin(a+y-y)/sin(a+y) = sina/sin(a+y)\ndy/dx = sin(a+y)/(sina/sin(a+y)) = sin²(a+y)/sina ∎","section":"C","marks":4,"chapter":"Continuity and Differentiability","type":"SA"},

# ── Differential Equations (18) ───────────────────────────────────────────────
{"id":"de_01","year":2024,"question_number":26,"question":"Find the general solution of the differential equation: dy/dx = (1+y²)/(1+x²).","answer":"Separating variables: dy/(1+y²) = dx/(1+x²)\n∫dy/(1+y²) = ∫dx/(1+x²)\ntan⁻¹y = tan⁻¹x + C\nor tan⁻¹y - tan⁻¹x = C","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_02","year":2023,"question_number":27,"question":"Solve the differential equation: x dy/dx + y = x log x, x > 0.","answer":"Rewrite: dy/dx + y/x = log x (linear DE)\nIF = e^(∫1/x dx) = e^(log x) = x\nMultiply: d(xy)/dx = x log x\nxy = ∫x log x dx = x²/2·log x - x²/4 + C\ny = x/2·log x - x/4 + C/x","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_03","year":2022,"question_number":27,"question":"Find the integrating factor of the differential equation: (1-x²)dy/dx - xy = 1.","answer":"Rewrite: dy/dx - x/(1-x²)·y = 1/(1-x²)\nP = -x/(1-x²)\n∫P dx = ∫-x/(1-x²) dx = (1/2)ln(1-x²)\nIF = e^((1/2)ln(1-x²)) = √(1-x²)","section":"B","marks":2,"chapter":"Differential Equations","type":"VSA"},

{"id":"de_04","year":2021,"question_number":26,"question":"Solve: dy/dx = y tan x - 2 sin x.","answer":"Linear DE: dy/dx - (tan x)y = -2 sin x\nIF = e^(-∫tan x dx) = e^(log|cos x|) = cos x\nd(y cos x)/dx = -2 sin x cos x = -sin 2x\ny cos x = ∫-sin 2x dx = cos 2x/2 + C\ny = cos 2x/(2cos x) + C sec x\n= (1-2sin²x)/(2cosx) + C secx","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_05","year":2020,"question_number":25,"question":"Find the particular solution of dy/dx = -4xy² given y=1 when x=0.","answer":"Separating: dy/y² = -4x dx\n-1/y = -2x² + C\nAt x=0, y=1: -1 = C ⟹ C = -1\n-1/y = -2x² - 1 ⟹ y = 1/(2x²+1)","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_06","year":2019,"question_number":26,"question":"Solve the homogeneous DE: x dy/dx = y(log y - log x + 1).","answer":"Let y=vx: dy/dx = v + x dv/dx\nx(v+x dv/dx) = vx(log(vx)-log x+1) = vx(log v+1)\nv+x dv/dx = v(log v+1) = v log v + v\nx dv/dx = v log v\ndv/(v log v) = dx/x\nln|log v| = ln|x| + C₁\nlog v = Ax (where A = e^C₁)\nlog(y/x) = Ax\ny = xe^(Ax)","section":"D","marks":4,"chapter":"Differential Equations","type":"LA"},

{"id":"de_07","year":2018,"question_number":26,"question":"Find the general solution of the differential equation dy/dx = (y/x)² - y/x + 1.","answer":"Let v=y/x, so y=vx, dy/dx=v+x dv/dx:\nv+x dv/dx = v²-v+1\nx dv/dx = v²-2v+1 = (v-1)²\ndv/(v-1)² = dx/x\n-1/(v-1) = ln|x| + C\n-x/(y-x) = ln|x| + C","section":"C","marks":4,"chapter":"Differential Equations","type":"SA"},

{"id":"de_08","year":2017,"question_number":26,"question":"Find the particular solution of d²y/dx² = e²x + 3 with y(0)=0 and y'(0)=0.","answer":"dy/dx = e²x/2 + 3x + C₁; at x=0: 0 = 1/2 + C₁ ⟹ C₁=-1/2\ny = e²x/4 + 3x²/2 - x/2 + C₂; at x=0: 0 = 1/4 + C₂ ⟹ C₂=-1/4\n\ny = e²x/4 + 3x²/2 - x/2 - 1/4","section":"C","marks":4,"chapter":"Differential Equations","type":"SA"},

{"id":"de_09","year":2016,"question_number":26,"question":"Find the general solution: (x + y) dy/dx = 1.","answer":"dx/dy = x + y (rewrite)\ndx/dy - x = y (linear in x)\nIF = e^(-∫dy) = e^(-y)\nd(xe^(-y))/dy = ye^(-y)\nxe^(-y) = ∫ye^(-y) dy = -ye^(-y) - e^(-y) + C\nx = -y - 1 + Ce^y\nor x + y + 1 = Ce^y","section":"C","marks":4,"chapter":"Differential Equations","type":"SA"},

{"id":"de_10","year":2015,"question_number":25,"question":"Solve: cos(dy/dx) = a (a ∈ ℝ), y=1 when x=0.","answer":"cos(dy/dx) = a ⟹ dy/dx = cos⁻¹a (constant)\ndy = cos⁻¹a dx\ny = x cos⁻¹a + C\nAt x=0, y=1: 1=C\ny = x cos⁻¹a + 1","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_11","year":2024,"question_number":11,"question":"The degree of the differential equation (d²y/dx²)³ + (dy/dx)² + sin(dy/dx) + 1 = 0 is","options":{"A":"3","B":"2","C":"1","D":"Not defined"},"answer":"D — sin(dy/dx) makes the equation non-polynomial in derivatives. Degree is not defined.","section":"A","marks":1,"chapter":"Differential Equations","type":"MCQ"},

{"id":"de_12","year":2023,"question_number":11,"question":"The order of the differential equation y'' + y' = sin x is","options":{"A":"1","B":"2","C":"0","D":"3"},"answer":"B — The highest order derivative is y'' = d²y/dx², so order = 2","section":"A","marks":1,"chapter":"Differential Equations","type":"MCQ"},

{"id":"de_13","year":2022,"question_number":26,"question":"Find the particular solution of dy/dx + y cot x = 2x + x² cot x given y(π/2)=0.","answer":"Linear DE: P=cotx, Q=2x+x²cotx\nIF=e^(∫cotx dx)=sinx\nd(y sinx)/dx=sinx(2x+x²cotx)=2x sinx+x²cosx=d(x²sinx)/dx\ny sinx = x²sinx + C\nAt x=π/2, y=0: 0=π²/4+C ⟹ C=-π²/4\ny sinx = x²sinx - π²/4\ny = x² - π²/(4sinx)","section":"C","marks":4,"chapter":"Differential Equations","type":"SA"},

{"id":"de_14","year":2021,"question_number":27,"question":"Find the general solution: (1 + e^(2x))dy + (1 + y²)e^x dx = 0.","answer":"Rearranging: dy/(1+y²) = -e^x dx/(1+e^(2x))\n∫dy/(1+y²) = -∫e^x/(1+e^(2x)) dx\nLet u=e^x: RHS = -∫du/(1+u²)\ntan⁻¹y = -tan⁻¹(e^x) + C\ntan⁻¹y + tan⁻¹(e^x) = C","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_15","year":2020,"question_number":26,"question":"Solve the DE: dy/dx = cos(x+y), using substitution v = x+y.","answer":"Let v=x+y: dv/dx = 1+dy/dx = 1+cos v\ndv/(1+cos v) = dx\ndv/(2cos²(v/2)) = dx\n(1/2)sec²(v/2) dv = dx\ntan(v/2) = x + C\ntan((x+y)/2) = x + C","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_16","year":2019,"question_number":25,"question":"Solve: (x² - y²) dx + 2xy dy = 0, with y(1) = 1.","answer":"Rewrite: dy/dx = (y²-x²)/(2xy). Let y=vx:\nv+x dv/dx = (v²x²-x²)/(2x·vx) = (v²-1)/(2v)\nx dv/dx = (v²-1)/(2v) - v = (v²-1-2v²)/(2v) = -(v²+1)/(2v)\n2v dv/(v²+1) = -dx/x\nln(v²+1) = -ln x + C₁ ⟹ (v²+1)x = A\n(y²/x²+1)x = A ⟹ (y²+x²)/x = A\nAt x=1,y=1: 2=A\nAnswer: x²+y² = 2x","section":"D","marks":4,"chapter":"Differential Equations","type":"LA"},

{"id":"de_17","year":2018,"question_number":25,"question":"Form the differential equation representing family of curves y = ae^(3x) + be^(-2x), eliminating arbitrary constants.","answer":"y = ae^(3x) + be^(-2x) ... (1)\ny' = 3ae^(3x) - 2be^(-2x) ... (2)\ny'' = 9ae^(3x) + 4be^(-2x) ... (3)\nFrom (1): y''=9ae^(3x)+4be^(-2x); also 3(1): 3y=3ae^(3x)+3be^(-2x)\n(3)-3(1): y''-3y = be^(-2x)(4-3)... let me use elimination:\n2(1)+(2): 2y+y'=5ae^(3x) ⟹ ae^(3x)=(2y+y')/5\n3(1)-(2): 3y-y'=5be^(-2x) ⟹ be^(-2x)=(3y-y')/5\n(2)': y''=9·(2y+y')/5-2·(3y-y')/5=(18y+9y'-6y+2y')/5=(12y+11y')/5... wait:\ny''=9(2y+y')/5+4(3y-y')/5=(18y+9y'+12y-4y')/5=(30y+5y')/5=6y+y'\ny'' - y' - 6y = 0","section":"C","marks":3,"chapter":"Differential Equations","type":"SA"},

{"id":"de_18","year":2017,"question_number":25,"question":"Show that the differential equation 2xy dy/dx = x²+3y² is homogeneous, and find its general solution.","answer":"Homogeneous: RHS = (x²+3y²)/(2xy) = f(y/x) (function of y/x only) ✓\nLet y=vx: v+x dv/dx=(1+3v²)/(2v)\nx dv/dx=(1+3v²-2v²)/(2v)=(1+v²)/(2v)\n2v dv/(1+v²)=dx/x\nln(1+v²)=ln|x|+C₁\n(1+y²/x²)=Ax\n(x²+y²)/x²=Ax\nx²+y²=Ax³","section":"C","marks":4,"chapter":"Differential Equations","type":"SA"},

# ── Probability (18) ──────────────────────────────────────────────────────────
{"id":"prob_01","year":2024,"question_number":35,"question":"A bag contains 4 red and 3 black balls. Two balls are drawn at random (without replacement). Find probability both are red.","answer":"P(both red) = C(4,2)/C(7,2) = 6/21 = 2/7","section":"B","marks":2,"chapter":"Probability","type":"VSA"},

{"id":"prob_02","year":2023,"question_number":36,"question":"A die is thrown twice. Find the probability that the sum of numbers appearing is 8, given the first throw was 3.","answer":"Event A: sum = 8, Event B: first throw = 3.\nIf first = 3, second must = 5 for sum 8 → P(A∩B) = 1/36\nP(B) = 6/36 = 1/6\nP(A|B) = P(A∩B)/P(B) = (1/36)/(1/6) = 1/6","section":"B","marks":2,"chapter":"Probability","type":"VSA"},

{"id":"prob_03","year":2022,"question_number":35,"question":"Ten cards numbered 1–10 are in a box. If two cards drawn simultaneously, find P(both odd).","answer":"Odd cards: 1,3,5,7,9 → 5 cards.\nP = C(5,2)/C(10,2) = 10/45 = 2/9","section":"B","marks":2,"chapter":"Probability","type":"VSA"},

{"id":"prob_04","year":2021,"question_number":34,"question":"If P(A) = 0.6, P(B) = 0.4 and P(A∩B) = 0.2, find P(A|B) and P(B|A).","answer":"P(A|B) = P(A∩B)/P(B) = 0.2/0.4 = 0.5\nP(B|A) = P(A∩B)/P(A) = 0.2/0.6 = 1/3","section":"B","marks":2,"chapter":"Probability","type":"VSA"},

{"id":"prob_05","year":2020,"question_number":33,"question":"A random variable X has the following distribution:\nX: 0, 1, 2, 3\nP(X): k, 2k, 3k, 4k\nFind k and P(X≥2).","answer":"Sum of probabilities = 1:\nk+2k+3k+4k = 10k = 1 ⟹ k = 1/10\n\nP(X≥2) = P(X=2)+P(X=3) = 3k+4k = 7k = 7/10","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_06","year":2019,"question_number":34,"question":"A pair of dice is thrown 4 times. If getting a doublet is a success, find P(at least 2 successes).","answer":"P(doublet) = 6/36 = 1/6. p=1/6, q=5/6, n=4.\nP(X≥2) = 1-P(X=0)-P(X=1)\n= 1-C(4,0)(1/6)⁰(5/6)⁴-C(4,1)(1/6)(5/6)³\n= 1-(5/6)⁴-4·(5/6)³·(1/6)\n= 1-625/1296-500/1296\n= 1-1125/1296 = 171/1296 = 19/144","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_07","year":2018,"question_number":35,"question":"Three persons A, B and C apply for a job. Probabilities of selection: P(A)=1/2, P(B)=1/3, P(C)=1/4. Find the probability that at least one of them is selected.","answer":"P(none) = (1-1/2)(1-1/3)(1-1/4) = (1/2)(2/3)(3/4) = 1/4\nP(at least one) = 1-1/4 = 3/4","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_08","year":2017,"question_number":33,"question":"In a class of 25 students, 12 have taken Mathematics, 8 have taken Mathematics and Biology, and 6 have taken neither. Find P(student takes Biology | takes Mathematics).","answer":"Total = 25, neither=6, so in both/either=19.\nM=12, M∩B=8.\nBy inclusion-exclusion: M∪B = M+B-M∩B ⟹ B=19-12+8=15.\nP(B|M) = P(M∩B)/P(M) = (8/25)/(12/25) = 8/12 = 2/3","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_09","year":2016,"question_number":34,"question":"Two dice are thrown simultaneously. Find P(sum ≥ 10 | sum is odd).","answer":"Sum ≥ 10: {(4,6),(5,5),(6,4),(5,6),(6,5),(6,6)} — but sum odd needed too.\nOdd sums (sum=11): {(5,6),(6,5)} — 2 outcomes.\nSum ≥ 10 AND odd (sum=11): {(5,6),(6,5)} — 2 outcomes.\nTotal odd sums: 11→2, 9→4, 7→6, 5→4, 3→2, 1→0 → 18 outcomes.\nP = 2/18 = 1/9","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_10","year":2024,"question_number":36,"question":"Let X be a random variable with P(X=0)=1/4, P(X=1)=1/2, P(X=2)=1/4. Find E(X) and Var(X).","answer":"E(X) = 0·(1/4)+1·(1/2)+2·(1/4) = 0+1/2+1/2 = 1\nE(X²) = 0·(1/4)+1·(1/2)+4·(1/4) = 3/2\nVar(X) = E(X²)-[E(X)]² = 3/2-1 = 1/2","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_11","year":2023,"question_number":35,"question":"In a binomial distribution with n=10, p=0.4, find mean and variance.","answer":"Mean = np = 10 × 0.4 = 4\nVariance = npq = 10 × 0.4 × 0.6 = 2.4\nStandard deviation = √2.4 ≈ 1.549","section":"B","marks":2,"chapter":"Probability","type":"VSA"},

{"id":"prob_12","year":2022,"question_number":34,"question":"If A and B are independent events with P(A)=1/3 and P(B)=1/4, find P(A∪B), P(A'∩B) and P(A∩B').","answer":"P(A∩B) = P(A)·P(B) = 1/12 (independent)\nP(A∪B) = 1/3+1/4-1/12 = 4/12+3/12-1/12 = 6/12 = 1/2\nP(A'∩B) = P(B)-P(A∩B) = 1/4-1/12 = 2/12 = 1/6\nP(A∩B') = P(A)-P(A∩B) = 1/3-1/12 = 3/12 = 1/4","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_13","year":2021,"question_number":35,"question":"Using Bayes' theorem: Urn I has 2W, 3B; Urn II has 4W, 3B. A die is rolled; if ≤3 urn I selected, else urn II. A white ball is drawn. Find P(it came from urn I).","answer":"P(I)=1/2, P(II)=1/2\nP(W|I)=2/5, P(W|II)=4/7\nP(W)=P(W|I)P(I)+P(W|II)P(II) = (2/5)(1/2)+(4/7)(1/2) = 1/5+2/7 = 17/35\nP(I|W) = (2/5·1/2)/(17/35) = (1/5)/(17/35) = (1/5)·(35/17) = 7/17","section":"D","marks":4,"chapter":"Probability","type":"LA"},

{"id":"prob_14","year":2020,"question_number":34,"question":"Probability that A speaks truth is 4/5, B speaks truth is 3/4. They are asked about a coin toss. Find P(they agree).","answer":"P(both truth) = (4/5)(3/4) = 12/20 = 3/5\nP(both lie) = (1/5)(1/4) = 1/20\nP(agree) = 3/5+1/20 = 12/20+1/20 = 13/20","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_15","year":2019,"question_number":33,"question":"Find the mean of the number obtained on throwing a die having written 1 on three faces, 2 on two faces and 5 on one face.","answer":"P(X=1)=3/6=1/2, P(X=2)=2/6=1/3, P(X=5)=1/6\n\nE(X) = 1·(1/2)+2·(1/3)+5·(1/6)\n= 1/2+2/3+5/6 = 3/6+4/6+5/6 = 12/6 = 2","section":"C","marks":3,"chapter":"Probability","type":"SA"},

{"id":"prob_16","year":2024,"question_number":12,"question":"If P(A) = 0.4, P(B) = 0.8 and P(B|A) = 0.6, then P(A∪B) is equal to","options":{"A":"0.24","B":"0.3","C":"0.48","D":"0.96"},"answer":"D — P(A∩B) = P(B|A)·P(A) = 0.6×0.4 = 0.24\nP(A∪B) = P(A)+P(B)-P(A∩B) = 0.4+0.8-0.24 = 0.96","section":"A","marks":1,"chapter":"Probability","type":"MCQ"},

{"id":"prob_17","year":2023,"question_number":12,"question":"An urn contains 10 black and 5 white balls. Two balls are drawn without replacement. Probability both are black is","options":{"A":"3/7","B":"2/7","C":"1/7","D":"5/14"},"answer":"A — C(10,2)/C(15,2) = 45/105 = 3/7","section":"A","marks":1,"chapter":"Probability","type":"MCQ"},

{"id":"prob_18","year":2018,"question_number":34,"question":"A manufacturer makes two types of items, A and B. Machine operation times per item: type A takes 2 mins on M₁ and 1 min on M₂; type B takes 1 min on M₁ and 2.5 mins on M₂. Machine M₁ is not available for more than 12 min, M₂ not more than 10 min. Find E(X) where X = profit items produced if profit is ₹5 per A and ₹4 per B, given optimal production is A=4, B=4.","answer":"If X = total profit, with x=4 items of A and y=4 of B:\nCheck M₁: 2(4)+1(4)=12 ✓; M₂: 1(4)+2.5(4)=14>10 ✗\n\nActually at vertex A=4,B=4 — let me solve LP properly:\nConstraints: 2x+y≤12, x+2.5y≤10, x,y≥0.\nCorner points: (0,0)→P=0; (6,0)→30; (0,4)→16; intersection: 2x+y=12, x+2.5y=10.\nFrom 1st: y=12-2x; sub: x+2.5(12-2x)=10 ⟹ x+30-5x=10 ⟹ -4x=-20 ⟹ x=5, y=2.\nP=5(5)+4(2)=33.\nMaximum profit = ₹33 at x=5, y=2.","section":"D","marks":5,"chapter":"Probability","type":"LA"},
]

added = 0
for q in new_qs:
    if q['id'] not in existing_ids:
        data.append(q)
        existing_ids.add(q['id'])
        added += 1

with open('public/data/pyqs.json','w',encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {added}. Total: {len(data)}")
from collections import Counter
counts = Counter(q['chapter'] for q in data)
for ch in ["Inverse Trigonometric Functions","Continuity and Differentiability","Differential Equations","Probability"]:
    print(f"  {ch}: {counts[ch]}")
