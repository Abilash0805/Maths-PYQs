// Compile content/<year>/*.md into data/bank.json (used by the app at build time)
// and public/search-index.json (fetched by the search page).
import fs from "node:fs";
import path from "node:path";
import { parsePaper, listPaperFiles, paperId, CHAPTERS } from "./content.mjs";

const ROOT = path.resolve(import.meta.dirname, "..");
const files = listPaperFiles(path.join(ROOT, "content"));
const LENIENT = process.argv.includes("--lenient");

function webpSize(file) {
  const b = fs.readFileSync(file);
  const fmt = b.toString("ascii", 12, 16);
  if (fmt === "VP8 ") return { w: b.readUInt16LE(26) & 0x3fff, h: b.readUInt16LE(28) & 0x3fff };
  if (fmt === "VP8L") {
    const bits = b.readUInt32LE(21);
    return { w: (bits & 0x3fff) + 1, h: ((bits >> 14) & 0x3fff) + 1 };
  }
  if (fmt === "VP8X") return { w: 1 + b.readUIntLE(24, 3), h: 1 + b.readUIntLE(27, 3) };
  throw new Error(`unknown webp ${file}`);
}
function imgSize(name) {
  const f = path.join(ROOT, "public/figures", name);
  if (!fs.existsSync(f)) return null;
  if (name.endsWith(".webp")) return webpSize(f);
  if (name.endsWith(".png")) {
    const b = fs.readFileSync(f);
    return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
  }
  return null;
}

const papers = [];
const questions = [];
const byKey = new Map();
const pending = [];
for (const file of files) {
  const { meta, blocks, errors } = parsePaper(file);
  if (errors.length) {
    console.error(errors.join("\n"));
    if (LENIENT) {
      console.error(`(lenient) skipping ${path.relative(ROOT, file)}`);
      continue;
    }
    process.exit(1);
  }
  const pid = paperId(meta.year, meta.code);
  const paper = {
    id: pid,
    year: Number(meta.year),
    code: meta.code,
    series: meta.series || "",
    title: meta.title || `CBSE ${meta.year} · ${meta.code}`,
    source: meta.source || "",
    total: Number(meta.questions || 0),
    items: [],
  };
  for (const b of blocks) {
    const num = `${b.qno}${b.part}`;
    if (b.kind === "q") {
      const id = `${pid}-q${num}`;
      const q = {
        id,
        ch: b.ch,
        marks: b.marks,
        type: b.type,
        topic: b.topic,
        year: paper.year,
        code: paper.code,
        paper: pid,
        qno: b.qno,
        part: b.part,
        question: b.question,
        options: b.options,
        key: b.key ?? null,
        solution: b.solution,
        figs: b.figs.map((f) => ({ src: `/figures/${f}`, ...(imgSize(f) ?? { w: 800, h: 450 }) })),
        sources: [{ year: paper.year, code: paper.code, q: num }],
      };
      questions.push(q);
      byKey.set(`${paper.year}:${paper.code}#${num}`, q);
      paper.items.push({ n: num, kind: "q", id });
    } else if (b.kind === "dup") {
      pending.push({ from: { year: paper.year, code: paper.code, q: num }, ref: b.ref });
      paper.items.push({ n: num, kind: "dup", ref: `${b.ref.year}:${b.ref.code}#${b.ref.q}` });
    } else {
      paper.items.push({ n: num, kind: "skip", reason: b.reason });
    }
  }
  papers.push(paper);
}
for (const d of pending) {
  const k = `${d.ref.year}:${d.ref.code}#${d.ref.q}`;
  const target = byKey.get(k) ?? byKey.get(`${k}a`);
  if (!target) {
    console.error(`unresolved duplicate ${d.from.year} ${d.from.code} Q${d.from.q} -> ${k}`);
    if (LENIENT) continue;
    process.exit(1);
  }
  target.sources.push(d.from);
  const paper = papers.find((p) => p.year === d.from.year && p.code === d.from.code);
  const item = paper.items.find((i) => i.n === d.from.q && i.kind === "dup");
  item.id = target.id;
}

// order: chapter, then most recent year first, then marks, then paper order
const chOrder = Object.fromEntries(CHAPTERS.map((c, i) => [c.key, i]));
questions.sort((a, b) => chOrder[a.ch] - chOrder[b.ch] || b.year - a.year || a.marks - b.marks || a.paper.localeCompare(b.paper) || a.qno - b.qno);
papers.sort((a, b) => b.year - a.year || a.code.localeCompare(b.code, "en", { numeric: true }));

const bank = { generated: new Date().toISOString(), chapters: CHAPTERS, papers, questions };
fs.mkdirSync(path.join(ROOT, "data"), { recursive: true });
fs.writeFileSync(path.join(ROOT, "data/bank.json"), JSON.stringify(bank));

const plain = (s) =>
  s
    .replace(/```plot[\s\S]*?```/g, " ")
    .replace(/\\(?:dfrac|frac|left|right|displaystyle|quad|qquad|,|;)/g, " ")
    .replace(/[{}$\\]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
const index = questions.map((q) => ({
  id: q.id,
  ch: q.ch,
  y: q.year,
  m: q.marks,
  t: q.type,
  c: q.code,
  n: `${q.qno}${q.part}`,
  q: q.question,
  o: q.options?.map((o) => o.t) ?? null,
  s: plain(q.topic + " " + q.question + " " + (q.options?.map((o) => o.t).join(" ") ?? "")),
}));
fs.writeFileSync(path.join(ROOT, "public/search-index.json"), JSON.stringify(index));
const skipped = papers.reduce((n, p) => n + p.items.filter((i) => i.kind === "skip").length, 0);
console.log(`bank: ${papers.length} papers, ${questions.length} questions, ${pending.length} duplicates merged, ${skipped} out-of-syllabus skipped`);
