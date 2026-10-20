import Link from "next/link";
import { LogoMark } from "./Logo";
import { NavLinks, MobileNav } from "./Nav";
import { ThemeToggle } from "./ThemeToggle";

export const NAV = [
  { href: "/chapters", label: "Chapters" },
  { href: "/papers", label: "Papers" },
  { href: "/search", label: "Search" },
  { href: "/saved", label: "Saved" },
  { href: "/syllabus", label: "Syllabus" },
];

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-40 border-b border-line/80 bg-bg/80 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-6xl items-center gap-3 px-4 sm:px-6">
        <Link href="/" className="flex items-center gap-2.5 rounded-xl pr-2" aria-label="Class 12 Maths PYQs — home">
          <LogoMark />
          <span className="leading-tight">
            <span className="block font-display text-[1.15rem] font-semibold text-ink">Maths PYQs</span>
            <span className="block font-mono text-[0.68rem] uppercase tracking-[0.14em] text-muted">CBSE Class XII</span>
          </span>
        </Link>
        <NavLinks items={NAV} />
        <div className="ml-auto flex items-center gap-1">
          <ThemeToggle />
          <MobileNav items={NAV} />
        </div>
      </div>
    </header>
  );
}
