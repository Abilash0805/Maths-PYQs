import Link from "next/link";
import { ArrowUpRight } from "lucide-react";
import { CHAPTERS, UNITS } from "@/lib/chapters";
import { chapterStats } from "@/lib/bank";
import { RevealGroup } from "./motion/Reveal";

const MARKS = [1, 2, 3, 4, 5];
const SHADE: Record<number, string> = { 1: "0.28", 2: "0.45", 3: "0.62", 4: "0.8", 5: "1" };

export function ChapterGrid() {
  return (
    <RevealGroup className="space-y-14">
      {UNITS.map((u) => {
        const chs = CHAPTERS.filter((c) => c.unit === u.key);
        return (
          <section key={u.key} aria-labelledby={`unit-${u.key}`} className={`hue-${u.hue}`}>
            <div data-reveal className="mb-5 flex flex-wrap items-end justify-between gap-3 border-b border-line pb-3">
              <div>
                <p className="font-mono text-xs uppercase tracking-[0.16em] text-[var(--hue)]">Unit {u.key.slice(1)}</p>
                <h3 id={`unit-${u.key}`} className="text-2xl font-semibold sm:text-[1.75rem]">
                  {u.name}
                </h3>
              </div>
              <div className="flex items-center gap-3 text-sm text-muted">
                <span>
                  <strong className="text-ink">{u.marks}</strong> / 80 marks
                </span>
                <span className="h-2 w-28 overflow-hidden rounded-full bg-surface-2" aria-hidden>
                  <span className="block h-full rounded-full bg-[var(--hue)]" style={{ width: `${(u.marks / 35) * 100}%` }} />
                </span>
              </div>
            </div>
            <ul className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {chs.map((c) => {
                const s = chapterStats(c.key);
                return (
                  <li key={c.key} data-reveal>
                    <Link
                      href={`/chapters/${c.slug}`}
                      className="group relative flex h-full flex-col rounded-2xl border border-line bg-surface p-5 shadow-card transition-[transform,border-color] duration-300 hover:-translate-y-1 hover:border-[var(--hue)]"
                    >
                      <div className="flex items-center justify-between">
                        <span className="rounded-lg bg-[var(--hue-soft)] px-2 py-0.5 font-mono text-xs font-medium text-[var(--hue)]">
                          Ch {String(c.no).padStart(2, "0")}
                        </span>
                        <ArrowUpRight className="size-5 text-muted transition-transform duration-300 group-hover:-translate-y-0.5 group-hover:translate-x-0.5 group-hover:text-[var(--hue)]" aria-hidden />
                      </div>
                      <h4 className="mt-3 font-display text-[1.35rem] font-semibold leading-snug">{c.name}</h4>
                      <p className="mt-1.5 text-[0.93rem] leading-snug text-muted">{c.blurb}</p>
                      <div className="mt-auto pt-5">
                        <p className="flex items-baseline gap-1.5">
                          <span className="text-2xl font-bold tabular-nums">{s.count}</span>
                          <span className="text-sm text-muted">questions{s.years.length ? ` · ${s.years.at(-1)}–${s.years[0]}` : ""}</span>
                        </p>
                        <div className="mt-2 flex h-2 overflow-hidden rounded-full bg-surface-2" aria-hidden>
                          {MARKS.filter((m) => s.byMarks[m]).map((m) => (
                            <span key={m} style={{ width: `${(s.byMarks[m] / Math.max(1, s.count)) * 100}%`, opacity: SHADE[m] }} className="h-full bg-[var(--hue)]" />
                          ))}
                        </div>
                        <p className="sr-only">
                          Marks split: {MARKS.filter((m) => s.byMarks[m]).map((m) => `${s.byMarks[m]} of ${m} mark${m > 1 ? "s" : ""}`).join(", ")}
                        </p>
                      </div>
                    </Link>
                  </li>
                );
              })}
            </ul>
          </section>
        );
      })}
    </RevealGroup>
  );
}
