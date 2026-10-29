import { ChevronLeft, ChevronRight, List, Maximize2, Minimize2, RotateCcw, ToggleRight } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { createPortal } from "react-dom";
import { digitalImage } from "../../api";
import { Markdown } from "../Markdown";
import { Values } from "./CircuitSteps";
import { ToolError } from "./Stepper";

/*
 * ```logicsteps fence: a logic-gate circuit that changes one step at a time, with notes under each step.
 * Same reading as ```circuitsteps, but each drawing is a `digital` circuit (skills/digital-figures.md).
 *
 *   title "Read the circuit left to right"     optional first line
 *   == Name the NOT outputs                     starts a step (its title, Markdown)
 *   {"kind":"circuit","nodes":[...],"wires":[...]}   a whole circuit (required in step 1; may span lines)
 *   label A "A = x̄₂"                            or edit the previous step's circuit:
 *   gate G NAND                                   change a gate's type
 *   node {"id":"N","gate":"NAND","x":260,"y":90}  add (or replace) a node
 *   drop N                                        remove a node and its wires
 *   wire N.out G.0 [x,y x,y ...]                  connect (replaces the wire into G.0)
 *   unwire G.0                                    disconnect an input
 *   hl A B                                        also highlight these nodes in this step
 *   #+ $C=\bar x_2x_3$                            add to "Found so far" from this step on
 *   --                                            ends the drawing
 *   Notes for this step (Markdown) until the next ==
 *
 * Nodes and wires that are new or changed since the previous step are drawn in the accent colour.
 * "Try inputs" lets the reader flip each input and see every wire's bit (combinational gates only).
 *
 * A step may instead draw a transistor network: {"kind":"cmos","pdn":{...}} (whole JSON), edited with
 *   show pdn                                      which halves to draw: both, pdn, pun or none ("?" box)
 *   inputs x1=1 x2=0                              show this row: transistors on/off and the conducting path
 *   inputs none                                   back to the plain drawing
 * A changed pull-down (and the pull-up that is its dual) is drawn in the accent colour; "Try inputs" flips the
 * transistor gate inputs and shows which network conducts.
 */

type Node = { id: string; gate: string; x: number; y: number; label?: string; inputs?: number; highlight?: boolean; value?: 0 | 1 };
type Wire = { start: string; end: string; via?: [number, number][]; highlight?: boolean; value?: 0 | 1 };
type Gates = { kind: "circuit"; title?: string; nodes: Node[]; wires: Wire[] };
type Network = { gate?: string; series?: Network[]; parallel?: Network[] };
type Cmos = {
  kind: "cmos";
  title?: string;
  pdn: Network;
  pullup?: "pmos" | "resistor";
  show?: "both" | "pdn" | "pun" | "none";
  output?: string;
  highlight?: ("pdn" | "pun")[];
  inputs?: Record<string, number> | null;
};
type Circuit = Gates | Cmos;
type Step = { title: string; circuit: Circuit; changed: Set<string>; values: string[]; notes: string };
export type LogicStepsSpec = { title?: string; steps: Step[] };

const SIMULATED: Record<string, (bits: number[]) => number> = {
  AND: (b) => +b.every(Boolean),
  OR: (b) => +b.some(Boolean),
  NAND: (b) => +!b.every(Boolean),
  NOR: (b) => +!b.some(Boolean),
  XOR: (b) => b.reduce((a, c) => a ^ c, 0),
  XNOR: (b) => 1 - b.reduce((a, c) => a ^ c, 0),
  NOT: (b) => 1 - b[0],
  BUF: (b) => b[0],
  OUTPUT: (b) => b[0],
};

function tokens(line: string) {
  return [...line.matchAll(/"((?:[^"\\]|\\.)*)"|(\S+)/g)].map((m) => (m[1] !== undefined ? m[1] : m[2]));
}

const nodeKey = (n: Node) => `n:${n.id}`;
const wireKey = (w: Wire) => `w:${w.end}`;
const same = (a: unknown, b: unknown) => JSON.stringify(a) === JSON.stringify(b);

