"use client";

import React from "react";

interface MathRendererProps {
  text: string;
  className?: string;
}

// Render text with inline math between $ signs and display math between $$ signs
export function MathRenderer({ text, className }: MathRendererProps) {
  if (!text) return null;

  // Split on display math first, then inline math
  const parts = parseTextWithMath(text);

  return (
    <span className={className}>
      {parts.map((part, i) => {
        if (part.type === "display-math") {
          return (
            <span key={i} className="block my-2 overflow-x-auto text-center font-mono text-sm">
              {renderMathFallback(part.content, true)}
            </span>
          );
        }
        if (part.type === "inline-math") {
          return (
            <span key={i} className="font-mono text-sm bg-slate-100 px-1 rounded">
              {renderMathFallback(part.content, false)}
            </span>
          );
        }
        return <span key={i}>{part.content}</span>;
      })}
    </span>
  );
}

interface TextPart {
  type: "text" | "inline-math" | "display-math";
  content: string;
}

function parseTextWithMath(text: string): TextPart[] {
  const parts: TextPart[] = [];
  let remaining = text;

  while (remaining.length > 0) {
    // Check for display math $$...$$
    const displayStart = remaining.indexOf("$$");
    // Check for inline math $...$
    const inlineStart = remaining.indexOf("$");

    if (displayStart === -1 && inlineStart === -1) {
      parts.push({ type: "text", content: remaining });
      break;
    }

    if (displayStart !== -1 && (inlineStart === -1 || displayStart <= inlineStart)) {
      if (displayStart > 0) {
        parts.push({ type: "text", content: remaining.substring(0, displayStart) });
      }
      const end = remaining.indexOf("$$", displayStart + 2);
      if (end === -1) {
        parts.push({ type: "text", content: remaining });
        break;
      }
      parts.push({ type: "display-math", content: remaining.substring(displayStart + 2, end) });
      remaining = remaining.substring(end + 2);
    } else if (inlineStart !== -1) {
      if (inlineStart > 0) {
        parts.push({ type: "text", content: remaining.substring(0, inlineStart) });
      }
      const end = remaining.indexOf("$", inlineStart + 1);
      if (end === -1) {
        parts.push({ type: "text", content: remaining });
        break;
      }
      parts.push({ type: "inline-math", content: remaining.substring(inlineStart + 1, end) });
      remaining = remaining.substring(end + 1);
    } else {
      parts.push({ type: "text", content: remaining });
      break;
    }
  }

  return parts;
}

function renderMathFallback(latex: string, _isDisplay: boolean): string {
  // Simple LaTeX to unicode/readable conversion
  return latex
    .replace(/\\frac\{([^}]+)\}\{([^}]+)\}/g, "($1)/($2)")
    .replace(/\\sqrt\{([^}]+)\}/g, "√($1)")
    .replace(/\\int/g, "∫")
    .replace(/\\sum/g, "Σ")
    .replace(/\\prod/g, "Π")
    .replace(/\\infty/g, "∞")
    .replace(/\\pi/g, "π")
    .replace(/\\theta/g, "θ")
    .replace(/\\alpha/g, "α")
    .replace(/\\beta/g, "β")
    .replace(/\\gamma/g, "γ")
    .replace(/\\delta/g, "δ")
    .replace(/\\lambda/g, "λ")
    .replace(/\\mu/g, "μ")
    .replace(/\\sigma/g, "σ")
    .replace(/\\omega/g, "ω")
    .replace(/\\rightarrow/g, "→")
    .replace(/\\leftarrow/g, "←")
    .replace(/\\Rightarrow/g, "⇒")
    .replace(/\\leq/g, "≤")
    .replace(/\\geq/g, "≥")
    .replace(/\\neq/g, "≠")
    .replace(/\\approx/g, "≈")
    .replace(/\\times/g, "×")
    .replace(/\\cdot/g, "·")
    .replace(/\\pm/g, "±")
    .replace(/\\in/g, "∈")
    .replace(/\\subset/g, "⊂")
    .replace(/\\cup/g, "∪")
    .replace(/\\cap/g, "∩")
    .replace(/\\{/g, "{")
    .replace(/\\}/g, "}")
    .replace(/\^2/g, "²")
    .replace(/\^3/g, "³")
    .replace(/\^n/g, "ⁿ")
    .replace(/\^-1/g, "⁻¹")
    .replace(/_{([^}]+)}/g, "_$1")
    .replace(/\^{([^}]+)}/g, "^$1")
    .replace(/\\text\{([^}]+)\}/g, "$1")
    .replace(/\\mathbf\{([^}]+)\}/g, "$1")
    .replace(/\\\\/, " ");
}

export default MathRenderer;
