"use client";

import React from "react";
import { cn } from "@/lib/utils";

interface ProgressBarProps {
  value: number;
  max: number;
  className?: string;
  color?: string;
  showLabel?: boolean;
}

export function ProgressBar({ value, max, className, color = "bg-blue-500", showLabel = false }: ProgressBarProps) {
  const pct = max === 0 ? 0 : Math.round((value / max) * 100);
  return (
    <div className={cn("w-full", className)}>
      {showLabel && (
        <div className="flex justify-between text-xs text-slate-500 mb-1">
          <span>{value} solved</span>
          <span>{pct}%</span>
        </div>
      )}
      <div className="h-2 w-full rounded-full bg-slate-100 overflow-hidden">
        <div
          className={cn("h-full rounded-full transition-all duration-500", color)}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}
