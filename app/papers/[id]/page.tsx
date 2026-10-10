import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Ban, Repeat } from "lucide-react";
import { QuestionCard } from "@/components/QuestionCard";
import { getPaper, getQuestion, papers } from "@/lib/bank";

export function generateStaticParams() {
  return papers.map((p) => ({ id: p.id }));
}

export async function generateMetadata(props: PageProps<"/papers/[id]">): Promise<Metadata> {
  const { id } = await props.params;
  const p = getPaper(id);
  if (!p) return {};
  return { title: `CBSE ${p.year} Maths ${p.code}`, description: `${p.title} — all questions with step-by-step solutions.` };
}

export default async function PaperPage(props: PageProps<"/papers/[id]">) {
  const { id } = await props.params;
  const p = getPaper(id);
  if (!p) notFound();
  return (
    <div className="mx-auto max-w-4xl px-4 pt-10 sm:px-6">
      <nav aria-label="Breadcrumb" className="text-sm text-muted">
        <Link href="/papers" className="hover:text-ink">
          Papers
        </Link>
        <span className="mx-2" aria-hidden>
          /
        </span>
        <span>{p.year}</span>
      </nav>
      <header className="mb-8 mt-4">
        <h1 className="text-4xl font-semibold sm:text-5xl">
          {p.year} · <span className="font-mono text-[0.8em]">{p.code}</span>
        </h1>
        <p className="mt-2 text-lg text-ink-2">{p.title}</p>
        {p.source && <p className="mt-1 text-sm text-muted">Source: {p.source}</p>}
      </header>
      <ol className="space-y-5">
        {p.items.map((it) => {
          if (it.kind === "skip")
            return (
              <li key={it.n} className="flex items-start gap-3 rounded-2xl border border-dashed border-line-strong px-4 py-3 text-ink-2">
                <Ban className="mt-1 size-4 shrink-0 text-muted" aria-hidden />
                <span>
                  <strong className="font-mono text-ink">Q{it.n}</strong> — not in the 2026-27 syllabus ({it.reason}).
                </span>
              </li>
            );
          const q = it.id ? getQuestion(it.id) : undefined;
          if (!q) return null;
          return (
            <li key={it.n}>
              {it.kind === "dup" && (
                <p className="mb-2 flex items-center gap-2 text-sm text-muted">
                  <Repeat className="size-4" aria-hidden />
                  <span>
                    <strong className="font-mono text-ink">Q{it.n}</strong> is the same as {q.year} · {q.code} · Q{q.qno}
                    {q.part}
                  </span>
                </p>
              )}
              <QuestionCard q={q} showChapter />
            </li>
          );
        })}
      </ol>
    </div>
  );
}
