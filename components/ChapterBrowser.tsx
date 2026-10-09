"use client";

import { Children, useEffect, useMemo, useState, type ReactNode } from "react";
import { motion } from "framer-motion";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { RotateCcw, Search } from "lucide-react";
import { useIdSet } from "@/lib/store";
import { RevealGroup } from "./motion/Reveal";

type Item = { id: string; year: number; marks: number; type: string; order: string; text: string };
type Sort = "new" | "old" | "marks";
type Filters = { q: string; marks: number | 0; type: string; year: number | 0; sort: Sort; hideDone: boolean };

const DEFAULT: Filters = { q: "", marks: 0, type: "", year: 0, sort: "new", hideDone: false };
const TYPES = [
  { v: "", l: "All types" },
  { v: "mcq", l: "MCQ" },
  { v: "ar", l: "Assertion–Reason" },
  { v: "sub", l: "Subjective" },
  { v: "case", l: "Case study" },
];

function fromUrl(): Partial<Filters> {
  const p = new URLSearchParams(window.location.search);
  const out: Partial<Filters> = {};
  if (p.get("q")) out.q = p.get("q")!;
  if (p.get("marks")) out.marks = Number(p.get("marks"));
  if (p.get("type")) out.type = p.get("type")!;
  if (p.get("year")) out.year = Number(p.get("year"));
  if (p.get("sort")) out.sort = p.get("sort") as Sort;
  return out;
}

