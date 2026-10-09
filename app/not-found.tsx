import Link from "next/link";

export default function NotFound() {
  return (
    <div className="mx-auto max-w-xl px-4 py-24 text-center">
      <p className="font-display text-7xl font-semibold text-primary">∄</p>
      <h1 className="mt-4 text-3xl font-semibold">This page does not exist</h1>
      <p className="mt-2 text-ink-2">The link may be old, or the question may have moved.</p>
      <div className="mt-8 flex justify-center gap-3">
        <Link href="/chapters" className="inline-flex min-h-11 items-center rounded-xl bg-primary px-4 font-bold text-primary-ink">
          Browse chapters
        </Link>
        <Link href="/search" className="inline-flex min-h-11 items-center rounded-xl border border-line-strong px-4 font-bold">
          Search
        </Link>
      </div>
    </div>
  );
}
