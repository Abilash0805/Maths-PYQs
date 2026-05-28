"use client";

import React, { useState, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { QuestionCard } from "./QuestionCard";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";
import { PYQItem } from "@/lib/types";
import { Search, Filter, X, SortAsc } from "lucide-react";
import { useBookmarks, useSolved } from "@/hooks/useBookmarks";

interface QuestionListProps {
  questions: PYQItem[];
  showChapter?: boolean;
  title?: string;
  emptyMessage?: string;
}

const YEARS = [2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023, 2024, 2025];
const MARKS = [1, 2, 3, 4, 5];

export function QuestionList({ questions, showChapter = false, title, emptyMessage }: QuestionListProps) {
  const [search, setSearch] = useState("");
  const [yearFilter, setYearFilter] = useState<number | null>(null);
  const [marksFilter, setMarksFilter] = useState<number | null>(null);
  const [typeFilter, setTypeFilter] = useState<string | null>(null);
  const [showFilters, setShowFilters] = useState(false);
  const [page, setPage] = useState(1);
  const PER_PAGE = 20;

  const { bookmarks, toggle: toggleBookmark } = useBookmarks();
  const { solved, toggle: toggleSolved } = useSolved();

  const filtered = useMemo(() => {
    let result = questions;
    if (search.trim()) {
      const q = search.toLowerCase();
      result = result.filter(
        (item) =>
          item.question.toLowerCase().includes(q) ||
          item.answer.toLowerCase().includes(q) ||
          item.chapter.toLowerCase().includes(q)
      );
    }
    if (yearFilter) result = result.filter((q) => q.year === yearFilter);
    if (marksFilter) result = result.filter((q) => q.marks === marksFilter);
    if (typeFilter) result = result.filter((q) => q.type === typeFilter);
    return result;
  }, [questions, search, yearFilter, marksFilter, typeFilter]);

  const paginated = filtered.slice(0, page * PER_PAGE);
  const hasMore = paginated.length < filtered.length;

  const activeFilters = [yearFilter, marksFilter, typeFilter].filter(Boolean).length;

  const clearFilters = () => {
    setYearFilter(null);
    setMarksFilter(null);
    setTypeFilter(null);
    setSearch("");
  };

  const availableYears = [...new Set(questions.map((q) => q.year))].sort((a, b) => b - a);
  const availableMarks = [...new Set(questions.map((q) => q.marks))].sort((a, b) => a - b);
  const availableTypes = [...new Set(questions.map((q) => q.type))];

  return (
    <div className="space-y-4">
      {/* Header */}
      {title && (
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-bold text-slate-900 dark:text-white">{title}</h2>
          <Badge variant="outline">{filtered.length} questions</Badge>
        </div>
      )}

      {/* Search + Filter bar */}
      <div className="flex gap-2">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-slate-400" />
          <Input
            placeholder="Search questions, formulas..."
            value={search}
            onChange={(e) => { setSearch(e.target.value); setPage(1); }}
            className="pl-9"
          />
          {search && (
            <button
              onClick={() => setSearch("")}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
            >
              <X className="size-4" />
            </button>
          )}
        </div>
        <Button
          variant={showFilters ? "default" : "outline"}
          size="sm"
          onClick={() => setShowFilters(!showFilters)}
          className="gap-1.5 shrink-0"
        >
          <Filter className="size-4" />
          Filters
          {activeFilters > 0 && (
            <span className="ml-0.5 flex h-4 w-4 items-center justify-center rounded-full bg-white text-primary text-xs font-bold">
              {activeFilters}
            </span>
          )}
        </Button>
      </div>

      {/* Filter panel */}
      <AnimatePresence>
        {showFilters && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <div className="rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 p-4 space-y-3">
              {/* Year filter */}
              <div>
                <p className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wide mb-2">Year</p>
                <div className="flex flex-wrap gap-1.5">
                  {availableYears.map((y) => (
                    <button
                      key={y}
                      onClick={() => { setYearFilter(yearFilter === y ? null : y); setPage(1); }}
                      className={cn(
                        "px-3 py-1 rounded-full text-xs font-medium transition-colors",
                        yearFilter === y
                          ? "bg-blue-600 text-white"
                          : "bg-white dark:bg-slate-700 border border-slate-200 dark:border-slate-600 text-slate-600 dark:text-slate-300 hover:border-blue-300"
                      )}
                    >
                      {y}
                    </button>
                  ))}
                </div>
              </div>

              {/* Marks filter */}
              <div>
                <p className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wide mb-2">Marks</p>
                <div className="flex flex-wrap gap-1.5">
                  {availableMarks.map((m) => (
                    <button
                      key={m}
                      onClick={() => { setMarksFilter(marksFilter === m ? null : m); setPage(1); }}
                      className={cn(
                        "px-3 py-1 rounded-full text-xs font-medium transition-colors",
                        marksFilter === m
                          ? "bg-blue-600 text-white"
                          : "bg-white dark:bg-slate-700 border border-slate-200 dark:border-slate-600 text-slate-600 dark:text-slate-300 hover:border-blue-300"
                      )}
                    >
                      {m}M
                    </button>
                  ))}
                </div>
              </div>

              {/* Type filter */}
              {availableTypes.length > 1 && (
                <div>
                  <p className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wide mb-2">Type</p>
                  <div className="flex flex-wrap gap-1.5">
                    {availableTypes.map((t) => (
                      <button
                        key={t}
                        onClick={() => { setTypeFilter(typeFilter === t ? null : t); setPage(1); }}
                        className={cn(
                          "px-3 py-1 rounded-full text-xs font-medium transition-colors",
                          typeFilter === t
                            ? "bg-blue-600 text-white"
                            : "bg-white dark:bg-slate-700 border border-slate-200 dark:border-slate-600 text-slate-600 dark:text-slate-300 hover:border-blue-300"
                        )}
                      >
                        {t}
                      </button>
                    ))}
                  </div>
                </div>
              )}

              {activeFilters > 0 && (
                <button
                  onClick={clearFilters}
                  className="text-xs text-red-500 hover:text-red-700 font-medium"
                >
                  Clear all filters
                </button>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Results count */}
      {(search || activeFilters > 0) && (
        <p className="text-sm text-slate-500 dark:text-slate-400">
          Found <strong className="text-slate-900 dark:text-slate-100">{filtered.length}</strong> questions
        </p>
      )}

      {/* Question list */}
      <div className="space-y-4">
        <AnimatePresence mode="popLayout">
          {paginated.length === 0 ? (
            <motion.div
              key="empty"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex flex-col items-center justify-center py-16 text-center"
            >
              <div className="text-4xl mb-3">📚</div>
              <p className="text-slate-500 dark:text-slate-400 text-sm">
                {emptyMessage || "No questions found"}
              </p>
              {(search || activeFilters > 0) && (
                <button onClick={clearFilters} className="mt-2 text-xs text-blue-600 hover:underline">
                  Clear filters
                </button>
              )}
            </motion.div>
          ) : (
            paginated.map((q) => (
              <QuestionCard
                key={q.id}
                question={q}
                isBookmarked={bookmarks.has(q.id)}
                isSolved={solved.has(q.id)}
                onBookmark={toggleBookmark}
                onSolve={toggleSolved}
                showChapter={showChapter}
              />
            ))
          )}
        </AnimatePresence>
      </div>

      {/* Load more */}
      {hasMore && (
        <div className="flex justify-center pt-4">
          <Button variant="outline" onClick={() => setPage((p) => p + 1)} className="gap-2">
            <SortAsc className="size-4" />
            Load more ({filtered.length - paginated.length} remaining)
          </Button>
        </div>
      )}
    </div>
  );
}

export default QuestionList;
