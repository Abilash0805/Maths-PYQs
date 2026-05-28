import { getAllQuestions } from "@/lib/data";
import { QuestionList } from "@/components/QuestionList";
import { Search } from "lucide-react";

export const metadata = {
  title: "Search Questions — CBSE Class 12 Maths PYQ",
};

export default function SearchPage() {
  const questions = getAllQuestions();

  return (
    <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-4xl mx-auto space-y-6">
      <div className="flex items-center gap-3">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 text-white">
          <Search className="size-5" />
        </div>
        <div>
          <h1 className="text-xl font-bold text-slate-900">Search Questions</h1>
          <p className="text-sm text-slate-500">
            Search across all {questions.length} questions
          </p>
        </div>
      </div>

      <QuestionList
        questions={questions}
        showChapter={true}
        emptyMessage="No questions match your search"
      />
    </div>
  );
}
