import type { ChapterKey } from "./chapters";

// CBSE Class XII Mathematics (041), 2026-27 — what is examined and what was rationalised out.
export const SYLLABUS: Record<ChapterKey, { inc: string[]; exc: string[] }> = {
  rf: {
    inc: ["Types of relations: reflexive, symmetric, transitive and equivalence relations", "Equivalence classes", "One-one and onto functions"],
    exc: ["Composite functions", "Inverse of a function", "Binary operations"],
  },
  itf: {
    inc: ["Definition, range, domain, principal value branch", "Graphs of inverse trigonometric functions"],
    exc: ["Elementary properties (sum/difference and multiple-angle identities)", "Solving equations involving inverse trigonometric functions"],
  },
  mat: {
    inc: [
      "Concept, notation, order, equality and types of matrices; zero and identity matrix",
      "Transpose; symmetric and skew-symmetric matrices",
      "Addition, multiplication, scalar multiplication and their properties",
      "Non-commutativity of multiplication; non-zero matrices whose product is zero (order 2)",
      "Invertible matrices and uniqueness of the inverse",
    ],
    exc: ["Elementary row and column operations"],
  },
  det: {
    inc: [
      "Determinant of a square matrix (up to 3 × 3), minors, cofactors",
      "Area of a triangle using determinants",
      "Adjoint and inverse of a square matrix",
      "Consistency of a system of linear equations; solving by the matrix method",
    ],
    exc: ["Properties of determinants (proofs using properties)"],
  },
  cd: {
    inc: [
      "Continuity and differentiability, chain rule",
      "Derivatives of inverse trigonometric functions and implicit functions",
      "Exponential and logarithmic functions; logarithmic differentiation",
      "Derivatives of functions in parametric form; second order derivatives",
    ],
    exc: ["Rolle's theorem and Lagrange's Mean Value Theorem"],
  },
  aod: {
    inc: ["Rate of change of quantities", "Increasing and decreasing functions", "Maxima and minima (first and second derivative tests), real-life problems"],
    exc: ["Tangents and normals", "Approximations using differentials"],
  },
  int: {
    inc: [
      "Integration as the inverse of differentiation",
      "Substitution, partial fractions and integration by parts",
      "Standard integrals of the forms ∫dx/(x² ± a²), ∫dx/√(ax² + bx + c), ∫√(a² ± x²)dx and related forms",
      "Fundamental theorem of calculus; properties and evaluation of definite integrals",
    ],
    exc: ["Definite integral as the limit of a sum"],
  },
  aoi: {
    inc: ["Area under simple curves: lines, circles, parabolas and ellipses (standard form)"],
    exc: ["Area between two curves"],
  },
  de: {
    inc: [
      "Order and degree; general and particular solutions",
      "Variables separable and homogeneous equations",
      "Linear equations dy/dx + Py = Q and dx/dy + Px = Q",
    ],
    exc: ["Formation of differential equations"],
  },
  vec: {
    inc: [
      "Vectors and scalars, magnitude, direction cosines and ratios",
      "Types of vectors, position vector, section formula",
      "Scalar (dot) product and vector (cross) product with applications",
    ],
    exc: ["Scalar triple product and coplanarity"],
  },
  "3d": {
    inc: [
      "Direction cosines and ratios of a line",
      "Vector and Cartesian equations of a line",
      "Skew lines, shortest distance, angle between two lines",
    ],
    exc: ["Planes (all forms), angle between line and plane, coplanar lines"],
  },
  lpp: {
    inc: [
      "Constraints, objective function, optimisation",
      "Graphical method in two variables; bounded and unbounded feasible regions",
      "Optimal feasible solutions (up to three non-trivial constraints)",
    ],
    exc: ["Different types of LPP (e.g. transportation)", "Problems with more than three non-trivial constraints"],
  },
  prob: {
    inc: [
      "Conditional probability and multiplication theorem",
      "Independent events, total probability, Bayes' theorem",
      "Random variable, probability distribution and mean",
    ],
    exc: ["Variance of a random variable", "Bernoulli trials and binomial distribution"],
  },
};
