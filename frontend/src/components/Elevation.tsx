import { ArrowUpDown, ChevronLeft, ChevronRight, Eye, RotateCcw } from "lucide-react";
import { useLayoutEffect, useMemo, useRef, useState } from "react";
import { Markdown } from "./Markdown";
import { Dialog } from "./ui";

/*
 * Height view ("elevation") of a circuit: every node is a horizontal level drawn at its potential,
 * ground (0 V) is the reference, and each element hangs vertically between its two levels. Series
 * elements share a column, so a loop reads as one straight line going up through the source and back
 * down through the loads.
 *
 * Views are written inside a schematic's source as comment lines, which the drawing parser ignores:
 *
 *   #@ view "As drawn"                       start a view (several views become tabs)
 *   #@ node a 30 "$a$: $30\,\mathrm{V}$"     node name, height in volts, axis label; add `ground`
 *                                            for a 0 V reference copy, `unknown` for an undetermined one,
 *                                            `terminal` for an open terminal (a lead ending in a circle)
 *   #@ el V g a "$30\,\mathrm{V}$" col=0 i="8 A" to=g
 *        kinds R V I E G B C (capacitor) L (inductor) X S (open switch) W (closed switch, wire or ideal ammeter). For V, E and B the first node is +;
 *        for I and G the arrow points from the first node to the second. A vertical element sits in column
 *        `col`; an element whose two nodes are at the same height lies flat between `col` and `col+1`,
 *        first node on the left. `i` is the actual current and `to` the node it flows toward.
 *        `plus=NODE v="$v_x$"` copies a voltage reference from the drawing: blue + at NODE, − at the other
 *        end, named v_x (it may sit on the lower end, which is what makes v_x negative). Without it, every
 *        element except V and E (whose symbols carry their own signs) gets black +/− marks at its actual
 *        polarity, + on the higher end, so "current enters +" reads as "absorbs".
 *   #@ mismatch t1 t2 "text"                 two levels that should be one node (an invalid circuit)
 *   #@ note "text"                           explanation under the drawing
 *   #@ scale illustrative                    symbolic values: heights only show the order
 *   #@ spoiler                               the view gives away a problem's answer
 *   #@ inline                                also draw the finished first view under the circuit (no dialog
 *                                            needed); the Height view button still opens tabs and steps
 */

type Node = {
  name: string;
  h: number;
  label: string;
  ground: boolean;
  unknown: boolean;
  terminal: boolean;
};
type El = {
  kind: string;
  a: string;
  b: string;
  label: string;
  col: number;
  cur?: string;
  to?: string;
  rail?: boolean;
  norail?: boolean;
  id?: string;
  plus?: string;
  vname?: string;
};
/** One step of a height-view solution; `show` lists the node names and element ids it works out. */
type Step = { text: string; show: string[] };
type View = {
  title: string;
  nodes: Map<string, Node>;
  els: El[];
  notes: string[];
  mismatches: { a: string; b: string; text: string }[];
  illustrative: boolean;
  noStraight: boolean;
  steps: Step[];
};
/** A supply rail: a node held at its voltage by a grounded source that the straight-line view leaves out. */
type Rail = {
  node: string;
  label: string;
  sub?: string;
  color?: string;
  el?: string;
};
/** What a step-by-step solution has worked out so far: hidden things show as "?", fresh ones are highlighted. */
type Reveal = { hidden: Set<string>; fresh: Set<string> };
const NONE: Reveal = { hidden: new Set(), fresh: new Set() };

function revealAt(view: View, step: number): Reveal {
  if (step >= view.steps.length) return NONE;
  const hidden = new Set<string>();
  const fresh = new Set<string>();
  view.steps.forEach((s, k) =>
    s.show.forEach((name) => (k + 1 > step ? hidden.add(name) : k + 1 === step && fresh.add(name))),
  );
  return { hidden, fresh };
}

/** "$a$: $30\,\mathrm{V}$" -> "$a$: ?" while the value is still unknown. */
function masked(label: string) {
  const at = label.indexOf(": ");
  return at >= 0 ? `${label.slice(0, at)}: ?` : "?";
}
export type Elevation = { views: View[]; spoiler: boolean; inline: boolean };

const PREFIX = /^\s*#@\s?/;
const MODE_KEY = "ol-elevation-mode";

export function drawingOnly(source: string) {
  return source
    .split("\n")
    .filter((line) => !PREFIX.test(line))
    .join("\n")
    .trim();
}

