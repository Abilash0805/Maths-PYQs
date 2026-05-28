import { getImportantQuestions, getFrequentlyRepeatedQuestions } from "@/lib/data";
import { QuestionList } from "@/components/QuestionList";
import { Star, TrendingUp } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export const metadata = {
  title: "Important Questions — CBSE Class 12 Maths PYQ",
};

export default function ImportantPage() {
  const important = getImportantQuestions();
  const repeated = getFrequentlyRepeatedQuestions();

  return (
    <div className="px-4 sm:px-6 lg:px-8 py-6 max-w-4xl mx-auto space-y-8">
      {/* Important questions (5-mark) */}
      <div>
        <div className="flex items-center gap-3 mb-5">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-amber-400 to-orange-500 text-white">
            <Star className="size-5" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-slate-900 dark:text-white">Important Questions</h1>
            <p className="text-sm text-slate-500 dark:text-slate-400">
              Long answer (5-mark) and marked important questions
            </p>
          </div>
          <Badge variant="warning" className="ml-auto">{important.length}</Badge>
        </div>

        <QuestionList
          questions={important}
          showChapter={true}
          emptyMessage="No important questions found"
        />
      </div>

      {/* Frequently repeated */}
      {repeated.length > 0 && (
        <div>
          <div className="flex items-center gap-3 mb-5">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-rose-500 to-pink-600 text-white">
              <TrendingUp className="size-5" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-slate-900 dark:text-white">Frequently Repeated</h2>
              <p className="text-sm text-slate-500 dark:text-slate-400">
                Questions that appeared in multiple years
              </p>
            </div>
            <Badge variant="destructive" className="ml-auto">{repeated.length}</Badge>
          </div>

          <QuestionList
            questions={repeated}
            showChapter={true}
            emptyMessage="No repeated questions found"
          />
        </div>
      )}
    </div>
  );
}
