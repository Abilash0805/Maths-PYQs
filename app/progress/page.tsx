"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { getAllQuestions, getChapterStats } from "@/lib/data";
import { CHAPTERS, CHAPTER_COLORS, CHAPTER_ICONS } from "@/lib/types";
import { ProgressBar } from "@/components/ProgressBar";
import { Badge } from "@/components/ui/badge";
import { TrendingUp, CheckCircle2, Bookmark, Trophy } from "lucide-react";
import { cn } from "@/lib/utils";

export default function ProgressPage() {
  const [solvedIds, setSolvedIds] = useState<Set<string>>(new Set());
  const [bookmarkIds, setBookmarkIds] = useState<Set<string>>(new Set());
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    try {
      const sv = localStorage.getItem("pyq-solved");
      if (sv) setSolvedIds(new Set(JSON.parse(sv)));
      const bk = localStorage.getItem("pyq-bookmarks");
      if (bk) setBookmarkIds(new Set(JSON.parse(bk)));
    } catch {}
    setLoaded(true);
  }, []);

  const allQuestions = getAllQuestions();
  const chapterStats = getChapterStats();

  const totalSolved = solvedIds.size;
  const totalBookmarked = bookmarkIds.size;
  const totalQuestions = allQuestions.length;
  const overallPct = totalQuestions === 0 ? 0 : Math.round((totalSolved / totalQuestions) * 100);

  return (
    <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-4xl mx-auto space-y-8">
      {/* Header */}
      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-green-500 to-emerald-600 text-white">
          <TrendingUp className="size-5" />
        </div>
        <div>
          <h1 className="text-xl font-bold text-slate-900">My Progress</h1>
          <p className="text-sm text-slate-500">Track your practice progress</p>
        </div>
      </div>

      {/* Overall stats */}
      <div className="grid grid-cols-3 gap-4">
        <div className="rounded-xl border border-slate-200 bg-white p-4 text-center">
          <CheckCircle2 className="size-6 text-green-500 mx-auto mb-1" />
          <div className="text-2xl font-bold text-slate-900">{totalSolved}</div>
          <div className="text-xs text-slate-500">Solved</div>
        </div>
        <div className="rounded-xl border border-slate-200 bg-white p-4 text-center">
          <Bookmark className="size-6 text-amber-500 mx-auto mb-1" />
          <div className="text-2xl font-bold text-slate-900">{totalBookmarked}</div>
          <div className="text-xs text-slate-500">Bookmarked</div>
        </div>
        <div className="rounded-xl border border-slate-200 bg-white p-4 text-center">
          <Trophy className="size-6 text-purple-500 mx-auto mb-1" />
          <div className="text-2xl font-bold text-slate-900">{overallPct}%</div>
          <div className="text-xs text-slate-500">Complete</div>
        </div>
      </div>

      {/* Overall progress */}
      <div className="rounded-xl border border-slate-200 bg-white p-5">
        <div className="flex items-center justify-between mb-3">
          <h2 className="font-semibold text-slate-900">Overall Progress</h2>
          <span className="text-sm text-slate-500">
            {totalSolved}/{totalQuestions}
          </span>
        </div>
        <ProgressBar
          value={totalSolved}
          max={totalQuestions}
          color="bg-gradient-to-r from-blue-500 to-indigo-500"
          showLabel={false}
        />
        <p className="mt-2 text-xs text-slate-500">
          {totalQuestions - totalSolved} questions remaining
        </p>
      </div>

      {/* Chapter-wise progress */}
      <div>
        <h2 className="text-base font-bold text-slate-900 mb-4">Chapter Progress</h2>
        <div className="space-y-3">
          {CHAPTERS.map((chapter) => {
            const stat = chapterStats.find((s) => s.chapter === chapter);
            const total = stat?.total || 0;
            const chapterQuestions = allQuestions.filter((q) => q.chapter === chapter);
            const solved = chapterQuestions.filter((q) => solvedIds.has(q.id)).length;
            const pct = total === 0 ? 0 : Math.round((solved / total) * 100);
            const gradient = CHAPTER_COLORS[chapter];
            const icon = CHAPTER_ICONS[chapter];

            return (
              <Link
                key={chapter}
                href={`/chapter/${encodeURIComponent(chapter)}`}
                className="flex items-center gap-3 rounded-xl border border-slate-200 bg-white p-4 hover:shadow-sm transition-shadow"
              >
                <div
                  className={cn(
                    "flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-gradient-to-br text-white text-xs font-bold",
                    gradient
                  )}
                >
                  {icon}
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between mb-1.5">
                    <span className="text-sm font-medium text-slate-800 truncate">
                      {chapter}
                    </span>
                    <span className="text-xs text-slate-500 ml-2 shrink-0">
                      {solved}/{total}
                    </span>
                  </div>
                  <ProgressBar
                    value={solved}
                    max={total}
                    color={`bg-gradient-to-r ${gradient}`}
                  />
                </div>
                <Badge
                  variant={pct === 100 ? "success" : pct > 50 ? "info" : "outline"}
                  className="shrink-0 text-xs"
                >
                  {pct}%
                </Badge>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
