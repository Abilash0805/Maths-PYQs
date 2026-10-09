"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Search } from "lucide-react";
import { CHAPTERS } from "@/lib/chapters";
import { useSearchIndex } from "./searchIndex";
import { MiniQuestion } from "./MiniQuestion";

const PAGE = 25;

export function SearchClient() {
  const data = useSearchIndex();
  const [q, setQ] = useState("");
  const [ch, setCh] = useState("");
  const [marks, setMarks] = useState(0);
  const [year, setYear] = useState(0);
  const [limit, setLimit] = useState(PAGE);
  const input = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const id = requestAnimationFrame(() => {
      const p = new URLSearchParams(window.location.search).get("q");
      if (p) setQ(p);
      input.current?.focus();
    });
    return () => cancelAnimationFrame(id);
  }, []);
  useEffect(() => {
    const url = q ? `?q=${encodeURIComponent(q)}` : window.location.pathname;
    window.history.replaceState(null, "", url);
  }, [q]);

  const years = useMemo(() => (data ? [...new Set(data.map((d) => d.y))].sort((a, b) => b - a) : []), [data]);
  const results = useMemo(() => {
    if (!data) return [];
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    return data.filter(
      (d) =>
        (!ch || d.ch === ch) &&
        (!marks || d.m === marks) &&
        (!year || d.y === year) &&
        terms.every((t) => d.s.includes(t) || d.c.includes(t) || String(d.y) === t),
    );
  }, [data, q, ch, marks, year]);

  const reset = (fn: () => void) => {
    fn();
    setLimit(PAGE);
  };
  const active = q || ch || marks || year;

  return (
    <div>
      <div className="rounded-2xl border border-line bg-surface p-3 shadow-card sm:p-4">
        <label className="relative block">
          <span className="sr-only">Search questions</span>
          <Search className="pointer-events-none absolute left-3.5 top-1/2 size-5 -translate-y-1/2 text-muted" aria-hidden />
          <input
            ref={input}
            type="search"
            value={q}
            onChange={(e) => reset(() => setQ(e.target.value))}
            placeholder="e.g. equivalence relation, Bayes, 65/2/1, shortest distance"
            className="h-12 w-full rounded-xl border border-line bg-bg pl-11 pr-3 text-[1.02rem] focus:border-primary focus:outline-none"
          />
        </label>
        <div className="mt-3 grid gap-2 sm:grid-cols-3">
          <label>
            <span className="sr-only">Chapter</span>
            <select value={ch} onChange={(e) => reset(() => setCh(e.target.value))} className="h-11 w-full cursor-pointer rounded-xl border border-line bg-bg px-3">
              <option value="">All chapters</option>
              {CHAPTERS.map((c) => (
                <option key={c.key} value={c.key}>
                  {c.no}. {c.name}
                </option>
              ))}
            </select>
          </label>
          <label>
            <span className="sr-only">Marks</span>
            <select value={marks} onChange={(e) => reset(() => setMarks(Number(e.target.value)))} className="h-11 w-full cursor-pointer rounded-xl border border-line bg-bg px-3">
              <option value={0}>Any marks</option>
              {[1, 2, 3, 4, 5, 6].map((m) => (
                <option key={m} value={m}>
                  {m} mark{m > 1 ? "s" : ""}
                </option>
              ))}
            </select>
          </label>
          <label>
            <span className="sr-only">Year</span>
            <select value={year} onChange={(e) => reset(() => setYear(Number(e.target.value)))} className="h-11 w-full cursor-pointer rounded-xl border border-line bg-bg px-3">
              <option value={0}>Any year</option>
              {years.map((y) => (
                <option key={y} value={y}>
                  {y}
                </option>
              ))}
            </select>
          </label>
        </div>
      </div>

      <p className="mt-5 text-sm text-ink-2" aria-live="polite">
        {data == null ? "Loading questions…" : active ? `${results.length} matching question${results.length === 1 ? "" : "s"}` : `${data.length} questions in the bank`}
      </p>
      <ul className="mt-4 space-y-4">
        <AnimatePresence initial={false}>
          {results.slice(0, limit).map((e) => (
            <motion.li key={e.id} layout="position" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }}>
              <MiniQuestion e={e} />
            </motion.li>
          ))}
        </AnimatePresence>
      </ul>
      {results.length > limit && (
        <div className="mt-6 text-center">
          <button type="button" onClick={() => setLimit((l) => l + PAGE)} className="inline-flex min-h-11 cursor-pointer items-center rounded-xl border border-line-strong px-5 font-bold hover:border-primary">
            Show more ({results.length - limit} left)
          </button>
        </div>
      )}
    </div>
  );
}
