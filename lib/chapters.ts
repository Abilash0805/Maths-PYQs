// Chapters and units of CBSE Class XII Mathematics (041), 2026-27 syllabus.

export type ChapterKey = "rf" | "itf" | "mat" | "det" | "cd" | "aod" | "int" | "aoi" | "de" | "vec" | "3d" | "lpp" | "prob";

export type Unit = { key: string; name: string; marks: number; hue: "violet" | "blue" | "teal" | "orange" | "pink" | "amber" };

export const UNITS: Unit[] = [
  { key: "u1", name: "Relations and Functions", marks: 8, hue: "violet" },
  { key: "u2", name: "Algebra", marks: 10, hue: "blue" },
  { key: "u3", name: "Calculus", marks: 35, hue: "teal" },
  { key: "u4", name: "Vectors and 3-D Geometry", marks: 14, hue: "orange" },
  { key: "u5", name: "Linear Programming", marks: 5, hue: "pink" },
  { key: "u6", name: "Probability", marks: 8, hue: "amber" },
];

export type Chapter = { key: ChapterKey; slug: string; name: string; unit: string; no: number; blurb: string };

export const CHAPTERS: Chapter[] = [
  { key: "rf", slug: "relations-and-functions", name: "Relations and Functions", unit: "u1", no: 1, blurb: "Equivalence relations, equivalence classes, one-one and onto functions." },
  { key: "itf", slug: "inverse-trigonometric-functions", name: "Inverse Trigonometric Functions", unit: "u1", no: 2, blurb: "Domain, range, principal value branches and graphs." },
  { key: "mat", slug: "matrices", name: "Matrices", unit: "u2", no: 3, blurb: "Types, operations, transpose, symmetric and skew-symmetric matrices, invertibility." },
  { key: "det", slug: "determinants", name: "Determinants", unit: "u2", no: 4, blurb: "Minors, cofactors, adjoint, inverse, area of a triangle and solving linear systems." },
  { key: "cd", slug: "continuity-and-differentiability", name: "Continuity and Differentiability", unit: "u3", no: 5, blurb: "Continuity, chain rule, implicit, parametric, logarithmic and second-order derivatives." },
  { key: "aod", slug: "application-of-derivatives", name: "Application of Derivatives", unit: "u3", no: 6, blurb: "Rate of change, increasing/decreasing functions, maxima and minima." },
  { key: "int", slug: "integrals", name: "Integrals", unit: "u3", no: 7, blurb: "Substitution, partial fractions, by parts, special forms and definite integrals." },
  { key: "aoi", slug: "application-of-integrals", name: "Application of Integrals", unit: "u3", no: 8, blurb: "Area under lines, circles, parabolas and ellipses." },
  { key: "de", slug: "differential-equations", name: "Differential Equations", unit: "u3", no: 9, blurb: "Order and degree, variable separable, homogeneous and linear equations." },
  { key: "vec", slug: "vector-algebra", name: "Vector Algebra", unit: "u4", no: 10, blurb: "Direction cosines, section formula, scalar and vector products." },
  { key: "3d", slug: "three-dimensional-geometry", name: "Three Dimensional Geometry", unit: "u4", no: 11, blurb: "Lines in space, angle between lines, shortest distance, foot of perpendicular." },
  { key: "lpp", slug: "linear-programming", name: "Linear Programming", unit: "u5", no: 12, blurb: "Graphical method, feasible regions and corner points." },
  { key: "prob", slug: "probability", name: "Probability", unit: "u6", no: 13, blurb: "Conditional probability, Bayes' theorem, random variables and their mean." },
];

export const chapterByKey = (k: string) => CHAPTERS.find((c) => c.key === k)!;
export const chapterBySlug = (s: string) => CHAPTERS.find((c) => c.slug === s);
export const unitOf = (c: Chapter) => UNITS.find((u) => u.key === c.unit)!;

export const TYPE_LABEL: Record<string, string> = { mcq: "MCQ", ar: "Assertion–Reason", sub: "Subjective", case: "Case study" };
