import type { Metadata } from "next";
import Link from "next/link";
import { ArrowUpRight } from "lucide-react";
import { RevealGroup } from "@/components/motion/Reveal";
import { papers, years } from "@/lib/bank";

export const metadata: Metadata = {
  title: "Year-wise papers",
  description: "Every CBSE Class XII Mathematics question paper (2015–2026) in the bank, set by set, with the questions in paper order.",
};

export default function PapersPage() {
  return (
    <div className="mx-auto max-w-6xl px-4 pt-12 sm:px-6">
      <header className="mb-10 max-w-2xl">
        <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Year-wise</p>
        <h1 className="mt-2 text-4xl font-semibold sm:text-5xl">Question papers</h1>
        <p className="mt-3 text-lg text-ink-2">
          Open any set to practise it in the original order. Questions outside the 2026-27 syllabus are listed but not solved, and repeats point to
          the first time a question appeared.
        </p>
      </header>
      <RevealGroup className="space-y-12">
        {years.map((y) => (
          <section key={y} id={`y${y}`} aria-labelledby={`h${y}`}>
            <h2 id={`h${y}`} data-reveal className="mb-4 border-b border-line pb-2 font-display text-3xl font-semibold">
              {y}
            </h2>
            <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {papers
                .filter((p) => p.year === y)
                .map((p) => {
                  const q = p.items.filter((i) => i.kind === "q").length;
                  const d = p.items.filter((i) => i.kind === "dup").length;
                  const s = p.items.filter((i) => i.kind === "skip").length;
                  return (
                    <li key={p.id} data-reveal>
                      <Link href={`/papers/${p.id}`} className="group flex h-full flex-col rounded-2xl border border-line bg-surface p-5 shadow-card transition hover:-translate-y-0.5 hover:border-primary">
                        <div className="flex items-start justify-between gap-2">
                          <div>
                            <p className="font-mono text-lg font-medium">{p.code}</p>
                            {p.series && <p className="text-sm text-muted">Series {p.series}</p>}
                          </div>
                          <ArrowUpRight className="size-5 text-muted transition group-hover:text-primary" aria-hidden />
                        </div>
                        <p className="mt-4 flex flex-wrap gap-x-4 gap-y-1 text-sm text-ink-2">
                          <span>
                            <strong className="text-ink">{q}</strong> new
                          </span>
                          {d > 0 && (
                            <span>
                              <strong className="text-ink">{d}</strong> repeated
                            </span>
                          )}
                          {s > 0 && (
                            <span>
                              <strong className="text-ink">{s}</strong> out of syllabus
                            </span>
                          )}
                        </p>
                      </Link>
                    </li>
                  );
                })}
            </ul>
          </section>
        ))}
      </RevealGroup>
    </div>
  );
}
