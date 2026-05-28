import Link from "next/link";
import { BookOpen, TrendingUp, Star, Zap, ArrowRight, Calendar } from "lucide-react";
import { getChapterStats, getAllQuestions, getAvailableYears } from "@/lib/data";
import { CHAPTERS, CHAPTER_COLORS, CHAPTER_ICONS, CHAPTER_BG } from "@/lib/types";
import { Badge } from "@/components/ui/badge";
import { cn } from "@/lib/utils";

export default function HomePage() {
  const stats = getChapterStats();
  const allQuestions = getAllQuestions();
  const years = getAvailableYears();
  const totalQuestions = allQuestions.length;
  const totalChapters = CHAPTERS.length;

  return (
    <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-6xl mx-auto space-y-8">
      {/* Hero */}
      <div className="rounded-2xl bg-gradient-to-br from-blue-600 via-blue-500 to-indigo-600 p-6 sm:p-8 text-white relative overflow-hidden">
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-4 right-4 text-8xl font-bold">∫</div>
          <div className="absolute bottom-4 left-4 text-6xl font-bold">Σ</div>
          <div className="absolute top-1/2 right-1/4 text-7xl font-bold">π</div>
        </div>
        <div className="relative">
          <Badge className="mb-3 bg-white/20 text-white border-white/30 hover:bg-white/30">
            CBSE Class 12 Mathematics
          </Badge>
          <h1 className="text-2xl sm:text-3xl font-bold mb-2">
            Previous Year Questions
          </h1>
          <p className="text-blue-100 text-sm sm:text-base max-w-xl mb-5">
            Practice with {totalQuestions}+ real exam questions from {years.length} years of CBSE papers.
            Complete solutions included.
          </p>
          <div className="flex flex-wrap gap-3">
            <div className="bg-white/15 rounded-xl px-4 py-2 text-center">
              <div className="text-2xl font-bold">{totalQuestions}</div>
              <div className="text-xs text-blue-100">Questions</div>
            </div>
            <div className="bg-white/15 rounded-xl px-4 py-2 text-center">
              <div className="text-2xl font-bold">{years.length}</div>
              <div className="text-xs text-blue-100">Years</div>
            </div>
            <div className="bg-white/15 rounded-xl px-4 py-2 text-center">
              <div className="text-2xl font-bold">{totalChapters}</div>
              <div className="text-xs text-blue-100">Chapters</div>
            </div>
            <div className="bg-white/15 rounded-xl px-4 py-2 text-center">
              <div className="text-2xl font-bold">100%</div>
              <div className="text-xs text-blue-100">Free</div>
            </div>
          </div>
        </div>
      </div>

      {/* Quick links */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        {[
          { href: "/search", label: "Search Questions", icon: "🔍", color: "bg-blue-50 dark:bg-blue-950/30 border-blue-200 dark:border-blue-800 text-blue-700 dark:text-blue-400" },
          { href: "/important", label: "Important Questions", icon: "⭐", color: "bg-amber-50 dark:bg-amber-950/30 border-amber-200 dark:border-amber-800 text-amber-700 dark:text-amber-400" },
          { href: "/bookmarks", label: "Bookmarks", icon: "🔖", color: "bg-purple-50 dark:bg-purple-950/30 border-purple-200 dark:border-purple-800 text-purple-700 dark:text-purple-400" },
          { href: "/progress", label: "My Progress", icon: "📊", color: "bg-green-50 dark:bg-green-950/30 border-green-200 dark:border-green-800 text-green-700 dark:text-green-400" },
        ].map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className={cn(
              "flex flex-col items-center gap-2 rounded-xl border p-4 text-center text-sm font-medium transition-all hover:shadow-sm hover:-translate-y-0.5",
              item.color
            )}
          >
            <span className="text-2xl">{item.icon}</span>
            <span>{item.label}</span>
          </Link>
        ))}
      </div>

      {/* Years */}
      <div>
        <div className="flex items-center gap-2 mb-3">
          <Calendar className="size-4 text-slate-500" />
          <h2 className="text-base font-bold text-slate-900 dark:text-white">Browse by Year</h2>
        </div>
        <div className="flex flex-wrap gap-2">
          {years.map((year) => {
            const count = allQuestions.filter((q) => q.year === year).length;
            return (
              <Link
                key={year}
                href={`/search?year=${year}`}
                className="group flex items-center gap-1.5 rounded-full border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-1.5 text-sm hover:border-blue-300 hover:bg-blue-50 dark:hover:bg-blue-950/30 transition-colors"
              >
                <span className="font-semibold text-slate-800 dark:text-slate-200">{year}</span>
                <span className="text-xs text-slate-400 dark:text-slate-500">({count})</span>
              </Link>
            );
          })}
        </div>
      </div>

      {/* Chapters grid */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <BookOpen className="size-4 text-slate-500" />
            <h2 className="text-base font-bold text-slate-900 dark:text-white">All Chapters</h2>
          </div>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {CHAPTERS.map((chapter, idx) => {
            const stat = stats.find((s) => s.chapter === chapter);
            const gradient = CHAPTER_COLORS[chapter];
            const icon = CHAPTER_ICONS[chapter];
            const bgClass = CHAPTER_BG[chapter];

            return (
              <Link
                key={chapter}
                href={`/chapter/${encodeURIComponent(chapter)}`}
                className={cn(
                  "group rounded-xl border p-4 transition-all hover:shadow-md hover:-translate-y-0.5",
                  bgClass
                )}
              >
                <div className="flex items-start gap-3">
                  <div
                    className={cn(
                      "flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-gradient-to-br text-white text-sm font-bold shadow-sm",
                      gradient
                    )}
                  >
                    {icon}
                  </div>
                  <div className="flex-1 min-w-0">
                    <h3 className="text-sm font-semibold text-slate-900 dark:text-white leading-tight mb-1">
                      {chapter}
                    </h3>
                    <div className="flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
                      <span className="font-medium text-slate-700 dark:text-slate-300">
                        {stat?.total || 0} questions
                      </span>
                      {stat && stat.years.length > 0 && (
                        <span>· {stat.years.length} years</span>
                      )}
                    </div>
                    {stat && stat.years.length > 0 && (
                      <div className="mt-2 flex flex-wrap gap-1">
                        {stat.years.slice(0, 5).map((y) => (
                          <span
                            key={y}
                            className="inline-block rounded px-1.5 py-0.5 text-[10px] font-medium bg-white/60 dark:bg-black/20 text-slate-600 dark:text-slate-300"
                          >
                            {y}
                          </span>
                        ))}
                        {stat.years.length > 5 && (
                          <span className="text-[10px] text-slate-400">+{stat.years.length - 5}</span>
                        )}
                      </div>
                    )}
                  </div>
                  <ArrowRight className="size-4 text-slate-300 dark:text-slate-600 group-hover:text-slate-500 dark:group-hover:text-slate-400 shrink-0 mt-0.5 transition-colors" />
                </div>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
}
