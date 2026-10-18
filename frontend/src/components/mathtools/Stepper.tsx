import katex from "katex";
import { ChevronLeft, ChevronRight, List, RotateCcw } from "lucide-react";
import { useMemo, useState } from "react";
import { Markdown } from "../Markdown";

/*
 * ```steps fence: an equation that transforms one step at a time.
 *
 *   title "Separate, then integrate"        optional first line
 *   $$ \dfrac{dy}{dt}=ty $$                 a step's equation (one line, or $$ ... $$ over several lines)
 *   Start from the equation.                the note under it (Markdown, inline $math$), until the next $$
 *   $$ \hl{\dfrac{1}{y}}\,dy=\hl{t\,dt} $$   \hl{...} highlights what changed in this step
 *   Divide by $y$ and multiply by $dt$.
 */

export type StepperSpec = { title?: string; steps: { latex: string; note: string }[] };

export function parseStepper(source: string): StepperSpec {
  const lines = source.split(/\r?\n/);
  const spec: StepperSpec = { steps: [] };
  let i = 0;
  while (i < lines.length && !lines[i].trim()) i++;
  const head = /^title\s+"(.*)"\s*$/.exec(lines[i]?.trim() ?? "");
  if (head) {
    spec.title = head[1];
    i++;
  }
  for (; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith("$$")) {
      let body = line.slice(2);
      while (!body.trimEnd().endsWith("$$") && i + 1 < lines.length) body += "\n" + lines[++i];
      if (!body.trimEnd().endsWith("$$")) throw new Error("a $$ equation is not closed");
      spec.steps.push({ latex: body.trimEnd().slice(0, -2).trim(), note: "" });
    } else if (line) {
      const last = spec.steps[spec.steps.length - 1];
      if (!last) throw new Error("text before the first $$ equation");
      last.note = last.note ? `${last.note}\n${line}` : line;
    }
  }
  if (!spec.steps.length) throw new Error("no $$ equations");
  return spec;
}

const MACROS = { "\\hl": "\\htmlClass{mt-hl}{#1}" };

export function texHtml(latex: string, display = true) {
  return katex.renderToString(latex, {
    displayMode: display,
    throwOnError: false,
    strict: "ignore",
    macros: { ...MACROS },
    trust: (ctx) => ctx.command === "\\htmlClass" && ctx.class === "mt-hl",
  });
}

export function Stepper({ source }: { source: string }) {
  const parsed = useMemo(() => {
    try {
      return { spec: parseStepper(source) };
    } catch (e) {
      return { error: (e as Error).message };
    }
  }, [source]);
  const [k, setK] = useState(0);
  const [all, setAll] = useState(false);
  const html = useMemo(() => parsed.spec?.steps.map((s) => texHtml(s.latex)) ?? [], [parsed]);
  if (!parsed.spec) return <ToolError kind="steps" message={parsed.error!} source={source} />;
  const { steps, title } = parsed.spec;
  const n = steps.length;
  const go = (d: number) => setK((v) => Math.min(n - 1, Math.max(0, v + d)));

  return (
    <div
      className="mt-card mt-stepper"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === "ArrowRight") go(1);
        else if (e.key === "ArrowLeft") go(-1);
        else return;
        e.preventDefault();
      }}
    >
      <div className="mt-head">
        <span className="mt-title">{title && <Markdown text={title} inline />}</span>
        <button className={`mt-icon ${all ? "active" : ""}`} onClick={() => setAll(!all)} title={all ? "One step at a time" : "Show every step"}>
          <List size={15} />
        </button>
      </div>
      {all ? (
        <ol className="mt-all">
          {steps.map((s, i) => (
            <li key={i}>
              <div className="mt-eq" dangerouslySetInnerHTML={{ __html: html[i] }} />
              {s.note && (
                <div className="mt-note">
                  <Markdown text={s.note} />
                </div>
              )}
            </li>
          ))}
        </ol>
      ) : (
        <>
          <div className="mt-stage">
            {/* Shared grid rows reserve space for each equation and the note
                separately, keeping the note and controls in fixed positions. */}
            {steps.map((s, i) => (
              <div key={i} className={`mt-step ${i === k ? "mt-active" : ""}`} aria-hidden={i !== k} inert={i !== k}>
                {i > 0 && <div className="mt-eq mt-prev" dangerouslySetInnerHTML={{ __html: html[i - 1] }} />}
                {i > 0 && <div className="mt-arrow">↓</div>}
                <div className={`mt-eq mt-current ${i === k ? "mt-fade" : ""}`} dangerouslySetInnerHTML={{ __html: html[i] }} />
                <div className="mt-note">
                  {s.note ? <Markdown text={s.note} /> : null}
                </div>
              </div>
            ))}
          </div>
          <div className="mt-nav">
            <button className="mt-btn" onClick={() => go(-1)} disabled={k === 0}>
              <ChevronLeft size={16} /> Back
            </button>
            <div className="mt-dots" aria-label={`Step ${k + 1} of ${n}`}>
              {steps.map((_, i) => (
                <button key={i} className={`mt-dot ${i === k ? "on" : i < k ? "done" : ""}`} onClick={() => setK(i)} aria-label={`Step ${i + 1}`} />
              ))}
            </div>
            {k < n - 1 ? (
              <button className="mt-btn mt-primary" onClick={() => go(1)}>
                Next <ChevronRight size={16} />
              </button>
            ) : (
              <button className="mt-btn" onClick={() => setK(0)}>
                <RotateCcw size={14} /> Again
              </button>
            )}
          </div>
        </>
      )}
    </div>
  );
}

export function ToolError({ kind, message, source }: { kind: string; message: string; source: string }) {
  return (
    <figure className="mt-card mt-error">
      <figcaption>
        The {kind} tool could not be drawn: {message}
      </figcaption>
      <pre>
        <code>{source}</code>
      </pre>
    </figure>
  );
}
