"use client";

import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Bookmark, BookmarkCheck, CheckCircle2, Circle, ChevronDown, ChevronUp, Star } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { cn, cleanMathText } from "@/lib/utils";
import { PYQItem, CHAPTER_COLORS } from "@/lib/types";

interface QuestionCardProps {
  question: PYQItem;
  isBookmarked: boolean;
  isSolved: boolean;
  onBookmark: (id: string) => void;
  onSolve: (id: string) => void;
  showChapter?: boolean;
}

const sectionLabels: Record<string, string> = {
  A: "MCQ · 1M",
  B: "VSA · 2M",
  C: "SA · 3M",
  D: "LA · 5M",
  E: "Case Study · 4M",
};

const marksColor: Record<number, string> = {
  1: "info",
  2: "info",
  3: "warning",
  4: "purple",
  5: "destructive",
};

export function QuestionCard({
  question,
  isBookmarked,
  isSolved,
  onBookmark,
  onSolve,
  showChapter = true,
}: QuestionCardProps) {
  const [showAnswer, setShowAnswer] = useState(false);
  const gradientClass = CHAPTER_COLORS[question.chapter] || "from-blue-500 to-blue-600";

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -8 }}
      transition={{ duration: 0.25 }}
      className={cn(
        "relative rounded-2xl border bg-white shadow-sm hover:shadow-md transition-shadow overflow-hidden",
        isSolved && "border-green-300",
        !isSolved && "border-slate-200"
      )}
    >
      {/* Accent top bar */}
      <div className={cn("h-1 w-full bg-gradient-to-r", gradientClass)} />

      <div className="p-5">
        {/* Header row */}
        <div className="flex flex-wrap items-center gap-2 mb-3">
          <span className="flex items-center gap-1.5 text-xs font-bold text-slate-500">
            <span className="text-slate-400">Q{question.question_number}</span>
          </span>

          <Badge variant="info" className="text-xs">
            {question.year}
            {question.term ? ` ${question.term}` : ""}
          </Badge>

          <Badge variant={(marksColor[question.marks] as any) || "outline"} className="text-xs">
            {sectionLabels[question.section] || `${question.marks}M`}
          </Badge>

          {showChapter && (
            <Badge variant="outline" className="text-xs hidden sm:flex">
              {question.chapter}
            </Badge>
          )}

          {question.is_important && (
            <Badge variant="warning" className="text-xs gap-1">
              <Star className="size-3" />
              Important
            </Badge>
          )}

          <div className="ml-auto flex items-center gap-1">
            <Button
              variant="ghost"
              size="icon-sm"
              onClick={() => onSolve(question.id)}
              className={cn(
                "transition-colors",
                isSolved
                  ? "text-green-600 hover:text-green-700"
                  : "text-slate-400 hover:text-green-600"
              )}
              title={isSolved ? "Mark as unsolved" : "Mark as solved"}
            >
              {isSolved ? <CheckCircle2 className="size-4" /> : <Circle className="size-4" />}
            </Button>
            <Button
              variant="ghost"
              size="icon-sm"
              onClick={() => onBookmark(question.id)}
              className={cn(
                "transition-colors",
                isBookmarked
                  ? "text-amber-500 hover:text-amber-600"
                  : "text-slate-400 hover:text-amber-500"
              )}
              title={isBookmarked ? "Remove bookmark" : "Bookmark"}
            >
              {isBookmarked ? <BookmarkCheck className="size-4" /> : <Bookmark className="size-4" />}
            </Button>
          </div>
        </div>

        {/* Question text */}
        <div className="text-sm text-slate-800 leading-relaxed font-medium mb-3 whitespace-pre-wrap">
          {cleanMathText(question.question)}
        </div>

        {/* MCQ options */}
        {question.options && Object.keys(question.options).length > 0 && (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-3">
            {Object.entries(question.options).map(([key, val]) => (
              <div
                key={key}
                className="flex items-start gap-2 text-sm text-slate-700 bg-slate-50 rounded-lg px-3 py-2"
              >
                <span className="font-semibold text-primary min-w-[18px]">({key})</span>
                <span className="whitespace-pre-wrap">{cleanMathText(val)}</span>
              </div>
            ))}
          </div>
        )}

        {/* Show/Hide Answer Button */}
        <Button
          onClick={() => setShowAnswer(!showAnswer)}
          variant={showAnswer ? "secondary" : "default"}
          size="sm"
          className="gap-1.5"
        >
          {showAnswer ? (
            <>
              <ChevronUp className="size-4" />
              Hide Answer
            </>
          ) : (
            <>
              <ChevronDown className="size-4" />
              Show Answer
            </>
          )}
        </Button>
      </div>

      {/* Answer section */}
      <AnimatePresence>
        {showAnswer && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3, ease: "easeInOut" }}
            className="overflow-hidden"
          >
            <div className="px-5 pb-5">
              <div className="rounded-xl border border-green-200 bg-green-50 p-4">
                <div className="flex items-center gap-2 mb-2">
                  <CheckCircle2 className="size-4 text-green-600 shrink-0" />
                  <span className="text-xs font-semibold text-green-700 uppercase tracking-wide">
                    Solution
                  </span>
                </div>
                <div className="text-sm text-slate-800 leading-relaxed whitespace-pre-wrap">
                  {cleanMathText(question.answer)}
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}

export default QuestionCard;
