/*
 * Current-flow simulation for a schematic drawing (the `#~` lines; grammar in skills/schematic.md "Current flow").
 *
 * The drawing is read in the same coordinates the server renders it in: elements are two-point segments, wires are
 * polylines, and a point lying inside a wire segment joins it (a T junction). Wires merge points into electrical nodes;
 * elements become modified-nodal-analysis stamps. Inductors and capacitors are stepped with backward Euler, so a
 * switch can be flipped at any moment and the transient plays out. Wire currents come from KCL on each node's wire
 * tree, so every drawn segment knows how much current it carries and which way.
 */

export type Pt = [number, number];
export type Kind = "R" | "V" | "I" | "L" | "C" | "S" | "W" | "OPEN";
export type Elem = { name: string; kind: Kind; a: Pt; b: Pt; value: number; closed: boolean; label: string; vlabel: string };
export type Seg = { a: Pt; b: Pt; elem?: string };
/** A readout: an element's current ("i", also plotted) or its voltage ("v", readout only). */
export type Probe = { name: string; label: string; what: "i" | "v" };
export type FlowSpec = {
  elems: Elem[];
  wires: Seg[];
  ground?: Pt;
  slow: number;
  probes: Probe[];
  groups: string[][]; // switches that move together (same label in the drawing, or a #~ gang line)
  init: Record<string, number>; // starting capacitor voltage or inductor current, overriding DC steady state
  note?: string;
};

const EPS = 1e-6;
const key = (p: Pt) => `${Math.round(p[0] * 1e4) / 1e4},${Math.round(p[1] * 1e4) / 1e4}`;

function tokens(line: string): string[] {
  const out: string[] = [];
  const re = /"([^"]*)"|(\S+)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(line))) out.push(m[1] ?? m[2]);
  return out;
}