function edit(circuit: Circuit, line: string, no: number): Circuit {
  const [cmd, ...t] = tokens(line);
  if (circuit.kind === "cmos") {
    if (cmd === "show") return { ...circuit, show: t[0] as Cmos["show"] };
    if (cmd === "inputs") {
      if (t[0] === "none") return { ...circuit, inputs: undefined };
      return { ...circuit, inputs: Object.fromEntries(t.map((p) => p.split("=")).map(([k, v]) => [k, Number(v)])) };
    }
    throw new Error(`line ${no}: a transistor drawing takes "show" or "inputs", not "${cmd}"`);
  }
  const c: Gates = { ...circuit, nodes: circuit.nodes.map((n) => ({ ...n })), wires: circuit.wires.map((w) => ({ ...w })) };
  const find = (id: string | undefined) => {
    const n = c.nodes.find((n) => n.id === id);
    if (!n) throw new Error(`line ${no}: no node "${id ?? ""}"`);
    return n;
  };
  switch (cmd) {
    case "label":
      find(t[0]).label = t[1] ?? "";
      return c;
    case "gate": {
      const n = find(t[0]);
      n.gate = t[1] ?? n.gate;
      const inputs = t.find((s) => s.startsWith("inputs="));
      if (inputs) n.inputs = Number(inputs.slice(7));
      return c;
    }
    case "node": {
      const n = JSON.parse(line.slice(4).trim()) as Node;
      c.nodes = [...c.nodes.filter((m) => m.id !== n.id), n];
      return c;
    }
    case "drop":
      find(t[0]);
      c.nodes = c.nodes.filter((n) => n.id !== t[0]);
      c.wires = c.wires.filter((w) => w.start.split(".")[0] !== t[0] && w.end.split(".")[0] !== t[0]);
      return c;
    case "wire": {
      if (!t[0] || !t[1]) throw new Error(`line ${no}: wire needs START.out END.pin`);
      const via = t.slice(2).map((p) => p.split(",").map(Number) as [number, number]);
      c.wires = [...c.wires.filter((w) => w.end !== t[1]), { start: t[0], end: t[1], ...(via.length ? { via } : {}) }];
      return c;
    }
    case "unwire":
      c.wires = c.wires.filter((w) => w.end !== t[0]);
      return c;
  }
  throw new Error(`line ${no}: unknown statement "${cmd}" (label, gate, node, drop, wire, unwire, hl)`);
}

export function parseLogicSteps(source: string): LogicStepsSpec {
  const lines = source.split(/\r?\n/);
  const spec: LogicStepsSpec = { steps: [] };
  let i = 0;
  while (i < lines.length && !lines[i].trim()) i++;
  const head = /^title\s+"(.*)"\s*$/.exec(lines[i]?.trim() ?? "");
  if (head) {
    spec.title = head[1];
    i++;
  }
  let previous: Circuit | undefined;
  type Draft = { title: string; json: string[]; edits: [string, number][]; focus: string[]; values: string[]; notes: string[]; inNotes: boolean };
  let step: Draft | undefined;
  const finish = () => {
    if (!step) return;
    let circuit = previous;
    if (step.json.length) {
      try {
        circuit = JSON.parse(step.json.join("\n")) as Circuit;
      } catch (e) {
        throw new Error(`step "${step.title}": the circuit is not valid JSON (${(e as Error).message})`);
      }
      if (circuit.kind === "circuit") circuit.wires ??= [];
      else if (circuit.kind !== "cmos") throw new Error(`step "${step.title}": the drawing must be a "circuit" or "cmos"`);
    }
    if (!circuit) throw new Error(`step "${step.title}" has no circuit (the first step needs one)`);
    for (const [line, no] of step.edits) circuit = edit(circuit, line, no);
    const changed = new Set(step.focus.map((id) => `n:${id}`));
    if (circuit.kind === "cmos") {
      const before = previous?.kind === "cmos" ? previous : undefined;
      const shows = (c: Cmos | undefined, half: "pdn" | "pun") => !!c && [half, "both"].includes(c.show ?? "both");
      const grew = !before || !same(before.pdn, circuit.pdn) || before.pullup !== circuit.pullup;
      for (const half of ["pdn", "pun"] as const)
        if (shows(circuit, half) && (grew || !shows(before, half)) && (before || step.focus.includes(half))) changed.add(half);
      for (const half of step.focus) if (half === "pdn" || half === "pun") changed.add(half);
    } else if (previous?.kind === "circuit") {
      const before = new Map<string, unknown>([...previous.nodes.map((n) => [nodeKey(n), n] as const), ...previous.wires.map((w) => [wireKey(w), w] as const)]);
      for (const part of [...circuit.nodes, ...circuit.wires]) {
        const key = "id" in part ? nodeKey(part) : wireKey(part);
        if (!same(before.get(key), part)) changed.add(key);
      }
    }
    spec.steps.push({ title: step.title, circuit, changed, values: step.values, notes: step.notes.join("\n").trim() });
    previous = circuit;
  };
  for (; i < lines.length; i++) {
    const raw = lines[i];
    const line = raw.trim();
    if (line.startsWith("==")) {
      finish();
      step = { title: line.slice(2).trim(), json: [], edits: [], focus: [], values: [], notes: [], inNotes: false };
    } else if (!step) {
      if (line) throw new Error("text before the first == step");
    } else if (step.inNotes) {
      step.notes.push(raw);
    } else if (line === "--") {
      step.inNotes = true;
    } else if (line.startsWith("#+")) {
      step.values.push(line.slice(2).trim());
    } else if (/^hl\s/.test(line)) {
      step.focus.push(...tokens(line).slice(1));
    } else if (/^(label|gate|node|drop|wire|unwire|show|inputs)\s/.test(line)) {
      step.edits.push([line, i + 1]);
    } else if (line) {
      step.json.push(raw);
    }
  }
  finish();
  if (!spec.steps.length) throw new Error("no == steps");
  return spec;
}

