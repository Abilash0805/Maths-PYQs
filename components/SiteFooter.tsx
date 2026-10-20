import Link from "next/link";
import { LogoMark } from "./Logo";

export function SiteFooter() {
  return (
    <footer className="mt-24 border-t border-line bg-surface/60">
      <div className="mx-auto grid max-w-6xl gap-8 px-4 py-12 sm:px-6 md:grid-cols-[1.4fr_1fr_1fr]">
        <div>
          <div className="flex items-center gap-2.5">
            <LogoMark className="size-8" />
            <span className="font-display text-lg font-semibold">Maths PYQs</span>
          </div>
          <p className="mt-3 max-w-md text-[0.95rem] text-muted">
            Questions are transcribed from official CBSE Class XII Mathematics (041) question papers, marking schemes and
            solved papers (2015–2026). Only questions within the 2026-27 syllabus are included. Solutions are written to
            match CBSE marking-scheme steps.
          </p>
          <p className="mt-4 text-sm text-muted">Built by Abilash</p>
        </div>
        <nav aria-label="Footer">
          <h2 className="font-mono text-xs uppercase tracking-[0.16em] text-muted">Practice</h2>
          <ul className="mt-3 space-y-2 text-[0.95rem]">
            <li><Link className="text-ink-2 hover:text-primary" href="/chapters">All chapters</Link></li>
            <li><Link className="text-ink-2 hover:text-primary" href="/papers">Year-wise papers</Link></li>
            <li><Link className="text-ink-2 hover:text-primary" href="/search">Search questions</Link></li>
            <li><Link className="text-ink-2 hover:text-primary" href="/saved">Saved questions</Link></li>
          </ul>
        </nav>
        <div>
          <h2 className="font-mono text-xs uppercase tracking-[0.16em] text-muted">About</h2>
          <ul className="mt-3 space-y-2 text-[0.95rem]">
            <li><Link className="text-ink-2 hover:text-primary" href="/syllabus">2026-27 syllabus &amp; exclusions</Link></li>
          </ul>
        </div>
      </div>
    </footer>
  );
}
