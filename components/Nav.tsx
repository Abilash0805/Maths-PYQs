"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import { Menu, X } from "lucide-react";

type Item = { href: string; label: string };

const isActive = (path: string, href: string) => path === href || path.startsWith(href + "/");

export function NavLinks({ items }: { items: Item[] }) {
  const path = usePathname();
  return (
    <nav aria-label="Main" className="ml-6 hidden md:block">
      <ul className="flex items-center gap-1">
        {items.map((it) => {
          const active = isActive(path, it.href);
          return (
            <li key={it.href} className="relative">
              <Link
                href={it.href}
                aria-current={active ? "page" : undefined}
                className={`relative z-10 block rounded-lg px-3 py-2 text-[0.95rem] transition-colors ${active ? "text-ink" : "text-ink-2 hover:text-ink"}`}
              >
                {it.label}
              </Link>
              {active && (
                <motion.span
                  layoutId="nav-pill"
                  className="absolute inset-0 rounded-lg bg-surface-2"
                  transition={{ type: "spring", stiffness: 420, damping: 34 }}
                />
              )}
            </li>
          );
        })}
      </ul>
    </nav>
  );
}

export function MobileNav({ items }: { items: Item[] }) {
  const [open, setOpen] = useState(false);
  const path = usePathname();
  // close the drawer whenever the route changes
  const [lastPath, setLastPath] = useState(path);
  if (path !== lastPath) {
    setLastPath(path);
    setOpen(false);
  }
  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    window.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [open]);

  return (
    <div className="md:hidden">
      <button
        type="button"
        aria-label={open ? "Close menu" : "Open menu"}
        aria-expanded={open}
        aria-controls="mobile-nav"
        onClick={() => setOpen((o) => !o)}
        className="grid size-11 cursor-pointer place-items-center rounded-xl text-ink-2 hover:bg-surface-2 hover:text-ink"
      >
        {open ? <X className="size-5" aria-hidden /> : <Menu className="size-5" aria-hidden />}
      </button>
      <AnimatePresence>
        {open && (
          <>
            <motion.div
              className="fixed inset-0 top-16 z-40 bg-ink/20 backdrop-blur-[2px]"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setOpen(false)}
            />
            <motion.nav
              id="mobile-nav"
              aria-label="Main"
              className="fixed inset-x-3 top-[4.5rem] z-50 rounded-2xl border border-line bg-surface p-2 shadow-card"
              initial={{ opacity: 0, y: -12, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -8, scale: 0.98, transition: { duration: 0.15 } }}
              transition={{ type: "spring", stiffness: 380, damping: 30 }}
            >
              <ul>
                {items.map((it, i) => (
                  <motion.li key={it.href} initial={{ opacity: 0, x: -8 }} animate={{ opacity: 1, x: 0, transition: { delay: 0.03 * i } }}>
                    <Link
                      href={it.href}
                      aria-current={isActive(path, it.href) ? "page" : undefined}
                      className="flex min-h-12 items-center rounded-xl px-4 text-lg text-ink aria-[current=page]:bg-surface-2 aria-[current=page]:font-bold"
                    >
                      {it.label}
                    </Link>
                  </motion.li>
                ))}
              </ul>
            </motion.nav>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}
