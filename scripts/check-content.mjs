// Validate every paper in content/: structure, numbering, duplicate references, figures and KaTeX.
// usage: node scripts/check-content.mjs [file-or-dir ...]
import fs from "node:fs";
import path from "node:path";
import katex from "katex";
import { parsePaper, listPaperFiles, mathSnippets, paperId, CHAPTERS } from "./content.mjs";
import { compilePlot } from "../lib/plot.ts";

const ROOT = path.resolve(import.meta.dirname, "..");
const contentDir = path.join(ROOT, "content");
const files = listPaperFiles(contentDir);
const only = process.argv.slice(2).map((p) => path.resolve(p));
const errors = [];
const papers = new Map();
for (const f of files) {
  const p = parsePaper(f);
  errors.push(...p.errors);
  papers.set(paperId(p.meta.year, p.meta.code), p);
}
const macros = {};
for (const [, p] of papers) {
  const file = p.blocks[0]?.file ?? "";
  if (only.length && !only.some((o) => file.startsWith(o))) continue;
  const n = Number(p.meta.questions || 0);
  const seen = new Set(p.blocks.map((b) => b.qno));
  for (let q = 1; q <= n; q++) if (!seen.has(q)) errors.push(`${file}: question ${q} missing`);
  for (const b of p.blocks) {
    if (b.kind === "dup") {
      const t = papers.get(paperId(b.ref.year, b.ref.code));
      const ok = t && t.blocks.some((x) => x.kind === "q" && `${x.qno}${x.part}` === b.ref.q);
      const okNoPart = t && t.blocks.some((x) => x.kind === "q" && `${x.qno}` === b.ref.q);
      if (!ok && !okNoPart) errors.push(`${b.file}:${b.line} dup ref not found ${b.ref.year}:${b.ref.code}#${b.ref.q}`);
      continue;
    }
    if (b.kind !== "q") continue;
    const texts = [b.question, b.solution, ...(b.options || []).map((o) => o.t)];
    for (const t of texts) {
      for (const s of mathSnippets(t)) {
        try {
          katex.renderToString(s.tex, { displayMode: s.display, throwOnError: true, strict: "ignore", macros });
        } catch (e) {
          errors.push(`${b.file}:${b.line} Q${b.qno}${b.part} KaTeX: ${e.message.split("\n")[0]}  in  ${s.tex.slice(0, 80)}`);
        }
      }
      // unbalanced $ check
      const stripped = t.replace(/\$\$[\s\S]+?\$\$/g, "").replace(/\$[^$\n]+?\$/g, "");
      if (stripped.includes("$")) errors.push(`${b.file}:${b.line} Q${b.qno}${b.part} unbalanced $`);
    }
    for (const fig of b.figs) if (!fs.existsSync(path.join(ROOT, "public/figures", fig))) errors.push(`${b.file}:${b.line} missing figure ${fig}`);
    for (const m of (b.question + "\n" + b.solution).matchAll(/!\[[^\]]*\]\(([^)]+)\)/g))
      if (!fs.existsSync(path.join(ROOT, "public/figures", m[1]))) errors.push(`${b.file}:${b.line} missing figure ${m[1]}`);
    for (const m of b.solution.matchAll(/```plot\n([\s\S]*?)```/g)) {
      try { compilePlot(JSON.parse(m[1])); } catch (e) { errors.push(`${b.file}:${b.line} Q${b.qno}${b.part} bad plot: ${e.message}`); }
    }
  }
}
// stats
const count = Object.fromEntries(CHAPTERS.map((c) => [c.key, 0]));
let q = 0, dup = 0, skip = 0;
for (const [, p] of papers) for (const b of p.blocks) {
  if (b.kind === "q") { q++; count[b.ch]++; } else if (b.kind === "dup") dup++; else skip++;
}
console.log(`papers=${papers.size} questions=${q} duplicates=${dup} skipped(out of syllabus)=${skip}`);
console.log(CHAPTERS.map((c) => `${c.key}:${count[c.key]}`).join("  "));
if (errors.length) {
  console.log(`\n${errors.length} problem(s):`);
  for (const e of errors) console.log("  " + e);
  process.exit(1);
}
console.log("OK");
