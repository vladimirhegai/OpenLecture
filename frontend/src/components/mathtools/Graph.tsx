import { Pause, Play, RotateCcw } from "lucide-react";
import { useEffect, useId, useMemo, useRef, useState } from "react";
import { Markdown } from "../Markdown";
import type { Compiled, Env } from "./expr";
import { constant, expr, fmtNum, parseSpec, sliderOf, SpecError, ticks, type Slider, type Stmt } from "./spec";
import { ToolError } from "./Stepper";

/*
 * ```graph fence: an interactive 2-D plot. Grammar in src/open_lecture/skills/math-tools.md. Summary:
 *   x MIN MAX label=  | y MIN MAX label= | equal | height=PX (on the x line) | title "…" | caption "…"
 *   slider NAME MIN MAX START step= label= [animate]      drag NAME X Y label= snap=   (binds NAME_x, NAME_y)
 *   curve "f(x)" from= to= | family NAME MIN MAX STEP "f(x)" | param "X(s)" "Y(s)" S0 S1
 *   field "F(x,y)" | solution "F(x,y)" x0= y0= | level "G(x,y)" values="…" | region "cond(x,y)"
 *   point "X" "Y" | arrow "X" "Y" x0= y0= | segment "X0" "Y0" "X1" "Y1" | circle "CX" "CY" "R"
 *   hline "Y" | vline "X" | text "X" "Y" "label" | readout "label" "EXPR" unit=
 *   every drawing statement takes label= color=1..6 dash; in curves x and t both mean the horizontal axis.
 */

const W = 560;
const PAD = { l: 44, r: 14, t: 12, b: 30 };

type Item = { st: Stmt; draw: (ctx: Ctx) => React.ReactNode; legend?: { label: string; color: number; dash: boolean; fill?: boolean; dot?: boolean } };
type Ctx = { env: Env; sx: (x: number) => number; sy: (y: number) => number; xmin: number; xmax: number; ymin: number; ymax: number; H: number };
type DragPt = { name: string; x: number; y: number; label?: string; color: number; snap: number };
type Model = {
  title?: string;
  caption?: string;
  xmin: number; xmax: number; ymin: number; ymax: number;
  xlabel?: string; ylabel?: string;
  H: number;
  sliders: Slider[];
  drags: DragPt[];
  lets: { name: string; fn: Compiled }[];
  items: Item[];
  labels: { st: Stmt; x: Compiled; y: Compiled; text: string; color: number }[];
  readouts: { label: string; fn: Compiled; unit: string }[];
};

export const col = (c: number) => (c >= 1 ? `var(--plot-${((c - 1) % 6) + 1})` : "var(--ink-3)");

function colorOf(st: Stmt, fallback: number) {
  const c = Number(st.opts.color ?? fallback);
  return Number.isFinite(c) && c >= 0 ? Math.round(c) : fallback;
}

/** Sample y = f(x) into an SVG path, breaking at gaps and vertical asymptotes. */
function pathOf(points: [number, number][], ctx: Ctx) {
  const span = ctx.ymax - ctx.ymin;
  let d = "";
  let pen = false;
  let prevY = NaN;
  for (const [x, y] of points) {
    const ok = Number.isFinite(x) && Number.isFinite(y) && y > ctx.ymin - 4 * span && y < ctx.ymax + 4 * span;
    if (!ok || (pen && Math.abs(y - prevY) > 2 * span)) {
      pen = false;
      if (!ok) continue;
    }
    d += `${pen ? "L" : "M"}${ctx.sx(x).toFixed(1)},${ctx.sy(y).toFixed(1)}`;
    pen = true;
    prevY = y;
  }
  return d;
}

function lineProps(st: Stmt, color: number, width = 2.2) {
  return {
    fill: "none",
    style: { stroke: col(color) },
    strokeWidth: Number(st.opts.width ?? width),
    strokeDasharray: st.args.includes("dash") ? "6 5" : undefined,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
  };
}

