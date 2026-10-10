import type { Metadata } from "next";
import { SearchClient } from "@/components/SearchClient";

export const metadata: Metadata = {
  title: "Search questions",
  description: "Search every CBSE Class XII Mathematics board question by keyword, chapter, marks and year.",
};

export default function SearchPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 pt-12 sm:px-6">
      <header className="mb-8">
        <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Search</p>
        <h1 className="mt-2 text-4xl font-semibold sm:text-5xl">Find a question</h1>
        <p className="mt-3 text-lg text-ink-2">Type a word from the question, a topic (&ldquo;Bayes&rdquo;, &ldquo;skew lines&rdquo;) or a paper code like 65/1/1.</p>
      </header>
      <SearchClient />
    </div>
  );
}