/** Every node's output bit for these input values, or undefined if the circuit has parts we don't simulate. */
function simulate(c: Gates, inputs: Record<string, number>) {
  if (c.nodes.some((n) => n.gate !== "INPUT" && !SIMULATED[n.gate])) return undefined;
  const into = new Map(c.wires.map((w) => [w.end, w.start.split(".")[0]]));
  const value = new Map<string, number>();
  const visit = (id: string, path: Set<string>): number => {
    if (value.has(id)) return value.get(id)!;
    const n = c.nodes.find((m) => m.id === id)!;
    if (n.gate === "INPUT") return inputs[id] ?? 0;
    if (path.has(id)) throw new Error("feedback loop");
    path.add(id);
    const count = ["NOT", "BUF", "OUTPUT"].includes(n.gate) ? 1 : n.inputs ?? 2;
    const bits = Array.from({ length: count }, (_, p) => {
      const from = into.get(`${id}.${p}`);
      return from ? visit(from, path) : 0;
    });
    const v = SIMULATED[n.gate](bits);
    value.set(id, v);
    return v;
  };
  try {
    for (const n of c.nodes) value.set(n.id, visit(n.id, new Set()));
  } catch {
    return undefined;
  }
  return value;
}

/** The circuit as drawn in one view: highlighted changes (stepping) or every wire's bit (trying inputs). */
function paint(c: Gates, changed: Set<string>, bits?: Map<string, number>): Gates {
  return {
    ...c,
    nodes: c.nodes.map((n) => ({ ...n, highlight: !bits && changed.has(nodeKey(n)), ...(bits ? { value: bits.get(n.id) as 0 | 1 } : {}) })),
    wires: c.wires.map((w) => ({ ...w, highlight: !bits && changed.has(wireKey(w)), ...(bits ? { value: bits.get(w.start.split(".")[0]) as 0 | 1 } : {}) })),
  };
}

/** A transistor drawing as shown: changed halves highlighted (stepping), or the tried inputs' current paths. */
function paintCmos(c: Cmos, changed: Set<string>, inputs?: Record<string, number>): Cmos {
  if (inputs) return { ...c, highlight: [], inputs: Object.fromEntries(gateNames(c.pdn).map((g) => [g, inputs[g] ?? 0])) };
  return { ...c, highlight: (["pdn", "pun"] as const).filter((h) => changed.has(h)) };
}

function gateNames(n: Network): string[] {
  const names = n.gate ? [n.gate] : (n.series ?? n.parallel ?? []).flatMap(gateNames);
  return [...new Set(names)].sort();
}

