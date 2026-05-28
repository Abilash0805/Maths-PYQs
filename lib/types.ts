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
  "Relations and Functions": "bg-blue-50 border-blue-200",
  "Inverse Trigonometric Functions": "bg-purple-50 border-purple-200",
  "Matrices": "bg-emerald-50 border-emerald-200",
  "Determinants": "bg-teal-50 border-teal-200",
  "Continuity and Differentiability": "bg-orange-50 border-orange-200",
  "Application of Derivatives": "bg-rose-50 border-rose-200",
  "Integrals": "bg-indigo-50 border-indigo-200",
  "Differential Equations": "bg-cyan-50 border-cyan-200",
  "Vector Algebra": "bg-violet-50 border-violet-200",
  "Three Dimensional Geometry": "bg-amber-50 border-amber-200",
  "Linear Programming": "bg-lime-50 border-lime-200",
  "Probability": "bg-pink-50 border-pink-200",
};
