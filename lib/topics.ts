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

// Snap a free-form topic label to the closest canonical sub-topic (keyword rules, first match wins).
const RULES: Record<ChapterKey, [RegExp, string][]> = {
  rf: [[/equivalen/, "Equivalence relations and classes"], [/number of|count/, "Counting relations and functions"], [/one-one|onto|bijecti|injecti|surjecti|function/, "One-one and onto functions"], [/./, "Types of relations"]],
  itf: [[/graph/, "Graphs of inverse trigonometric functions"], [/domain|range|branch/, "Domain and range"], [/simplif/, "Simplification"], [/./, "Principal values"]],
  mat: [[/symmetric|skew/, "Symmetric and skew-symmetric matrices"], [/transpose/, "Transpose"], [/invertib|inverse/, "Invertible matrices"], [/type|order|diagonal|scalar matri|identity|construct|equal/, "Types of matrices"], [/./, "Operations on matrices"]],
  det: [[/area/, "Area of a triangle"], [/system|equation|consisten/, "Systems of linear equations"], [/minor|cofactor/, "Minors and cofactors"], [/adj|inverse/, "Adjoint and inverse"], [/propert|\|ka\||kA/, "Properties of |A| and |adj A|"], [/./, "Evaluation of determinants"]],
  cd: [[/differentiab/, "Differentiability"], [/continu/, "Continuity"], [/second/, "Second order derivatives"], [/parametric/, "Parametric differentiation"], [/logarithm/, "Logarithmic differentiation"], [/inverse trig/, "Derivatives of inverse trigonometric functions"], [/./, "Chain rule and implicit differentiation"]],
  aod: [[/rate/, "Rate of change"], [/increas|decreas|monoton/, "Increasing and decreasing functions"], [/absolute|closed interval/, "Absolute maxima and minima"], [/word|optimi|case/, "Optimisation problems"], [/./, "Local maxima and minima"]],
  int: [
    [/propert|odd|even|f\(a|modulus|piecewise|king/, "Properties of definite integrals"],
    [/partial/, "Partial fractions"],
    [/parts/, "Integration by parts"],
    [/form|special|√|sqrt/, "Special forms"],
    [/substitut/, "Integration by substitution"],
    [/definite|evaluat/, "Definite integrals"],
    [/./, "Standard integrals"],
  ],
  aoi: [[/circle|circular|ellipse/, "Area of circles and ellipses"], [/triangle|lines|polygon|line and the axes/, "Area enclosed by lines"], [/line|between|bounded/, "Area bounded by a curve and a line"], [/./, "Area under a curve"]],
  de: [[/order|degree/, "Order and degree"], [/homogeneous/, "Homogeneous equations"], [/linear|integrating factor/, "Linear differential equations"], [/separab/, "Variable separable"], [/./, "General and particular solutions"]],
  vec: [[/cross|vector product|area|lagrange/, "Vector product and area"], [/magnitude|addition|unit vector|sum of/, "Basic concepts of vectors"], [/scalar|dot|projection|perpendicular|angle/, "Scalar product and projection"], [/direction/, "Direction cosines and ratios"], [/position|section|collinear|median|diagonal|divid/, "Position vectors and section formula"], [/./, "Basic concepts of vectors"]],
  "3d": [[/shortest|between .*lines|parallel lines|skew/, "Shortest distance between lines"], [/foot|image|perpendicular distance|distance of a point|reflection/, "Foot of perpendicular and image"], [/intersect|collinear/, "Intersection and collinearity"], [/angle|perpendicular/, "Angle between two lines"], [/direction/, "Direction cosines and ratios"], [/./, "Equation of a line"]],
  lpp: [[/unbounded/, "Graphical method – unbounded region"], [/word|manufactur|diet|formulat|case|problem/, "Word problems"], [/term|basic|objective|constraint|definition/, "Terminology and basics"], [/feasible|corner/, "Feasible region and corner points"], [/./, "Graphical method – bounded region"]],
  prob: [[/bayes|total/, "Total probability and Bayes' theorem"], [/mean|expect/, "Mean of a random variable"], [/random|distribution/, "Random variables and probability distributions"], [/independ|multiplication/, "Multiplication theorem and independent events"], [/./, "Conditional probability"]],
};

export function canonicalTopic(ch: ChapterKey, label: string): string {
  const l = label.trim();
  if (TOPICS[ch].includes(l)) return l;
  const low = l.toLowerCase();
  for (const [re, t] of RULES[ch]) if (re.test(low)) return t;
  return TOPICS[ch][0];
}
