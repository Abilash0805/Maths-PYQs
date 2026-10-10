// Parser for the question-bank source files in content/<year>/*.md (format: content/README.md)
import fs from "node:fs";
import path from "node:path";

import { CHAPTERS } from "../lib/chapters.ts";
export { CHAPTERS };
const CH_KEYS = new Set(CHAPTERS.map((c) => c.key));
const TYPES = new Set(["mcq", "ar", "sub", "case"]);

export function paperId(year, code) {
  return `${year}-${code.replace(/\//g, "-")}`;
}

function parseFrontMatter(lines, file) {
  if (lines[0] !== "---") throw new Error(`${file}: missing front matter`);
  const meta = {};
  let i = 1;
  for (; i < lines.length && lines[i] !== "---"; i++) {
    const m = lines[i].match(/^(\w+):\s*(.*)$/);
    if (m) meta[m[1]] = m[2].trim();
  }
  return { meta, next: i + 1 };
}

/** Parse one paper file into { meta, blocks, errors } */
export function parsePaper(file) {
  const text = fs.readFileSync(file, "utf8").replace(/\r\n/g, "\n");
  const lines = text.split("\n");
  const { meta, next } = parseFrontMatter(lines, file);
  const errors = [];
  const blocks = [];
  let cur = null;
  const year = Number(meta.year);
  const code = meta.code;
  for (let i = next; i < lines.length; i++) {
    const line = lines[i];
    const h = line.match(/^=== (\d+)([ab]?)\s*(.*)$/);
    if (h) {
      if (cur) blocks.push(cur);
      const qno = Number(h[1]);
      const part = h[2] || "";
      const rest = h[3].trim();
      cur = { file, line: i + 1, year, code, qno, part, raw: [] };
      if (rest.startsWith("=")) {
        cur.kind = "dup";
        const ref = rest.slice(1).trim();
        const m = ref.match(/^(?:(\d{4}):)?([^#\s]+)#(\d+[ab]?)$/);
        if (!m) errors.push(`${file}:${i + 1} bad dup ref '${ref}'`);
        else cur.ref = { year: m[1] ? Number(m[1]) : year, code: m[2], q: m[3] };
      } else if (rest.startsWith("x")) {
        cur.kind = "skip";
        cur.reason = rest.slice(1).trim();
        if (!cur.reason) errors.push(`${file}:${i + 1} skip without reason`);
      } else {
        cur.kind = "q";
        const f = rest.replace(/^\|/, "").split("|").map((s) => s.trim());
        const [ch, marks, type] = f;
        if (!CH_KEYS.has(ch)) errors.push(`${file}:${i + 1} bad chapter '${ch}'`);
        if (!/^\d+$/.test(marks || "")) errors.push(`${file}:${i + 1} bad marks '${marks}'`);
        if (!TYPES.has(type)) errors.push(`${file}:${i + 1} bad type '${type}'`);
        Object.assign(cur, { ch, marks: Number(marks), type });
      }
      continue;
    }
    if (cur) cur.raw.push({ text: line, line: i + 1 });
  }
  if (cur) blocks.push(cur);

  for (const b of blocks) {
    if (b.kind !== "q") {
      if (b.raw.some((r) => r.text.trim())) errors.push(`${file}:${b.line} text after dup/skip header`);
      continue;
    }
    b.topic = "";
    b.figs = [];
    const body = [];
    const sol = [];
    let inSol = false;
    for (const r of b.raw) {
      if (!inSol && body.length === 0 && r.text.startsWith("@topic ")) { b.topic = r.text.slice(7).trim(); continue; }
      if (!inSol && body.length === 0 && r.text.startsWith("@fig ")) { b.figs.push(r.text.slice(5).trim()); continue; }
      const a = r.text.match(/^--- ans\s*([A-D])?\s*$/);
      if (a && !inSol) { inSol = true; b.key = a[1] || null; continue; }
      (inSol ? sol : body).push(r.text);
    }
    if (!inSol) errors.push(`${file}:${b.line} Q${b.qno}${b.part} has no '--- ans' section`);
    // options for mcq / ar
    b.options = null;
    let qtext = body;
    if (b.type === "mcq" || b.type === "ar") {
      const firstOpt = body.findIndex((l) => /^\(A\)\s/.test(l));
      if (firstOpt === -1) errors.push(`${file}:${b.line} Q${b.qno} mcq without options`);
      else {
        const optLines = body.slice(firstOpt).filter((l) => l.trim());
        const opts = [];
        for (const l of optLines) {
          const m = l.match(/^\(([A-D])\)\s+(.*)$/);
          if (m) opts.push({ k: m[1], t: m[2] });
          else if (opts.length) opts[opts.length - 1].t += "\n" + l;
        }
        if (opts.length !== 4) errors.push(`${file}:${b.line} Q${b.qno} has ${opts.length} options`);
        b.options = opts;
        qtext = body.slice(0, firstOpt);
      }
      if (!b.key) errors.push(`${file}:${b.line} Q${b.qno} mcq without answer key`);
    }
    b.question = trimBlank(qtext).join("\n");
    b.solution = trimBlank(sol).join("\n");
    if (!b.question) errors.push(`${file}:${b.line} Q${b.qno} empty question`);
    if (!b.solution) errors.push(`${file}:${b.line} Q${b.qno} empty solution`);
    delete b.raw;
  }
  return { meta, blocks, errors };
}

function trimBlank(arr) {
  let s = 0, e = arr.length;
  while (s < e && !arr[s].trim()) s++;
  while (e > s && !arr[e - 1].trim()) e--;
  return arr.slice(s, e);
}

export function listPaperFiles(root) {
  const out = [];
  for (const y of fs.readdirSync(root).sort()) {
    const d = path.join(root, y);
    if (!/^\d{4}$/.test(y) || !fs.statSync(d).isDirectory()) continue;
    for (const f of fs.readdirSync(d).sort()) if (f.endsWith(".md")) out.push(path.join(d, f));
  }
  return out;
}

/** Extract all math snippets (for validation) from a markdown-ish body */
export function mathSnippets(s) {
  const out = [];
  const re = /\$\$([\s\S]+?)\$\$|\$([^$\n]+?)\$/g;
  let m;
  while ((m = re.exec(s))) out.push({ tex: m[1] ?? m[2], display: !!m[1] });
  return out;
}