export function ChapterBrowser({ items, years, children }: { items: Item[]; years: number[]; children: ReactNode }) {
  const kids = Children.toArray(children);
  const [f, setF] = useState<Filters>(DEFAULT);
  const done = useIdSet("done");
  const set = (patch: Partial<Filters>) => setF((old) => ({ ...old, ...patch }));

  // restore filters from the URL once on the client (keeps the page fully static)
  useEffect(() => {
    const id = requestAnimationFrame(() => {
      const u = fromUrl();
      if (Object.keys(u).length) setF((old) => ({ ...old, ...u }));
    });
    return () => cancelAnimationFrame(id);
  }, []);

  useEffect(() => {
    const p = new URLSearchParams();
    if (f.q) p.set("q", f.q);
    if (f.marks) p.set("marks", String(f.marks));
    if (f.type) p.set("type", f.type);
    if (f.year) p.set("year", String(f.year));
    if (f.sort !== "new") p.set("sort", f.sort);
    const qs = p.toString();
    window.history.replaceState(null, "", qs ? `?${qs}${window.location.hash}` : window.location.pathname + window.location.hash);
    ScrollTrigger.refresh();
  }, [f]);

  const marksAvail = useMemo(() => [...new Set(items.map((i) => i.marks))].sort((a, b) => a - b), [items]);
  const typesAvail = useMemo(() => new Set(items.map((i) => i.type)), [items]);

  const visible = useMemo(() => {
    const terms = f.q.toLowerCase().split(/\s+/).filter(Boolean);
    const idx = items
      .map((it, i) => ({ it, i }))
      .filter(({ it }) => (!f.marks || it.marks === f.marks) && (!f.type || it.type === f.type) && (!f.year || it.year === f.year))
      .filter(({ it }) => !f.hideDone || !done.set.has(it.id))
      .filter(({ it }) => terms.every((t) => it.text.includes(t) || String(it.year) === t));
    if (f.sort === "old") idx.sort((a, b) => a.it.year - b.it.year || a.it.order.localeCompare(b.it.order));
    else if (f.sort === "marks") idx.sort((a, b) => a.it.marks - b.it.marks || b.it.year - a.it.year || a.it.order.localeCompare(b.it.order));
    return idx.map((x) => x.i);
  }, [items, f, done.set]);

  const doneCount = items.filter((i) => done.set.has(i.id)).length;
  const pct = items.length ? Math.round((doneCount / items.length) * 100) : 0;
  const filtered = JSON.stringify({ ...f, sort: "new" }) !== JSON.stringify({ ...DEFAULT, sort: "new" });

  const chip = (active: boolean) =>
    `min-h-10 shrink-0 cursor-pointer rounded-full border px-3.5 text-sm font-bold transition-colors ${
      active ? "border-[var(--hue)] bg-[var(--hue-soft)] text-[var(--hue)]" : "border-line bg-surface text-ink-2 hover:border-line-strong hover:text-ink"
    }`;

  return (
    <>
      <div className="sticky top-16 z-30 -mx-4 border-b border-line bg-bg/90 px-4 py-3 backdrop-blur-md sm:-mx-6 sm:px-6">
        <div className="flex flex-col gap-3">
          <div className="flex gap-2">
            <label className="relative flex-1">
              <span className="sr-only">Search in this chapter</span>
              <Search className="pointer-events-none absolute left-3 top-1/2 size-[1.1rem] -translate-y-1/2 text-muted" aria-hidden />
              <input
                type="search"
                value={f.q}
                onChange={(e) => set({ q: e.target.value })}
                placeholder="Search this chapter (e.g. inverse, 2024, area)"
                className="h-11 w-full rounded-xl border border-line bg-surface pl-10 pr-3 text-[0.98rem] text-ink placeholder:text-muted focus:border-[var(--hue)] focus:outline-none"
              />
            </label>
            <label className="shrink-0">
              <span className="sr-only">Year</span>
              <select
                value={f.year}
                onChange={(e) => set({ year: Number(e.target.value) })}
                className="h-11 cursor-pointer rounded-xl border border-line bg-surface px-3 text-[0.95rem] text-ink focus:border-[var(--hue)] focus:outline-none"
              >
                <option value={0}>All years</option>
                {years.map((y) => (
                  <option key={y} value={y}>
                    {y}
                  </option>
                ))}
              </select>
            </label>
            <label className="hidden shrink-0 sm:block">
              <span className="sr-only">Sort</span>
              <select
                value={f.sort}
                onChange={(e) => set({ sort: e.target.value as Sort })}
                className="h-11 cursor-pointer rounded-xl border border-line bg-surface px-3 text-[0.95rem] text-ink focus:border-[var(--hue)] focus:outline-none"
              >
                <option value="new">Newest first</option>
                <option value="old">Oldest first</option>
                <option value="marks">By marks</option>
              </select>
            </label>
          </div>
          <div className="-mx-1 flex items-center gap-2 overflow-x-auto px-1 pb-0.5 [scrollbar-width:none]">
            <div role="group" aria-label="Marks" className="flex shrink-0 gap-2">
              <button type="button" className={chip(!f.marks)} aria-pressed={!f.marks} onClick={() => set({ marks: 0 })}>
                All marks
              </button>
              {marksAvail.map((m) => (
                <button key={m} type="button" className={chip(f.marks === m)} aria-pressed={f.marks === m} onClick={() => set({ marks: f.marks === m ? 0 : m })}>
                  {m} mark{m > 1 ? "s" : ""}
                </button>
              ))}
            </div>
            <span className="mx-1 h-6 w-px shrink-0 bg-line" aria-hidden />
            <div role="group" aria-label="Question type" className="flex shrink-0 gap-2">
              {TYPES.filter((t) => !t.v || typesAvail.has(t.v)).map((t) => (
                <button key={t.v} type="button" className={chip(f.type === t.v)} aria-pressed={f.type === t.v} onClick={() => set({ type: t.v })}>
                  {t.l}
                </button>
              ))}
            </div>
            <span className="mx-1 h-6 w-px shrink-0 bg-line" aria-hidden />
            <button type="button" className={chip(f.hideDone)} aria-pressed={f.hideDone} onClick={() => set({ hideDone: !f.hideDone })}>
              Hide done
            </button>
          </div>
        </div>
      </div>

      <div className="mt-6 flex flex-wrap items-center justify-between gap-3">
        <p className="text-sm text-ink-2" aria-live="polite">
          Showing <strong className="text-ink">{visible.length}</strong> of {items.length} questions
        </p>
        <div className="flex items-center gap-3 text-sm text-muted">
          <span>
            {doneCount} done · {pct}%
          </span>
          <span className="h-2 w-32 overflow-hidden rounded-full bg-surface-2" aria-hidden>
            <motion.span className="block h-full rounded-full bg-[var(--hue)]" initial={false} animate={{ width: `${pct}%` }} transition={{ type: "spring", stiffness: 120, damping: 20 }} />
          </span>
        </div>
      </div>

      {visible.length === 0 ? (
        <div className="mt-10 rounded-2xl border border-dashed border-line-strong p-10 text-center">
          <p className="text-lg font-bold">No questions match these filters.</p>
          <button type="button" onClick={() => setF(DEFAULT)} className="mt-4 inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl border border-line-strong px-4 font-bold hover:border-primary">
            <RotateCcw className="size-4" aria-hidden /> Reset filters
          </button>
        </div>
      ) : (
        <RevealGroup className="mt-5 space-y-5">{visible.map((i) => kids[i])}</RevealGroup>
      )}
      {filtered && visible.length > 0 && (
        <div className="mt-8 text-center">
          <button type="button" onClick={() => setF(DEFAULT)} className="inline-flex min-h-11 cursor-pointer items-center gap-2 rounded-xl px-4 text-sm font-bold text-muted hover:text-ink">
            <RotateCcw className="size-4" aria-hidden /> Clear filters
          </button>
        </div>
      )}
    </>
  );
}