/** Marching squares: segments where g(x,y) = level. */
function contour(g: (x: number, y: number) => number, level: number, ctx: Ctx, nx = 96, ny = 64) {
  const xs = (i: number) => ctx.xmin + ((ctx.xmax - ctx.xmin) * i) / nx;
  const ys = (j: number) => ctx.ymin + ((ctx.ymax - ctx.ymin) * j) / ny;
  const v: number[][] = [];
  for (let i = 0; i <= nx; i++) {
    v.push([]);
    for (let j = 0; j <= ny; j++) v[i].push(g(xs(i), ys(j)) - level);
  }
  let d = "";
  const lerp = (a: number, b: number, fa: number, fb: number) => a + ((b - a) * fa) / (fa - fb);
  for (let i = 0; i < nx; i++)
    for (let j = 0; j < ny; j++) {
      const a = v[i][j], b = v[i + 1][j], c = v[i + 1][j + 1], e = v[i][j + 1];
      if (![a, b, c, e].every(Number.isFinite)) continue;
      const pts: [number, number][] = [];
      if (a > 0 !== b > 0) pts.push([lerp(xs(i), xs(i + 1), a, b), ys(j)]);
      if (b > 0 !== c > 0) pts.push([xs(i + 1), lerp(ys(j), ys(j + 1), b, c)]);
      if (c > 0 !== e > 0) pts.push([lerp(xs(i + 1), xs(i), c, e), ys(j + 1)]);
      if (e > 0 !== a > 0) pts.push([xs(i), lerp(ys(j + 1), ys(j), e, a)]);
      // a sign change across a jump (e.g. 1/x) is not a level crossing
      const big = Math.max(Math.abs(a), Math.abs(b), Math.abs(c), Math.abs(e));
      if (big > 1e6) continue;
      for (let p = 0; p + 1 < pts.length; p += 2)
        d += `M${ctx.sx(pts[p][0]).toFixed(1)},${ctx.sy(pts[p][1]).toFixed(1)}L${ctx.sx(pts[p + 1][0]).toFixed(1)},${ctx.sy(pts[p + 1][1]).toFixed(1)}`;
    }
  return d;
}

/**
 * The solution curve of dy/dx = F(x, y) through (x0, y0), traced both ways until it leaves the window.
 * It steps by arc length along the direction field (RK4, in window-normalised units) and keeps the direction
 * continuous, so it turns smoothly through vertical tangents (where F is infinite, e.g. N = 0 in M dx + N dy = 0)
 * instead of jumping to another curve.
 */
