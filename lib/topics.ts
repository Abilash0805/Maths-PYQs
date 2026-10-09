import type { ChapterKey } from "./chapters";

// Canonical sub-topics per chapter (used for @topic labels and the chapter-page topic filter).
export const TOPICS: Record<ChapterKey, string[]> = {
  rf: ["Types of relations", "Equivalence relations and classes", "Counting relations and functions", "One-one and onto functions"],
  itf: ["Domain and range", "Principal values", "Graphs of inverse trigonometric functions", "Simplification"],
  mat: ["Types of matrices", "Operations on matrices", "Transpose", "Symmetric and skew-symmetric matrices", "Invertible matrices"],
  det: ["Evaluation of determinants", "Minors and cofactors", "Adjoint and inverse", "Properties of |A| and |adj A|", "Area of a triangle", "Systems of linear equations"],
  cd: [
    "Continuity",
    "Differentiability",
    "Chain rule and implicit differentiation",
    "Derivatives of inverse trigonometric functions",
    "Logarithmic differentiation",
    "Parametric differentiation",
    "Second order derivatives",
  ],
  aod: ["Rate of change", "Increasing and decreasing functions", "Local maxima and minima", "Absolute maxima and minima", "Optimisation problems"],
  int: [
    "Standard integrals",
    "Integration by substitution",
    "Partial fractions",
    "Integration by parts",
    "Special forms",
    "Definite integrals",
    "Properties of definite integrals",
  ],
  aoi: ["Area under a curve", "Area bounded by a curve and a line", "Area of circles and ellipses", "Area enclosed by lines"],
  de: ["Order and degree", "General and particular solutions", "Variable separable", "Homogeneous equations", "Linear differential equations"],
  vec: ["Basic concepts of vectors", "Direction cosines and ratios", "Position vectors and section formula", "Scalar product and projection", "Vector product and area"],
  "3d": [
    "Direction cosines and ratios",
    "Equation of a line",
    "Angle between two lines",
    "Shortest distance between lines",
    "Foot of perpendicular and image",
    "Intersection and collinearity",
  ],
  lpp: ["Terminology and basics", "Feasible region and corner points", "Graphical method – bounded region", "Graphical method – unbounded region", "Word problems"],
  prob: [
    "Conditional probability",
    "Multiplication theorem and independent events",
    "Total probability and Bayes' theorem",
    "Random variables and probability distributions",
    "Mean of a random variable",
  ],
};
