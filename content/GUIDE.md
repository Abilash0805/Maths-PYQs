# Editorial guide — CBSE Class XII Mathematics PYQ bank

This guide is binding for every paper file in `content/<year>/`. The file format is in
`content/README.md`; `content/2026/65-1-1.md` is the reference example of quality and style.

## 1. Syllabus filter (CBSE 2026-27, Mathematics 041)

Keep only questions that can be answered within the 2026-27 syllabus (the rationalised syllabus,
unchanged since 2023-24). If a question (or one alternative of an OR-question) needs a deleted topic,
record it as `=== N x <reason>` (or `=== Na x <reason>`) — never silently drop it.

| Chapter (key) | In syllabus | OUT of syllabus (skip) |
|---|---|---|
| Relations & Functions (`rf`) | reflexive/symmetric/transitive/equivalence relations, equivalence classes, counting relations, one-one/onto/bijective functions | composition of functions (gof), invertible functions / inverse of a function, binary operations |
| Inverse Trig (`itf`) | domain, range, principal value branches, graphs, principal values (incl. $\sin^{-1}(\sin\theta)$ type), simplification by substitution + ordinary trig identities (as asked in 2023-26 papers) | questions that need the deleted ITF property formulas ($\tan^{-1}x+\tan^{-1}y=\dots$, $2\tan^{-1}x=\sin^{-1}\frac{2x}{1+x^2}$ etc.), solving ITF equations, proving ITF identities |
| Matrices (`mat`) | everything else | elementary row/column operations (e.g. inverse by elementary operations) |
| Determinants (`det`) | evaluation, minors, cofactors, adjoint, inverse, area of triangle, consistency, solving systems by matrix method, $|kA|$, $|\operatorname{adj}A|$ type results | "using properties of determinants, prove/show …" |
| Continuity & Differentiability (`cd`) | continuity, differentiability, chain rule, implicit, inverse-trig, exp/log, logarithmic differentiation, parametric, second order | Rolle's theorem, Lagrange's Mean Value Theorem |
| Application of Derivatives (`aod`) | rate of change, increasing/decreasing, maxima/minima (local & absolute, word problems) | tangents and normals, approximations/differentials/errors |
| Integrals (`int`) | all integration methods, definite integrals and their properties | definite integral as the limit of a sum |
| Application of Integrals (`aoi`) | area under simple curves: regions bounded by lines/axes/ordinates and at most ONE circle/parabola/ellipse (standard form) | regions bounded by two or more non-linear curves (circle & parabola, two parabolas, two circles …) |
| Differential Equations (`de`) | order, degree, general/particular solutions (incl. verifying a solution), variable separable, homogeneous, linear ($\frac{dy}{dx}+Py=Q$, $\frac{dx}{dy}+Px=Q$) | formation of differential equations (eliminating arbitrary constants) |
| Vector Algebra (`vec`) | everything else (dot/cross product, projection, section formula, direction cosines, areas) | scalar triple product, coplanarity of vectors |
| 3-D Geometry (`3d`) | direction cosines/ratios, equations of a line, angle between lines, shortest distance (skew & parallel), foot of perpendicular, image of a point in a line, intersection of lines | anything involving a **plane** (equation of plane, line–plane angle/intersection, distance from plane), coplanarity of lines |
| Linear Programming (`lpp`) | graphical method, corner points, bounded/unbounded regions, feasible-region figures, two-variable word problems with up to three non-trivial constraints | transportation problems; problems with more than three non-trivial constraints |
| Probability (`prob`) | conditional probability, multiplication theorem, independent events, total probability, Bayes' theorem, random variable, probability distribution, mean (expectation) | variance / standard deviation of a random variable, Bernoulli trials, binomial distribution |

A question is classified into the chapter whose concept it actually tests (e.g. "solve the system
using $A^{-1}$" → `det`; area under a curve → `aoi`; max/min word problem → `aod`).

## 2. Transcription fidelity

* Transcribe from the **page image**, never from the PDF text layer (it drops symbols).
* Keep the printed wording, numbers and signs exactly. Do not "correct" a question; if it contains a
  misprint, keep it and mention the issue briefly in the solution.
* All mathematics goes in LaTeX: `$…$` inline, `$$…$$` display. Use:
  * vectors `\vec{a}`, `\overrightarrow{AB}`, unit vectors `\hat{i}, \hat{j}, \hat{k}`
  * transpose `A'`, inverse `A^{-1}`, adjoint `\operatorname{adj}A`, determinant `|A|`
  * matrices `\begin{bmatrix}…\end{bmatrix}`, determinants `\begin{vmatrix}…\end{vmatrix}`
  * piecewise functions `\begin{cases}…\end{cases}`
  * inverse trig `\sin^{-1}x`, sets `\mathbb{R}, \mathbb{Z}, \mathbb{N}`, `\in`, `\le`, `\ge`, `\ne`
  * fractions in text lines `\dfrac{}{}`; integrals `\displaystyle\int_a^b`
  * degrees `30^\circ`; probability `P(A \mid B)` or `P(A|B)`, complement `A'` or `\bar{A}`
* `₹` and ordinary words stay outside math.
* MCQ / assertion–reason options are lines that start with `(A) `, `(B) `, `(C) `, `(D) ` at column 0, one
  option per line (the assertion–reason codes (A)–(D) are written in full, as in the reference file).
* Case studies: keep the passage, then sub-parts on their own lines `(i) … **[1]**`,
  `(iii) (a) … **[2]**`, `**OR**`, `(iii) (b) … **[2]**`.
* Internal choice ("OR") questions outside case studies are split into two blocks `Na` and `Nb`.

## 3. Figures

Every diagram, graph, table-as-image or case-study picture that belongs to a question is cropped and
attached with `@fig <file>`. File name: `<year>-<code with dashes>-q<N>.webp` (append `-2`, `-3` for a
second figure). Use the crop tool and then **look at the result** to make sure it is complete and
contains no stray question text. Do not crop plain text.

## 4. Solutions (exam-ready)

Write the answer a top CBSE candidate would write in the board exam, following the marking-scheme value
points:

* State the formula/theorem used, define events/variables, show every step that earns marks, and end
  with a clearly stated final answer (bold or `\boxed{}`), with units ("sq. units", "cm/s").
* MCQ and assertion–reason: the key goes in the `--- ans X` line; the solution is a short justification
  (2–6 lines). Assertion–reason: say explicitly whether A and R are true and whether R explains A.
* 2-mark: concise but complete; 3-mark: all working; 5-mark: full solution with every step;
  case study: answer each part under bold labels **(i)**, **(ii)**, **(iii) (a)**, **(iii) (b)**.
* LPP: draw the graph (`plot` block), list corner points in a table, state the optimum (and for an
  unbounded region, the half-plane check).
* Area questions: include a `plot` block sketch of the region and set up the integral clearly.
* Use `\Rightarrow`, `\therefore`, `\because` naturally; keep each line to one logical step.
* Every answer must be mathematically verified. Cross-check final answers with the official CBSE
  marking scheme / solved paper when one is available; if the official key is wrong, give the correct
  answer and say so briefly.

## 5. Duplicates

Inside one year, a question that is identical (same wording **and** same numbers) to one already
written in an earlier set is recorded as `=== N = 65/1/1#12` (or `#25a` for an OR-part). If anything at
all differs (numbers, function, options), it is a new question and is written out in full.