function view(s: Step, inputs?: Record<string, number>): Circuit {
  const c = s.circuit;
  return c.kind === "cmos" ? paintCmos(c, s.changed, inputs) : paint(c, s.changed, inputs ? simulate(c, inputs) : undefined);
}

/** digital.dimensions: the room one transistor network takes up. */
function dimensions(n: Network): [number, number] {
  if (n.gate) return [Math.max(110, n.gate.length * 16 + 60), 70];
  const sizes = (n.series ?? n.parallel ?? []).map(dimensions);
  return n.series
    ? [Math.max(...sizes.map((d) => d[0])), sizes.reduce((a, d) => a + d[1], 0)]
    : [sizes.reduce((a, d) => a + d[0], 0), Math.max(...sizes.map((d) => d[1])) + 30];
}

function dual(n: Network): Network {
  if (n.gate) return n;
  return n.series ? { parallel: n.series.map(dual) } : { series: (n.parallel ?? []).map(dual) };
}

/** The server's SVG size for a drawing (digital.circuit_svg, digital.cmos_size), so every step can share one scale. */
function size(c: Circuit) {
  if (c.kind === "cmos") {
    const [pw, ph] = c.pullup === "resistor" ? [110, 90] : dimensions(dual(c.pdn));
    const [nw, nh] = dimensions(c.pdn);
    return { w: Math.max(pw, nw) + 140 + (c.inputs ? 230 : 0), h: ph + nh + 160 };
  }
  const pins = (n: Node) => (n.gate === "INPUT" ? 0 : ["NOT", "BUF", "OUTPUT"].includes(n.gate) ? 1 : n.inputs ?? 2);
  return {
    w: Math.max(...c.nodes.map((n) => n.x)) + 120,
    h: Math.max(...c.nodes.map((n) => n.y + Math.max(50, pins(n) * 11))) + 45,
  };
}

function Drawing({ circuit, frame, alt, big, onExpand }: { circuit: Circuit; frame: { w: number; h: number }; alt: string; big?: boolean; onExpand?: () => void }) {
  const source = JSON.stringify(circuit);
  const [state, setState] = useState<{ url?: string; error?: string }>({});
  useEffect(() => {
    let live = true;
    digitalImage(source).then(
      (url) => live && setState({ url }),
      (e: Error) => live && setState({ error: e.message }),
    );
    return () => {
      live = false;
    };
  }, [source]);
  const own = size(circuit);
  if (state.error) return <div className="ls-error">This step could not be drawn: {state.error}</div>;
  return (
    <div
      className={`ls-frame ${onExpand ? "zoomable" : ""}`}
      title={onExpand ? "Click to enlarge" : undefined}
      onClick={onExpand}
      // Expanded: as big as fits under the controls; inline: up to a bit under the drawing's own size.
      style={{ aspectRatio: `${frame.w} / ${frame.h}`, maxWidth: big ? `min(${frame.w * 1.7}px, calc((100vh - 330px) * ${frame.w / frame.h}))` : frame.w }}
    >
      {state.url && <img src={state.url} alt={alt} style={{ width: `${(own.w / frame.w) * 100}%` }} />}
    </div>
  );
}

function InputBar({ circuit, inputs, flip }: { circuit: Circuit; inputs: Record<string, number>; flip: (id: string) => void }) {
  const names =
    circuit.kind === "cmos"
      ? gateNames(circuit.pdn).map((id) => ({ id, label: id.replace(/(\d+)$/, (d) => [...d].map((c) => "₀₁₂₃₄₅₆₇₈₉"[+c]).join("")) }))
      : circuit.nodes.filter((n) => n.gate === "INPUT").map((n) => ({ id: n.id, label: n.label || n.id }));
  return (
    <div className="ls-inputs">
      <span className="cs-notes-label">Inputs</span>
      {names
        .sort((a, b) => a.label.localeCompare(b.label))
        .map((n) => (
          <button key={n.id} className={`ls-bit ${inputs[n.id] ? "on" : ""}`} onClick={() => flip(n.id)} title="Click to flip">
            {n.label} = {inputs[n.id] ?? 0}
          </button>
        ))}
    </div>
  );
}

