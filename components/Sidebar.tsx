"use client";

import React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { motion } from "framer-motion";
import { cn } from "@/lib/utils";
import { CHAPTERS, CHAPTER_COLORS, CHAPTER_ICONS } from "@/lib/types";
import { BookOpen, Home, Search, Bookmark, TrendingUp, Star, X } from "lucide-react";

interface ChapterStat {
  chapter: string;
  total: number;
  years: number[];
  important: number;
}

interface SidebarProps {
  stats: ChapterStat[];
  isOpen?: boolean;
  onClose?: () => void;
}

export function Sidebar({ stats, isOpen = true, onClose }: SidebarProps) {
  const pathname = usePathname();

  const navLinks = [
    { href: "/", label: "Home", icon: Home },
    { href: "/search", label: "Search", icon: Search },
    { href: "/bookmarks", label: "Bookmarks", icon: Bookmark },
    { href: "/important", label: "Important", icon: Star },
    { href: "/progress", label: "My Progress", icon: TrendingUp },
  ];

  return (
    <aside
      className={cn(
        "flex flex-col h-full bg-white border-r border-slate-200",
        "w-72 shrink-0"
      )}
    >
      {/* Logo */}
      <div className="flex items-center justify-between px-5 py-4 border-b border-slate-200">
        <Link href="/" className="flex items-center gap-2.5 group">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 text-white text-sm font-bold shadow-md group-hover:shadow-blue-200 transition-shadow">
            M
          </div>
          <div>
            <p className="text-sm font-bold text-slate-900 leading-none">MathsPYQ</p>
            <p className="text-xs text-slate-500 leading-none mt-0.5">CBSE Class 12</p>
          </div>
        </Link>
        {onClose && (
          <button onClick={onClose} className="p-1.5 rounded-lg hover:bg-slate-100 text-slate-500 lg:hidden">
            <X className="size-4" />
          </button>
        )}
      </div>

      {/* Navigation */}
      <div className="px-3 py-3 border-b border-slate-200">
        {navLinks.map(({ href, label, icon: Icon }) => (
          <Link
            key={href}
            href={href}
            className={cn(
              "flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors mb-0.5",
              pathname === href
                ? "bg-blue-50 text-blue-700"
                : "text-slate-600 hover:bg-slate-100 hover:text-slate-900"
            )}
          >
            <Icon className="size-4 shrink-0" />
            {label}
          </Link>
        ))}
      </div>

      {/* Chapters */}
      <div className="flex-1 overflow-y-auto px-3 py-3">
        <p className="text-xs font-semibold text-slate-400 uppercase tracking-wider px-3 mb-2">
          Chapters
        </p>
        <div className="space-y-0.5">
          {CHAPTERS.map((chapter) => {
            const stat = stats.find((s) => s.chapter === chapter);
            const href = `/chapter/${encodeURIComponent(chapter)}`;
            const isActive = pathname === href;
            const gradient = CHAPTER_COLORS[chapter];
            const icon = CHAPTER_ICONS[chapter];

            return (
              <Link
                key={chapter}
                href={href}
                className={cn(
                  "flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm transition-colors group",
                  isActive
                    ? "bg-blue-50 text-blue-700"
                    : "text-slate-600 hover:bg-slate-50 hover:text-slate-900"
                )}
              >
                <div
                  className={cn(
                    "flex h-6 w-6 shrink-0 items-center justify-center rounded-md bg-gradient-to-br text-white text-[9px] font-bold",
                    gradient
                  )}
                >
                  {icon}
                </div>
                <span className="flex-1 text-xs font-medium leading-tight">{chapter}</span>
                {stat && (
                  <span className="text-xs text-slate-400 font-mono shrink-0">
                    {stat.total}
                  </span>
                )}
              </Link>
            );
          })}
        </div>
      </div>

      {/* Bottom stats */}
      <div className="px-5 py-3 border-t border-slate-200">
        <p className="text-xs text-slate-500">
          {stats.reduce((a, b) => a + b.total, 0)} questions · 2015–2025
        </p>
      </div>
    </aside>
  );
}
