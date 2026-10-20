import type { Metadata } from "next";
import Link from "next/link";
import { Check, Minus } from "lucide-react";
import { CHAPTERS, UNITS } from "@/lib/chapters";
import { SYLLABUS } from "@/lib/syllabus";
import { papers, stats } from "@/lib/bank";

export const metadata: Metadata = {
  title: "2026-27 syllabus",
  description: "The CBSE Class XII Mathematics 2026-27 syllabus used to filter this question bank, and every past question left out because of it.",
};

export default function SyllabusPage() {
  const s = stats();
  const excluded = papers.flatMap((p) => p.items.filter((i) => i.kind === "skip").map((i) => ({ p, i })));
  return (
    <div className="mx-auto max-w-5xl px-4 pt-12 sm:px-6">
      <header className="mb-10 max-w-3xl">
        <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Syllabus filter</p>
        <h1 className="mt-2 text-4xl font-semibold sm:text-5xl">CBSE 2026-27 syllabus</h1>
        <p className="mt-3 text-lg text-ink-2">
          Mathematics (041) is examined for 80 marks across six units. Every past question was checked against this syllabus:{" "}
          <strong className="text-ink">{s.questions.toLocaleString("en-IN")}</strong> are included and{" "}
          <strong className="text-ink">{s.skipped}</strong> were left out because they need a topic that is no longer examined.
        </p>
      </header>

      <div className="space-y-10">
        {UNITS.map((u) => (
          <section key={u.key} className={`hue-${u.hue}`} aria-labelledby={`s-${u.key}`}>
            <h2 id={`s-${u.key}`} className="flex flex-wrap items-baseline justify-between gap-2 border-b border-line pb-2 text-2xl font-semibold">
              {u.name}
              <span className="font-sans text-base font-normal text-muted">{u.marks} marks</span>
            </h2>
            <div className="mt-4 grid gap-4 md:grid-cols-2">
              {CHAPTERS.filter((c) => c.unit === u.key).map((c) => (
                <div key={c.key} className="rounded-2xl border border-line bg-surface p-5">
                  <h3 className="text-xl font-semibold">
                    <Link href={`/chapters/${c.slug}`} className="hover:text-[var(--hue)]">
                      {c.no}. {c.name}
                    </Link>
                  </h3>
                  <ul className="mt-3 space-y-1.5 text-[0.95rem]">
                    {SYLLABUS[c.key].inc.map((t) => (
                      <li key={t} className="flex gap-2">
                        <Check className="mt-1 size-4 shrink-0 text-ok" aria-label="Included" />
                        <span>{t}</span>
                      </li>
                    ))}
                  </ul>
                  <p className="mt-4 font-mono text-[0.7rem] uppercase tracking-[0.16em] text-muted">Not examined</p>
                  <ul className="mt-1.5 space-y-1.5 text-[0.95rem] text-muted">
                    {SYLLABUS[c.key].exc.map((t) => (
                      <li key={t} className="flex gap-2">
                        <Minus className="mt-1 size-4 shrink-0" aria-label="Excluded" />
                        <span>{t}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>

      <section className="mt-16" aria-labelledby="excluded-h">
        <h2 id="excluded-h" className="text-3xl font-semibold">
          Past questions left out ({excluded.length})
        </h2>
        <p className="mt-2 text-ink-2">Listed for transparency; they are not part of the 2026-27 examination.</p>
        <div className="mt-5 overflow-x-auto rounded-2xl border border-line bg-surface">
          <table className="w-full text-left text-[0.95rem]">
            <thead className="bg-surface-2 text-sm">
              <tr>
                <th className="px-4 py-2.5 font-bold">Paper</th>
                <th className="px-4 py-2.5 font-bold">Question</th>
                <th className="px-4 py-2.5 font-bold">Reason</th>
              </tr>
            </thead>
            <tbody>
              {excluded.map(({ p, i }) => (
                <tr key={`${p.id}-${i.n}`} className="border-t border-line">
                  <td className="px-4 py-2 font-mono text-sm">
                    <Link href={`/papers/${p.id}`} className="hover:text-primary">
                      {p.year} · {p.code}
                    </Link>
                  </td>
                  <td className="px-4 py-2 font-mono text-sm">Q{i.n}</td>
                  <td className="px-4 py-2 text-ink-2">{i.reason}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
