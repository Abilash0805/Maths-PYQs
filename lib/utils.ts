import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function cleanMathText(text: string): string {
  if (!text) return text;
  return text
    // --- Inverse trig: sin-1 / sin^(-1) / sin^{-1} → sin⁻¹ ---
    .replace(/\b(cosec|sinh|cosh|tanh|sin|cos|tan|cot|sec)[-–−]1\b/g, "$1⁻¹")
    .replace(/\b(cosec|sinh|cosh|tanh|sin|cos|tan|cot|sec)\^[\({][-–−]1[\)}]/g, "$1⁻¹")
    .replace(/\b(cosec|sinh|cosh|tanh|sin|cos|tan|cot|sec)\^\{[-–−]1\}/g, "$1⁻¹")

    // --- Powers: x^2 → x², x^3 → x³, etc. ---
    .replace(/\^0\b/g, "⁰")
    .replace(/\^2\b/g, "²")
    .replace(/\^3\b/g, "³")
    .replace(/\^4\b/g, "⁴")
    .replace(/\^5\b/g, "⁵")
    .replace(/\^6\b/g, "⁶")
    .replace(/\^n\b/g, "ⁿ")
    .replace(/\^T\b/g, "ᵀ")
    // e^x → eˣ  (common in differentiation/integration)
    .replace(/\be\^x\b/g, "eˣ")
    .replace(/\be\^\{x\}\b/g, "eˣ")

    // --- Subscripts: x_1 → x₁, x_2 → x₂ ---
    .replace(/_0\b/g, "₀")
    .replace(/_1\b/g, "₁")
    .replace(/_2\b/g, "₂")
    .replace(/_3\b/g, "₃")

    // --- Unit vectors: i^, j^, k^ → î, ĵ, k̂ ---
    .replace(/\bi\^/g, "î")
    .replace(/\bj\^/g, "ĵ")
    .replace(/\bk\^/g, "k̂")

    // --- Remove stray caret/hat/wedge artifacts ---
    .replace(/\^\^+/g, "")
    .replace(/\^∧|∧\^/g, "")
    .replace(/\s*∧\s*(?=[a-zA-Z∈⇒])/g, " ")

    // --- sqrt notation ---
    .replace(/sqrt\s*\(([^)]+)\)/g, "√($1)")
    .replace(/\\sqrt\s*\{([^}]+)\}/g, "√($1)")

    // --- Arithmetic symbols ---
    // +- or +− → ± (but not inside a number like 1+-2)
    .replace(/\+\s*[-−]\s*(?!\d)/g, "±")
    .replace(/\+\s*[-−](?=\s)/g, "±")

    // --- Arrows and implication ---
    .replace(/==>/g, "⟹")
    .replace(/(?<![=<>!])=>(?![=>])/g, "⟹")
    // \\ followed by text → ∴ (therefore, from CBSE marking scheme)
    .replace(/\n\s*\\\s+/g, "\n∴ ")
    .replace(/\s+\\\s+([A-Za-z∴∀∈⇒])/g, " ∴ $1")

    // --- Comparison operators ---
    .replace(/(?<![=<>!])<=(?![=>])/g, "≤")
    .replace(/(?<![=<>!])>=(?![=>])/g, "≥")
    .replace(/!=/g, "≠")

    // --- LaTeX/plain-text math escapes ---
    .replace(/\\in\b/g, "∈")
    .replace(/\\notin\b/g, "∉")
    .replace(/\\infty\b/g, "∞")
    .replace(/\\times\b/g, "×")
    .replace(/\\cdot\b/g, "⋅")
    .replace(/\\pm\b/g, "±")
    .replace(/\\leq\b/g, "≤")
    .replace(/\\geq\b/g, "≥")
    .replace(/\\neq\b/g, "≠")
    .replace(/\\forall\b/g, "∀")
    .replace(/\\exists\b/g, "∃")
    .replace(/\\alpha\b/g, "α")
    .replace(/\\beta\b/g, "β")
    .replace(/\\theta\b/g, "θ")
    .replace(/\\pi\b/g, "π")
    .replace(/\\lambda\b/g, "λ")
    .replace(/\\mu\b/g, "μ")

    // --- Remove garbled PDF artifacts ---
    // Box/replacement chars
    .replace(/[□■▪▫▢▣▤▥▦▧▨▩�]/g, "")
    // PUA chars from PDF font encoding (matrix brackets, vector markers)
    .replace(/[-]/g, "")
    // Remaining Windows-1252 artifacts (Î=∈, ®=→, £=≤, Þ=⇒)
    .replace(/\bÎ\b/g, "∈")
    .replace(/\s*®\s*/g, " → ")
    .replace(/£/g, "≤")
    .replace(/Þ/g, "⇒")
    .replace(/\s*¢\s*/g, "′")
    // Garbled fraction characters
    .replace(/[æöçèø÷]{2,}/g, "")

    // --- Strip annotation leftovers ---
    .replace(/\[CBSE\s+M\s*arking\s+Scheme[,\s]*\d*\]/g, "")
    .replace(/\[CBSE Marking Scheme[,\s]*\d*\]/g, "")
    .replace(/\*\s*Out\s+of\s+Syllabus/g, "")
    .replace(/SOLVED PAPER\s*[-–]\s*\d{4}[^\n]*/g, "")
    // Strip mark fractions like "1½" at end of lines (CBSE step marks)
    .replace(/\s+\d+½\s*$/gm, "")
    .replace(/\s+½\s*$/gm, "")

    // --- Whitespace cleanup ---
    .replace(/\n{3,}/g, "\n\n")
    .replace(/[ \t]{2,}/g, " ")
    .replace(/[ \t]+\n/g, "\n")
    .trim();
}
