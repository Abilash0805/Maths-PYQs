import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { QuestionCard } from "@/components/QuestionCard";
import { chapterByKey } from "@/lib/chapters";
import { getQuestion, questions, questionsIn } from "@/lib/bank";

export function generateStaticParams() {
  return questions.map((q) => ({ id: q.id }));
}

const plain = (s: string) => s.replace(/\$\$?([^$]*)\$\$?/g, "$1").replace(/\\[a-zA-Z]+/g, " ").replace(/[{}*\\]/g, "").replace(/\s+/g, " ").trim();

export async function generateMetadata(props: PageProps<"/q/[id]">): Promise<Metadata> {
  const { id } = await props.params;
  const q = getQuestion(id);
  if (!q) return {};
  const ch = chapterByKey(q.ch);
  return {
    title: `${ch.name} · ${q.year} ${q.code} Q${q.qno}${q.part}`,
    description: `${plain(q.question).slice(0, 150)}… — CBSE ${q.year} board question (${q.marks} mark${q.marks > 1 ? "s" : ""}) with step-by-step solution.`,
  };
}

export default async function QuestionPage(props: PageProps<"/q/[id]">) {
  const { id } = await props.params;
  const q = getQuestion(id);
  if (!q) notFound();
  const ch = chapterByKey(q.ch);
  const list = questionsIn(q.ch);
  const i = list.findIndex((x) => x.id === q.id);
  const prev = list[i - 1];
  const next = list[i + 1];
  return (
    <div className="mx-auto max-w-3xl px-4 pt-10 sm:px-6">
      <nav aria-label="Breadcrumb" className="mb-6 text-sm text-muted">
        <Link href="/chapters" className="hover:text-ink">
          Chapters
        </Link>
        <span className="mx-2" aria-hidden>
          /
        </span>
        <Link href={`/chapters/${ch.slug}`} className="hover:text-ink">
          {ch.name}
        </Link>
      </nav>
      <h1 className="sr-only">
        {ch.name}: CBSE {q.year} question {q.qno}
        {q.part}
      </h1>
      <QuestionCard q={q} showChapter linkTitle={false} />
      <nav aria-label="More questions" className="mt-8 grid gap-3 sm:grid-cols-2">
        {prev ? (
          <Link href={`/q/${prev.id}`} className="group flex min-h-14 items-center gap-2 rounded-2xl border border-line bg-surface p-4 hover:border-primary">
            <ChevronLeft className="size-5 text-muted group-hover:text-primary" aria-hidden />
            <span className="text-sm">
              <span className="block text-muted">Previous</span>
              <span className="font-mono">
                {prev.year} · {prev.code} · Q{prev.qno}
                {prev.part}
              </span>
            </span>
          </Link>
        ) : (
          <span />
        )}
        {next && (
          <Link href={`/q/${next.id}`} className="group flex min-h-14 items-center justify-end gap-2 rounded-2xl border border-line bg-surface p-4 text-right hover:border-primary">
            <span className="text-sm">
              <span className="block text-muted">Next</span>
              <span className="font-mono">
                {next.year} · {next.code} · Q{next.qno}
                {next.part}
              </span>
            </span>
            <ChevronRight className="size-5 text-muted group-hover:text-primary" aria-hidden />
          </Link>
        )}
      </nav>
    </div>
  );
}
