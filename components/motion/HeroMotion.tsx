"use client";

import { useRef, type ReactNode } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger, SplitText, useGSAP);

/**
 * Intro choreography for the home hero: headline words rise in, supporting copy and the preview card
 * follow, preview solution lines write in one by one, and the background glyphs drift on scroll.
 */
export function HeroMotion({ children, className }: { children: ReactNode; className?: string }) {
  const ref = useRef<HTMLDivElement>(null);
  useGSAP(
    () => {
      const mm = gsap.matchMedia();
      mm.add("(prefers-reduced-motion: no-preference)", () => {
        const split = SplitText.create("[data-hero-title]", { type: "words", mask: "words" });
        const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
        tl.from("[data-hero-eyebrow]", { y: 12, autoAlpha: 0, duration: 0.5 })
          .from(split.words, { yPercent: 110, duration: 0.8, stagger: 0.05 }, "-=0.2")
          .from("[data-hero-copy]", { y: 16, autoAlpha: 0, duration: 0.6 }, "-=0.45")
          .from("[data-hero-cta] > *", { y: 14, autoAlpha: 0, duration: 0.5, stagger: 0.08 }, "-=0.35")
          .from("[data-hero-card]", { y: 40, rotate: -1.5, autoAlpha: 0, duration: 0.9, ease: "expo.out" }, 0.35)
          .from("[data-hero-line]", { x: -10, autoAlpha: 0, duration: 0.45, stagger: 0.32 }, "-=0.2")
          .from("[data-hero-check]", { scale: 0.4, autoAlpha: 0, duration: 0.5, ease: "back.out(2.2)" }, "-=0.1");

        gsap.utils.toArray<HTMLElement>("[data-glyph]").forEach((g, i) => {
          gsap.to(g, {
            yPercent: (i % 2 ? -1 : 1) * (40 + i * 12),
            rotate: (i % 2 ? -1 : 1) * 12,
            ease: "none",
            scrollTrigger: { trigger: ref.current, start: "top top", end: "bottom top", scrub: 0.6 },
          });
        });
        return () => split.revert();
      });
      return () => mm.revert();
    },
    { scope: ref },
  );
  return (
    <div ref={ref} className={className}>
      {children}
    </div>
  );
}
