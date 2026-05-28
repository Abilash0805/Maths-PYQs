export type QuestionType = "MCQ" | "VSA" | "SA" | "LA" | "Case Study";
export type Section = "A" | "B" | "C" | "D" | "E";

export interface PYQItem {
  id: string;
  year: number;
  question_number: number;
  question: string;
  options?: Record<string, string>;
  answer: string;
  section: Section;
  marks: number;
  chapter: string;
  type: QuestionType;
  term?: string;
  is_important?: boolean;
}

export const CHAPTERS = [
  "Relations and Functions",
  "Inverse Trigonometric Functions",
  "Matrices",
  "Determinants",
  "Continuity and Differentiability",
  "Application of Derivatives",
  "Integrals",
  "Differential Equations",
  "Vector Algebra",
  "Three Dimensional Geometry",
  "Linear Programming",
  "Probability",
] as const;

export type Chapter = (typeof CHAPTERS)[number];

export const CHAPTER_ICONS: Record<string, string> = {
  "Relations and Functions": "∘",
  "Inverse Trigonometric Functions": "θ⁻¹",
  "Matrices": "⊞",
  "Determinants": "|A|",
  "Continuity and Differentiability": "∂",
  "Application of Derivatives": "∇",
  "Integrals": "∫",
  "Differential Equations": "dy",
  "Vector Algebra": "→",
  "Three Dimensional Geometry": "xyz",
  "Linear Programming": "LP",
  "Probability": "P(E)",
};

export const CHAPTER_COLORS: Record<string, string> = {
  "Relations and Functions": "from-blue-500 to-blue-600",
  "Inverse Trigonometric Functions": "from-purple-500 to-purple-600",
  "Matrices": "from-emerald-500 to-emerald-600",
  "Determinants": "from-teal-500 to-teal-600",
  "Continuity and Differentiability": "from-orange-500 to-orange-600",
  "Application of Derivatives": "from-rose-500 to-rose-600",
  "Integrals": "from-indigo-500 to-indigo-600",
  "Differential Equations": "from-cyan-500 to-cyan-600",
  "Vector Algebra": "from-violet-500 to-violet-600",
  "Three Dimensional Geometry": "from-amber-500 to-amber-600",
  "Linear Programming": "from-lime-500 to-lime-600",
  "Probability": "from-pink-500 to-pink-600",
};

export const CHAPTER_BG: Record<string, string> = {
  "Relations and Functions": "bg-blue-50 dark:bg-blue-950/30 border-blue-200 dark:border-blue-800",
  "Inverse Trigonometric Functions": "bg-purple-50 dark:bg-purple-950/30 border-purple-200 dark:border-purple-800",
  "Matrices": "bg-emerald-50 dark:bg-emerald-950/30 border-emerald-200 dark:border-emerald-800",
  "Determinants": "bg-teal-50 dark:bg-teal-950/30 border-teal-200 dark:border-teal-800",
  "Continuity and Differentiability": "bg-orange-50 dark:bg-orange-950/30 border-orange-200 dark:border-orange-800",
  "Application of Derivatives": "bg-rose-50 dark:bg-rose-950/30 border-rose-200 dark:border-rose-800",
  "Integrals": "bg-indigo-50 dark:bg-indigo-950/30 border-indigo-200 dark:border-indigo-800",
  "Differential Equations": "bg-cyan-50 dark:bg-cyan-950/30 border-cyan-200 dark:border-cyan-800",
  "Vector Algebra": "bg-violet-50 dark:bg-violet-950/30 border-violet-200 dark:border-violet-800",
  "Three Dimensional Geometry": "bg-amber-50 dark:bg-amber-950/30 border-amber-200 dark:border-amber-800",
  "Linear Programming": "bg-lime-50 dark:bg-lime-950/30 border-lime-200 dark:border-lime-800",
  "Probability": "bg-pink-50 dark:bg-pink-950/30 border-pink-200 dark:border-pink-800",
};
