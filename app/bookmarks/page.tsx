"use client";

import React, { useState, useEffect } from "react";
import { getAllQuestions } from "@/lib/data";
import { QuestionList } from "@/components/QuestionList";
import { Bookmark } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { PYQItem } from "@/lib/types";

export default function BookmarksPage() {
  const [bookmarkedQuestions, setBookmarkedQuestions] = useState<PYQItem[]>([]);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    try {
      const stored = localStorage.getItem("pyq-bookmarks");
      if (stored) {
        const ids = new Set<string>(JSON.parse(stored));
        const all = getAllQuestions();
        setBookmarkedQuestions(all.filter((q) => ids.has(q.id)));
      }
    } catch {}
    setLoaded(true);
  }, []);

  return (
    <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-4xl mx-auto space-y-6">
      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-amber-400 to-amber-600 text-white">
          <Bookmark className="size-5" />
        </div>
        <div>
          <h1 className="text-xl font-bold text-slate-900 dark:text-white">Bookmarks</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400">
            Your saved questions
          </p>
        </div>
        {loaded && (
          <Badge variant="warning" className="ml-auto">
            {bookmarkedQuestions.length}
          </Badge>
        )}
      </div>

      {loaded ? (
        <QuestionList
          questions={bookmarkedQuestions}
          showChapter={true}
          emptyMessage="No bookmarks yet. Click the bookmark icon on any question to save it."
        />
      ) : (
        <div className="space-y-4">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="h-32 rounded-2xl bg-slate-100 dark:bg-slate-800 animate-pulse" />
          ))}
        </div>
      )}
    </div>
  );
}
