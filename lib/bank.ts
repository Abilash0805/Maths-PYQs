// Server-side access to the compiled question bank (data/bank.json, built by scripts/build-data.mjs).
import "server-only";
import bankJson from "@/data/bank.json";
import type { ChapterKey } from "./chapters";

export type Fig = { src: string; w: number; h: number };
export type Source = { year: number; code: string; q: string };
export type Question = {
  id: string;
  ch: ChapterKey;
  marks: number;
  type: "mcq" | "ar" | "sub" | "case";
  topic: string;
  year: number;
  code: string;
  paper: string;
  qno: number;
  part: string;
  question: string;
  options: { k: string; t: string }[] | null;
  key: string | null;
  solution: string;
  figs: Fig[];
  sources: Source[];
};
export type PaperItem = { n: string; kind: "q" | "dup" | "skip"; id?: string; ref?: string; reason?: string };
export type Paper = { id: string; year: number; code: string; series: string; title: string; source: string; total: number; items: PaperItem[] };

const bank = bankJson as unknown as { papers: Paper[]; questions: Question[] };

export const questions: Question[] = bank.questions;
export const papers: Paper[] = bank.papers;
const byId = new Map(questions.map((q) => [q.id, q]));

export const getQuestion = (id: string) => byId.get(id);
export const questionsIn = (ch: string) => questions.filter((q) => q.ch === ch);
export const getPaper = (id: string) => papers.find((p) => p.id === id);
export const years = [...new Set(papers.map((p) => p.year))].sort((a, b) => b - a);

export function stats() {
  const skipped = papers.reduce((n, p) => n + p.items.filter((i) => i.kind === "skip").length, 0);
  const repeats = questions.reduce((n, q) => n + q.sources.length - 1, 0);
  return { questions: questions.length, papers: papers.length, years: years.length, skipped, repeats };
}

export function chapterStats(ch: string) {
  const qs = questionsIn(ch);
  const byMarks: Record<number, number> = {};
  for (const q of qs) byMarks[q.marks] = (byMarks[q.marks] ?? 0) + 1;
  const topics = new Map<string, number>();
  for (const q of qs) if (q.topic) topics.set(q.topic, (topics.get(q.topic) ?? 0) + 1);
  const topTopics = [...topics.entries()].sort((a, b) => b[1] - a[1]).slice(0, 4).map(([t]) => t);
  const yrs = [...new Set(qs.map((q) => q.year))].sort((a, b) => b - a);
  return { count: qs.length, byMarks, topTopics, years: yrs };
}

export const sourceLabel = (s: Source) => `${s.year} · ${s.code} · Q${s.q}`;
