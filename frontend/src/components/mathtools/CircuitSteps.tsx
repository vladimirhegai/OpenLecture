import { ChevronLeft, ChevronRight, List, RotateCcw } from "lucide-react";
import { useEffect, useMemo, useRef, useState } from "react";
import { arrowHead, loadSvg, meshGeometry, useAutoLayout, wrapPart, type Box, type Parsed } from "./svgLayout";
import { drawingOnly } from "../Elevation";
import { Markdown } from "../Markdown";
import { texHtml, ToolError } from "./Stepper";

/*
 * ```circuitsteps fence: a circuit that transforms one step at a time, with notes under each step.
 *
 *   title "Find $V_o$ with Thévenin"         optional first line
 *   == Pull out the load                      starts a step (its title, Markdown)
 *   V1 0,3 -> 3,3 "$6\,\mathrm{V}$"           the step's whole drawing (schematic language)
 *   #= mesh 1.5,1.5 "$I_1$" ccw               optional overlays drawn on top (grid points, see below)
 *   --                                        ends the drawing
 *   Notes for this step (Markdown, $math$, lists, blank lines) until the next ==
 *
 * Overlays (every one takes color=purple|pink|blue|green|orange|accent):
 *   #= mesh CX,CY "$I_1$" cw|ccw r=0.9        mesh-current loop arrow with its name in the middle
 *   #= path X,Y -> X,Y -> ... "label" [thin]  thick arrow along wires: a KVL walk or where a current flows
 *   #= sign X,Y +|-                           polarity box (+ blue, − pink)
 *   #= text X,Y "$2\,\mathrm{V}$"             a callout (Markdown/LaTeX), centred on the point
 *   #= region X0,Y0 X1,Y1 "supernode"         dashed box (supernode, supermesh, "the part we replace")
 *
 * Values found:  #+ $I_1=1\,\mathrm{mA}$     goes in the "Found so far" panel beside the circuit from this
 *                                           step on (highlighted in the step that finds it)
 *
 * Each step is compared with the previous one: drawing parts that appear fade in and stay
 * highlighted, parts that disappear flash red and fade out; new overlays draw themselves in.
 * All steps share one frame, so a part that does not change does not move.
 */

type Pt = [number, number];
type Overlay =
  | { kind: "mesh"; at: Pt; label: string; ccw: boolean; r: number; color: string }
  | { kind: "path"; pts: Pt[]; label: string; thin: boolean; color: string }
  | { kind: "sign"; at: Pt; plus: boolean; color: string }
  | { kind: "text"; at: Pt; label: string; color: string }
  | { kind: "region"; a: Pt; b: Pt; label: string; color: string };
type Step = { title: string; drawing: string; overlays: { key: string; o: Overlay }[]; values: string[]; notes: string };
export type CircuitStepsSpec = { title?: string; steps: Step[] };

const UNIT = 36; // the server draws one grid unit as 36 SVG units, with y pointing down
const COLORS = new Set(["purple", "pink", "blue", "green", "orange", "accent"]);

