import { Pause, Play, RotateCcw } from "lucide-react";
import { useEffect, useLayoutEffect, useMemo, useRef, useState } from "react";
import { Markdown } from "../Markdown";
import { Circuit, cutInductors, type FlowSpec, type Pt, type Snapshot, type State } from "./circuit";

/*
 * Current flow over a rendered schematic: dots stream along every wire and element at a speed set by the current,
 * switches can be flipped (button or click on the switch), and the transient plays in slow motion. The overlay uses
 * the server SVG's own coordinates: one grid unit is 36 SVG units, y up (schematic.py renders with schemdraw).
 */

const U = 36;
const GAP = 15; // SVG units between dots
const MAX_SPEED = 75; // SVG units per second at the largest current seen
const HISTORY = 8; // seconds of plot
const X = (p: Pt) => p[0] * U;
const Y = (p: Pt) => -p[1] * U;

// Readouts keep one unit and a fixed number of decimals while the numbers run, so the boxes never change width.
// Both come from the largest value the circuit reaches (a quick preview run), so they are right from the start.
type Unit = { scale: number; unit: string; digits: number };

function unitFor(max: number, base: "A" | "V"): Unit {
  const [scale, unit] = max >= 0.1 ? [1, base] : max >= 1e-4 ? [1e3, "m" + base] : [1e6, "µ" + base];
  const top = max * scale;
  return { scale, unit, digits: top >= 1000 ? 0 : top >= 100 ? 1 : 2 };
}

function fmt(x: number, u: Unit) {
  return `${(Math.abs(x) * u.scale).toFixed(u.digits)} ${u.unit}`;
}

/** One time unit from the slow-motion factor: what fits the visible few seconds of simulated time. */
function fmtT(t: number, slow: number) {
  return HISTORY / slow < 0.5 ? `${(t * 1e3).toFixed(2)} ms` : `${t.toFixed(3)} s`;
}

/**
 * A "t = 0" switch label follows the clock: t < 0 before the switch is touched, t = 0 for a moment as it moves,
 * t > 0 after. Any other label is shown as written.
 */
function switchLabel(label: string, S: { moved: boolean; events: number[]; clock: number }) {
  if (!/^\$?\s*t\s*=\s*0\s*\$?$/.test(label)) return label;
  if (!S.moved) return "$t<0$";
  const last = S.events[S.events.length - 1];
  return last !== undefined && S.clock - last < 0.6 ? "$t=0$" : "$t>0$";
}

/** The first non-transparent background behind an element, so a switch can be redrawn over the drawing. */
function backgroundOf(el: Element | null): string {
  for (let e = el; e; e = e.parentElement) {
    const c = getComputedStyle(e).backgroundColor;
    if (c && c !== "transparent" && !/rgba\(.*,\s*0\)$/.test(c)) return c;
  }
  return "white";
}

