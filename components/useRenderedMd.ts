"use client";

import { useEffect, useState } from "react";

type Renderer = (src: string) => string;
let loader: Promise<Renderer> | null = null;

/** Loads KaTeX + the markdown renderer on first use (keeps them out of the initial bundle). */
export function loadRenderer(): Promise<Renderer> {
  loader ??= Promise.all([import("katex"), import("@/lib/md")]).then(([k, md]) => {
    const katex = (k as unknown as { default: Parameters<typeof md.renderMarkdown>[1] }).default ?? k;
    return (src: string) => md.renderMarkdown(src, katex);
  });
  return loader;
}

export function useRenderedMd(src: string | null) {
  const [html, setHtml] = useState<{ src: string; html: string } | null>(null);
  useEffect(() => {
    if (src == null) return;
    let alive = true;
    loadRenderer().then((render) => alive && setHtml({ src, html: render(src) }));
    return () => {
      alive = false;
    };
  }, [src]);
  return html && html.src === src ? html.html : null;
}
