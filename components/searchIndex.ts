"use client";

import { useEffect, useState } from "react";

export type Entry = { id: string; ch: string; y: number; m: number; t: string; c: string; n: string; q: string; o: string[] | null; s: string };

let cache: Promise<Entry[]> | null = null;
const load = () => (cache ??= fetch("/search-index.json").then((r) => (r.ok ? r.json() : [])).catch(() => []));

export function useSearchIndex() {
  const [data, setData] = useState<Entry[] | null>(null);
  useEffect(() => {
    let alive = true;
    load().then((d) => alive && setData(d.map((e: Entry) => ({ ...e, s: e.s.toLowerCase() }))));
    return () => {
      alive = false;
    };
  }, []);
  return data;
}