function tokenize(line: string) {
  const out: string[] = [];
  const re = /"((?:[^"\\]|\\.)*)"|(\S+)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(line))) out.push(m[1] !== undefined ? `"${m[1]}` : m[2]);
  return out; // quoted tokens keep a leading " so they can be told apart
}

function parseOverlay(line: string, no: number): Overlay {
  const t = tokenize(line.replace(/^#=\s*/, ""));
  const kind = t.shift();
  const pt = (s: string | undefined): Pt => {
    const m = /^(-?[\d.]+),(-?[\d.]+)$/.exec(s ?? "");
    if (!m) throw new Error(`line ${no}: expected a point X,Y, got "${s ?? ""}"`);
    return [Number(m[1]), Number(m[2])];
  };
  const label = t.find((s) => s.startsWith('"'))?.slice(1) ?? "";
  const opt = (k: string) => t.find((s) => s.startsWith(k + "="))?.slice(k.length + 1);
  const flag = (k: string) => t.includes(k);
  const color = opt("color") ?? "";
  if (color && !COLORS.has(color)) throw new Error(`line ${no}: unknown color "${color}"`);
  switch (kind) {
    case "mesh":
      if (!flag("cw") && !flag("ccw")) throw new Error(`line ${no}: mesh needs cw or ccw`);
      return { kind, at: pt(t[0]), label, ccw: flag("ccw"), r: Number(opt("r") ?? 0.9), color: color || "purple" };
    case "path": {
      const pts = t.filter((s) => /^-?[\d.]+,-?[\d.]+$/.test(s)).map(pt);
      if (pts.length < 2) throw new Error(`line ${no}: path needs at least two points (X,Y -> X,Y)`);
      return { kind, pts, label, thin: flag("thin"), color: color || "pink" };
    }
    case "sign":
      if (!flag("+") && !flag("-")) throw new Error(`line ${no}: sign needs + or -`);
      return { kind, at: pt(t[0]), plus: flag("+"), color };
    case "text":
      return { kind, at: pt(t[0]), label, color };
    case "region":
      return { kind, a: pt(t[0]), b: pt(t[1]), label, color: color || "accent" };
  }
  throw new Error(`line ${no}: unknown overlay "${kind ?? ""}" (mesh, path, sign, text, region)`);
}

export function parseCircuitSteps(source: string): CircuitStepsSpec {
  const lines = source.split(/\r?\n/);
  const spec: CircuitStepsSpec = { steps: [] };
  let i = 0;
  while (i < lines.length && !lines[i].trim()) i++;
  const head = /^title\s+"(.*)"\s*$/.exec(lines[i]?.trim() ?? "");
  if (head) {
    spec.title = head[1];
    i++;
  }
  let step: (Step & { inNotes: boolean; lines: string[]; noteLines: string[] }) | undefined;
  const finish = () => {
    if (!step) return;
    const drawing = step.lines.join("\n").trim();
    if (!drawingOnly(drawing)) throw new Error(`step "${step.title}" has no drawing`);
    spec.steps.push({ title: step.title, drawing, overlays: step.overlays, values: step.values, notes: step.noteLines.join("\n").trim() });
  };
  for (; i < lines.length; i++) {
    const raw = lines[i];
    const line = raw.trim();
    if (line.startsWith("==")) {
      finish();
      step = { title: line.slice(2).trim(), drawing: "", overlays: [], values: [], notes: "", inNotes: false, lines: [], noteLines: [] };
    } else if (!step) {
      if (line) throw new Error("text before the first == step");
    } else if (step.inNotes) {
      step.noteLines.push(raw);
    } else if (line === "--") {
      step.inNotes = true;
    } else if (line.startsWith("#=")) {
      step.overlays.push({ key: line.replace(/\s+/g, " "), o: parseOverlay(line, i + 1) });
    } else if (line.startsWith("#+")) {
      step.values.push(line.slice(2).trim());
    } else {
      step.lines.push(raw);
    }
  }
  finish();
  if (!spec.steps.length) throw new Error("no == steps");
  return spec;
}

/** Which of `now` are not in `before`, counting repeats (two identical wires are two parts). */
function minus(now: Parsed["parts"], before: Parsed["parts"]) {
  const left = new Map<string, number>();
  for (const p of before) left.set(p.html, (left.get(p.html) ?? 0) + 1);
  return now.map((p) => {
    const n = left.get(p.html) ?? 0;
    if (n > 0) left.set(p.html, n - 1);
    return n === 0;
  });
}

const S = ([x, y]: Pt): Pt => [x * UNIT, -y * UNIT];

function overlayBox(o: Overlay): Box {
  const pts: Pt[] =
    o.kind === "mesh"
      ? [[o.at[0] - o.r, o.at[1] - o.r], [o.at[0] + o.r, o.at[1] + o.r]]
      : o.kind === "path"
        ? o.pts
        : o.kind === "region"
          ? [o.a, o.b]
          : [[o.at[0] - 0.5, o.at[1] - 0.25], [o.at[0] + 0.5, o.at[1] + 0.25]];
  const s = pts.map(S);
  const xs = s.map((p) => p[0]);
  const ys = s.map((p) => p[1]);
  return { x: Math.min(...xs), y: Math.min(...ys), w: Math.max(...xs) - Math.min(...xs), h: Math.max(...ys) - Math.min(...ys) };
}

function union(boxes: Box[]): Box {
  const x0 = Math.min(...boxes.map((b) => b.x));
  const y0 = Math.min(...boxes.map((b) => b.y));
  const x1 = Math.max(...boxes.map((b) => b.x + b.w));
  const y1 = Math.max(...boxes.map((b) => b.y + b.h));
  return { x: x0, y: y0, w: x1 - x0, h: y1 - y0 };
}

/** A label inside the SVG: KaTeX/Markdown in a foreignObject centred on (x, y). `.cs-mov` lets autoLayout move it. */
function Label({ x, y, text, size = 11 }: { x: number; y: number; text: string; size?: number }) {
  const w = 140;
  const h = size * 2.6;
  const pure = /^\$[^$]+\$$/.test(text.trim());
  return (
    <g className="cs-mov">
      <foreignObject x={x - w / 2} y={y - h / 2} width={w} height={h} className="cs-label-fo">
        <div className="cs-label" style={{ fontSize: size }}>
          <span className="cs-label-in">
            {pure ? <span dangerouslySetInnerHTML={{ __html: texHtml(text.trim().slice(1, -1), false) }} /> : <Markdown text={text} inline />}
          </span>
        </div>
      </foreignObject>
    </g>
  );
}

/** Data the layout pass needs: mesh centre and radius (it may shrink the ring), path points (obstacles). */
function overlayData(o: Overlay): Record<string, string> {
  if (o.kind === "mesh") {
    const [cx, cy] = S(o.at);
    return { "data-kind": "mesh", "data-cx": `${cx}`, "data-cy": `${cy}`, "data-r": `${o.r * UNIT}`, "data-ccw": o.ccw ? "1" : "0" };
  }
  if (o.kind === "path") return { "data-kind": "path", "data-pts": o.pts.map((p) => S(p).join(",")).join(" ") };
  return { "data-kind": o.kind };
}

function OverlayShape({ o }: { o: Overlay }) {
  switch (o.kind) {
    case "mesh": {
      const [cx, cy] = S(o.at);
      const geo = meshGeometry(cx, cy, o.r * UNIT, o.ccw);
      return (
        <>
          <path className="cs-stroke" d={geo.d} pathLength={1} />
          <polygon className="cs-head" points={geo.head} />
          {o.label && <Label x={cx} y={cy} text={o.label} size={13} />}
        </>
      );
    }
    case "path": {
      const s = o.pts.map(S);
      const last = s[s.length - 1];
      const prev = s[s.length - 2];
      const dir: Pt = [last[0] - prev[0], last[1] - prev[1]];
      const mid: Pt = [(s[0][0] + s[1][0]) / 2, (s[0][1] + s[1][1]) / 2];
      const vertical = Math.abs(s[1][0] - s[0][0]) < Math.abs(s[1][1] - s[0][1]);
      return (
        <>
          <path
            className={`cs-stroke ${o.thin ? "cs-thin" : "cs-thick"}`}
            d={`M ${s.map((p) => p.join(" ")).join(" L ")}`}
            pathLength={1}
          />
          <polygon className="cs-head" points={arrowHead(last, dir, o.thin ? 9 : 13)} />
          {o.label && <Label x={mid[0] + (vertical ? 22 : 0)} y={mid[1] + (vertical ? 0 : -14)} text={o.label} />}
        </>
      );
    }
    case "sign": {
      const [x, y] = S(o.at);
      const k = 5;
      return (
        <g className={o.plus ? "cs-plus" : "cs-minus"}>
          <rect x={x - 7} y={y - 7} width={14} height={14} rx={2.5} />
          <path d={o.plus ? `M ${x - k} ${y} L ${x + k} ${y} M ${x} ${y - k} L ${x} ${y + k}` : `M ${x - k} ${y} L ${x + k} ${y}`} />
        </g>
      );
    }
    case "text": {
      const [x, y] = S(o.at);
      return <Label x={x} y={y} text={o.label} size={12} />;
    }
    case "region": {
      const [x0, y1] = S(o.a);
      const [x1, y0] = S(o.b);
      const [x, y, w, h] = [Math.min(x0, x1), Math.min(y0, y1), Math.abs(x1 - x0), Math.abs(y1 - y0)];
      return (
        <>
          <rect className="cs-region" x={x} y={y} width={w} height={h} rx={10} />
          {o.label && (
            <g className="cs-mov">
              <text className="cs-region-label" x={x + 6} y={y + h - 6}>
                {o.label}
              </text>
            </g>
          )}
        </>
      );
    }
  }
}

function Frame({ k, steps, svgs, frame, diff }: { k: number; steps: Step[]; svgs: Parsed[]; frame: Box; diff: boolean }) {
  const now = svgs[k].parts;
  const before = k > 0 && diff ? svgs[k - 1].parts : now;
  const added = minus(now, before);
  const lost = minus(before, now);
  const removed = before.filter((_, i) => lost[i]);
  const html = now.map((p, i) => wrapPart(p, added[i] ? "cs-add" : "")).join("") + removed.map((p) => wrapPart(p, "cs-gone")).join("");
  const ref = useRef<SVGSVGElement>(null);
  useAutoLayout(ref, [k, html]);
  const nowKeys = new Set(steps[k].overlays.map((o) => o.key));
  const oldKeys = new Set(k > 0 && diff ? steps[k - 1].overlays.map((o) => o.key) : nowKeys);
  const gone = k > 0 && diff ? steps[k - 1].overlays.filter((o) => !nowKeys.has(o.key)) : [];
  const list = [...steps[k].overlays.map((o) => ({ ...o, cls: oldKeys.has(o.key) ? "" : "cs-ov-new" })), ...gone.map((o) => ({ ...o, cls: "cs-gone" }))];
  const regions = list.filter((o) => o.o.kind === "region");
  const others = list.filter((o) => o.o.kind !== "region");
  const pad = 6;
  const draw = (o: (typeof list)[number], i: number) => (
    <g key={o.key + i} className={`cs-ov cs-c-${o.o.color || "none"} ${o.cls}`} {...overlayData(o.o)}>
      <OverlayShape o={o.o} />
    </g>
  );
  return (
    <svg
      ref={ref}
      className="cs-svg"
      viewBox={`${frame.x - pad} ${frame.y - pad} ${frame.w + 2 * pad} ${frame.h + 2 * pad}`}
      width={((frame.w + 2 * pad) * 4) / 3}
      role="img"
      aria-label={steps[k].title}
    >
      {regions.map(draw)}
      <g dangerouslySetInnerHTML={{ __html: html }} />
      {others.map(draw)}
    </svg>
  );
}

/** The "Found so far" panel: every `#+` value from steps 1..k; the ones found in step k are highlighted. */
export function Values({ steps, k, fresh }: { steps: Pick<Step, "values">[]; k: number; fresh?: boolean }) {
  // A value repeated in a later step (same text) stays listed once, under the step that first found it.
  const seen = new Set<string>();
  const found = steps
    .slice(0, k + 1)
    .flatMap((s, i) => s.values.map((v) => ({ v, now: i === k })))
    .filter(({ v }) => {
      const key = v.replace(/\s+/g, "");
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    });
  const box = useRef<HTMLElement>(null);
  useEffect(() => {
    // keep the newest values in view when the list is longer than the circuit is tall
    if (box.current) box.current.scrollTop = box.current.scrollHeight;
  }, [k]);
  return (
    <aside className="cs-values" ref={box}>
      <div className="cs-notes-label">Found so far</div>
      {found.length ? (
        <ul>
          {found.map(({ v, now }, i) => (
            <li key={i} className={now ? `cs-val-new ${fresh ? "mt-fade" : ""}` : ""}>
              <Markdown text={v} inline />
            </li>
          ))}
        </ul>
      ) : (
        <div className="cs-values-empty">Nothing yet</div>
      )}
    </aside>
  );
}

