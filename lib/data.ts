import pyqsData from "@/public/data/pyqs.json";
import { PYQItem, CHAPTERS } from "./types";

const rawData = pyqsData as PYQItem[];

export function getAllQuestions(): PYQItem[] {
  return rawData;
}

export function getQuestionsByChapter(chapter: string): PYQItem[] {
  return rawData.filter((q) => q.chapter === chapter);
}

export function getQuestionsByYear(year: number): PYQItem[] {
  return rawData.filter((q) => q.year === year);
}

export function getChapterStats() {
  return CHAPTERS.map((chapter) => {
    const questions = getQuestionsByChapter(chapter);
    const years = [...new Set(questions.map((q) => q.year))].sort((a, b) => b - a);
    return {
      chapter,
      total: questions.length,
      years,
      important: questions.filter((q) => q.is_important).length,
    };
  });
}

export function getAvailableYears(): number[] {
  const years = [...new Set(rawData.map((q) => q.year))];
  return years.sort((a, b) => b - a);
}

export function searchQuestions(query: string): PYQItem[] {
  const q = query.toLowerCase();
  return rawData.filter(
    (item) =>
      item.question.toLowerCase().includes(q) ||
      item.answer.toLowerCase().includes(q) ||
      item.chapter.toLowerCase().includes(q)
  );
}

export function getFrequentlyRepeatedQuestions(): PYQItem[] {
  const seen = new Map<string, number>();
  rawData.forEach((q) => {
    const key = q.question.substring(0, 80).toLowerCase().trim();
    seen.set(key, (seen.get(key) || 0) + 1);
  });
  return rawData.filter((q) => {
    const key = q.question.substring(0, 80).toLowerCase().trim();
    return (seen.get(key) || 0) >= 2;
  });
}

export function getImportantQuestions(): PYQItem[] {
  return rawData.filter((q) => q.is_important || q.marks >= 5);
}