export function CurrentFlow({ url, spec, alt }: { url: string; spec: FlowSpec; alt: string }) {
  const circuit = useMemo(() => new Circuit(spec), [spec]);
  const plotted = useMemo(() => spec.probes.filter((p) => p.what === "i"), [spec]);
  const [viewBox, setViewBox] = useState<string | null>(null);
  const [bg, setBg] = useState("white");
  const wrap = useRef<HTMLDivElement>(null);
  const sim = useRef<{ s: State; snap: Snapshot; off: number[]; imax: number; vmax: number; cut: string[]; since: number; moved: boolean; hist: { t: number; v: number[] }[]; clock: number; events: number[] } | null>(null);
  const [, setFrame] = useState(0);
  const [running, setRunning] = useState(true);

  useEffect(() => {
    let live = true;
    fetch(url)
      .then((r) => r.text())
      .then((svg) => {
        const vb = /viewBox="([^"]+)"/.exec(svg)?.[1];
        if (live && vb) setViewBox(vb);
      });
    return () => {
      live = false;
    };
  }, [url]);
  useLayoutEffect(() => setBg(backgroundOf(wrap.current)), [viewBox]);

  const volts = (snap: Snapshot) => spec.probes.filter((p) => p.what === "v").map((p) => Math.abs(snap.v[p.name]));
  // a preview run (flip every switch, play about 10 s of view, flip back, play again) finds the peaks for the units
  const peaks = useMemo(() => {
    let imax = 1e-12, vmax = 1e-12;
    const look = (snap: Snapshot) => {
      imax = Math.max(imax, ...snap.seg.map(Math.abs));
      vmax = Math.max(vmax, ...volts(snap));
    };
    const s = circuit.initial();
    look(circuit.dc(s));
    for (let pass = 0; pass < 2; pass++) {
      for (const e of spec.elems) if (e.kind === "S") s.closed[e.name] = !s.closed[e.name];
      for (let k = 0; k < 600; k++) look(circuit.step(s, 1 / 60 / spec.slow));
    }
    return { imax, vmax, amp: unitFor(imax, "A"), volt: unitFor(vmax, "V") };
  }, [circuit]); // eslint-disable-line react-hooks/exhaustive-deps
  const reset = () => {
    const s = circuit.initial();
    const snap = circuit.dc(s);
    for (const e of spec.elems) if (e.kind === "C") snap.v[e.name] = s.vC[e.name]; // a #~ init charge shows from the start
    sim.current = { s, snap, off: circuit.segs.map(() => 0), imax: peaks.imax, vmax: peaks.vmax, cut: [], since: 0, moved: false, hist: [], clock: 0, events: [] };
    setFrame((f) => f + 1);
  };
  useEffect(reset, [circuit, peaks]); // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    if (!running) return;
    let raf = 0;
    let last = performance.now();
    const tick = (now: number) => {
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      const S = sim.current;
      if (S) {
        const simDt = dt / spec.slow;
        const n = 8;
        for (let k = 0; k < n; k++) S.snap = circuit.step(S.s, simDt / n);
        S.since += simDt;
        S.clock += dt;
        S.imax = Math.max(S.imax, ...S.snap.seg.map(Math.abs));
        S.vmax = Math.max(S.vmax, ...volts(S.snap));
        S.snap.seg.forEach((i, k) => (S.off[k] -= (i / S.imax) * MAX_SPEED * dt));
        S.hist.push({ t: S.clock, v: plotted.map((p) => S.snap.elem[p.name]) });
        while (S.hist.length && S.hist[0].t < S.clock - HISTORY) S.hist.shift();
        while (S.events.length && S.events[0] < S.clock - HISTORY) S.events.shift();
      }
      setFrame((f) => f + 1);
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [running, circuit, spec, plotted]);

  const S = sim.current;
  const switches = spec.elems.filter((e) => e.kind === "S");
  const groupOf = (name: string) => spec.groups.find((g) => g.includes(name)) ?? [name];
  const flip = (name: string) => {
    if (!S) return;
    for (const n of groupOf(name)) S.s.closed[n] = !S.s.closed[n];
    S.cut = cutInductors(spec, S.s, 1e-3 * S.imax);
    S.since = 0;
    S.moved = true;
    S.events.push(S.clock);
    setRunning(true);
    setFrame((f) => f + 1);
  };

  return (
    <div className="flow">
      <div className="flow-stage" ref={wrap}>
        <img src={url} alt={alt} />
        {viewBox && S && (
          <svg className="flow-overlay" viewBox={viewBox} preserveAspectRatio="none" aria-hidden>
            {switches.map((e) => {
              const [ax, ay, bx, by] = [X(e.a), Y(e.a), X(e.b), Y(e.b)];
              const len = Math.hypot(bx - ax, by - ay);
              const ux = (bx - ax) / len, uy = (by - ay) / len;
              const cx = (ax + bx) / 2, cy = (ay + by) / 2, rot = (Math.atan2(uy, ux) * 180) / Math.PI;
              // schemdraw draws the switch body one grid unit long at the middle, contacts 0.12 in from its ends
              const c1: Pt = [cx - ux * 0.38 * U, cy - uy * 0.38 * U];
              const c2: Pt = [cx + ux * 0.38 * U, cy + uy * 0.38 * U];
              const blade = 0.76 * U;
              const closed = S.s.closed[e.name];
              const ang = Math.atan2(uy, ux) - (closed ? 0 : Math.PI / 6);
              const tip: Pt = [c1[0] + Math.cos(ang) * blade, c1[1] + Math.sin(ang) * blade];
              const mask = Math.min(len - 4, 1.4 * U); // the body, its action arrow and label; the leads stay as drawn
              return (
                <g key={e.name} className="flow-switch" onClick={() => flip(e.name)}>
                  <title>{closed ? "Click to open the switch" : "Click to close the switch"}</title>
                  <rect x={cx - mask / 2} y={cy - 46} width={mask} height={61} transform={`rotate(${rot} ${cx} ${cy})`} style={{ fill: bg }} />
                  <line x1={ax} y1={ay} x2={c1[0]} y2={c1[1]} />
                  <line x1={c2[0]} y1={c2[1]} x2={bx} y2={by} />
                  <line x1={c1[0]} y1={c1[1]} x2={tip[0]} y2={tip[1]} />
                  <circle cx={c1[0]} cy={c1[1]} r={3.4} style={{ fill: bg }} />
                  <circle cx={c2[0]} cy={c2[1]} r={3.4} style={{ fill: bg }} />
                  <rect className="flow-hit" x={cx - len / 2} y={cy - 22} width={len} height={44} transform={`rotate(${rot} ${cx} ${cy})`} />
                </g>
              );
            })}
            {circuit.segs.map((seg, k) => {
              const i = S.snap.seg[k];
              const level = Math.abs(i) / S.imax;
              if (level < 0.004) return null;
              return (
                <line
                  key={k}
                  className="flow-dots"
                  x1={X(seg.a)}
                  y1={Y(seg.a)}
                  x2={X(seg.b)}
                  y2={Y(seg.b)}
                  strokeDasharray={`0 ${GAP}`}
                  strokeDashoffset={S.off[k] % GAP}
                  style={{ opacity: 0.3 + 0.7 * Math.min(1, level) }}
                />
              );
            })}
          </svg>
        )}
        {viewBox && S && (
          <div className="flow-labels">
            {switches.map((e) => {
              // the drawing's switch (and its label) is masked; put the label back above the live switch
              const [vx, vy, vw, vh] = viewBox.split(/\s+/).map(Number);
              const len = Math.hypot(X(e.b) - X(e.a), Y(e.b) - Y(e.a));
              const nx = (Y(e.b) - Y(e.a)) / len, ny = -(X(e.b) - X(e.a)) / len; // left of the a->b direction
              const cx = (X(e.a) + X(e.b)) / 2 + nx * 22, cy = (Y(e.a) + Y(e.b)) / 2 + ny * 22;
              return e.label ? (
                <span key={e.name} style={{ left: `${((cx - vx) / vw) * 100}%`, top: `${((cy - vy) / vh) * 100}%` }}>
                  <Markdown text={switchLabel(e.label, S)} inline />
                </span>
              ) : null;
            })}
          </div>
        )}
      </div>
      {S && (
        <div className="flow-panel">
          <div className="flow-controls">
            {spec.groups.map((g) => {
              const e = switches.find((s) => s.name === g[0])!;
              // one switch: Open / Close; switches that move together: Move / Move back
              const text =
                g.length > 1
                  ? S.s.closed[e.name] === e.closed ? "Move the switch" : "Move it back"
                  : `${S.s.closed[e.name] ? "Open" : "Close"} ${spec.groups.length > 1 ? e.name : "the switch"}`;
              return (
                <button key={e.name} className="mt-btn mt-primary" onClick={() => flip(e.name)}>
                  {text}
                </button>
              );
            })}
            <button className="mt-icon" onClick={() => setRunning(!running)} title={running ? "Pause" : "Play"}>
              {running ? <Pause size={14} /> : <Play size={14} />}
            </button>
            <button className="mt-icon" onClick={reset} title="Start again">
              <RotateCcw size={14} />
            </button>
            <span className="flow-time">
              {S.moved ? <><span className="flow-num">{fmtT(S.since, spec.slow)}</span> since the switch moved</> : "steady state: nothing is changing"} · slowed {spec.slow.toLocaleString()}×
            </span>
          </div>
          {spec.probes.length > 0 && (
            <>
              <div className="mt-readouts">
                {spec.probes.map((p) => {
                  const k = plotted.indexOf(p);
                  const value =
                    p.what === "v"
                      ? fmt(S.snap.v[p.name], peaks.volt)
                      : fmt(Math.abs(S.snap.elem[p.name]) < 1e-4 * S.imax ? 0 : S.snap.elem[p.name], peaks.amp);
                  return (
                    <span key={p.name + p.what} className="mt-readout" style={k >= 0 ? { boxShadow: `inset 3px 0 0 var(--plot-${k + 1})` } : undefined}>
                      <Markdown text={p.label} inline /> <b className="flow-num">{value}</b>
                    </span>
                  );
                })}
              </div>
              {plotted.length > 0 && <Scope hist={S.hist} events={S.events} clock={S.clock} imax={S.imax} />}
            </>
          )}
          {S.cut.length > 0 && (
            <div className="flow-warn">
              This cuts off the inductor's current. A real inductor's current can't jump, so its voltage spikes and a spark
              jumps the switch. The simulation just lets the current fall to 0.
            </div>
          )}
          {spec.note && <div className="mt-hint"><Markdown text={spec.note} inline /></div>}
        </div>
      )}
    </div>
  );
}

