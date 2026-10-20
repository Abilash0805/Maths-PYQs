import Link from "next/link";
import { Md } from "./Md";
import { CardShell } from "./CardShell";
import type { Question } from "@/lib/bank";
import { chapterByKey, TYPE_LABEL, unitOf } from "@/lib/chapters";

const marksLabel = (m: number) => `${m} mark${m === 1 ? "" : "s"}`;

export function QuestionMeta({ q, showChapter }: { q: Question; showChapter?: boolean }) {
  const ch = chapterByKey(q.ch);
  return (
    <div className="flex flex-wrap items-center gap-x-2 gap-y-1.5 text-sm">
      <span className="font-mono text-[0.8rem] tracking-tight text-ink-2">
        {q.year} · {q.code} · Q{q.qno}
        {q.part && <span className="text-muted">{q.part === "a" ? " (a)" : " (b)"}</span>}
      </span>
      <span className="rounded-full bg-accent-soft px-2.5 py-0.5 text-[0.8rem] font-bold text-accent">{marksLabel(q.marks)}</span>
      <span className="rounded-full border border-line px-2.5 py-0.5 text-[0.8rem] text-ink-2">{TYPE_LABEL[q.type]}</span>
      {showChapter && (
        <Link
          href={`/chapters/${ch.slug}`}
          className={`hue-${unitOf(ch).hue} rounded-full bg-[var(--hue-soft)] px-2.5 py-0.5 text-[0.8rem] font-bold text-[var(--hue)] hover:underline`}
        >
          {ch.name}
        </Link>
      )}
    </div>
  );
}

function Figures({ q }: { q: Question }) {
  return q.figs.map((f) => (
    <figure key={f.src} className="my-4 overflow-hidden rounded-xl border border-line bg-white p-2 sm:p-3">
      {/* eslint-disable-next-line @next/next/no-img-element -- static figure with known dimensions */}
      <img src={f.src} width={f.w} height={f.h} alt={`Figure for ${q.year} ${q.code} question ${q.qno}`} loading="lazy" className="mx-auto h-auto max-h-[19rem] w-auto max-w-full" />
    </figure>
  ));
}

/** Splits the statement so figures sit where the paper puts them: at a `[[fig]]` line, after the
 * opening passage of a case study, or after the statement otherwise. */
function splitForFigure(q: Question): [string, string] {
  const marker = q.question.split(/\n\[\[fig\]\]\n/);
  if (marker.length === 2) return [marker[0], marker[1]];
  if (q.figs.length && q.type === "case") {
    const i = q.question.indexOf("\n\n");
    if (i > 0) return [q.question.slice(0, i), q.question.slice(i + 2)];
  }
  return [q.question, ""];
}

export function QuestionBody({ q }: { q: Question }) {
  const [before, after] = splitForFigure(q);
  return (
    <>
      <Md src={before} className="text-[1.03rem] leading-relaxed" />
      <Figures q={q} />
      {after && <Md src={after} className="text-[1.03rem] leading-relaxed" />}
      {q.options && (
        <ol className={`mt-4 grid gap-2 ${q.type === "ar" ? "" : "sm:grid-cols-2"}`} aria-label="Options">
          {q.options.map((o) => (
            <li key={o.k} className="opt flex items-start gap-3 rounded-xl border border-line bg-surface px-3 py-2.5 transition-colors" data-correct={o.k === q.key}>
              <span className="opt-key mt-0.5 grid size-7 shrink-0 place-items-center rounded-lg bg-surface-2 font-mono text-sm font-medium text-ink-2 transition-colors">
                {o.k}
              </span>
              <Md src={o.t} className="min-w-0 pt-0.5" />
            </li>
          ))}
        </ol>
      )}
    </>
  );
}

export function QuestionCard({ q, showChapter = false, linkTitle = true }: { q: Question; showChapter?: boolean; linkTitle?: boolean }) {
  const repeats = q.sources.slice(1);
  return (
    <article id={q.id} data-reveal className="qcard rounded-2xl border border-line bg-surface p-4 shadow-card sm:p-6">
      <CardShell id={q.id} solution={q.solution} answerKey={q.key} permalink={linkTitle ? `/q/${q.id}` : null}>
        <QuestionMeta q={q} showChapter={showChapter} />
        {q.topic && <p className="mt-1.5 text-sm text-muted">{q.topic}</p>}
        <div className="mt-4">
          <QuestionBody q={q} />
        </div>
        {repeats.length > 0 && (
          <p className="mt-4 text-sm text-muted">
            <span className="font-bold text-ink-2">Also asked in:</span>{" "}
            {repeats.map((s, i) => (
              <span key={`${s.year}${s.code}${s.q}`} className="font-mono text-[0.8rem]">
                {i > 0 && ", "}
                {s.year} {s.code} Q{s.q}
              </span>
            ))}
          </p>
        )}
      </CardShell>
    </article>
  );
}
