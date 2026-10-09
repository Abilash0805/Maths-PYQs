"use client";

import Link from "next/link";
import type { ReactNode } from "react";
import { ArrowUpRight } from "lucide-react";
import { chapterByKey, TYPE_LABEL, unitOf } from "@/lib/chapters";
import type { Entry } from "./searchIndex";
import { useRenderedMd } from "./useRenderedMd";

/** Compact, client-rendered question preview used by search and saved lists. */
export function MiniQuestion({ e, action }: { e: Entry; action?: ReactNode }) {
  const html = useRenderedMd(e.q.replace(/\n\[\[fig\]\]\n/, "\n"));
  const ch = chapterByKey(e.ch);
  return (
    <article className={`hue-${unitOf(ch).hue} rounded-2xl border border-line bg-surface p-4 shadow-card sm:p-5`}>
      <div className="flex flex-wrap items-center gap-2 text-sm">
        <span className="font-mono text-[0.8rem] text-ink-2">
          {e.y} · {e.c} · Q{e.n}
        </span>
        <span className="rounded-full bg-accent-soft px-2.5 py-0.5 text-[0.8rem] font-bold text-accent">
          {e.m} mark{e.m > 1 ? "s" : ""}
        </span>
        <span className="rounded-full border border-line px-2.5 py-0.5 text-[0.8rem] text-ink-2">{TYPE_LABEL[e.t]}</span>
        <span className="rounded-full bg-[var(--hue-soft)] px-2.5 py-0.5 text-[0.8rem] font-bold text-[var(--hue)]">{ch.name}</span>
      </div>
      <div className="mt-3 max-h-56 overflow-hidden [mask-image:linear-gradient(black_75%,transparent)]">
        {html ? <div className="md" dangerouslySetInnerHTML={{ __html: html }} /> : <div className="h-12 animate-pulse rounded bg-line" />}
      </div>
      <div className="mt-3 flex items-center gap-2">
        <Link href={`/q/${e.id}`} className="inline-flex min-h-11 items-center gap-1.5 rounded-xl bg-primary px-4 text-sm font-bold text-primary-ink hover:brightness-110">
          Open with solution <ArrowUpRight className="size-4" aria-hidden />
        </Link>
        {action}
      </div>
    </article>
  );
}
