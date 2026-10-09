import type { Metadata } from "next";
import { SavedClient } from "@/components/SavedClient";

export const metadata: Metadata = { title: "Saved questions", description: "Questions you bookmarked for revision." };

export default function SavedPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 pt-12 sm:px-6">
      <header className="mb-8">
        <p className="font-mono text-xs uppercase tracking-[0.16em] text-primary">Revision list</p>
        <h1 className="mt-2 text-4xl font-semibold sm:text-5xl">Saved questions</h1>
        <p className="mt-3 text-lg text-ink-2">Questions you save are stored on this device only.</p>
      </header>
      <SavedClient />
    </div>
  );
}
