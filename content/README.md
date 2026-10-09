# Question bank source format

Every file in `content/<year>/` is one question paper (one CBSE set). Each file
accounts for **every** question number in the paper, so nothing is silently lost.

```
---
year: 2026
code: 65/1/1
series: 1PQRS
title: CBSE Board Examination 2026 · Set 1
---

=== 1 | itf | 1 | mcq
If $2\cos^{-1}x = y$, then
(A) $0 \le y \le \pi$
(B) $-\pi \le y \le \pi$
(C) $0 \le y \le 2\pi$
(D) $-\pi \le y \le 0$
--- ans C
Since $0 \le \cos^{-1}x \le \pi$ ... (solution)

=== 5 = 65/1/1#12          ← identical to Q12 of set 65/1/1 (same year)
=== 6 = 2025:65/2/1#3      ← identical to a question from another year
=== 7 x tangents & normals ← asked, but out of the 2026-27 syllabus (reason)
```

Block header: `=== <number>[a|b] | <chapter> | <marks> | <type>`

* `a`/`b` suffix = the two alternatives of an internal choice (“OR”) question.
* chapter: `rf itf mat det cd aod int aoi de vec 3d lpp prob`
* type: `mcq` (incl. one-word options), `ar` (assertion–reason), `sub` (subjective), `case` (case study)

Optional directive lines right after the header:

* `@topic <text>` – sub-topic label
* `@fig <file>` – figure shown with the question (stored in `public/figures/`)

Body syntax (question and solution): `$inline$`, `$$display$$`, `**bold**`,
pipe tables, `![caption](file.png)` figures and fenced `plot` blocks (JSON spec,
rendered as an SVG graph). A single newline is a line break; a blank line starts
a new paragraph.

## Graphs in solutions (`plot` blocks)

````
```plot
{"x":[-1,8],"y":[-1,8],
 "lines":[{"a":1,"b":1,"c":7,"label":"x + y = 7"}],
 "fns":[{"f":"sqrt(4*x)","from":0,"to":4,"label":"y² = 4x"}],
 "params":[{"x":"t*t","y":"2*t","t":[-2,2]}],
 "circles":[{"cx":0,"cy":0,"r":3}], "ellipses":[{"cx":0,"cy":0,"rx":4,"ry":2}],
 "polygons":[{"pts":[[0,0],[7,0],[3,4],[0,2]]}],
 "areas":[{"upper":"sqrt(4*x)","lower":"0","from":0,"to":4}],
 "points":[{"x":3,"y":4,"label":"B(3, 4)"}], "labels":[{"x":2,"y":1,"text":"R"}]}
```
````

* `x`, `y`: visible window. `lines`: $ax + by = c$. `fns`: $y = f(x)$ as a JavaScript expression in `x`
  (`x**2`, `sqrt`, `abs`, `sin`, `exp`, `log`, `PI` …). `params`: parametric curves in `t`.
* `polygons` and `areas` are shaded (feasible regions, areas under curves).
* Labels are plain text (use Unicode: `x²`, `√`, `≤`, `−`). Add `"dash": true` to draw a dashed curve.
