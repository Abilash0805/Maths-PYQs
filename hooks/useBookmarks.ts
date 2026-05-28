"use client";

import { useState, useEffect } from "react";

export function useBookmarks() {
  const [bookmarks, setBookmarks] = useState<Set<string>>(new Set());

  useEffect(() => {
    try {
      const stored = localStorage.getItem("pyq-bookmarks");
      if (stored) setBookmarks(new Set(JSON.parse(stored)));
    } catch {}
  }, []);

  const toggle = (id: string) => {
    setBookmarks((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      try {
        localStorage.setItem("pyq-bookmarks", JSON.stringify([...next]));
      } catch {}
      return next;
    });
  };

  return { bookmarks, toggle };
}

export function useSolved() {
  const [solved, setSolved] = useState<Set<string>>(new Set());

  useEffect(() => {
    try {
      const stored = localStorage.getItem("pyq-solved");
      if (stored) setSolved(new Set(JSON.parse(stored)));
    } catch {}
  }, []);

  const toggle = (id: string) => {
    setSolved((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      try {
        localStorage.setItem("pyq-solved", JSON.stringify([...next]));
      } catch {}
      return next;
    });
  };

  return { solved, toggle };
}
