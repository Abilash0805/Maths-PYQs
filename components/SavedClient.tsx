"use client";

import Link from "next/link";
import { BookmarkX } from "lucide-react";
import { useIdSet } from "@/lib/store";
import { useSearchIndex } from "./searchIndex";
import { MiniQuestion } from "./MiniQuestion";

export function SavedClient() {
  const data = useSearchIndex();
  const saved = useIdSet("saved");
  if (!data) return <p className="text-ink-2">Loading…</p>;
  const list = data.filter((d) => saved.set.has(d.id));
  if (!list.length)
    return (
      <div className="rounded-2xl border border-dashed border-line-strong p-10 text-center">
        <p className="text-lg font-bold">Nothing saved yet.</p>
        <p className="mt-1 text-ink-2">Use the bookmark button on any question to add it here.</p>
        <Link href="/chapters" className="mt-5 inline-flex min-h-11 items-center rounded-xl bg-primary px-4 font-bold text-primary-ink">
          Browse chapters
        </Link>
      </div>
    );
  return (
    <ul className="space-y-4">
      {list.map((e) => (
        <li key={e.id}>
          <MiniQuestion
            e={e}
            action={
              <button
                type="button"
                onClick={() => saved.toggle(e.id)}
                className="inline-flex min-h-11 cursor-pointer items-center gap-1.5 rounded-xl border border-line px-3.5 text-sm text-ink-2 hover:border-line-strong hover:text-ink"
              >
                <BookmarkX className="size-4" aria-hidden /> Remove
              </button>
            }
          />
        </li>
      ))}
    </ul>
  );
}