function integrate(F: Compiled, env: Env, x0: number, y0: number, ctx: Ctx) {
  const sx = ctx.xmax - ctx.xmin, sy = ctx.ymax - ctx.ymin;
  const h = 0.004;
  const f = (x: number, y: number) => F({ ...env, x, t: x, y });
  const dirAt = (x: number, y: number, prev: [number, number]): [number, number] | null => {
    const s = f(x, y);
    if (Number.isNaN(s)) return null;
    let du = 0, dv = Math.sign(s);
    if (Number.isFinite(s)) {
      du = 1 / sx;
      dv = s / sy;
      const l = Math.hypot(du, dv);
      du /= l;
      dv /= l;
    }
    return du * prev[0] + dv * prev[1] < 0 ? [-du, -dv] : [du, dv];
  };
  const run = (dir: number) => {
    const out: [number, number][] = [[x0, y0]];
    let x = x0, y = y0;
    let prev: [number, number] = [dir, 0];
    for (let n = 0; n < 3000; n++) {
      const k1 = dirAt(x, y, prev);
      const k2 = k1 && dirAt(x + (h / 2) * k1[0] * sx, y + (h / 2) * k1[1] * sy, k1);
      const k3 = k2 && dirAt(x + (h / 2) * k2[0] * sx, y + (h / 2) * k2[1] * sy, k1);
      const k4 = k3 && dirAt(x + h * k3[0] * sx, y + h * k3[1] * sy, k1);
      if (!k1 || !k2 || !k3 || !k4) break;
      const du = (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6, dv = (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6;
      x += h * du * sx;
      y += h * dv * sy;
      prev = [du, dv];
      if (!Number.isFinite(x) || !Number.isFinite(y)) break;
      out.push([x, y]);
      if (x < ctx.xmin - 0.02 * sx || x > ctx.xmax + 0.02 * sx || y > ctx.ymax + 0.5 * sy || y < ctx.ymin - 0.5 * sy) break;
      // a closed curve (a level curve such as an ellipse) is done once it comes back to the start
      if (n > 40 && Math.hypot((x - x0) / sx, (y - y0) / sy) < h) break;
    }
    return out;
  };
  return [...run(-1).reverse(), ...run(1).slice(1)];
}

function build(source: string): Model {
  const sts = parseSpec(source);
  const m: Model = { xmin: -5, xmax: 5, ymin: -5, ymax: 5, H: 300, sliders: [], drags: [], lets: [], items: [], labels: [], readouts: [] };
  let equal = false;
  let hset = false;
  // names first: sliders and draggable points can be used by any statement
  for (const st of sts) {
    if (st.kind === "slider") m.sliders.push(sliderOf(st));
    if (st.kind === "drag") {
      const [name, x, y] = st.args;
      if (!name) throw new SpecError(`line ${st.line}: drag needs a name`);
      m.drags.push({ name, x: constant(x, 0, st), y: constant(y, 0, st), label: st.opts.label, color: colorOf(st, 1), snap: constant(st.opts.snap, 0, st) });
    }
  }
  const names = new Set([...m.sliders.map((s) => s.name), ...m.drags.flatMap((d) => [`${d.name}_x`, `${d.name}_y`])]);
  // let NAME "EXPR": a named value from sliders, points and earlier lets, usable everywhere after it is defined
  for (const st of sts)
    if (st.kind === "let") {
      const [name, body] = st.args;
      if (!name || !/^[A-Za-z_][A-Za-z_0-9]*$/.test(name)) throw new SpecError(`line ${st.line}: let needs a name`);
      m.lets.push({ name, fn: expr(body, names, st) });
      names.add(name);
    }
  const withX = new Set([...names, "x", "t"]);
  const withXY = new Set([...names, "x", "y", "t"]);
  const withS = new Set([...names, "s"]);
  let auto = 1;
  const next = (st: Stmt) => colorOf(st, auto++);
  const legend = (st: Stmt, color: number, fill = false) =>
    st.opts.label ? { label: st.opts.label, color, dash: st.args.includes("dash"), fill } : undefined;

  for (const st of sts) {
    const a = st.args;
    switch (st.kind) {
      case "slider":
      case "drag":
      case "let":
        break;
      case "title":
        m.title = a[0];
        break;
      case "caption":
        m.caption = a[0];
        break;
      case "x":
        m.xmin = constant(a[0], -5, st);
        m.xmax = constant(a[1], 5, st);
        m.xlabel = st.opts.label;
        if (st.opts.height) {
          m.H = constant(st.opts.height, 300, st);
          hset = true;
        }
        break;
      case "y":
        m.ymin = constant(a[0], -5, st);
        m.ymax = constant(a[1], 5, st);
        m.ylabel = st.opts.label;
        break;
      case "equal":
        equal = true;
        break;
      case "curve": {
        const f = expr(a[0], withX, st);
        const from = st.opts.from ? expr(st.opts.from, names, st) : null;
        const to = st.opts.to ? expr(st.opts.to, names, st) : null;
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => {
            const x0 = Math.max(ctx.xmin, from ? from(ctx.env) : ctx.xmin);
            const x1 = Math.min(ctx.xmax, to ? to(ctx.env) : ctx.xmax);
            const pts: [number, number][] = [];
            for (let i = 0; i <= 400; i++) {
              const x = x0 + ((x1 - x0) * i) / 400;
              pts.push([x, f({ ...ctx.env, x, t: x })]);
            }
            return <path d={pathOf(pts, ctx)} {...lineProps(st, c)} />;
          },
        });
        break;
      }
      case "family": {
        const [name, lo, hi, step, body] = a;
        const f = expr(body, new Set([...withX, name]), st);
        const v0 = constant(lo, 0, st), v1 = constant(hi, 0, st), dv = constant(step, 1, st);
        if (!(dv > 0) || (v1 - v0) / dv > 60) throw new SpecError(`line ${st.line}: family step must be positive (at most 60 curves)`);
        const from = st.opts.from ? expr(st.opts.from, new Set([...names, name]), st) : null;
        const to = st.opts.to ? expr(st.opts.to, new Set([...names, name]), st) : null;
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => {
            const out: React.ReactNode[] = [];
            for (let v = v0, n = 0; v <= v1 + dv * 1e-9; v += dv, n++) {
              const pts: [number, number][] = [];
              const e = { ...ctx.env, [name]: v };
              const x0 = Math.max(ctx.xmin, from ? from(e) : ctx.xmin), x1 = Math.min(ctx.xmax, to ? to(e) : ctx.xmax);
              for (let i = 0; i <= 300; i++) {
                const x = x0 + ((x1 - x0) * i) / 300;
                pts.push([x, f({ ...ctx.env, x, t: x, [name]: v })]);
              }
              out.push(<path key={n} d={pathOf(pts, ctx)} {...lineProps(st, c, 1.4)} opacity={0.55} />);
            }
            return <>{out}</>;
          },
        });
        break;
      }
      case "param": {
        const fx = expr(a[0], withS, st), fy = expr(a[1], withS, st);
        const s0 = expr(a[2] ?? "0", names, st), s1 = expr(a[3] ?? "1", names, st);
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => {
            const lo = s0(ctx.env), hi = s1(ctx.env);
            const pts: [number, number][] = [];
            for (let i = 0; i <= 400; i++) {
              const s = lo + ((hi - lo) * i) / 400;
              const env = { ...ctx.env, s };
              pts.push([fx(env), fy(env)]);
            }
            return <path d={pathOf(pts, ctx)} {...lineProps(st, c)} />;
          },
        });
        break;
      }
      case "field": {
        const F = expr(a[0], withXY, st);
        const c = colorOf(st, 0);
        m.items.push({
          st,
          draw: (ctx) => {
            const density = constant(st.opts.density, 22, st);
            const iw = W - PAD.l - PAD.r, ih = ctx.H - PAD.t - PAD.b;
            const cell = iw / density;
            const ny = Math.max(2, Math.round(ih / cell));
            let d = "";
            for (let i = 0; i < density; i++)
              for (let j = 0; j < ny; j++) {
                const px = PAD.l + (i + 0.5) * cell, py = PAD.t + ((j + 0.5) * ih) / ny;
                const x = ctx.xmin + ((px - PAD.l) / iw) * (ctx.xmax - ctx.xmin);
                const y = ctx.ymax - ((py - PAD.t) / ih) * (ctx.ymax - ctx.ymin);
                const slope = F({ ...ctx.env, x, y, t: x });
                if (!Number.isFinite(slope)) continue;
                let dx = iw / (ctx.xmax - ctx.xmin);
                let dy = -slope * (ih / (ctx.ymax - ctx.ymin));
                const len = Math.hypot(dx, dy) || 1;
                const half = cell * 0.36;
                dx = (dx / len) * half;
                dy = (dy / len) * half;
                d += `M${(px - dx).toFixed(1)},${(py - dy).toFixed(1)}L${(px + dx).toFixed(1)},${(py + dy).toFixed(1)}`;
              }
            return <path d={d} style={{ stroke: c ? col(c) : "var(--ink-3)" }} strokeWidth={1.3} strokeLinecap="round" opacity={0.75} />;
          },
        });
        break;
      }
      case "solution": {
        const F = expr(a[0], withXY, st);
        const x0 = expr(st.opts.x0 ?? "0", names, st), y0 = expr(st.opts.y0 ?? "0", names, st);
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => <path d={pathOf(integrate(F, ctx.env, x0(ctx.env), y0(ctx.env), ctx), ctx)} {...lineProps(st, c, 2.6)} />,
        });
        break;
      }
      case "level": {
        const G = expr(a[0], withXY, st);
        const vals = st.opts.values ? st.opts.values.split(",").map((v) => expr(v.trim(), names, st)) : [expr(st.opts.value ?? "0", names, st)];
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => {
            const g = (x: number, y: number) => G({ ...ctx.env, x, y, t: x });
            return <path d={vals.map((v) => contour(g, v(ctx.env), ctx)).join("")} {...lineProps(st, c, 1.8)} />;
          },
        });
        break;
      }
      case "region": {
        const R = expr(a[0], withXY, st);
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c, true),
          draw: (ctx) => {
            const nx = 112, ny = 72;
            const iw = W - PAD.l - PAD.r, ih = ctx.H - PAD.t - PAD.b;
            const cw = iw / nx, ch = ih / ny;
            let d = "";
            for (let j = 0; j < ny; j++) {
              let run = -1;
              for (let i = 0; i <= nx; i++) {
                const x = ctx.xmin + ((i + 0.5) / nx) * (ctx.xmax - ctx.xmin);
                const y = ctx.ymax - ((j + 0.5) / ny) * (ctx.ymax - ctx.ymin);
                const on = i < nx && R({ ...ctx.env, x, y, t: x }) > 0;
                if (on && run < 0) run = i;
                if (!on && run >= 0) {
                  d += `M${(PAD.l + run * cw).toFixed(1)},${(PAD.t + j * ch).toFixed(1)}h${((i - run) * cw + 0.4).toFixed(1)}v${(ch + 0.4).toFixed(1)}h${(-(i - run) * cw - 0.4).toFixed(1)}z`;
                  run = -1;
                }
              }
            }
            return <path d={d} style={{ fill: col(c) }} opacity={0.16} />;
          },
        });
        break;
      }
      case "point":
      case "arrow": {
        const fx = expr(a[0], names, st), fy = expr(a[1], names, st);
        const bx = expr(st.opts.x0 ?? "0", names, st), by = expr(st.opts.y0 ?? "0", names, st);
        const c = next(st);
        const arrow = st.kind === "arrow";
        const lg = legend(st, c);
        m.items.push({
          st,
          legend: lg && !arrow ? { ...lg, dot: true } : lg,
          draw: (ctx) => {
            const X = ctx.sx(fx(ctx.env)), Y = ctx.sy(fy(ctx.env));
            if (!Number.isFinite(X) || !Number.isFinite(Y)) return null;
            if (!arrow) return <circle cx={X} cy={Y} r={4.5} style={{ fill: col(c) }} />;
            const X0 = ctx.sx(bx(ctx.env)), Y0 = ctx.sy(by(ctx.env));
            const len = Math.hypot(X - X0, Y - Y0);
            if (len < 1) return null;
            const ux = (X - X0) / len, uy = (Y - Y0) / len, hl = Math.min(11, len * 0.4);
            const head = `M${X},${Y}L${X - hl * ux + hl * 0.45 * uy},${Y - hl * uy - hl * 0.45 * ux}L${X - hl * ux - hl * 0.45 * uy},${Y - hl * uy + hl * 0.45 * ux}Z`;
            return (
              <g>
                <line x1={X0} y1={Y0} x2={X - hl * 0.8 * ux} y2={Y - hl * 0.8 * uy} {...lineProps(st, c, 2.4)} />
                <path d={head} style={{ fill: col(c) }} />
              </g>
            );
          },
        });
        break;
      }
      case "segment": {
        const f = a.slice(0, 4).map((s) => expr(s, names, st));
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => {
            const [x0, y0, x1, y1] = f.map((g) => g(ctx.env));
            return <line x1={ctx.sx(x0)} y1={ctx.sy(y0)} x2={ctx.sx(x1)} y2={ctx.sy(y1)} {...lineProps(st, c, 1.8)} />;
          },
        });
        break;
      }
      case "circle": {
        const [fcx, fcy, fr] = a.slice(0, 3).map((s) => expr(s, names, st));
        const c = next(st);
        m.items.push({
          st,
          legend: legend(st, c),
          draw: (ctx) => {
            const pts: [number, number][] = [];
            const cx = fcx(ctx.env), cy = fcy(ctx.env), r = fr(ctx.env);
            for (let i = 0; i <= 200; i++) pts.push([cx + r * Math.cos((2 * Math.PI * i) / 200), cy + r * Math.sin((2 * Math.PI * i) / 200)]);
            return <path d={pathOf(pts, ctx)} {...lineProps(st, c, 1.6)} />;
          },
        });
        break;
      }
      case "hline":
      case "vline": {
        const f = expr(a[0], names, st);
        const c = colorOf(st, 0);
        const horiz = st.kind === "hline";
        m.items.push({
          st,
          legend: st.opts.label ? { label: st.opts.label, color: c, dash: true } : undefined,
          draw: (ctx) => {
            const v = f(ctx.env);
            if (!Number.isFinite(v)) return null;
            const p = horiz
              ? { x1: PAD.l, x2: W - PAD.r, y1: ctx.sy(v), y2: ctx.sy(v) }
              : { x1: ctx.sx(v), x2: ctx.sx(v), y1: PAD.t, y2: ctx.H - PAD.b };
            return <line {...p} style={{ stroke: c ? col(c) : "var(--ink-3)" }} strokeWidth={1.4} strokeDasharray="5 5" />;
          },
        });
        break;
      }
      case "text":
        m.labels.push({ st, x: expr(a[0], names, st), y: expr(a[1], names, st), text: a[2] ?? "", color: colorOf(st, 0) });
        break;
      case "readout":
        m.readouts.push({ label: a[0] ?? "", fn: expr(a[1], names, st), unit: st.opts.unit ?? "" });
        break;
      default:
        throw new SpecError(`line ${st.line}: unknown statement "${st.kind}"`);
    }
  }
  if (!(m.xmax > m.xmin) || !(m.ymax > m.ymin)) throw new SpecError("x and y ranges need MIN < MAX");
  if (equal) {
    // one unit is the same length on both axes; if the height is capped, widen the other range instead of squashing
    const iw = W - PAD.l - PAD.r;
    if (!hset) m.H = Math.round(Math.min(400, Math.max(180, (iw * (m.ymax - m.ymin)) / (m.xmax - m.xmin) + PAD.t + PAD.b)));
    const ih = m.H - PAD.t - PAD.b;
    const kx = iw / (m.xmax - m.xmin), ky = ih / (m.ymax - m.ymin);
    if (ky < kx) {
      const c = (m.xmin + m.xmax) / 2, half = iw / ky / 2;
      [m.xmin, m.xmax] = [c - half, c + half];
    } else if (kx < ky) {
      const c = (m.ymin + m.ymax) / 2, half = ih / kx / 2;
      [m.ymin, m.ymax] = [c - half, c + half];
    }
  }
  return m;
}