export function LogicSteps({ source }: { source: string }) {
  const parsed = useMemo(() => {
    try {
      return { spec: parseLogicSteps(source) };
    } catch (e) {
      return { error: (e as Error).message };
    }
  }, [source]);
  const [k, setK] = useState(0);
  const [all, setAll] = useState(false);
  const [trying, setTrying] = useState(false);
  const [inputs, setInputs] = useState<Record<string, number>>({});
  const [big, setBig] = useState(false);
  useEffect(() => {
    if (!big) return;
    const key = (e: KeyboardEvent) => e.key === "Escape" && setBig(false);
    document.addEventListener("keydown", key);
    return () => document.removeEventListener("keydown", key);
  }, [big]);
  if (!parsed.spec) return <ToolError kind="logicsteps" message={parsed.error!} source={source} />;
  const { steps, title } = parsed.spec;
  const n = steps.length;
  const go = (d: number) => setK((v) => Math.min(n - 1, Math.max(0, v + d)));
  const frame = steps.map((s) => size(view(s, trying ? inputs : undefined))).reduce((a, b) => ({ w: Math.max(a.w, b.w), h: Math.max(a.h, b.h) }));
  const hasValues = steps.some((s) => s.values.length);
  const canTry = steps.every((s) => s.circuit.kind === "cmos" || simulate(s.circuit, {}));
  const transistors = steps.some((s) => s.circuit.kind === "cmos");
  const flip = (id: string) => setInputs((v) => ({ ...v, [id]: v[id] ? 0 : 1 }));

  const card = (
    <div
      className={`mt-card cs-card ls-card ${big ? "ls-big" : ""}`}
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
        {canTry && (
          <button className={`mt-icon ls-try ${trying ? "active" : ""}`} onClick={() => setTrying(!trying)} title={trying ? "Back to the step highlights" : transistors ? "Flip the inputs and watch which transistors turn on" : "Flip the inputs and watch every wire"}>
            <ToggleRight size={15} /> <span>Try inputs</span>
          </button>
        )}
        <button className={`mt-icon ${all ? "active" : ""}`} onClick={() => setAll(!all)} title={all ? "One step at a time" : "Show every step"}>
          <List size={15} />
        </button>
        <button className="mt-icon ls-expand" onClick={() => setBig(!big)} title={big ? "Back to the note (Esc)" : "Enlarge"}>
          {big ? <Minimize2 size={15} /> : <Maximize2 size={15} />}
        </button>
      </div>
      {trying && <InputBar circuit={steps[all ? 0 : k].circuit} inputs={inputs} flip={flip} />}
      {all ? (
        <ol className="cs-all">
          {steps.map((s, i) => (
            <li key={i}>
              <div className="cs-step-title">
                <span className="cs-num">Step {i + 1}</span> <Markdown text={s.title} inline />
              </div>
              <div className={`cs-body ${hasValues ? "cs-with-values" : ""}`}>
                <div className="cs-stage">
                  <Drawing circuit={view(s, trying ? inputs : undefined)} frame={frame} alt={s.title} big={big} onExpand={big ? undefined : () => setBig(true)} />
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
            <div className="cs-stage mt-fade" key={k}>
              <Drawing circuit={view(steps[k], trying ? inputs : undefined)} frame={frame} alt={steps[k].title} big={big} onExpand={big ? undefined : () => setBig(true)} />
            </div>
            {hasValues && <Values steps={steps} k={k} fresh />}
          </div>
          <div className="cs-legend" style={{ visibility: trying || k > 0 ? "visible" : "hidden" }}>
            {trying ? (
              <>
                {transistors ? (
                  <>
                    <span className="cs-key ls-key-one" /> on, and the path that sets f <span className="cs-key ls-key-zero" /> off
                  </>
                ) : (
                  <>
                    <span className="cs-key ls-key-one" /> wire is 1 <span className="cs-key ls-key-zero" /> wire is 0
                  </>
                )}
              </>
            ) : (
              <>
                <span className="cs-key cs-key-add" /> new or changed in this step
              </>
            )}
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
  if (!big) return card;
  return createPortal(
    <div className="zoom-scrim ls-scrim" onPointerDown={(e) => e.target === e.currentTarget && setBig(false)}>
      {card}
    </div>,
    document.body,
  );
}
