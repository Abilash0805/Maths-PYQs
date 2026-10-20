import katex from "katex";
import { renderMarkdown } from "@/lib/md";

/** Server-rendered maths markdown (questions, options, full solutions on question pages). */
export function Md({ src, className = "", as: Tag = "div" }: { src: string; className?: string; as?: "div" | "span" }) {
  return <Tag className={`md ${className}`} dangerouslySetInnerHTML={{ __html: renderMarkdown(src, katex) }} />;
}