export function Graph({ source }: { source: string }) {
  const built = useMemo(() => {
    try {
      return { m: build(source) };
    } catch (e) {
      return { error: (e as Error).message };
    }
  }, [source]);
  if (!built.m) return <ToolError kind="graph" message={built.error!} source={source} />;
  return <GraphView m={built.m} />;
}

function initial(m: Model) {
  return {
    sliders: Object.fromEntries(m.sliders.map((s) => [s.name, s.value])),
    drags: Object.fromEntries(m.drags.map((d) => [d.name, [d.x, d.y] as [number, number]])),
  };
}

function GraphView({ m }: { m: Model }) {
  const [state, setState] = useState(() => initial(m));
  const [hover, setHover] = useState<[number, number] | null>(null);
  const [dragging, setDragging] = useState<string | null>(null);
  const [playing, setPlaying] = useState<string | null>(null);
  const svg = useRef<SVGSVGElement>(null);
  const clip = `mt-clip${useId().replace(/:/g, "")}`;
  useEffect(() => setState(initial(m)), [m]);

  // animate one slider back and forth across its range
  useEffect(() => {
    if (!playing) return;
    const s = m.sliders.find((v) => v.name === playing);
    if (!s) return;
    let raf = 0;
    let last = performance.now();
    let dir = 1;
    const tick = (now: number) => {
      const dt = (now - last) / 1000;
      last = now;
      setState((st) => {
        let v = st.sliders[s.name] + (dir * (s.max - s.min) * dt) / 4;
        if (v >= s.max) { v = s.max; dir = -1; }
        if (v <= s.min) { v = s.min; dir = 1; }
        return { ...st, sliders: { ...st.sliders, [s.name]: v } };
      });
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [playing, m]);

  const env: Env = { ...state.sliders };
  for (const [name, [x, y]] of Object.entries(state.drags)) {
    env[`${name}_x`] = x;
    env[`${name}_y`] = y;
  }
  for (const l of m.lets) env[l.name] = l.fn(env);
  const { xmin, xmax, ymin, ymax, H } = m;
  const iw = W - PAD.l - PAD.r, ih = H - PAD.t - PAD.b;
  const sx = (x: number) => PAD.l + ((x - xmin) / (xmax - xmin)) * iw;
  const sy = (y: number) => PAD.t + ((ymax - y) / (ymax - ymin)) * ih;
  const ctx: Ctx = { env, sx, sy, xmin, xmax, ymin, ymax, H };

  const toData = (e: React.PointerEvent): [number, number] => {
    const r = svg.current!.getBoundingClientRect();
    const px = ((e.clientX - r.left) / r.width) * W, py = ((e.clientY - r.top) / r.height) * H;
    return [xmin + ((px - PAD.l) / iw) * (xmax - xmin), ymax - ((py - PAD.t) / ih) * (ymax - ymin)];
  };
  const onMove = (e: React.PointerEvent) => {
    const [x, y] = toData(e);
    setHover([x, y]);
    if (dragging) {
      const d = m.drags.find((p) => p.name === dragging)!;
      const snap = (v: number) => (d.snap > 0 ? Math.round(v / d.snap) * d.snap : v);
      const cx = Math.min(xmax, Math.max(xmin, snap(x))), cy = Math.min(ymax, Math.max(ymin, snap(y)));
      setState((st) => ({ ...st, drags: { ...st.drags, [dragging]: [cx, cy] } }));
    }
  };

  const xt = ticks(xmin, xmax, 7), yt = ticks(ymin, ymax, 5);
  const ax = ymin <= 0 && ymax >= 0 ? sy(0) : H - PAD.b;
  const ay = xmin <= 0 && xmax >= 0 ? sx(0) : PAD.l;
  const legends = m.items.map((it) => it.legend).filter((l): l is NonNullable<Item["legend"]> => !!l);
  const changed = JSON.stringify(state) !== JSON.stringify(initial(m));

  return (
    <figure className="mt-card mt-graph">
      {(m.title || changed) && (
        <div className="mt-head">
          <span className="mt-title">{m.title && <Markdown text={m.title} inline />}</span>
          {changed && (
            <button className="mt-icon" onClick={() => { setPlaying(null); setState(initial(m)); }} title="Reset">
              <RotateCcw size={14} />
            </button>
          )}
        </div>
      )}
      <div className="mt-plot">
        <svg
          ref={svg}
          viewBox={`0 0 ${W} ${H}`}
          className={dragging ? "dragging" : ""}
          onPointerMove={onMove}
          onPointerLeave={() => !dragging && setHover(null)}
          onPointerUp={() => setDragging(null)}
          role="img"
          aria-label={m.title ?? "Interactive graph"}
        >
          <defs>
            <clipPath id={clip}>
              <rect x={PAD.l} y={PAD.t} width={iw} height={ih} />
            </clipPath>
          </defs>
          {xt.map((v) => (
            <g key={`x${v}`}>
              <line className="mt-grid" x1={sx(v)} x2={sx(v)} y1={PAD.t} y2={H - PAD.b} />
              <text className="mt-tick" x={sx(v)} y={H - PAD.b + 16} textAnchor="middle">{fmtNum(v)}</text>
            </g>
          ))}
          {yt.map((v) => (
            <g key={`y${v}`}>
              <line className="mt-grid" x1={PAD.l} x2={W - PAD.r} y1={sy(v)} y2={sy(v)} />
              <text className="mt-tick" x={PAD.l - 6} y={sy(v) + 4} textAnchor="end">{fmtNum(v)}</text>
            </g>
          ))}
          <line className="mt-axis" x1={PAD.l} x2={W - PAD.r} y1={ax} y2={ax} />
          <line className="mt-axis" x1={ay} x2={ay} y1={PAD.t} y2={H - PAD.b} />
          <g clipPath={`url(#${clip})`}>
            {m.items.map((it, i) => (
              <g key={i}>{it.draw(ctx)}</g>
            ))}
          </g>
          {m.drags.map((d) => {
            const [x, y] = state.drags[d.name];
            return (
              <g key={d.name} className="mt-drag" onPointerDown={(e) => { (e.currentTarget.ownerSVGElement as SVGSVGElement).setPointerCapture(e.pointerId); setDragging(d.name); }}>
                <circle cx={sx(x)} cy={sy(y)} r={14} className="mt-drag-hit" />
                <circle cx={sx(x)} cy={sy(y)} r={6.5} style={{ fill: col(d.color) }} className="mt-drag-dot" />
              </g>
            );
          })}
        </svg>
        <div className="mt-overlay">
          {m.xlabel && <span className="mt-axis-label mt-xl" style={{ top: `${((ax - 4) / H) * 100}%` }}><Markdown text={m.xlabel} inline /></span>}
          {m.ylabel && <span className="mt-axis-label mt-yl" style={{ left: `${((ay + 7) / W) * 100}%`, top: `${(PAD.t / H) * 100}%` }}><Markdown text={m.ylabel} inline /></span>}
          {m.drags.map((d) => {
            const [x, y] = state.drags[d.name];
            return d.label ? (
              <span key={d.name} className="mt-label" style={{ left: `${((sx(x) + 9) / W) * 100}%`, top: `${((sy(y) - 9) / H) * 100}%`, color: col(d.color) }}>
                <Markdown text={d.label} inline />
              </span>
            ) : null;
          })}
          {m.labels.map((l, i) => {
            const X = sx(l.x(env)), Y = sy(l.y(env));
            if (!Number.isFinite(X) || !Number.isFinite(Y)) return null;
            return (
              <span key={i} className="mt-label" style={{ left: `${(X / W) * 100}%`, top: `${(Y / H) * 100}%`, color: l.color ? col(l.color) : undefined }}>
                <Markdown text={l.text} inline />
              </span>
            );
          })}
        </div>
        {hover && (
          <span className="mt-cursor">
            ({fmtNum(hover[0])}, {fmtNum(hover[1])})
          </span>
        )}
      </div>
      {legends.length > 0 && (
        <div className="mt-legend">
          {legends.map((l, i) => (
            <span key={i}>
              <i className={`mt-swatch ${l.dash ? "dash" : ""} ${l.fill ? "fill" : ""} ${l.dot ? "dot" : ""}`} style={{ color: l.color ? col(l.color) : "var(--ink-3)" }} />
              <Markdown text={l.label} inline />
            </span>
          ))}
        </div>
      )}
      {m.sliders.length > 0 && (
        <div className="mt-sliders">
          {m.sliders.map((s) => (
            <label key={s.name} className="mt-slider">
              <span className="mt-slider-name"><Markdown text={s.label} inline /></span>
              <input
                type="range"
                min={s.min}
                max={s.max}
                step={s.step}
                value={state.sliders[s.name]}
                onChange={(e) => { setPlaying(null); setState((st) => ({ ...st, sliders: { ...st.sliders, [s.name]: Number(e.target.value) } })); }}
              />
              <span className="mt-slider-value">{fmtNum(state.sliders[s.name])}</span>
              {s.animate && (
                <button className="mt-icon" onClick={(e) => { e.preventDefault(); setPlaying(playing === s.name ? null : s.name); }} title={playing === s.name ? "Pause" : "Play"}>
                  {playing === s.name ? <Pause size={14} /> : <Play size={14} />}
                </button>
              )}
            </label>
          ))}
        </div>
      )}
      {m.readouts.length > 0 && (
        <div className="mt-readouts">
          {m.readouts.map((r, i) => (
            <span key={i} className="mt-readout">
              <Markdown text={r.label} inline /> <b>{fmtNum(r.fn(env))}{r.unit}</b>
            </span>
          ))}
        </div>
      )}
      {m.drags.length > 0 && <div className="mt-hint">Drag the dots.</div>}
      {m.caption && (
        <figcaption>
          <Markdown text={m.caption} inline />
        </figcaption>
      )}
    </figure>
  );
}