function Scope({ hist, events, clock, imax }: { hist: { t: number; v: number[] }[]; events: number[]; clock: number; imax: number }) {
  const W = 560, H = 110, L = 8, R = 8, T = 8, B = 18;
  const lo = 0, hi = Math.max(imax * 0.05, ...hist.flatMap((h) => h.v.map(Math.abs)));
  const sx = (t: number) => L + ((t - (clock - HISTORY)) / HISTORY) * (W - L - R);
  const sy = (v: number) => T + ((hi - v) / (hi - lo || 1)) * (H - T - B);
  const n = hist[0]?.v.length ?? 0;
  return (
    <svg className="flow-scope" viewBox={`0 0 ${W} ${H}`} role="img" aria-label="Currents over time">
      <line className="mt-axis" x1={L} x2={W - R} y1={sy(0)} y2={sy(0)} />
      {events.map((t, k) => (
        <line key={k} x1={sx(t)} x2={sx(t)} y1={T} y2={H - B} className="flow-event" />
      ))}
      {Array.from({ length: n }, (_, k) => (
        <polyline key={k} fill="none" strokeWidth={k === 0 ? 4.5 : 2} strokeOpacity={k === 0 ? 0.55 : 1} style={{ stroke: `var(--plot-${k + 1})` }} points={hist.map((h) => `${sx(h.t).toFixed(1)},${sy(Math.abs(h.v[k])).toFixed(1)}`).join(" ")} />
      ))}
      <text className="mt-tick" x={W - R} y={H - 4} textAnchor="end">now</text>
      <text className="mt-tick" x={L} y={H - 4}>{HISTORY} s ago</text>
      <text className="mt-tick" x={W / 2} y={H - 4} textAnchor="middle">dashed line = switch moved</text>
    </svg>
  );
}
