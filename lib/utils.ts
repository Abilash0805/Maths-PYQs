import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function cleanMathText(text: string): string {
  if (!text) return text;
  return text
    // Inverse trig notation: sin-1 → sin⁻¹
    .replace(/\bsin-1\b/g, "sin⁻¹")
    .replace(/\bcos-1\b/g, "cos⁻¹")
    .replace(/\btan-1\b/g, "tan⁻¹")
    .replace(/\bcot-1\b/g, "cot⁻¹")
    .replace(/\bsec-1\b/g, "sec⁻¹")
    .replace(/\bcosec-1\b/g, "cosec⁻¹")
    // Vector arrow: a→ → a⃗
    .replace(/([a-zA-Z])\s*→\s*/g, "$1⃗ ")
    // Unit vectors: i^, j^, k^ → î, ĵ, k̂
    .replace(/\bi\^/g, "î").replace(/\bj\^/g, "ĵ").replace(/\bk\^/g, "k̂")
    // Clean stray hat symbols
    .replace(/\s*∧\s*/g, " ")
    .replace(/\^∧|∧\^/g, "")
    // Collapse extra whitespace
    .replace(/\s{2,}/g, " ")
    .trim();
}
