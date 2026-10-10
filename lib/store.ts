"use client";
// Tiny localStorage-backed sets (saved questions, completed questions) shared across components.
import { useCallback, useSyncExternalStore } from "react";

type Name = "saved" | "done";
const listeners = new Set<() => void>();
const cache: Record<string, { raw: string | null; set: Set<string> }> = {};
const EMPTY = new Set<string>();

function read(name: Name): Set<string> {
  let raw: string | null = null;
  try {
    raw = localStorage.getItem(`pyq:${name}`);
  } catch {}
  const c = cache[name];
  if (c && c.raw === raw) return c.set;
  let set = new Set<string>();
  try {
    set = new Set(raw ? (JSON.parse(raw) as string[]) : []);
  } catch {}
  cache[name] = { raw, set };
  return set;
}

function write(name: Name, set: Set<string>) {
  try {
    localStorage.setItem(`pyq:${name}`, JSON.stringify([...set]));
  } catch {}
  listeners.forEach((l) => l());
}

function subscribe(cb: () => void) {
  listeners.add(cb);
  const onStorage = (e: StorageEvent) => e.key?.startsWith("pyq:") && cb();
  window.addEventListener("storage", onStorage);
  return () => {
    listeners.delete(cb);
    window.removeEventListener("storage", onStorage);
  };
}

export function useIdSet(name: Name) {
  const set = useSyncExternalStore(subscribe, () => read(name), () => EMPTY);
  const toggle = useCallback(
    (id: string) => {
      const next = new Set(read(name));
      if (next.has(id)) next.delete(id);
      else next.add(id);
      write(name, next);
    },
    [name],
  );
  return { set, toggle };
}
