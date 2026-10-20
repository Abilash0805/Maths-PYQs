"use client";

import { useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger, useGSAP);

/** Counts from 0 to `value` when scrolled into view; renders the final value for SSR and reduced motion. */
export function CountUp({ value, className }: { value: number; className?: string }) {
  const ref = useRef<HTMLSpanElement>(null);
  useGSAP(
    () => {
      const el = ref.current;
      if (!el) return;
      const mm = gsap.matchMedia();
      mm.add("(prefers-reduced-motion: no-preference)", () => {
        const o = { v: 0 };
        el.textContent = "0";
        gsap.to(o, {
          v: value,
          duration: 1.4,
          ease: "power2.out",
          scrollTrigger: { trigger: el, start: "top 95%", once: true },
          onUpdate: () => {
            el.textContent = Math.round(o.v).toLocaleString("en-IN");
          },
        });
        return () => {
          el.textContent = value.toLocaleString("en-IN");
        };
      });
      return () => mm.revert();
    },
    { dependencies: [value] },
  );
  return (
    <span ref={ref} className={className}>
      {value.toLocaleString("en-IN")}
    </span>
  );
}
