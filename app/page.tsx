import Link from "next/link";
import { ArrowRight, BookOpenCheck, Search, Sigma } from "lucide-react";
import { ChapterGrid } from "@/components/ChapterGrid";
import { Md } from "@/components/Md";
import { CountUp } from "@/components/motion/CountUp";
import { HeroMotion } from "@/components/motion/HeroMotion";
import { RevealGroup } from "@/components/motion/Reveal";
import { CHAPTERS } from "@/lib/chapters";
import { papers, stats, years } from "@/lib/bank";

const GLYPHS = [
  { c: "∫", cls: "left-[4%] top-[18%] text-7xl" },
  { c: "Σ", cls: "right-[6%] top-[10%] text-6xl" },
  { c: "π", cls: "left-[46%] top-[6%] text-5xl" },
  { c: "dy/dx", cls: "right-[30%] bottom-[8%] text-4xl" },
  { c: "√", cls: "left-[18%] bottom-[6%] text-6xl" },
  { c: "λ", cls: "right-[2%] bottom-[30%] text-5xl" },
];

export default function Home() {
  const s = stats();
  const firstYear = years.at(-1);
  const lastYear = years[0];
  return (
    <>
      <HeroMotion className="relative overflow-hidden border-b border-line">
        <div className="grid-paper absolute inset-0 [mask-image:radial-gradient(ellipse_at_top,black_35%,transparent_75%)]" aria-hidden />
        {GLYPHS.map((g) => (
          <span key={g.c} data-glyph className={`pointer-events-none absolute hidden select-none font-display text-primary/15 md:block ${g.cls}`} aria-hidden>
            {g.c}
          </span>
        ))}
        <div className="relative mx-auto grid max-w-6xl items-center gap-12 px-4 pb-20 pt-14 sm:px-6 md:pt-20 lg:grid-cols-[1.15fr_1fr]">
          <div>
            <p data-hero-eyebrow className="inline-flex items-center gap-2 rounded-full border border-line bg-surface px-3 py-1 font-mono text-xs uppercase tracking-[0.14em] text-ink-2">
              <span className="size-1.5 rounded-full bg-accent" aria-hidden />
              <span className="hidden sm:inline">CBSE Class XII · Maths 041 ·</span>
              <span>2026-27 syllabus</span>
            </p>
            <h1 data-hero-title className="mt-5 text-[2.6rem] font-semibold leading-[1.05] sm:text-6xl">
              Every board question, solved the way examiners mark it.
            </h1>
            <p data-hero-copy className="mt-5 max-w-xl text-lg text-ink-2">
              {s.questions.toLocaleString("en-IN")} previous-year questions from {s.papers} CBSE papers ({firstYear === lastYear ? firstYear : `${firstYear}–${lastYear}`}), sorted
              chapter-wise, trimmed to the current syllabus and paired with step-by-step solutions.
            </p>
            <div data-hero-cta className="mt-8 flex flex-wrap gap-3">
              <Link href="/chapters" className="inline-flex min-h-12 items-center gap-2 rounded-xl bg-primary px-5 text-[1.02rem] font-bold text-primary-ink transition hover:brightness-110">
                Start practising <ArrowRight className="size-[1.1rem]" aria-hidden />
              </Link>
              <Link href="/search" className="inline-flex min-h-12 items-center gap-2 rounded-xl border border-line-strong bg-surface px-5 text-[1.02rem] font-bold text-ink transition hover:border-primary">
                <Search className="size-[1.1rem]" aria-hidden /> Find a question
              </Link>
            </div>
          </div>

          <div data-hero-card className="relative">
            <div className="absolute -inset-3 -z-10 hidden rotate-2 rounded-[1.75rem] bg-primary-soft/60 sm:block" aria-hidden />
            <div className="rounded-2xl border border-line bg-surface p-5 shadow-card sm:p-6">
              <div className="flex flex-wrap items-center gap-2 text-sm">
                <span className="font-mono text-[0.8rem] text-ink-2">2026 · 65/1/1 · Q26</span>
                <span className="rounded-full bg-accent-soft px-2.5 py-0.5 text-[0.8rem] font-bold text-accent">3 marks</span>
              </div>
              <Md className="mt-3 text-[1.05rem]" src={"Evaluate: $\\displaystyle\\int_{0}^{1} x\\tan^{-1}x\\,dx$"} />
              <div className="mt-4 space-y-2 rounded-xl border border-primary/25 bg-primary-soft/40 p-3 text-[0.8rem] sm:p-4 sm:text-[0.95rem]">
                <p className="font-mono text-[0.7rem] uppercase tracking-[0.16em] text-primary">Solution</p>
                <div data-hero-line>
                  <Md src={"$I = \\left[\\tan^{-1}x\\cdot\\dfrac{x^2}{2}\\right]_0^1 - \\dfrac{1}{2}\\displaystyle\\int_0^1 \\dfrac{x^2}{1+x^2}\\,dx$"} />
                </div>
                <div data-hero-line>
                  <Md src={"$= \\dfrac{\\pi}{8} - \\dfrac{1}{2}\\Big[x - \\tan^{-1}x\\Big]_0^1$"} />
                </div>
                <div data-hero-line className="flex items-center gap-3">
                  <Md src={"$\\therefore\\ I = \\boxed{\\dfrac{\\pi}{4} - \\dfrac{1}{2}}$"} />
                  <span data-hero-check className="rounded-full bg-ok px-2.5 py-0.5 text-xs font-bold text-surface">
                    Full marks
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </HeroMotion>

      <section aria-label="Question bank in numbers" className="border-b border-line bg-surface/70">
        <dl className="mx-auto grid max-w-6xl grid-cols-2 gap-y-6 px-4 py-8 sm:px-6 md:grid-cols-4">
          {[
            { v: s.questions, l: "questions with solutions" },
            { v: s.papers, l: "question papers" },
            { v: s.years, l: "exam years" },
            { v: CHAPTERS.length, l: "chapters" },
          ].map((x) => (
            <div key={x.l} className="px-2">
              <dt className="sr-only">{x.l}</dt>
              <dd>
                <CountUp value={x.v} className="block font-display text-4xl font-semibold tabular-nums text-ink sm:text-5xl" />
                <span className="text-[0.95rem] text-muted">{x.l}</span>
              </dd>
            </div>
          ))}
        </dl>
      </section>

      <section id="chapters" aria-labelledby="chapters-h" className="mx-auto max-w-6xl px-4 pt-20 sm:px-6">
        <div className="mb-10 max-w-2xl">
          <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Chapter-wise</p>
          <h2 id="chapters-h" className="mt-2 text-4xl font-semibold sm:text-5xl">
            Thirteen chapters, six units
          </h2>
          <p className="mt-3 text-lg text-ink-2">Weightage follows the 2026-27 CBSE blueprint. Pick a chapter to see every question asked from it.</p>
        </div>
        <ChapterGrid />
      </section>

      <section aria-labelledby="how-h" className="mx-auto mt-24 max-w-6xl px-4 sm:px-6">
        <RevealGroup className="grid gap-4 md:grid-cols-3">
          <div data-reveal className="md:col-span-3">
            <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">How to use it</p>
            <h2 id="how-h" className="mt-2 text-4xl font-semibold">Practise like it&apos;s the real paper</h2>
          </div>
          {[
            { icon: BookOpenCheck, t: "Attempt first", d: "Read the question exactly as printed, with every figure and option. Write your answer on paper before you peek." },
            { icon: Sigma, t: "Compare step by step", d: "Open the solution to check each step against the way the CBSE marking scheme awards marks." },
            { icon: ArrowRight, t: "Track and revisit", d: "Mark questions done, save the tricky ones and filter by year, marks or question type." },
          ].map((x, i) => (
            <div key={x.t} data-reveal className="rounded-2xl border border-line bg-surface p-6 shadow-card">
              <div className="flex items-center gap-3">
                <span className="grid size-10 place-items-center rounded-xl bg-primary-soft text-primary">
                  <x.icon className="size-5" aria-hidden />
                </span>
                <span className="font-mono text-sm text-muted">0{i + 1}</span>
              </div>
              <h3 className="mt-4 text-2xl font-semibold">{x.t}</h3>
              <p className="mt-2 text-ink-2">{x.d}</p>
            </div>
          ))}
        </RevealGroup>
      </section>

      <section aria-labelledby="years-h" className="mx-auto mt-24 max-w-6xl px-4 sm:px-6">
        <div className="rounded-3xl border border-line bg-surface p-6 shadow-card sm:p-10">
          <div className="flex flex-wrap items-end justify-between gap-4">
            <div>
              <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Year-wise</p>
              <h2 id="years-h" className="mt-2 text-3xl font-semibold sm:text-4xl">
                Papers from {firstYear} to {lastYear}
              </h2>
            </div>
            <Link href="/papers" className="inline-flex min-h-11 items-center gap-2 rounded-xl border border-line-strong px-4 font-bold hover:border-primary">
              All papers <ArrowRight className="size-4" aria-hidden />
            </Link>
          </div>
          <ul className="mt-6 flex flex-wrap gap-2">
            {years.map((y) => {
              const n = papers.filter((p) => p.year === y).length;
              return (
                <li key={y}>
                  <Link href={`/papers#y${y}`} className="inline-flex min-h-11 items-center gap-2 rounded-xl bg-surface-2 px-4 font-mono text-sm hover:bg-primary-soft hover:text-primary">
                    {y}
                    <span className="text-muted">
                      {n} set{n > 1 ? "s" : ""}
                    </span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </div>
      </section>
    </>
  );
}
