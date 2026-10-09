import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { ChapterBrowser } from "@/components/ChapterBrowser";
import { QuestionCard } from "@/components/QuestionCard";
import { CHAPTERS, chapterBySlug, unitOf } from "@/lib/chapters";
import { chapterStats, questionsIn } from "@/lib/bank";

export function generateStaticParams() {
  return CHAPTERS.map((c) => ({ slug: c.slug }));
}

export async function generateMetadata(props: PageProps<"/chapters/[slug]">): Promise<Metadata> {
  const { slug } = await props.params;
  const ch = chapterBySlug(slug);
  if (!ch) return {};
  const s = chapterStats(ch.key);
  return {
    title: `${ch.name} PYQs`,
    description: `${s.count} CBSE Class XII board questions on ${ch.name} with step-by-step solutions — ${ch.blurb}`,
  };
}

const plain = (s: string) => s.replace(/\$[^$]*\$/g, " ").replace(/[*_|]/g, " ").replace(/\s+/g, " ").trim().toLowerCase();

export default async function ChapterPage(props: PageProps<"/chapters/[slug]">) {
  const { slug } = await props.params;
  const ch = chapterBySlug(slug);
  if (!ch) notFound();
  const unit = unitOf(ch);
  const qs = questionsIn(ch.key);
  const s = chapterStats(ch.key);
  const prev = CHAPTERS[ch.no - 2];
  const next = CHAPTERS[ch.no];
  const items = qs.map((q) => ({
    id: q.id,
    year: q.year,
    marks: q.marks,
    type: q.type,
    order: `${q.paper}-${String(q.qno).padStart(2, "0")}${q.part}`,
    text: plain(`${q.topic} ${q.question} ${q.options?.map((o) => o.t).join(" ") ?? ""} ${q.code}`),
  }));

  return (
    <div className={`hue-${unit.hue}`}>
      <header className="border-b border-line bg-surface/60">
        <div className="mx-auto max-w-4xl px-4 pb-10 pt-10 sm:px-6">
          <nav aria-label="Breadcrumb" className="text-sm text-muted">
            <Link href="/chapters" className="hover:text-ink">
              Chapters
            </Link>
            <span className="mx-2" aria-hidden>
              /
            </span>
            <span>{unit.name}</span>
          </nav>
          <p className="mt-6 font-mono text-sm text-[var(--hue)]">Chapter {String(ch.no).padStart(2, "0")}</p>
          <h1 className="mt-1 text-4xl font-semibold sm:text-5xl">{ch.name}</h1>
          <p className="mt-3 max-w-2xl text-lg text-ink-2">{ch.blurb}</p>
          <dl className="mt-6 flex flex-wrap gap-x-8 gap-y-3 text-sm">
            <div>
              <dt className="text-muted">Questions</dt>
              <dd className="text-2xl font-bold tabular-nums">{s.count}</dd>
            </div>
            {[1, 2, 3, 4, 5]
              .filter((m) => s.byMarks[m])
              .map((m) => (
                <div key={m}>
                  <dt className="text-muted">
                    {m} mark{m > 1 ? "s" : ""}
                  </dt>
                  <dd className="text-2xl font-bold tabular-nums">{s.byMarks[m]}</dd>
                </div>
              ))}
            <div>
              <dt className="text-muted">Unit weightage</dt>
              <dd className="text-2xl font-bold tabular-nums">{unit.marks}</dd>
            </div>
          </dl>
        </div>
      </header>

      <div className="mx-auto max-w-4xl px-4 sm:px-6">
        {qs.length === 0 ? (
          <p className="py-16 text-center text-muted">Questions for this chapter are being added.</p>
        ) : (
          <ChapterBrowser items={items} years={s.years}>
            {qs.map((q) => (
              <QuestionCard key={q.id} q={q} />
            ))}
          </ChapterBrowser>
        )}

        <nav aria-label="Other chapters" className="mt-16 grid gap-3 sm:grid-cols-2">
          {prev ? (
            <Link href={`/chapters/${prev.slug}`} className="group flex min-h-16 items-center gap-3 rounded-2xl border border-line bg-surface p-4 hover:border-primary">
              <ChevronLeft className="size-5 text-muted group-hover:text-primary" aria-hidden />
              <span>
                <span className="block text-sm text-muted">Previous chapter</span>
                <span className="font-bold">{prev.name}</span>
              </span>
            </Link>
          ) : (
            <span />
          )}
          {next && (
            <Link href={`/chapters/${next.slug}`} className="group flex min-h-16 items-center justify-end gap-3 rounded-2xl border border-line bg-surface p-4 text-right hover:border-primary">
              <span>
                <span className="block text-sm text-muted">Next chapter</span>
                <span className="font-bold">{next.name}</span>
              </span>
              <ChevronRight className="size-5 text-muted group-hover:text-primary" aria-hidden />
            </Link>
          )}
        </nav>
      </div>
    </div>
  );
}
