"use client";

import Link from "next/link";
import { useState, type ReactNode } from "react";
import { AnimatePresence, motion, useReducedMotion } from "framer-motion";
import { Bookmark, BookmarkCheck, CheckCircle2, ChevronDown, Circle, Link2 } from "lucide-react";
import { useIdSet } from "@/lib/store";
import { loadRenderer, useRenderedMd } from "./useRenderedMd";

export function CardShell({
  id,
  solution,
  answerKey,
  permalink,
  children,
  defaultOpen = false,
}: {
  id: string;
  solution: string;
  answerKey: string | null;
  permalink: string | null;
  children: ReactNode;
  defaultOpen?: boolean;
}) {
  const [open, setOpen] = useState(defaultOpen);
  const saved = useIdSet("saved");
  const done = useIdSet("done");
  const isSaved = saved.set.has(id);
  const isDone = done.set.has(id);
  const reduce = useReducedMotion();

  return (
    <div data-open={open}>
      {children}
      <div className="mt-5 flex flex-wrap items-center gap-2 border-t border-line pt-4">
        <button
          type="button"
          onClick={() => setOpen((o) => !o)}
          onPointerEnter={() => void loadRenderer()}
          onFocus={() => void loadRenderer()}
          aria-expanded={open}
          aria-controls={`${id}-sol`}
          className="inline-flex min-h-11 flex-1 cursor-pointer items-center justify-center gap-2 rounded-xl bg-primary px-4 font-bold text-primary-ink transition-[transform,filter] hover:brightness-110 active:scale-[0.98] sm:flex-none"
        >
          {open ? "Hide solution" : "Show solution"}
          <ChevronDown className={`size-4 transition-transform duration-300 ${open ? "rotate-180" : ""}`} aria-hidden />
        </button>
        <button
          type="button"
          onClick={() => done.toggle(id)}
          aria-pressed={isDone}
          aria-label={isDone ? "Marked as done" : "Mark as done"}
          className={`inline-flex min-h-11 min-w-11 cursor-pointer items-center justify-center gap-2 rounded-xl border px-3 text-[0.95rem] transition-colors sm:px-3.5 ${
            isDone ? "border-ok bg-ok-soft text-ok" : "border-line text-ink-2 hover:border-line-strong hover:text-ink"
          }`}
        >
          {isDone ? <CheckCircle2 className="size-[1.1rem]" aria-hidden /> : <Circle className="size-[1.1rem]" aria-hidden />}
          <span className="hidden sm:inline">{isDone ? "Done" : "Mark done"}</span>
        </button>
        <button
          type="button"
          onClick={() => saved.toggle(id)}
          aria-pressed={isSaved}
          aria-label={isSaved ? "Remove from saved" : "Save question"}
          className={`grid size-11 cursor-pointer place-items-center rounded-xl border transition-colors ${
            isSaved ? "border-accent bg-accent-soft text-accent" : "border-line text-ink-2 hover:border-line-strong hover:text-ink"
          }`}
        >
          {isSaved ? <BookmarkCheck className="size-5" aria-hidden /> : <Bookmark className="size-5" aria-hidden />}
        </button>
        {permalink && (
          <Link
            href={permalink}
            aria-label="Open this question on its own page"
            className="grid size-11 place-items-center rounded-xl text-muted transition-colors hover:bg-surface-2 hover:text-ink sm:ml-auto"
          >
            <Link2 className="size-5" aria-hidden />
          </Link>
        )}
      </div>
      <AnimatePresence initial={false}>
        {open && (
          <motion.section
            id={`${id}-sol`}
            aria-label="Solution"
            key="sol"
            initial={reduce ? { opacity: 0 } : { height: 0, opacity: 0 }}
            animate={reduce ? { opacity: 1 } : { height: "auto", opacity: 1 }}
            exit={reduce ? { opacity: 0 } : { height: 0, opacity: 0, transition: { duration: 0.22, ease: [0.4, 0, 1, 1] } }}
            transition={{ duration: 0.38, ease: [0.22, 1, 0.36, 1] }}
            className="overflow-hidden"
          >
            <Solution src={solution} answerKey={answerKey} />
          </motion.section>
        )}
      </AnimatePresence>
    </div>
  );
}

function Solution({ src, answerKey }: { src: string; answerKey: string | null }) {
  const html = useRenderedMd(src);
  return (
    <div className="mt-4 rounded-xl border border-primary/25 bg-primary-soft/40 p-4 sm:p-5">
      <div className="mb-3 flex flex-wrap items-center gap-2">
        <span className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Solution</span>
        {answerKey && (
          <span className="rounded-full bg-ok px-2.5 py-0.5 text-sm font-bold text-surface">Correct option: ({answerKey})</span>
        )}
      </div>
      {html ? (
        <div className="md" dangerouslySetInnerHTML={{ __html: html }} />
      ) : (
        <div className="space-y-2" aria-busy="true" aria-label="Loading solution">
          {[92, 78, 85, 60].map((w) => (
            <div key={w} className="h-4 animate-pulse rounded bg-line" style={{ width: `${w}%` }} />
          ))}
        </div>
      )}
    </div>
  );
}