const point = (t: string): Pt | null => {
  const m = /^\(?(-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)?$/.exec(t);
  return m ? [Number(m[1]), Number(m[2])] : null;
};

const PREFIX: Record<string, number> = { p: 1e-12, n: 1e-9, u: 1e-6, m: 1e-3, "": 1, k: 1e3, M: 1e6, G: 1e9 };

/** 8m, 2.5k, 10u, 1e-3: a number with an optional SI prefix. */
export function siValue(t: string): number {
  const m = /^(-?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*([pnumkMG]?)$/.exec(t.replace("µ", "u"));
  if (!m) return NaN;
  return Number(m[1]) * PREFIX[m[2]];
}

const UNIT: Partial<Record<Kind, string>> = { R: "Ω", V: "V", I: "A", L: "H", C: "F" };
// a symbolic label ($R$, $V_s$) gets a stand-in value; together these give every RC and RL pair τ = 1 ms
const STAND_IN: Partial<Record<Kind, number>> = { R: 1e3, V: 10, I: 10e-3, L: 1, C: 1e-6 };
const WORD: Partial<Record<Kind, string>> = { R: "resistor", L: "inductor", C: "capacitor", V: "source", I: "source", W: "ammeter" };

/** The value written in a drawing label: "$4\,\mathrm{k\Omega}$" -> 4000, "$2\,\mu\mathrm{F}$" -> 2e-6. NaN if symbolic. */
export function labelValue(label: string, kind: Kind): number {
  const s = label
    .replace(/\$/g, "")
    .replace(/\\(?:mathrm|text|textrm|rm)\s*\{([^}]*)\}/g, "$1")
    .replace(/\\Omega/g, "Ω")
    .replace(/\\mu\s*|µ|μ/g, "u")
    .replace(/\\[,;:! ]|~|[{}\s]/g, "");
  const m = /^(-?\d*\.?\d+(?:[eE][-+]?\d+)?)([pnumkMG]?)(Ω|V|A|H|F)?$/.exec(s);
  if (!m || (m[3] && m[3] !== UNIT[kind])) return NaN;
  return Number(m[1]) * PREFIX[m[2]];
}

/** 1000 -> "1 kΩ", 1e-6 -> "1 µF" */
export function fmtSI(v: number, unit: string): string {
  if (!v) return `0 ${unit}`;
  const steps: [number, string][] = [[1e9, "G"], [1e6, "M"], [1e3, "k"], [1, ""], [1e-3, "m"], [1e-6, "µ"], [1e-9, "n"], [1e-12, "p"]];
  const [scale, p] = steps.find(([s]) => Math.abs(v) >= s * 0.9995) ?? [1e-12, "p"];
  return `${Number((v / scale).toPrecision(3))} ${p}${unit}`; // no line break inside "1 kΩ"
}

const KINDS: [string, Kind][] = [["AM", "W"], ["VM", "OPEN"], ["R", "R"], ["C", "C"], ["L", "L"], ["V", "V"], ["I", "I"], ["B", "V"], ["S", "S"]];

/**
 * Read the drawing plus `#~` lines. Returns null when the source has no `#~ flow` line.
 * `#~ flow` alone is enough: values come from the labels (symbols get stand-ins, listed in the note), the slow-motion
 * factor from the time constants, readouts from the L, C and R elements, and switches with the same label move together.
 */
export function parseFlow(source: string): FlowSpec | string | null {
  const lines = source.split(/\r?\n/);
  if (!lines.some((l) => /^\s*#~\s*flow\b/.test(l))) return null;
  const values: Record<string, number> = {};
  const spec: FlowSpec = { elems: [], wires: [], slow: 0, probes: [], groups: [], init: {} };
  const gangs: string[][] = [];
  const standIns: string[] = [];
  // two passes: the #~ lines (usually at the end) first, so element values are known when elements are read
  const ordered = [...lines.filter((l) => /^\s*#~/.test(l)), ...lines.filter((l) => !/^\s*#~/.test(l))];
  for (const raw of ordered) {
    const flow = /^\s*#~\s?(.*)$/.exec(raw);
    if (flow) {
      const [kw, ...rest] = tokens(flow[1]);
      if (kw === "value" || kw === "init") {
        const v = siValue(rest[1] ?? "");
        if (!rest[0] || !Number.isFinite(v)) return `#~ ${kw} needs a name and a number: ${flow[1]}`;
        (kw === "value" ? values : spec.init)[rest[0].toUpperCase()] = v;
      } else if (kw === "slow") spec.slow = Math.max(1, siValue(rest[0] ?? "1") || 1);
      else if (kw === "probe" && rest[0]) {
        const what = rest[1] === "v" || rest[1] === "i" ? (rest.splice(1, 1)[0] as "i" | "v") : "i";
        spec.probes.push({ name: rest[0].toUpperCase(), label: rest[1] ?? "", what });
      } else if (kw === "gang") gangs.push(rest.map((r) => r.toUpperCase()));
      else if (kw === "note") spec.note = rest.join(" ");
      continue;
    }
    if (/^\s*#/.test(raw) || !raw.trim()) continue;
    const t = tokens(raw.replace(/\s#.*$/, ""));
    const head = t[0];
    const word = head.toLowerCase();
    const pts: Pt[] = [];
    for (let i = 1; i < t.length; i++) {
      const p = point(t[i]);
      if (p && (i === 1 || t[i - 1] === "->")) pts.push(p);
    }
    if (word === "wire") {
      for (let i = 0; i + 1 < pts.length; i++) spec.wires.push({ a: pts[i], b: pts[i + 1] });
    } else if (word === "ground") {
      if (pts[0] && !spec.ground) spec.ground = pts[0];
    } else if (["gap", "dot", "terminal", "label"].includes(word)) {
      continue;
    } else if (pts.length === 2) {
      const kind = KINDS.find(([p]) => head.toUpperCase().startsWith(p))?.[1];
      if (!kind) return `${head}: current flow supports R, L, C, V, I, B, S, AM and VM elements only`;
      const opts = Object.fromEntries([...raw.matchAll(/(\w+)=("[^"]*"|\S+)/g)].map((m) => [m[1], m[2].replace(/^"|"$/g, "")]));
      const name = head.toUpperCase();
      const label = /(?<!=)"([^"]*)"/.exec(raw)?.[1] ?? ""; // the element's own label, not an option value like i="..."
      let value = values[name];
      if (UNIT[kind] && !Number.isFinite(value)) {
        value = labelValue(label, kind);
        if (!Number.isFinite(value)) {
          value = STAND_IN[kind]!;
          standIns.push(`${label || head} = ${fmtSI(value, UNIT[kind]!)}`);
        }
      }
      if (kind === "R" && !(value > 0)) return `${head} must be a positive resistance`;
      // a switch that opens at t = 0 was closed before it, unless the drawing says otherwise
      const closed = opts.state ? opts.state === "closed" : opts.action === "open";
      spec.elems.push({ name, kind, a: pts[0], b: pts[1], value: value ?? 0, closed, label, vlabel: opts.v ?? opts.v_rev ?? "" });
    }
  }
  const byName = new Map(spec.elems.map((e) => [e.name, e]));
  for (const p of spec.probes) if (!byName.has(p.name)) return `#~ probe ${p.name}: no such element`;
  for (const n of [...Object.keys(spec.init), ...gangs.flat()]) if (!byName.has(n)) return `#~ ${n}: no such element`;

  // switch groups: #~ gang lines first, then switches sharing a label ("$t=0$" twice is one switch drawn as two)
  const placed = new Set(gangs.flat());
  spec.groups = gangs.filter((g) => g.length);
  const byLabel = new Map<string, string[]>();
  for (const s of spec.elems.filter((e) => e.kind === "S" && !placed.has(e.name)))
    byLabel.set(s.label || s.name, [...(byLabel.get(s.label || s.name) ?? []), s.name]);
  spec.groups.push(...byLabel.values());

  if (!spec.probes.length) spec.probes = autoProbes(spec.elems);
  for (const p of spec.probes) if (!p.label) p.label = probeLabel(byName.get(p.name)!, p.what);
  if (!spec.slow) spec.slow = autoSlow(spec);
  if (spec.note === undefined) {
    spec.note = "Dots show the current: faster dots, more current.";
    if (standIns.length) spec.note += ` Symbols set to: ${standIns.join(", ")}.`;
    const starts = Object.entries(spec.init).map(([n, v]) => {
      const e = byName.get(n)!;
      return e.kind === "C" ? `${e.vlabel || e.label || n} = ${fmtSI(v, "V")}` : `${e.label || n} carries ${fmtSI(v, "A")}`;
    });
    if (starts.length) spec.note += ` Starts with ${starts.join(", ")}.`;
  }
  return spec;
}

/** Up to three currents (inductors, capacitors, then resistors) plus each capacitor's voltage. */
function autoProbes(elems: Elem[]): Probe[] {
  const rank: Partial<Record<Kind, number>> = { L: 0, C: 1, R: 2 };
  const cur = elems.filter((e) => e.kind in rank).sort((p, q) => rank[p.kind]! - rank[q.kind]!).slice(0, 3);
  const volt = elems.filter((e) => e.kind === "C").slice(0, 2);
  return [...cur.map((e) => ({ name: e.name, label: "", what: "i" as const })), ...volt.map((e) => ({ name: e.name, label: "", what: "v" as const }))];
}

function probeLabel(e: Elem, what: "i" | "v"): string {
  const own = e.label.replace(/\$/g, "").trim() ? e.label : e.name;
  if (what === "v") return e.vlabel ? `${WORD[e.kind] ?? ""} voltage ${e.vlabel}:` : `voltage on ${own}:`;
  return `${WORD[e.kind] ?? e.name} ${own}:`;
}

/**
 * Slow motion so the slowest time constant plays over about 2 s: τ from the resistance each L or C sees (sources
 * off, the other L short, the other C open), before and after the switches move, rounded to 1, 2 or 5 × 10^k.
 */
function autoSlow(spec: FlowSpec): number {
  const taus: number[] = [];
  const configs = [false, true].map((flipped) =>
    Object.fromEntries(spec.elems.filter((e) => e.kind === "S").map((e) => [e.name, flipped !== e.closed])),
  );
  for (const target of spec.elems.filter((e) => e.kind === "L" || e.kind === "C")) {
    for (const closed of configs) {
      const rth = seenResistance(spec, target, closed);
      if (target.kind === "C" && rth < 1e7) taus.push(rth * target.value);
      if (target.kind === "L" && rth > 1e-2 && rth < 1e7) taus.push(target.value / rth);
    }
  }
  const tau = Math.max(0, ...taus.filter((x) => x > 0));
  if (!tau) return 1;
  const want = Math.log10(2 / tau);
  const nice = [1, 2, 5, 10].map((m) => Math.floor(want) + Math.log10(m));
  const best = nice.reduce((p, q) => (Math.abs(q - want) < Math.abs(p - want) ? q : p));
  return Math.max(1, Math.round(10 ** best));
}

/** The resistance an element sees with every source off (other L short, other C open): a 1 A test source in its place. */
export function seenResistance(spec: FlowSpec, target: Elem, closed: Record<string, boolean>): number {
  const test: FlowSpec = {
    ...spec,
    elems: spec.elems.map((e) =>
      e === target ? { ...e, kind: "I" as Kind, value: 1 } : e.kind === "V" || e.kind === "I" ? { ...e, value: 0 } : e,
    ),
  };
  return Math.abs(new Circuit(test).dc({ t: 0, iL: {}, vC: {}, closed }).v[target.name]);
}

/** Inductors still carrying current (above `floor`) that the present switch positions leave with no path. */
export function cutInductors(spec: FlowSpec, s: State, floor: number): string[] {
  return spec.elems
    .filter((e) => e.kind === "L" && Math.abs(s.iL[e.name] ?? 0) > floor && seenResistance(spec, e, s.closed) > 1e6)
    .map((e) => e.name);
}

function onSegment(p: Pt, a: Pt, b: Pt) {
  const cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]);
  if (Math.abs(cross) > EPS * Math.max(1, Math.hypot(b[0] - a[0], b[1] - a[1]))) return false;
  const dot = (p[0] - a[0]) * (b[0] - a[0]) + (p[1] - a[1]) * (b[1] - a[1]);
  const len = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2;
  return dot > EPS && dot < len - EPS;
}

/** Linear solve with partial pivoting; returns null when singular. */
function solve(A: number[][], z: number[]): number[] | null {
  const n = z.length;
  const M = A.map((row, i) => [...row, z[i]]);
  for (let c = 0; c < n; c++) {
    let p = c;
    for (let r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r;
    if (Math.abs(M[p][c]) < 1e-15) return null;
    [M[c], M[p]] = [M[p], M[c]];
    for (let r = c + 1; r < n; r++) {
      const f = M[r][c] / M[c][c];
      if (f) for (let k = c; k <= n; k++) M[r][k] -= f * M[c][k];
    }
  }
  const x = new Array(n).fill(0);
  for (let r = n - 1; r >= 0; r--) {
    let s = M[r][n];
    for (let k = r + 1; k < n; k++) s -= M[r][k] * x[k];
    x[r] = s / M[r][r];
  }
  return x;
}

export type State = { t: number; iL: Record<string, number>; vC: Record<string, number>; closed: Record<string, boolean> };
export type Snapshot = { elem: Record<string, number>; seg: number[]; v: Record<string, number> };

export class Circuit {
  spec: FlowSpec;
  segs: Seg[] = []; // every drawn conductor piece: wire pieces, then one per element
  private node: Record<string, number> = {}; // point key -> electrical node (0 = ground)
  private nNodes = 0;
  private wireOf: number[][] = []; // electrical node -> indexes of its wire pieces

  constructor(spec: FlowSpec) {
    this.spec = spec;
    // points where something attaches: element and wire ends, plus the ground
    const ends: Pt[] = [];
    for (const e of spec.elems) ends.push(e.a, e.b);
    for (const w of spec.wires) ends.push(w.a, w.b);
    if (spec.ground) ends.push(spec.ground);
    // split wires at every attachment point that lies inside them (T junctions)
    for (const w of spec.wires) {
      const inside = ends.filter((p) => onSegment(p, w.a, w.b));
      const along = (p: Pt) => (p[0] - w.a[0]) * (w.b[0] - w.a[0]) + (p[1] - w.a[1]) * (w.b[1] - w.a[1]);
      const uniq = [...new Map(inside.map((p) => [key(p), p])).values()].sort((p, q) => along(p) - along(q));
      const chain = [w.a, ...uniq, w.b];
      for (let i = 0; i + 1 < chain.length; i++) this.segs.push({ a: chain[i], b: chain[i + 1] });
    }
    const nWire = this.segs.length;
    // union-find over wire pieces
    const parent: Record<string, string> = {};
    const find = (k: string): string => {
      parent[k] ??= k;
      while (parent[k] !== k) k = parent[k] = parent[parent[k]];
      return k;
    };
    for (const p of ends) find(key(p));
    for (let i = 0; i < nWire; i++) parent[find(key(this.segs[i].a))] = find(key(this.segs[i].b));
    const roots = new Map<string, number>();
    const groundRoot = spec.ground ? find(key(spec.ground)) : find(key(spec.elems[0]?.b ?? [0, 0]));
    roots.set(groundRoot, 0);
    for (const p of ends) {
      const r = find(key(p));
      if (!roots.has(r)) roots.set(r, roots.size);
      this.node[key(p)] = roots.get(r)!;
    }
    this.nNodes = roots.size;
    this.wireOf = Array.from({ length: this.nNodes }, () => []);
    for (let i = 0; i < nWire; i++) this.wireOf[this.node[key(this.segs[i].a)]].push(i);
    for (const e of spec.elems) this.segs.push({ a: e.a, b: e.b, elem: e.name });
  }

  initial(): State {
    const closed = Object.fromEntries(this.spec.elems.filter((e) => e.kind === "S").map((e) => [e.name, e.closed]));
    const s: State = { t: 0, iL: {}, vC: {}, closed };
    const dc = this.dc(s);
    for (const e of this.spec.elems) {
      if (e.kind === "L") s.iL[e.name] = dc.elem[e.name];
      if (e.kind === "C") s.vC[e.name] = dc.v[e.name];
      const start = this.spec.init[e.name];
      if (start !== undefined && e.kind === "L") s.iL[e.name] = start;
      if (start !== undefined && e.kind === "C") s.vC[e.name] = start;
    }
    return s;
  }

  /** DC steady state: inductors are wires, capacitors are open. */
  dc(s: State): Snapshot {
    return this.stamp(s, null);
  }

  /** One backward-Euler step of length h; updates s in place and returns the currents at the new time. */
  step(s: State, h: number): Snapshot {
    const snap = this.stamp(s, h);
    for (const e of this.spec.elems) {
      if (e.kind === "L") s.iL[e.name] = snap.elem[e.name];
      if (e.kind === "C") s.vC[e.name] = snap.v[e.name];
    }
    s.t += h;
    return snap;
  }

  /** Assemble and solve MNA. h = null is DC. Element currents run from a to b. */
  private stamp(s: State, h: number | null): Snapshot {
    const nV = this.nNodes - 1; // node 0 is ground
    const vsrc = this.spec.elems.filter((e) => e.kind === "V");
    const N = nV + vsrc.length;
    const A = Array.from({ length: N }, () => new Array(N).fill(0));
    const z = new Array(N).fill(0);
    const na = (e: Elem) => this.node[key(e.a)];
    const nb = (e: Elem) => this.node[key(e.b)];
    const G = (p: number, q: number, g: number) => {
      if (p) A[p - 1][p - 1] += g;
      if (q) A[q - 1][q - 1] += g;
      if (p && q) {
        A[p - 1][q - 1] -= g;
        A[q - 1][p - 1] -= g;
      }
    };
    const J = (p: number, q: number, i: number) => {
      // current i forced from p to q through the element: leaves node p, enters node q
      if (p) z[p - 1] -= i;
      if (q) z[q - 1] += i;
    };
    for (let k = 1; k <= nV; k++) A[k - 1][k - 1] += 1e-9; // gmin keeps floating nodes solvable
    const short = 1e-4;
    const cond: Record<string, number> = {};
    for (const e of this.spec.elems) {
      const p = na(e), q = nb(e);
      if (p === q) continue;
      switch (e.kind) {
        case "R":
          G(p, q, (cond[e.name] = 1 / e.value));
          break;
        case "W":
          G(p, q, (cond[e.name] = 1 / short));
          break;
        case "S":
          if (s.closed[e.name]) G(p, q, (cond[e.name] = 1 / short));
          break;
        case "I":
          J(p, q, e.value);
          break;
        case "L":
          if (h === null) G(p, q, (cond[e.name] = 1 / short));
          else {
            G(p, q, (cond[e.name] = h / e.value));
            J(p, q, s.iL[e.name] ?? 0);
          }
          break;
        case "C":
          if (h !== null) {
            G(p, q, (cond[e.name] = e.value / h));
            J(p, q, -(e.value / h) * (s.vC[e.name] ?? 0));
          }
          break;
      }
    }
    vsrc.forEach((e, k) => {
      const p = na(e), q = nb(e), r = nV + k;
      if (p) {
        A[p - 1][r] += 1;
        A[r][p - 1] += 1;
      }
      if (q) {
        A[q - 1][r] -= 1;
        A[r][q - 1] -= 1;
      }
      z[r] = e.value;
    });
    const x = solve(A, z) ?? new Array(N).fill(0);
    const V = (n: number) => (n ? x[n - 1] : 0);
    const elem: Record<string, number> = {};
    const v: Record<string, number> = {};
    for (const e of this.spec.elems) {
      const dv = V(na(e)) - V(nb(e));
      v[e.name] = dv;
      if (na(e) === nb(e)) elem[e.name] = 0;
      else if (e.kind === "I") elem[e.name] = e.value;
      else if (e.kind === "V") elem[e.name] = x[nV + vsrc.indexOf(e)]; // branch variable = current leaving node a into the source
      else if (e.kind === "L" && h !== null) elem[e.name] = (s.iL[e.name] ?? 0) + cond[e.name] * dv;
      else if (e.kind === "C") elem[e.name] = h === null ? 0 : cond[e.name] * dv - (e.value / h) * (s.vC[e.name] ?? 0);
      else elem[e.name] = (cond[e.name] ?? 0) * dv;
    }
    return { elem, v, seg: this.wireCurrents(elem) };
  }

  /** Current in every drawn piece (from its a to its b): elements from the solve, wires by KCL on each wire tree. */
  private wireCurrents(elem: Record<string, number>): number[] {
    const out = new Array(this.segs.length).fill(0);
    const nWire = this.segs.length - this.spec.elems.length;
    this.spec.elems.forEach((e, k) => (out[nWire + k] = elem[e.name]));
    // net current leaving the wire network into elements, per point: element current a->b leaves the wires at a
    const inj: Record<string, number> = {};
    for (const e of this.spec.elems) {
      inj[key(e.a)] = (inj[key(e.a)] ?? 0) - elem[e.name];
      inj[key(e.b)] = (inj[key(e.b)] ?? 0) + elem[e.name];
    }
    for (const pieces of this.wireOf) {
      if (!pieces.length) continue;
      const adj: Record<string, { to: string; seg: number; fwd: boolean }[]> = {};
      for (const i of pieces) {
        const ka = key(this.segs[i].a), kb = key(this.segs[i].b);
        (adj[ka] ??= []).push({ to: kb, seg: i, fwd: true });
        (adj[kb] ??= []).push({ to: ka, seg: i, fwd: false });
      }
      // spanning tree from the first point; each edge carries the injection of the subtree below it toward the root
      const root = key(this.segs[pieces[0]].a);
      const seen = new Set([root]);
      const order: { k: string; via?: { seg: number; fwd: boolean } }[] = [{ k: root }];
      for (let qi = 0; qi < order.length; qi++)
        for (const n of adj[order[qi].k] ?? [])
          if (!seen.has(n.to)) {
            seen.add(n.to);
            order.push({ k: n.to, via: { seg: n.seg, fwd: n.fwd } });
          }
      const sub: Record<string, number> = {};
      for (let qi = order.length - 1; qi > 0; qi--) {
        const { k, via } = order[qi];
        const total = (sub[k] ?? 0) + (inj[k] ?? 0);
        // flow from child k toward its parent; the piece runs parent->child when fwd
        out[via!.seg] = via!.fwd ? -total : total;
        const parentKey = via!.fwd ? key(this.segs[via!.seg].a) : key(this.segs[via!.seg].b);
        sub[parentKey] = (sub[parentKey] ?? 0) + total;
      }
    }
    return out;
  }
}