export function CircuitSteps({ source }: { source: string }) {
  const parsed = useMemo(() => {
    try {
      return { spec: parseCircuitSteps(source) };
    } catch (e) {
      return { error: (e as Error).message };
    }
  }, [source]);
  const [svgs, setSvgs] = useState<{ list?: Parsed[]; error?: string }>({});
  const [k, setK] = useState(0);
  const [all, setAll] = useState(false);
  useEffect(() => {
    if (!parsed.spec) return;
    let live = true;
    Promise.all(parsed.spec.steps.map((s) => loadSvg(drawingOnly(s.drawing)))).then(
      (list) => live && setSvgs({ list }),
      (e: Error) => live && setSvgs({ error: e.message }),
    );
    return () => {
      live = false;
    };
  }, [parsed]);
  const frame = useMemo(
    () =>
      svgs.list &&
      parsed.spec &&
      union([...svgs.list.map((s) => s.box), ...parsed.spec.steps.flatMap((s) => s.overlays.map((o) => overlayBox(o.o)))]),
    [svgs, parsed],
  );
  if (!parsed.spec) return <ToolError kind="circuitsteps" message={parsed.error!} source={source} />;
  if (svgs.error) return <ToolError kind="circuitsteps" message={svgs.error} source={source} />;
  const { steps, title } = parsed.spec;
  const n = steps.length;
  const go = (d: number) => setK((v) => Math.min(n - 1, Math.max(0, v + d)));
  const ready = svgs.list && frame;
  const hasValues = steps.some((s) => s.values.length);

  return (
    <div
      className="mt-card cs-card"
      tabIndex={0}
      onKeyDown={(e) => {
        if (all) return;
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
      {!ready ? (
        <div className="schematic-wait" />
      ) : all ? (
        <ol className="cs-all">
          {steps.map((s, i) => (
            <li key={i}>
              <div className="cs-step-title">
                <span className="cs-num">Step {i + 1}</span> <Markdown text={s.title} inline />
              </div>
              <div className={`cs-body ${hasValues ? "cs-with-values" : ""}`}>
                <div className="cs-stage">
                  <Frame k={i} steps={steps} svgs={svgs.list!} frame={frame!} diff={false} />
                </div>
                {hasValues && <Values steps={steps} k={i} />}
              </div>
              {s.notes && (
                <div className="cs-notes">
                  <Markdown text={s.notes} />
                </div>
              )}
            </li>
          ))}
        </ol>
      ) : (
        <>
          {/* Every step's title and notes sit in one grid cell, so the card is as tall as the longest step
              and Next never changes the page height. */}
          <div className="cs-stack">
            {steps.map((s, i) => (
              <div key={i} className={`cs-step-title ${i === k ? "on" : ""}`} aria-hidden={i !== k}>
                <span className="cs-num">
                  Step {i + 1} of {n}
                </span>{" "}
                <Markdown text={s.title} inline />
              </div>
            ))}
          </div>
          <div className={`cs-body ${hasValues ? "cs-with-values" : ""}`}>
            <div className="cs-stage">
              <Frame key={k} k={k} steps={steps} svgs={svgs.list!} frame={frame!} diff />
            </div>
            {hasValues && <Values steps={steps} k={k} fresh />}
          </div>
          <div className="cs-legend" style={{ visibility: k > 0 ? "visible" : "hidden" }}>
            <span className="cs-key cs-key-add" /> new in this step <span className="cs-key cs-key-gone" /> removed
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
          {steps.some((s) => s.notes) && (
            <div className="cs-stack cs-notes-stack">
              {steps.map((s, i) => (
                <div key={i} className={`cs-notes ${i === k ? "on mt-fade" : ""} ${s.notes ? "" : "cs-empty"}`} aria-hidden={i !== k}>
                  <div className="cs-notes-label">Notes</div>
                  <Markdown text={s.notes} />
                </div>
              ))}
            </div>
          )}
        </>
      )}
    </div>
  );
}
