# Maths PYQs — CBSE Class XII Mathematics

Every CBSE Class XII Mathematics (041) board-exam question from 2015 to 2026, transcribed from the
original question papers, sorted chapter-wise, filtered to the **2026-27 syllabus** and paired with
step-by-step, exam-ready solutions.

## What's inside

- **Chapter pages** (`/chapters/[slug]`) — every question of a chapter with filters for year, marks,
  question type, text search, sorting and a "hide done" toggle. Solutions open inline.
- **Year-wise papers** (`/papers`) — each set (e.g. 2026 · 65/1/1) in its original order. Repeated
  questions point to their first appearance; out-of-syllabus questions are listed with the reason.
- **Question pages** (`/q/[id]`) — a shareable page per question.
- **Search** (`/search`), **Saved** (`/saved`, stored on the device) and the **syllabus** used for
  filtering (`/syllabus`, including the list of every excluded past question).

## Content

Questions live as plain text in `content/<year>/<paper>.md` — one file per question paper. The format
is documented in [`content/README.md`](content/README.md) and the editorial rules (syllabus filter,
notation, solution style) in [`content/GUIDE.md`](content/GUIDE.md).

- All mathematics is LaTeX, rendered with KaTeX; graphs in solutions are `plot` blocks rendered to SVG.
- Figures from the papers are in `public/figures/`.
- `npm run check` validates every file (structure, numbering, duplicate links, figures and that every
  formula compiles).
- `node scripts/find-dupes.mjs` lists questions that look identical across papers.

`scripts/build-data.mjs` compiles the content into `data/bank.json` and `public/search-index.json`;
it runs automatically before `npm run dev` and `npm run build`.

## Stack

Next.js 16 (App Router, fully static with Cache Components), React 19, Tailwind CSS 4, KaTeX,
GSAP (ScrollTrigger, SplitText) with Lenis smooth scrolling, and framer-motion.

## Development

```bash
npm install
npm run dev      # http://localhost:3000
npm run check    # validate content
npm run build    # production build
```
