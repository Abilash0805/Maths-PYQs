import type { Metadata } from "next";
import { ChapterGrid } from "@/components/ChapterGrid";
import { stats } from "@/lib/bank";

export const metadata: Metadata = {
  title: "All chapters",
  description: "CBSE Class XII Mathematics previous-year questions organised into the 13 chapters of the 2026-27 syllabus.",
};

export default function ChaptersPage() {
  const s = stats();
  return (
    <div className="mx-auto max-w-6xl px-4 pt-12 sm:px-6">
      <header className="mb-12 max-w-2xl">
        <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Chapter-wise PYQs</p>
        <h1 className="mt-2 text-4xl font-semibold sm:text-5xl">All chapters</h1>
        <p className="mt-3 text-lg text-ink-2">
          {s.questions.toLocaleString("en-IN")} questions across 13 chapters. Each chapter page lets you filter by year, marks and question type.
        </p>
      </header>
      <ChapterGrid />
    </div>
  );
}
