# CBSE Class 12 Mathematics PYQ Platform

A premium-looking web app for CBSE Class 12 Mathematics Previous Year Questions (2015–2025), built with Next.js, TypeScript, and Tailwind CSS.

## Features

- **323+ real questions** extracted from official CBSE solved papers (2015–2025)
- **Chapter-wise organization** across all 12 CBSE Class 12 Math chapters
- **Show/Hide answers** with smooth animations
- **Search & filter** by keyword, year, marks, and question type
- **Bookmark system** — save questions to revisit
- **Progress tracker** — mark questions as solved, track per-chapter progress
- **Important questions** — 5-mark and frequently repeated questions
- **Dark mode** — full light/dark theme support
- **Responsive** — works on mobile, tablet, and desktop
- **Static generation** — all chapter pages pre-rendered at build time

## Tech Stack

- **Next.js 16** (App Router, Static Site Generation)
- **TypeScript**
- **Tailwind CSS v4**
- **Framer Motion** — animations
- **Radix UI** — accessible components
- **Lucide React** — icons
- **next-themes** — dark mode

## Project Structure

```
├── app/
│   ├── page.tsx              # Homepage — chapter grid + stats
│   ├── chapter/[chapter]/    # Chapter-wise questions page
│   ├── search/               # Full-text search across all questions
│   ├── bookmarks/            # Saved/bookmarked questions
│   ├── important/            # High-mark & repeated questions
│   └── progress/             # Solved progress tracker
├── components/
│   ├── QuestionCard.tsx      # Individual question card with show/hide answer
│   ├── QuestionList.tsx      # Paginated list with search + filters
│   ├── Sidebar.tsx           # Desktop navigation sidebar
│   ├── MobileHeader.tsx      # Mobile top bar + slide-out sidebar
│   ├── ProgressBar.tsx       # Chapter progress bars
│   └── ThemeToggle.tsx       # Light/dark mode toggle
├── lib/
│   ├── types.ts              # TypeScript types, chapter constants
│   ├── data.ts               # Data access functions
│   └── utils.ts              # cn() helper
├── hooks/
│   └── useBookmarks.ts       # Bookmark + solved state (localStorage)
├── public/data/
│   └── pyqs.json             # Extracted questions data (~323 questions)
└── extract_pyqs.py           # PDF extraction script
```

## Getting Started

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Re-extracting Questions

If you want to re-run the PDF extraction:

```bash
# Place PDFs in ./pdfs/PYQs/
python3 extract_pyqs.py
```

The script reads all PDFs from `./pdfs/PYQs/` and outputs structured JSON to `./public/data/pyqs.json`.

## Building for Production

```bash
npm run build
npm start
```

The build generates fully static pages for all 12 chapters.

## Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

Import the repository on Vercel — zero configuration needed.