function tokens(line: string) {
  const out: { key?: string; value: string }[] = [];
  const re = /(\w+)="([^"]*)"|"([^"]*)"|(\S+)/g;
  for (let m = re.exec(line); m; m = re.exec(line)) {
    if (m[1]) out.push({ key: m[1], value: m[2] });
    else if (m[3] !== undefined) out.push({ value: m[3] });
    else {
      const eq = /^(\w+)=(\S+)$/.exec(m[4]);
      out.push(eq ? { key: eq[1], value: eq[2] } : { value: m[4] });
    }
  }
  return out;
}

export function parseElevation(source: string): Elevation | null {
  const lines = source.split("\n").filter((line) => PREFIX.test(line));
  if (!lines.length) return null;
  const spec: Elevation = { views: [], spoiler: false, inline: false };
  const fresh = (title: string): View => ({
    title,
    nodes: new Map(),
    els: [],
    notes: [],
    mismatches: [],
    illustrative: false,
    noStraight: false,
    steps: [],
  });
  let view: View | null = null;
  const current = () => {
    if (!view) {
      view = fresh("Height view");
      spec.views.push(view);
    }
    return view;
  };
  for (const raw of lines) {
    const t = tokens(raw.replace(PREFIX, ""));
    if (!t.length) continue;
    const word = t[0].value;
    const plain = t
      .slice(1)
      .filter((x) => !x.key)
      .map((x) => x.value);
    const opt = Object.fromEntries(t.filter((x) => x.key).map((x) => [x.key, x.value]));
    if (word === "view") {
      view = fresh(plain[0] ?? `View ${spec.views.length + 1}`);
      spec.views.push(view);
    } else if (word === "spoiler") spec.spoiler = true;
    else if (word === "inline") spec.inline = true;
    else if (word === "scale") current().illustrative = plain[0] === "illustrative";
    else if (word === "straight") current().noStraight = plain[0] === "off";
    else if (word === "note") current().notes.push(plain[0] ?? "");
    else if (word === "step")
      current().steps.push({
        text: plain[0] ?? "",
        show: (opt.show ?? "")
          .split(",")
          .map((s: string) => s.trim())
          .filter(Boolean),
      });
    else if (word === "mismatch")
      current().mismatches.push({
        a: plain[0],
        b: plain[1],
        text: plain[2] ?? "",
      });
    else if (word === "node") {
      const [name, h, label, ...flags] = plain;
      current().nodes.set(name, {
        name,
        h: Number(h),
        label: label ?? name,
        ground: flags.includes("ground"),
        unknown: flags.includes("unknown"),
        terminal: flags.includes("terminal"),
      });
    } else if (word === "el") {
      const [kind, a, b, label, ...flags] = plain;
      current().els.push({
        kind: kind.toUpperCase(),
        a,
        b,
        label: label ?? "",
        col: Number(opt.col ?? 0),
        cur: opt.i,
        to: opt.to,
        rail: flags.includes("rail"),
        norail: flags.includes("norail"),
        id: opt.id,
        plus: opt.plus,
        vname: opt.v,
      });
    }
  }
  spec.views = spec.views.filter((v) => v.els.length);
  return spec.views.length ? spec : null;
}

/**
 * The straight-line ("rail") form, as drawn in electronics: a grounded voltage source is not drawn;
 * its other end becomes a labelled supply rail and the circuit hangs from it down to ground, splitting
 * into branches where the circuit branches. Each node keeps at most one rail and at least one element.
 * Returns null when nothing would change.
 */
export function straighten(view: View): { view: View; rails: Rail[] } | null {
  if (view.noStraight) return null;
  const node = (name: string) => view.nodes.get(name);
  const grounded = (el: El) => !!node(el.a)?.ground !== !!node(el.b)?.ground;
  const candidates = view.els
    .map((el, i) => ({ el, i }))
    .filter(({ el }) => grounded(el) && !el.norail && (el.rail || el.kind === "V" || el.kind === "B"));
  // Only a source feeding the highest level becomes a rail: the river starts at the top. A source
  // partway down stays drawn, because a rail floating mid-picture reads as nonsense.
  const highest = Math.max(...[...view.nodes.values()].map((n) => n.h));
  const byNode = new Map<string, typeof candidates>();
  for (const c of candidates) {
    const top = node(c.el.a)?.ground ? c.el.b : c.el.a;
    if (node(top)?.h !== highest || node(top)?.unknown) continue;
    byNode.set(top, [...(byNode.get(top) ?? []), c]);
  }
  const flowUp = (el: El) => {
    if (!el.cur || !el.to) return null;
    const from = el.to === el.a ? el.b : el.a;
    return (node(el.to)?.h ?? 0) > (node(from)?.h ?? 0);
  };
  const removed = new Set<number>();
  const rails: Rail[] = [];
  for (const [name, list] of byNode) {
    const pick = list.find((c) => c.el.rail) ?? list.find((c) => flowUp(c.el)) ?? list[0];
    const keeps = view.els.some((e, i) => i !== pick.i && !removed.has(i) && (e.a === name || e.b === name));
    if (!keeps) continue;
    removed.add(pick.i);
    const up = flowUp(pick.el);
    const unknown = node(name)?.unknown;
    const full = node(name)?.label ?? name;
    rails.push({
      node: name,
      // "top right: 30 V" -> "30 V": the axis already names the node, the rail just shows its voltage.
      label: full.includes(": ") ? full.slice(full.indexOf(": ") + 2) : full,
      sub: pick.el.cur && up !== null ? `${up ? "supplies" : "takes in"} ${pick.el.cur}` : undefined,
      color: up === null || unknown ? undefined : up ? DELIVER : ABSORB,
      el: pick.el.id,
    });
  }
  if (!removed.size) return null;
  const els = view.els.filter((_, i) => !removed.has(i));
  // Close the gap the removed source column leaves; a flat element also occupies the next column.
  const h = (name: string) => node(name)?.h ?? 0;
  const used = new Set<number>();
  for (const e of els) {
    used.add(e.col);
    if (h(e.a) === h(e.b)) used.add(e.col + 1);
  }
  const remap = new Map([...used].sort((a, b) => a - b).map((c, i) => [c, i]));
  return {
    view: {
      ...view,
      els: els.map((e) => ({ ...e, col: remap.get(e.col) ?? e.col })),
    },
    rails,
  };
}

// ---------- layout ----------

const AXIS = 150;
const FIRST = 110; // clear of the axis even with a current label left of the first column
const COLW = 150;
const TOP = 78; // room above the highest level for a rail's bar and label
const SPAN = 340;
const MINGAP = 64; // room for two elements' +/− marks to meet at one level
const ABSORB = "#d9822b";
const DELIVER = "#2e9d6a";
const REFERENCE = "#3b7ddd"; // the drawing's own +/− references, blue like the textbook's

/** Half the height of an element's drawn body, so polarity marks sit just beyond it. */
function bodyHalf(kind: string, len: number) {
  const s = Math.max(0, Math.min(46, len - 16));
  if (s < 18 || kind === "W") return 0;
  if ("VIEG".includes(kind)) return Math.min(17, s / 2);
  if (kind === "B" || kind === "C") return 10; // the plates are thin, but the label beside them is not
  if (kind === "R" || kind === "S" || kind === "L") return s / 2;
  return Math.min(s, 34) / 2;
}

/** Rough rendered width of a label in px: LaTeX commands count as one glyph, markup as none. */
function textWidth(text: string, px = 7.6) {
  const plain = text
    .replace(/\\(mathrm|text|operatorname)\b/g, "")
    .replace(/\\[,;! ]/g, " ")
    .replace(/\\[a-zA-Z]+/g, "x")
    .replace(/[${}^_\\]/g, "");
  return plain.length * px;
}

function layout(view: View) {
  const heights = [...new Set([...view.nodes.values()].map((n) => n.h))].sort((a, b) => b - a);
  const max = heights[0];
  const range = Math.max(heights[0] - heights[heights.length - 1], 1e-9);
  const ys = new Map<number, number>();
  let last = -Infinity;
  for (const h of heights) {
    const y = Math.max(TOP + ((max - h) / range) * SPAN, last + MINGAP);
    ys.set(h, y);
    last = y;
  }
  const y = (name: string) => ys.get(view.nodes.get(name)?.h ?? 0) ?? TOP;
  // Columns are spaced by their labels: a vertical element's name sits to its right and its current
  // label to its left, so the gap between two columns must fit both.
  const flatOf = (el: El) => y(el.a) === y(el.b);
  const right = new Map<number, number>();
  const left = new Map<number, number>();
  const cols = new Set<number>();
  for (const el of view.els) {
    cols.add(el.col);
    if (flatOf(el)) {
      cols.add(el.col + 1);
      continue;
    }
    if (el.label) right.set(el.col, Math.max(right.get(el.col) ?? 0, 26 + textWidth(el.label)));
    if (el.cur) left.set(el.col, Math.max(left.get(el.col) ?? 0, 40 + textWidth(el.cur, 7)));
  }
  const order = [...cols].sort((a, b) => a - b);
  const xs = new Map<number, number>();
  let x = AXIS + Math.max(FIRST, (left.get(order[0]) ?? 0) + 24);
  order.forEach((c, k) => {
    if (k) x += Math.max(COLW, (right.get(order[k - 1]) ?? 0) + (left.get(c) ?? 0) + 18);
    xs.set(c, x);
  });
  const colX = (c: number) => xs.get(c) ?? AXIS + FIRST;
  const placed = view.els.map((el) => {
    const flat = flatOf(el);
    const xa = colX(el.col);
    const xb = flat ? colX(el.col + 1) : xa;
    return { el, flat, xa, xb, ya: y(el.a), yb: y(el.b) };
  });
  const lastX = Math.max(...placed.map((p) => Math.max(p.xa, p.xb)));
  const lastCol = order[order.length - 1];
  const width = lastX + Math.max(view.mismatches.length ? 260 : 190, (right.get(lastCol) ?? 0) + 40);
  const height = last + 70;
  return { ys, y, placed, width, height, lastX };
}

// ---------- symbols, drawn along +y from (0,0) to (0,len) and rotated into place ----------

function Symbol({ kind, len }: { kind: string; len: number }) {
  const s = Math.max(0, Math.min(46, len - 16));
  const m = len / 2;
  const top = m - s / 2;
  const bot = m + s / 2;
  const leads = (gapTop: number, gapBot: number) => (
    <>
      <line x1={0} y1={0} x2={0} y2={gapTop} />
      <line x1={0} y1={gapBot} x2={0} y2={len} />
    </>
  );
  if (s < 18 || kind === "W") return <line x1={0} y1={0} x2={0} y2={len} />;
  const r = Math.min(17, s / 2);
  const plusMinus = (
    <>
      <line x1={-4} y1={m - r * 0.48} x2={4} y2={m - r * 0.48} />
      <line x1={0} y1={m - r * 0.48 - 4} x2={0} y2={m - r * 0.48 + 4} />
      <line x1={-4} y1={m + r * 0.48} x2={4} y2={m + r * 0.48} />
    </>
  );
  const arrow = (
    <>
      <line x1={0} y1={m - r * 0.6} x2={0} y2={m + r * 0.55} />
      <path d={`M -4 ${m + r * 0.2} L 0 ${m + r * 0.62} L 4 ${m + r * 0.2}`} fill="none" />
    </>
  );
  switch (kind) {
    case "R": {
      const pts = [`0,${top}`];
      for (let k = 0; k < 6; k++) pts.push(`${k % 2 ? -7 : 7},${top + ((k + 0.5) * s) / 6}`);
      pts.push(`0,${bot}`);
      return (
        <>
          {leads(top, bot)}
          <polyline points={pts.join(" ")} fill="none" />
        </>
      );
    }
    case "V":
      return (
        <>
          {leads(m - r, m + r)}
          <circle cx={0} cy={m} r={r} fill="var(--elev-bg)" />
          {plusMinus}
        </>
      );
    case "I":
      return (
        <>
          {leads(m - r, m + r)}
          <circle cx={0} cy={m} r={r} fill="var(--elev-bg)" />
          {arrow}
        </>
      );
    case "E":
    case "G":
      return (
        <>
          {leads(m - r, m + r)}
          <path d={`M 0 ${m - r} L ${r} ${m} L 0 ${m + r} L ${-r} ${m} Z`} fill="var(--elev-bg)" />
          {kind === "E" ? plusMinus : arrow}
        </>
      );
    case "B":
      return (
        <>
          {leads(m - 3, m + 3)}
          <line x1={-13} y1={m - 3} x2={13} y2={m - 3} />
          <line x1={-7} y1={m + 3} x2={7} y2={m + 3} strokeWidth={3} />
        </>
      );
    case "C":
      return (
        <>
          {leads(m - 4, m + 4)}
          <line x1={-13} y1={m - 4} x2={13} y2={m - 4} />
          <line x1={-13} y1={m + 4} x2={13} y2={m + 4} />
        </>
      );
    case "L": {
      // Four coil loops along the element, bulging to the right.
      const turns = 4;
      const step = s / turns;
      let d = `M 0 ${top}`;
      for (let k = 0; k < turns; k++) d += ` a ${step / 2} ${step / 2} 0 0 1 0 ${step}`;
      return (
        <>
          {leads(top, bot)}
          <path d={d} fill="none" />
        </>
      );
    }
    case "S":
      return (
        <>
          {leads(top + 4, bot - 4)}
          <circle cx={0} cy={top + 4} r={3} fill="var(--elev-bg)" />
          <circle cx={0} cy={bot - 4} r={3} fill="var(--elev-bg)" />
          <line x1={0} y1={top + 7} x2={12} y2={bot - 8} />
        </>
      );
    default: {
      const h = Math.min(s, 34);
      return (
        <>
          {leads(m - h / 2, m + h / 2)}
          <rect x={-10} y={m - h / 2} width={20} height={h} fill="var(--elev-bg)" />
        </>
      );
    }
  }
}

function Label({
  x,
  y,
  align,
  color,
  text,
  small,
  fresh,
  sign,
}: {
  x: number;
  y: number;
  align: "left" | "right" | "center";
  color?: string;
  text: string;
  small?: boolean;
  fresh?: boolean;
  sign?: boolean;
}) {
  const shift = align === "left" ? "0" : align === "right" ? "-100%" : "-50%";
  return (
    <div
      className={`elev-label ${small ? "small" : ""} ${fresh ? "fresh" : ""} ${sign ? "sign" : ""}`}
      style={{ left: x, top: y, transform: `translate(${shift}, -50%)`, color }}
    >
      {sign ? text : <Markdown text={text} inline />}
    </div>
  );
}

/** Scale a diagram of natural width `width` down to the space available (not below 60%, then it scrolls). */
function useFit(width: number) {
  const ref = useRef<HTMLDivElement>(null);
  const [avail, setAvail] = useState<number | null>(null);
  useLayoutEffect(() => {
    const el = ref.current;
    if (!el) return;
    const update = () => setAvail(el.clientWidth);
    update();
    const observer = new ResizeObserver(update);
    observer.observe(el);
    return () => observer.disconnect();
  }, []);
  return { ref, k: avail ? Math.max(0.6, Math.min(1, avail / width)) : 1 };
}

function Diagram({
  view,
  supply = [],
  straight = false,
  reveal = NONE,
}: {
  view: View;
  supply?: Rail[];
  straight?: boolean;
  reveal?: Reveal;
}) {
  const { ys, y, placed, width, height, lastX } = useMemo(() => layout(view), [view]);
  const fit = useFit(width);
  const node = (name: string) => view.nodes.get(name);

  // Rails: one horizontal wire per node through all its element ends.
  const ends = new Map<string, number[]>();
  for (const p of placed) {
    ends.set(p.el.a, [...(ends.get(p.el.a) ?? []), p.xa]);
    ends.set(p.el.b, [...(ends.get(p.el.b) ?? []), p.xb]);
  }

  // Axis labels, one per height; a level not yet worked out reads "?".
  const axis = new Map<number, string[]>();
  const freshHeights = new Set<number>();
  for (const n of view.nodes.values()) {
    const list = axis.get(n.h) ?? [];
    const text = reveal.hidden.has(n.name) ? masked(n.label) : n.label;
    if (!list.includes(text)) list.push(text);
    axis.set(n.h, list);
    if (reveal.fresh.has(n.name)) freshHeights.add(n.h);
  }

  const labels: React.ReactNode[] = [];
  const shapes: React.ReactNode[] = [];

  placed.forEach((p, i) => {
    const { el, flat, xa, xb, ya, yb } = p;
    const len = flat ? xb - xa : Math.abs(yb - ya);
    const rotate = flat ? -90 : yb < ya ? 180 : 0;
    shapes.push(
      <g key={`e${i}`} transform={`translate(${xa} ${ya}) rotate(${rotate})`}>
        <Symbol kind={el.kind} len={len} />
      </g>,
    );
    // "$9\,\Omega$: falls $18\,\mathrm{V}$" shows only "$9\,\Omega$" until a step works the element out.
    const pending = !!el.id && reveal.hidden.has(el.id);
    const text = pending && el.label.includes(": ") ? el.label.slice(0, el.label.indexOf(": ")) : el.label;
    const isNewEl = !!el.id && reveal.fresh.has(el.id) && text.includes(": ");
    if (flat) {
      if (text)
        labels.push(<Label key={`l${i}`} x={(xa + xb) / 2} y={ya - 24} align="center" text={text} fresh={isNewEl} />);
    } else if (text) {
      labels.push(<Label key={`l${i}`} x={xa + 26} y={(ya + yb) / 2} align="left" text={text} fresh={isNewEl} />);
    }
    // Polarity marks beside the body: the drawing's own reference (blue, named), or else the actual
    // polarity (+ on the higher end). Voltage sources and diamonds already carry signs in their symbol.
    if (!flat) {
      const na = node(el.a);
      const nb = node(el.b);
      const reference = !!el.plus;
      let plus = el.plus;
      if (!plus && el.kind === "B") plus = el.a;
      else if (!plus && !"VEW".includes(el.kind) && na && nb && !na.unknown && !nb.unknown && na.h !== nb.h) {
        // Until a step has placed both ends, the actual polarity would give the answer away.
        const secret = (!!el.id && reveal.hidden.has(el.id)) || reveal.hidden.has(el.a) || reveal.hidden.has(el.b);
        if (!secret) plus = na.h > nb.h ? el.a : el.b;
      }
      if (plus) {
        const mid = (ya + yb) / 2;
        const off = Math.max(8, Math.min(bodyHalf(el.kind, len) + 11, len / 2 - 12));
        const toward = (plus === el.a ? ya : yb) < mid ? -1 : 1;
        const color = reference ? REFERENCE : undefined;
        labels.push(
          <Label key={`p${i}`} x={xa + 18} y={mid + toward * off} align="center" color={color} text="+" sign />,
        );
        labels.push(
          <Label key={`n${i}`} x={xa + 18} y={mid - toward * off} align="center" color={color} text="−" sign />,
        );
        if (reference && el.vname)
          labels.push(
            <Label key={`v${i}`} x={xa + 29} y={mid + toward * off} align="left" color={color} text={el.vname} />,
          );
      }
    }
    if (el.cur && el.to && !(el.id && reveal.hidden.has(el.id))) {
      const from = el.to === el.a ? el.b : el.a;
      const hFrom = node(from)?.h ?? 0;
      const hTo = node(el.to)?.h ?? 0;
      // A node with an undetermined potential makes "uphill" meaningless, so stay neutral.
      const undetermined = node(from)?.unknown || node(el.to)?.unknown;
      const color = undetermined ? "var(--ink-3)" : hFrom > hTo ? ABSORB : hFrom < hTo ? DELIVER : "var(--ink-3)";
      const [fx, fy] = from === el.a ? [xa, ya] : [xb, yb];
      const [tx, ty] = from === el.a ? [xb, yb] : [xa, ya];
      // Arrow sits beside the element's middle (left of it, or below a flat one), pointing along the
      // actual flow, so it never covers the symbol even on a short element.
      const ax = (fx + tx) / 2 - (flat ? 0 : 28);
      const ay = (fy + ty) / 2 + (flat ? 16 : 0);
      const angle = (Math.atan2(ty - fy, tx - fx) * 180) / Math.PI;
      shapes.push(
        <g key={`c${i}`} transform={`translate(${ax} ${ay}) rotate(${angle})`} fill={color} stroke="none">
          <path d="M 7 0 L -6 -6 L -6 6 Z" />
        </g>,
      );
      const isNew = !!el.id && reveal.fresh.has(el.id);
      labels.push(
        flat ? (
          <Label key={`i${i}`} x={ax} y={ay + 18} align="center" color={color} text={el.cur} small fresh={isNew} />
        ) : (
          <Label key={`i${i}`} x={ax - 12} y={ay} align="right" color={color} text={el.cur} small fresh={isNew} />
        ),
      );
    }
  });

  // Something attached at x leaves this level going down (side = 1) or up (side = -1).
  const leaves = (x: number, yy: number, side: 1 | -1) =>
    placed.some(
      (p) => !p.flat && p.xa === x && (side === 1 ? Math.max(p.ya, p.yb) > yy + 1 : Math.min(p.ya, p.yb) < yy - 1),
    );

  const rails: React.ReactNode[] = [];
  const ground = (key: string, x: number, yy: number) => {
    const below = !leaves(x, yy, 1);
    const gx = below ? x : x - 26;
    if (!below) rails.push(<line key={`gs${key}`} x1={x} y1={yy} x2={gx} y2={yy} />);
    rails.push(
      <g key={`g${key}`} transform={`translate(${gx} ${yy})`}>
        <line x1={0} y1={0} x2={0} y2={10} />
        <line x1={-10} y1={10} x2={10} y2={10} />
        <line x1={-6} y1={14} x2={6} y2={14} />
        <line x1={-2.5} y1={18} x2={2.5} y2={18} />
      </g>,
    );
  };
  for (const [name, xs] of ends) {
    const n = node(name);
    if (!n) continue;
    const yy = y(name);
    const lo = Math.min(...xs);
    const hi = Math.max(...xs);
    // In the straight-line view every branch runs into its own ground instead of a return wire.
    if (straight && n.ground) {
      for (const x of new Set(xs)) ground(`${name}${x}`, x, yy);
      continue;
    }
    if (hi > lo)
      rails.push(
        <line key={`r${name}`} x1={lo} y1={yy} x2={hi} y2={yy} strokeDasharray={n.unknown ? "6 5" : undefined} />,
      );
    const counts = new Map<number, number>();
    xs.forEach((x) => counts.set(x, (counts.get(x) ?? 0) + 1));
    for (const x of new Set(xs)) {
      if ((x > lo && x < hi) || (counts.get(x)! >= 2 && hi > lo))
        rails.push(<circle key={`d${name}${x}`} cx={x} cy={yy} r={3.2} fill="currentColor" />);
    }
    if (n.ground) ground(name, lo, yy);
    // A terminal (e.g. a of a Thevenin pair a-b) ends in a short lead and an open circle on the right.
    if (n.terminal) {
      rails.push(<line key={`tl${name}`} x1={hi} y1={yy} x2={hi + 34} y2={yy} />);
      rails.push(<circle key={`tc${name}`} cx={hi + 38} cy={yy} r={4} fill="var(--elev-bg)" />);
    }
  }

  // Supply rails: a bar with the node's voltage where the source used to be, like "9 V" chalked
  // above a resistor. It sits on the side of the level that nothing else uses.
  supply.forEach((rail, i) => {
    let s = rail;
    const xs = ends.get(s.node);
    if (!xs) return;
    const x = Math.min(...xs);
    const yy = y(s.node);
    if (reveal.hidden.has(s.node)) s = { ...s, label: "?" };
    if (s.el && reveal.hidden.has(s.el)) s = { ...s, sub: undefined };
    // When the level runs on sideways from here, a bar on top would sit on that element's label:
    // feed the rail in from the left instead, as a short stub ending in an upright bar.
    if (placed.some((p) => p.flat && p.ya === yy && Math.min(p.xa, p.xb) === x)) {
      const bx = x - 36;
      rails.push(
        <g key={`s${i}`}>
          <line x1={x} y1={yy} x2={bx} y2={yy} />
          <line x1={bx} y1={yy - 16} x2={bx} y2={yy + 16} strokeWidth={3.2} />
        </g>,
      );
      labels.push(<Label key={`sl${i}`} x={bx - 10} y={yy} align="right" text={s.label} small />);
      if (s.sub)
        labels.push(<Label key={`ss${i}`} x={bx} y={yy + 30} align="center" color={s.color} text={s.sub} small />);
      return;
    }
    const dir = leaves(x, yy, -1) ? 1 : -1; // -1: bar above the level
    const by = yy + dir * 22;
    rails.push(
      <g key={`s${i}`}>
        <line x1={x} y1={yy} x2={x} y2={by} />
        <line x1={x - 18} y1={by} x2={x + 18} y2={by} strokeWidth={3.2} />
      </g>,
    );
    labels.push(<Label key={`sl${i}`} x={x} y={by + dir * 14} align="center" text={s.label} small />);
    if (s.sub) labels.push(<Label key={`ss${i}`} x={x + 26} y={by} align="left" color={s.color} text={s.sub} small />);
  });

  const mismatch = view.mismatches.map((mm, i) => {
    const y1 = y(mm.a);
    const y2 = y(mm.b);
    const x = lastX + 60 + i * 30;
    const endA = Math.max(...(ends.get(mm.a) ?? [lastX]));
    const endB = Math.max(...(ends.get(mm.b) ?? [lastX]));
    labels.push(<Label key={`m${i}`} x={x + 12} y={(y1 + y2) / 2} align="left" color="#c0392b" text={mm.text} small />);
    return (
      <g key={`mm${i}`} stroke="#c0392b" strokeDasharray="5 4">
        <line x1={endA} y1={y1} x2={x} y2={y1} />
        <line x1={endB} y1={y2} x2={x} y2={y2} />
        <line x1={x} y1={y1} x2={x} y2={y2} strokeDasharray={undefined} strokeWidth={2} />
      </g>
    );
  });

  const k = fit.k;
  return (
    <div ref={fit.ref} className="elev-fit">
      <div
        style={{
          width: width * k,
          height: height * k,
          margin: "0 auto",
          position: "relative",
        }}
      >
        <div
          className="elev-canvas"
          style={{
            width,
            height,
            position: "absolute",
            left: 0,
            top: 0,
            transform: k < 1 ? `scale(${k})` : undefined,
            transformOrigin: "0 0",
          }}
        >
          <svg width={width} height={height} className="elev-svg">
            <g className="elev-guides">
              {[...ys.entries()].map(([h, yy]) => (
                <line key={h} x1={AXIS} y1={yy} x2={width - 10} y2={yy} />
              ))}
            </g>
            <line className="elev-axis" x1={AXIS} y1={TOP - 24} x2={AXIS} y2={height - 30} />
            <path
              className="elev-axis"
              d={`M ${AXIS - 5} ${TOP - 16} L ${AXIS} ${TOP - 26} L ${AXIS + 5} ${TOP - 16}`}
              fill="none"
            />
            <g className="elev-ink">
              {rails}
              {shapes}
              {mismatch}
            </g>
          </svg>
          <div className="elev-axis-title">voltage (height)</div>
          {[...ys.entries()].map(([h, yy]) => (
            <Label
              key={`a${h}`}
              x={AXIS - 10}
              y={yy}
              align="right"
              text={mergeLabels(axis.get(h) ?? [])}
              small
              fresh={freshHeights.has(h)}
            />
          ))}
          {labels}
        </div>
      </div>
    </div>
  );
}

/** Labels of nodes at one level: "a: 12 V" and "b: 12 V" become "a, b: 12 V"; a bare "12 V" joins them. */
function mergeLabels(texts: string[]) {
  const byValue = new Map<string, string[]>();
  const bare: string[] = [];
  for (const text of texts) {
    const at = text.indexOf(": ");
    if (at < 0) bare.push(text);
    else byValue.set(text.slice(at + 2), [...(byValue.get(text.slice(at + 2)) ?? []), text.slice(0, at)]);
  }
  return [
    ...[...byValue].map(([value, names]) => `${[...new Set(names)].join(", ")}: ${value}`),
    ...bare.filter((text) => !byValue.has(text)),
  ].join(", ");
}

export function ElevationDialog({ spec, onClose }: { spec: Elevation; onClose: () => void }) {
  const [tab, setTab] = useState(0);
  const [revealed, setRevealed] = useState(!spec.spoiler);
  const [mode, setMode] = useState<"straight" | "loop">(() => {
    try {
      return localStorage.getItem(MODE_KEY) === "straight" ? "straight" : "loop";
    } catch {
      return "loop";
    }
  });
  const view = spec.views[Math.min(tab, spec.views.length - 1)];
  const total = view.steps.length;
  // Step k shows what steps 1..k have worked out; `total` is the finished picture.
  const [step, setStep] = useState(spec.views[0].steps.length);
  const reveal = useMemo(() => revealAt(view, step), [view, step]);
  const openTab = (i: number) => {
    setTab(i);
    setStep(spec.views[i].steps.length);
  };
  const straight = useMemo(() => straighten(view), [view]);
  const showStraight = mode === "straight" && straight;
  const level = (n: string) => view.nodes.get(n);
  const cues = {
    grey: view.els.some(
      (e) => e.cur && e.to && (level(e.a)?.h === level(e.b)?.h || level(e.a)?.unknown || level(e.b)?.unknown),
    ),
    floating: [...view.nodes.values()].some((n) => n.unknown),
    mismatch: view.mismatches.length > 0,
    grounds: showStraight || [...view.nodes.values()].filter((n) => n.ground).length > 1,
  };
  const choose = (next: "straight" | "loop") => {
    setMode(next);
    try {
      localStorage.setItem(MODE_KEY, next);
    } catch {
      // the choice just isn't remembered
    }
  };
  return (
    <Dialog title="Height view: voltage as height" onClose={onClose} className="elev-dialog">
      <div className="dialog-body elev-body">
        <div className="elev-controls">
          {spec.views.length > 1 && (
            <div className="elev-tabs" role="tablist">
              {spec.views.map((v, i) => (
                <button
                  key={i}
                  role="tab"
                  aria-selected={i === tab}
                  className={i === tab ? "active" : ""}
                  onClick={() => openTab(i)}
                >
                  <Markdown text={v.title} inline />
                </button>
              ))}
            </div>
          )}
          {straight && (
            <div className="elev-mode" role="group" aria-label="Drawing style">
              <button
                className={mode === "loop" ? "active" : ""}
                onClick={() => choose("loop")}
                title="Draw every source, so each loop is closed"
              >
                Full loop
              </button>
              <button
                className={mode === "straight" ? "active" : ""}
                onClick={() => choose("straight")}
                title="Grounded sources become labelled supply rails; the circuit hangs from them down to ground"
              >
                Straight line
              </button>
            </div>
          )}
        </div>
        <div className={`elev-stage ${revealed ? "" : "hidden-answer"}`}>
          <div className="elev-scroll">
            {showStraight ? (
              <Diagram view={straight.view} supply={straight.rails} straight reveal={reveal} />
            ) : (
              <Diagram view={view} reveal={reveal} />
            )}
          </div>
          {total > 0 && (
            <div className="elev-steps">
              <div className="elev-steps-head">
                <span className="elev-steps-title">Solve with heights</span>
                <span className="elev-steps-count">
                  {step}/{total}
                </span>
                <div className="elev-steps-buttons">
                  <button onClick={() => setStep(0)} disabled={step === 0} title="Start from the given values only">
                    <RotateCcw size={14} /> Restart
                  </button>
                  <button onClick={() => setStep(step - 1)} disabled={step === 0}>
                    <ChevronLeft size={14} /> Back
                  </button>
                  <button className="primary" onClick={() => setStep(step + 1)} disabled={step >= total}>
                    Next step <ChevronRight size={14} />
                  </button>
                  <button onClick={() => setStep(total)} disabled={step >= total}>
                    Show all
                  </button>
                </div>
              </div>
              {step === 0 ? (
                <p className="elev-steps-hint">
                  Only the given values are drawn; every <b>?</b> is still unknown. The level with the ⏚ symbol is
                  ground (0 V). The steps always run in the same order: ground, fixed heights, currents, the rest of the
                  heights, then the answer and its checks. Each step fills in one more height or current.
                </p>
              ) : (
                <ol className="elev-step-list">
                  {view.steps.slice(0, step).map((s, k) => (
                    <li key={k} className={k === step - 1 && step < total ? "current" : ""}>
                      <Markdown text={s.text} inline />
                    </li>
                  ))}
                </ol>
              )}
            </div>
          )}
          {view.notes.length > 0 && step >= total && (
            <ul className="elev-notes">
              {view.notes.map((n, i) => (
                <li key={i}>
                  <Markdown text={n} inline />
                </li>
              ))}
            </ul>
          )}
          {!revealed && (
            <div className="elev-spoiler">
              <p>This view shows the solved circuit, so it gives the answer away. Try the problem first.</p>
              <div className="elev-spoiler-buttons">
                {total > 0 && (
                  <button
                    className="primary"
                    onClick={() => {
                      setStep(0);
                      setRevealed(true);
                    }}
                  >
                    <ChevronRight size={15} /> Walk me through it
                  </button>
                )}
                <button className={total > 0 ? "" : "primary"} onClick={() => setRevealed(true)}>
                  <Eye size={15} /> Show the answer
                </button>
              </div>
            </div>
          )}
        </div>
        <div className="elev-legend">
          <span>
            <i style={{ color: ABSORB }}>▼</i> current flows <b>downhill</b> through the element: it <b>absorbs</b>{" "}
            energy
          </span>
          <span>
            <i style={{ color: DELIVER }}>▲</i> current flows <b>uphill</b>: the element <b>delivers</b> energy
          </span>
          <span>
            <b>+ −</b> actual polarity: + is the higher end. <b style={{ color: REFERENCE }}>+ −</b> the drawing's
            reference for a named voltage: when its + sits on the lower end, that voltage is negative
          </span>
          {showStraight && (
            <span>
              <b>━</b> a bar with a voltage is a <b>supply rail</b>: a source to ground holds that point at that voltage
              (switch to Full loop to see the source)
            </span>
          )}
          {cues.grey && (
            <span>
              <i style={{ color: "var(--ink-3)" }}>{"▶︎"}</i> grey arrow: the current's direction only. The element is
              flat (no height change, so no energy changes hands) or one end floats (its power can't be found)
            </span>
          )}
          {cues.floating && (
            <span>
              <b>- - -</b> a dashed level <b>floats</b>: nothing fixes its height, so it is drawn at an arbitrary place
            </span>
          )}
          {cues.mismatch && (
            <span>
              <b style={{ color: "#c0392b" }}>]</b> red bracket: two levels that would have to be one node, so the
              connection is <b>invalid</b>
            </span>
          )}
          {cues.grounds && (
            <span>
              <b>⏚</b> every ground symbol is the same 0 V node, drawn once per branch
            </span>
          )}
          <span className="elev-scale">
            {view.illustrative
              ? "Symbolic values: heights show which point is higher, not exact amounts."
              : "Height is the voltage measured from ground (0 V). Drawn to scale, except that levels very close together are spread apart so they stay readable."}
          </span>
        </div>
      </div>
    </Dialog>
  );
}

/** The finished first view drawn in the page, under its circuit, with a one-line legend (Full loop form). */
export function ElevationInline({ spec }: { spec: Elevation }) {
  const view = spec.views[0];
  return (
    <div className="elev-inline">
      <div className="elev-inline-title">In heights (voltage = height, ground = 0 V)</div>
      <div className="elev-scroll">
        <Diagram view={view} />
      </div>
      <div className="elev-inline-legend">
        <span>
          <i style={{ color: ABSORB }}>▼</i> falls through it: <b>absorbs</b>
        </span>
        <span>
          <i style={{ color: DELIVER }}>▲</i> climbs through it: <b>delivers</b>
        </span>
      </div>
    </div>
  );
}

export function ElevationButton({ onClick }: { onClick: () => void }) {
  return (
    <button
      className="elev-open"
      onClick={onClick}
      title="Show this circuit with voltage as height"
      aria-label="Open height view"
    >
      <ArrowUpDown size={14} />
      Height view
    </button>
  );
}
