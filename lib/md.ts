// Renders the question-bank markdown subset (see content/README.md) to an HTML string.
// Used on the server for question statements and lazily in the browser for solutions.
import { compilePlot, type PlotSpec } from "./plot.ts";

export type Katex = {
  renderToString: (tex: string, opts: Record<string, unknown>) => string;
};

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const escAttr = (s: string) => esc(s).replace(/"/g, "&quot;");

export function plotSvg(spec: PlotSpec): string {
  const p = compilePlot(spec);
  const parts: string[] = [];
  for (const e of p.prims) {
    switch (e.kind) {
      case "grid":
        parts.push(`<path class="pl-grid" d="${e.d}"/>`);
        break;
      case "axis":
        parts.push(`<path class="pl-axis" d="${e.d}"/>`);
        break;
      case "region":
        parts.push(`<path class="pl-region" d="${e.d}"/>`);
        break;
      case "curve":
        parts.push(`<path class="pl-curve pl-s${e.series % 4}${e.dash ? " pl-dash" : ""}" d="${e.d}"/>`);
        break;
      case "tick":
        parts.push(`<text class="pl-tick" x="${e.x}" y="${e.y}" text-anchor="${e.anchor}">${esc(e.text)}</text>`);
        break;
      case "point":
        parts.push(`<circle class="pl-point" cx="${e.x}" cy="${e.y}" r="3.5"/>`);
        break;
      case "label":
        parts.push(
          `<text class="pl-label${e.series !== undefined ? ` pl-t${e.series % 4}` : ""}" x="${e.x}" y="${e.y}" text-anchor="${e.anchor}">${esc(e.text)}</text>`,
        );
        break;
    }
  }
  return `<figure class="plot"><svg viewBox="0 0 ${p.width} ${p.height}" role="img" aria-label="Graph"><defs></defs>${parts.join("")}</svg></figure>`;
}

function inline(s: string) {
  return s
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[\s(])\*([^*\s][^*]*?)\*(?=[\s).,;:!?]|$)/g, "$1<em>$2</em>");
}

export function renderMarkdown(src: string, katex: Katex, opts: { mathml?: boolean } = {}): string {
  const tokens: string[] = [];
  const tok = (html: string, block = false) => {
    tokens.push(html);
    return `\u0000${block ? "B" : "I"}${tokens.length - 1}\u0000`;
  };
  const output = opts.mathml === false ? "html" : "htmlAndMathml";
  const kx = (tex: string, display: boolean) => {
    try {
      return katex.renderToString(tex, { displayMode: display, throwOnError: false, strict: "ignore", output, trust: false });
    } catch {
      return `<code>${esc(tex)}</code>`;
    }
  };

  let s = src.replace(/\r\n/g, "\n");
  s = s.replace(/```plot\n([\s\S]*?)```/g, (_, json) => {
    try {
      return "\n\n" + tok(plotSvg(JSON.parse(json)), true) + "\n\n";
    } catch {
      return "";
    }
  });
  s = s.replace(/\$\$([\s\S]+?)\$\$/g, (_, tex) => tok(`<div class="math-display">${kx(tex.trim(), true)}</div>`, true));
  s = s.replace(/\$([^$\n]+?)\$/g, (_, tex) => tok(kx(tex, false)));
  s = s.replace(/!\[([^\]]*)\]\(([^)\s]+)\)/g, (_, alt, file) =>
    tok(`<figure class="fig"><img src="/figures/${escAttr(file)}" alt="${escAttr(alt || "Figure")}" loading="lazy"/></figure>`, true),
  );

  const isBlockTok = (line: string) => /^\s*(\u0000B\d+\u0000\s*)+$/.test(line);
  const restore = (h: string) => h.replace(/\u0000[BI](\d+)\u0000/g, (_, i) => tokens[Number(i)]);

  const out: string[] = [];
  for (const block of s.split(/\n\s*\n/)) {
    const lines = block.split("\n").filter((l) => l.trim() !== "");
    if (!lines.length) continue;
    if (lines.every((l) => l.trim().startsWith("|"))) {
      const rows = lines
        .map((l) => l.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim()))
        .filter((r) => !r.every((c) => /^:?-{2,}:?$/.test(c)));
      const [head, ...body] = rows;
      out.push(
        `<div class="table-wrap"><table><thead><tr>${head.map((c) => `<th>${inline(esc(c))}</th>`).join("")}</tr></thead><tbody>${body
          .map((r) => `<tr>${r.map((c) => `<td>${inline(esc(c))}</td>`).join("")}</tr>`)
          .join("")}</tbody></table></div>`,
      );
      continue;
    }
    if (lines.every((l) => /^\s*- /.test(l))) {
      out.push(`<ul>${lines.map((l) => `<li>${inline(esc(l.replace(/^\s*- /, "")))}</li>`).join("")}</ul>`);
      continue;
    }
    let para: string[] = [];
    const flush = () => {
      if (para.length) out.push(`<p>${para.map((l) => inline(esc(l))).join("<br/>")}</p>`);
      para = [];
    };
    for (const l of lines) {
      if (isBlockTok(l)) {
        flush();
        out.push(l.trim());
      } else para.push(l);
    }
    flush();
  }
  return restore(out.join("\n"));
}
