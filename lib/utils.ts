import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function cleanMathText(text: string): string {
  if (!text) return text;
  return text
    .replace(/\s*∧\s*/g, "̂")            // hat notation: remove stray ∧ symbols
    .replace(/([a-zA-Z])\^/g, "$1̂")      // letter^ → letter with hat
    .replace(/→\s*→/g, "→")              // double arrows → single
    .replace(/\|\s*\|/g, "|")             // normalize double bars
    .replace(/\s{2,}/g, " ")              // collapse multiple spaces
    .replace(/([a-z])\s*∧\s*([a-z])/gi, "$1̂$2")  // i∧j → î ĵ style
    .replace(/\^∧|∧\^/g, "^")            // ^^  → ^
    .trim();
}
