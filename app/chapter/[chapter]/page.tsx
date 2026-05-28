import { notFound } from "next/navigation";
import { getQuestionsByChapter, getAllQuestions } from "@/lib/data";
import { CHAPTERS, CHAPTER_COLORS, CHAPTER_ICONS, CHAPTER_BG } from "@/lib/types";
import { Badge } from "@/components/ui/badge";
import { QuestionList } from "@/components/QuestionList";
import { cn } from "@/lib/utils";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ chapter: string }>;
}

export async function generateStaticParams() {
  return CHAPTERS.map((chapter) => ({
    chapter,
  }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { chapter } = await params;
  const decoded = decodeURIComponent(chapter);
  return {
    title: `${decoded} — CBSE Class 12 Maths PYQ`,
  };
}

export default async function ChapterPage({ params }: Props) {
  const { chapter } = await params;
  const decoded = decodeURIComponent(chapter);

  if (!CHAPTERS.includes(decoded as any)) {
    notFound();
  }

  const questions = getQuestionsByChapter(decoded);
  const years = [...new Set(questions.map((q) => q.year))].sort((a, b) => b - a);
  const totalMarks5 = questions.filter((q) => q.marks === 5).length;
  const totalMarks3 = questions.filter((q) => q.marks === 3).length;
  const totalMCQ = questions.filter((q) => q.type === "MCQ").length;

  const gradient = CHAPTER_COLORS[decoded];
  const icon = CHAPTER_ICONS[decoded];
  const bgClass = CHAPTER_BG[decoded];

  return (
    <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-4xl mx-auto space-y-6">
      {/* Chapter header */}
      <div className={cn("rounded-2xl border p-6", bgClass)}>
        <div className="flex items-start gap-4">
          <div
            className={cn(
              "flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-gradient-to-br text-white text-lg font-bold shadow-md",
              gradient
            )}
          >
            {icon}
          </div>
          <div className="flex-1">
            <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-1">{decoded}</h1>
            <p className="text-sm text-slate-500 dark:text-slate-400 mb-3">
              CBSE Class 12 Mathematics — Chapter-wise PYQs
            </p>
            <div className="flex flex-wrap gap-2">
              <Badge variant="info">{questions.length} Questions</Badge>
              <Badge variant="outline">{years.length} Years</Badge>
              {totalMCQ > 0 && <Badge variant="secondary">{totalMCQ} MCQs</Badge>}
              {totalMarks3 > 0 && <Badge variant="warning">{totalMarks3} Short Ans</Badge>}
              {totalMarks5 > 0 && <Badge variant="destructive">{totalMarks5} Long Ans</Badge>}
            </div>
          </div>
        </div>
      </div>

      {/* Year summary */}
      {years.length > 0 && (
        <div className="flex flex-wrap gap-1.5">
          {years.map((y) => {
            const cnt = questions.filter((q) => q.year === y).length;
            return (
              <span
                key={y}
                className="inline-flex items-center gap-1 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-1 text-xs font-medium text-slate-600 dark:text-slate-300"
              >
                {y} <span className="text-slate-400">({cnt})</span>
              </span>
            );
          })}
        </div>
      )}

      {/* Questions */}
      <QuestionList
        questions={questions}
        showChapter={false}
        title="All Questions"
        emptyMessage="No questions found for this chapter"
      />
    </div>
  );
}
