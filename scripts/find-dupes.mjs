// Report questions that look identical across different papers but are not yet linked as duplicates.
// usage: node --no-warnings scripts/find-dupes.mjs [threshold=0.93]
import path from "node:path";
import { parsePaper, listPaperFiles } from "./content.mjs";

const ROOT = path.resolve(import.meta.dirname, "..");
const threshold = Number(process.argv[2] ?? 0.93);
const norm = (s) =>
  s
    .replace(/\\(dfrac|tfrac)/g, "\\frac")
    .replace(/\\(displaystyle|left|right|,|;|!|quad|qquad)/g, "")
    .replace(/\*\*\[\d\]\*\*/g, "")
    .replace(/[\s{}$*.,:;?]/g, "")
    .toLowerCase();

const items = [];
for (const f of listPaperFiles(path.join(ROOT, "content"))) {
  const { meta, blocks } = parsePaper(f);
  for (const b of blocks)
    if (b.kind === "q")
      items.push({ ref: `${meta.year}:${meta.code}#${b.qno}${b.part}`, year: Number(meta.year), code: meta.code, ch: b.ch, n: norm(b.question + (b.options ?? []).map((o) => o.t).join("|")) });
}

// bigram Dice similarity
const grams = (s) => {
  const m = new Map();
  for (let i = 0; i < s.length - 1; i++) {
    const g = s.slice(i, i + 2);
    m.set(g, (m.get(g) ?? 0) + 1);
  }
  return m;
};
for (const it of items) it.g = grams(it.n);
const dice = (a, b) => {
  let inter = 0;
  for (const [g, c] of a.g) inter += Math.min(c, b.g.get(g) ?? 0);
  return (2 * inter) / Math.max(1, a.n.length - 1 + b.n.length - 1);
};

let found = 0;
for (let i = 0; i < items.length; i++)
  for (let j = i + 1; j < items.length; j++) {
    const a = items[i], b = items[j];
    if (a.code === b.code && a.year === b.year) continue;
    if (a.ch !== b.ch) continue;
    const r = Math.min(a.n.length, b.n.length) / Math.max(a.n.length, b.n.length);
    if (r < 0.85) continue;
    const d = dice(a, b);
    if (d >= threshold) {
      found++;
      console.log(`${d.toFixed(3)}  ${a.ref}  <->  ${b.ref}${a.n === b.n ? "   [identical]" : ""}`);
    }
  }
console.log(`${found} candidate pair(s) at threshold ${threshold}`);
