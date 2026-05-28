"use client";

import React, { useState } from "react";
import { Menu } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Sidebar } from "./Sidebar";
import { cn } from "@/lib/utils";

interface MobileHeaderProps {
  stats: { chapter: string; total: number; years: number[]; important: number }[];
}

export function MobileHeader({ stats }: MobileHeaderProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <>
      <header className="lg:hidden sticky top-0 z-40 bg-white/80 backdrop-blur border-b border-slate-200 px-4 py-3 flex items-center gap-3">
        <Button variant="ghost" size="icon" onClick={() => setSidebarOpen(true)}>
          <Menu className="size-5" />
        </Button>
        <div className="flex items-center gap-2">
          <div className="flex h-7 w-7 items-center justify-center rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 text-white text-xs font-bold">
            M
          </div>
          <span className="font-bold text-sm text-slate-900">MathsPYQ</span>
        </div>
        <span className="ml-auto text-xs font-medium text-white bg-blue-600 rounded-full px-3 py-1">
          Built by Abilash
        </span>
      </header>

      {/* Overlay */}
      {sidebarOpen && (
        <div
          className="lg:hidden fixed inset-0 z-50 bg-black/50 backdrop-blur-sm"
          onClick={() => setSidebarOpen(false)}
        >
          <div
            className="absolute left-0 top-0 h-full"
            onClick={(e) => e.stopPropagation()}
          >
            <Sidebar stats={stats} onClose={() => setSidebarOpen(false)} />
          </div>
        </div>
      )}
    </>
  );
}
