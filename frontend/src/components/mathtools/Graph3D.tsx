import { RotateCcw } from "lucide-react";
import { useMemo, useRef, useState } from "react";
import { Markdown } from "../Markdown";
import type { Compiled, Env } from "./expr";
import { col } from "./Graph";
import { constant, expr, fmtNum, parseSpec, sliderOf, SpecError, type Slider, type Stmt } from "./spec";
import { ToolError } from "./Stepper";

/*
 * ```graph3d fence: a surface z = F(x, y) you can rotate by dragging. Grammar in skills/math-tools.md. Summary:
 *   x MIN MAX label= | y MIN MAX label= | z MIN MAX label= (optional; else fitted) | view az=DEG el=DEG
 *   slider NAME MIN MAX START step= label=
 *   surface "F(x,y)" label= mesh=N        plane "C" label=   (horizontal plane z = C; marks where F = C)
 *   levels values="a,b,c"                 (level curves F = a, b, c drawn on the floor)
 *   curve3 "X(s)" "Y(s)" "Z(s)" S0 S1 label= color=      point3 "X" "Y" "Z" label= color=
 *   title "…" | caption "…"
 */

const W = 560;
const H = 380;

type Model = {
  title?: string;
  caption?: string;
  x: [number, number]; y: [number, number]; z?: [number, number];
  labels: { x?: string; y?: string; z?: string };
  az: number; el: number;
  sliders: Slider[];
  surface?: { F: Compiled; label?: string; mesh: number };
  plane?: { C: Compiled; label?: string };
  levels: Compiled[];
  curves: { X: Compiled; Y: Compiled; Z: Compiled; s0: Compiled; s1: Compiled; color: number; label?: string }[];
  points: { X: Compiled; Y: Compiled; Z: Compiled; color: number; label?: string }[];
};

function build(source: string): Model {
  const sts = parseSpec(source);
  const m: Model = { x: [-2, 2], y: [-2, 2], labels: {}, az: -55, el: 28, sliders: [], levels: [], curves: [], points: [] };
  for (const st of sts) if (st.kind === "slider") m.sliders.push(sliderOf(st));
  const names = new Set(m.sliders.map((s) => s.name));
  const xy = new Set([...names, "x", "y"]);
  const ss = new Set([...names, "s"]);
  let auto = 1;
  const color = (st: Stmt) => Number(st.opts.color ?? auto++);
  for (const st of sts) {
    const a = st.args;
    switch (st.kind) {
      case "slider":
        break;
      case "title":
        m.title = a[0];
        break;
      case "caption":
        m.caption = a[0];
        break;
      case "x":
      case "y":
      case "z":
        m[st.kind] = [constant(a[0], -2, st), constant(a[1], 2, st)];
        m.labels[st.kind] = st.opts.label;
        if (!(m[st.kind]![1] > m[st.kind]![0])) throw new SpecError(`line ${st.line}: ${st.kind} needs MIN < MAX`);
        break;
      case "view":
        m.az = constant(st.opts.az, m.az, st);
        m.el = constant(st.opts.el, m.el, st);
        break;
      case "surface":
        m.surface = { F: expr(a[0], xy, st), label: st.opts.label, mesh: Math.min(40, Math.max(8, constant(st.opts.mesh, 30, st))) };
        break;
      case "plane":
        m.plane = { C: expr(a[0], names, st), label: st.opts.label };
        break;
      case "levels":
        m.levels = (st.opts.values ?? "").split(",").filter(Boolean).map((v) => expr(v.trim(), names, st));
        break;
      case "curve3":
        m.curves.push({ X: expr(a[0], ss, st), Y: expr(a[1], ss, st), Z: expr(a[2], ss, st), s0: expr(a[3] ?? "0", names, st), s1: expr(a[4] ?? "1", names, st), color: color(st), label: st.opts.label });
        break;
      case "point3":
        m.points.push({ X: expr(a[0], names, st), Y: expr(a[1], names, st), Z: expr(a[2], names, st), color: color(st), label: st.opts.label });
        break;
      default:
        throw new SpecError(`line ${st.line}: unknown statement "${st.kind}"`);
    }
  }
  if (!m.surface && !m.curves.length && !m.points.length) throw new SpecError("nothing to draw (add a surface, curve3 or point3)");
  return m;
}

export function Graph3D({ source }: { source: string }) {
  const built = useMemo(() => {
    try {
      return { m: build(source) };
    } catch (e) {
      return { error: (e as Error).message };
    }
  }, [source]);
  if (!built.m) return <ToolError kind="graph3d" message={built.error!} source={source} />;
  return <View3D m={built.m} />;
}

type Prim = { depth: number; node: React.ReactNode };

function View3D({ m }: { m: Model }) {
  const [view, setView] = useState({ az: m.az, el: m.el });
  const [sl, setSl] = useState<Record<string, number>>(() => Object.fromEntries(m.sliders.map((s) => [s.name, s.value])));
  const drag = useRef<{ x: number; y: number; az: number; el: number } | null>(null);
  const env: Env = sl;

  const scene = useMemo(() => {
    const [x0, x1] = m.x, [y0, y1] = m.y;
    const N = m.surface?.mesh ?? 0;
    const F = m.surface ? (x: number, y: number) => m.surface!.F({ ...env, x, y }) : null;
    // sample the surface once; fit z if no range was given
    const grid: number[][] = [];
    if (F)
      for (let i = 0; i <= N; i++) {
        grid.push([]);
        for (let j = 0; j <= N; j++) grid[i].push(F(x0 + ((x1 - x0) * i) / N, y0 + ((y1 - y0) * j) / N));
      }
    let [z0, z1] = m.z ?? [Infinity, -Infinity];
    if (!m.z) {
      for (const row of grid) for (const v of row) if (Number.isFinite(v)) { z0 = Math.min(z0, v); z1 = Math.max(z1, v); }
      for (const c of m.curves)
        for (let i = 0; i <= 60; i++) {
          const s = c.s0(env) + ((c.s1(env) - c.s0(env)) * i) / 60;
          const v = c.Z({ ...env, s });
          if (Number.isFinite(v)) { z0 = Math.min(z0, v); z1 = Math.max(z1, v); }
        }
      if (!Number.isFinite(z0)) [z0, z1] = [-1, 1];
      if (z1 - z0 < 1e-9) { z0 -= 1; z1 += 1; }
    }
    return { grid, z: [z0, z1] as [number, number], N };
  }, [m, sl]); // eslint-disable-line react-hooks/exhaustive-deps

  const [x0, x1] = m.x, [y0, y1] = m.y, [z0, z1] = scene.z;
  const az = (view.az * Math.PI) / 180, el = (view.el * Math.PI) / 180;
  const ca = Math.cos(az), sa = Math.sin(az), ce = Math.cos(el), se = Math.sin(el);
  // one fixed zoom for every angle: the box [-1,1] x [-1,1] x [-0.75,0.75] must fit at any azimuth
  const fit = useMemo(() => {
    let w = 0, top = 0, bottom = 0;
    for (let a = 0; a < 360; a += 10)
      for (const e of [m.el, 4, 88]) {
        const A = (a * Math.PI) / 180, E = (e * Math.PI) / 180;
        for (const u of [-1, 1]) for (const v of [-1, 1]) for (const z of [-0.75, 0.75]) {
          const u1 = u * Math.cos(A) - v * Math.sin(A), v1 = u * Math.sin(A) + v * Math.cos(A);
          const yy = z * Math.cos(E) + v1 * Math.sin(E);
          w = Math.max(w, Math.abs(u1));
          top = Math.max(top, yy);
          bottom = Math.min(bottom, yy);
        }
      }
    const S = Math.min((W / 2 - 36) / w, (H - 56) / (top - bottom));
    return { S, cy: 22 + S * top };
  }, [m.el]);
  const S = fit.S;
  const norm = (x: number, y: number, z: number) => [((x - x0) / (x1 - x0)) * 2 - 1, ((y - y0) / (y1 - y0)) * 2 - 1, (((z - z0) / (z1 - z0)) * 2 - 1) * 0.75];
  const proj = (x: number, y: number, z: number) => {
    const [u, v, w] = norm(x, y, z);
    const u1 = u * ca - v * sa, v1 = u * sa + v * ca;
    return { X: W / 2 + S * u1, Y: fit.cy - S * (w * ce + v1 * se), d: -v1 * ce + w * se };
  };
  /** Sutherland-Hodgman: keep the part of a 3-D polygon with z0 <= z <= z1. */
  const clipZ = (poly: number[][]) => {
    let out = poly;
    for (const [lim, keep] of [[z1, (z: number) => z <= z1], [z0, (z: number) => z >= z0]] as const) {
      const next: number[][] = [];
      for (let k = 0; k < out.length; k++) {
        const P = out[k], Q = out[(k + 1) % out.length];
        const pin = keep(P[2]), qin = keep(Q[2]);
        if (pin) next.push(P);
        if (pin !== qin) {
          const t = (lim - P[2]) / (Q[2] - P[2]);
          next.push([P[0] + t * (Q[0] - P[0]), P[1] + t * (Q[1] - P[1]), lim]);
        }
      }
      out = next;
      if (out.length < 3) return [];
    }
    return out;
  };
  const prims: Prim[] = [];
  const floor: React.ReactNode[] = [];

  // floor: box outline, then level curves
  const fc = [proj(x0, y0, z0), proj(x1, y0, z0), proj(x1, y1, z0), proj(x0, y1, z0)];
  floor.push(<path key="floor" d={`M${fc.map((p) => `${p.X.toFixed(1)},${p.Y.toFixed(1)}`).join("L")}Z`} className="mt3-floor" />);
  const N = scene.N, g = scene.grid;
  const gx = (i: number) => x0 + ((x1 - x0) * i) / N, gy = (j: number) => y0 + ((y1 - y0) * j) / N;
  const segs = (level: number, zAt: (l: number) => number) => {
    const out: [ReturnType<typeof proj>, ReturnType<typeof proj>][] = [];
    const lerp = (a: number, b: number, fa: number, fb: number) => a + ((b - a) * (fa - level)) / (fa - fb);
    for (let i = 0; i < N; i++)
      for (let j = 0; j < N; j++) {
        const a = g[i][j], b = g[i + 1][j], c = g[i + 1][j + 1], e = g[i][j + 1];
        if (![a, b, c, e].every(Number.isFinite)) continue;
        const pts: [number, number][] = [];
        if (a > level !== b > level) pts.push([lerp(gx(i), gx(i + 1), a, b), gy(j)]);
        if (b > level !== c > level) pts.push([gx(i + 1), lerp(gy(j), gy(j + 1), b, c)]);
        if (c > level !== e > level) pts.push([lerp(gx(i + 1), gx(i), c, e), gy(j + 1)]);
        if (e > level !== a > level) pts.push([gx(i), lerp(gy(j + 1), gy(j), e, a)]);
        for (let p = 0; p + 1 < pts.length; p += 2) out.push([proj(pts[p][0], pts[p][1], zAt(level)), proj(pts[p + 1][0], pts[p + 1][1], zAt(level))]);
      }
    return out;
  };
  if (N) {
    m.levels.forEach((L, k) => {
      const d = segs(L(env), () => z0).map(([p, q]) => `M${p.X.toFixed(1)},${p.Y.toFixed(1)}L${q.X.toFixed(1)},${q.Y.toFixed(1)}`).join("");
      floor.push(<path key={`lv${k}`} d={d} style={{ stroke: col(2) }} strokeWidth={1.4} fill="none" opacity={0.8} />);
    });
  }

  // surface quads, shaded by height and by a light from the upper left
  if (N) {
    for (let i = 0; i < N; i++)
      for (let j = 0; j < N; j++) {
        const zs = [g[i][j], g[i + 1][j], g[i + 1][j + 1], g[i][j + 1]];
        if (!zs.every(Number.isFinite)) continue;
        if (zs.every((z) => z > z1) || zs.every((z) => z < z0)) continue;
        const c3 = clipZ([[gx(i), gy(j), zs[0]], [gx(i + 1), gy(j), zs[1]], [gx(i + 1), gy(j + 1), zs[2]], [gx(i), gy(j + 1), zs[3]]]);
        if (c3.length < 3) continue;
        const p = c3.map(([x, y, z]) => proj(x, y, z));
        const q4 = [[gx(i), gy(j), zs[0]], [gx(i + 1), gy(j), zs[1]], [gx(i + 1), gy(j + 1), zs[2]], [gx(i), gy(j + 1), zs[3]]];
        const n0 = q4.map(([x, y, z]) => norm(x, y, z));
        const ux = n0[2][0] - n0[0][0], uy = n0[2][1] - n0[0][1], uz = n0[2][2] - n0[0][2];
        const vx = n0[3][0] - n0[1][0], vy = n0[3][1] - n0[1][1], vz = n0[3][2] - n0[1][2];
        let nx = uy * vz - uz * vy, ny = uz * vx - ux * vz, nz = ux * vy - uy * vx;
        const len = Math.hypot(nx, ny, nz) || 1;
        nx /= len; ny /= len; nz /= len;
        const light = Math.abs(nx * -0.35 + ny * -0.45 + nz * 0.82);
        const t = ((zs[0] + zs[1] + zs[2] + zs[3]) / 4 - z0) / (z1 - z0);
        const hue = 225 - 195 * Math.min(1, Math.max(0, t));
        const fill = `hsl(${hue.toFixed(0)} 62% ${(30 + 34 * light).toFixed(0)}%)`;
        const d = `M${p.map((q) => `${q.X.toFixed(1)},${q.Y.toFixed(1)}`).join("L")}Z`;
        prims.push({ depth: p.reduce((acc, q) => acc + q.d, 0) / p.length, node: <path key={`q${i}-${j}`} d={d} fill={fill} stroke={fill} strokeWidth={0.6} opacity={0.94} /> });
      }
  }

  // plane z = C, with the level curve F = C drawn where it cuts the surface
  if (m.plane) {
    const C = m.plane.C(env);
    if (Number.isFinite(C) && C >= z0 && C <= z1) {
      const P = 10;
      for (let i = 0; i < P; i++)
        for (let j = 0; j < P; j++) {
          const xa = x0 + ((x1 - x0) * i) / P, xb = x0 + ((x1 - x0) * (i + 1)) / P;
          const ya = y0 + ((y1 - y0) * j) / P, yb = y0 + ((y1 - y0) * (j + 1)) / P;
          const p = [proj(xa, ya, C), proj(xb, ya, C), proj(xb, yb, C), proj(xa, yb, C)];
          prims.push({ depth: (p[0].d + p[2].d) / 2 + 0.002, node: <path key={`p${i}-${j}`} d={`M${p.map((q) => `${q.X.toFixed(1)},${q.Y.toFixed(1)}`).join("L")}Z`} className="mt3-plane" /> });
        }
      if (N)
        for (const [p, q] of segs(C, (l) => l)) {
          prims.push({ depth: (p.d + q.d) / 2 + 0.01, node: <line key={`c${p.X}${p.Y}`} x1={p.X} y1={p.Y} x2={q.X} y2={q.Y} style={{ stroke: col(2) }} strokeWidth={3} strokeLinecap="round" /> });
        }
      if (N)
        floor.push(
          <path key="shadow" d={segs(C, () => z0).map(([p, q]) => `M${p.X.toFixed(1)},${p.Y.toFixed(1)}L${q.X.toFixed(1)},${q.Y.toFixed(1)}`).join("")} style={{ stroke: col(2) }} strokeWidth={2.2} fill="none" strokeDasharray="5 4" />,
        );
    }
  }

  // 3-D curves and points
  m.curves.forEach((c, k) => {
    const lo = c.s0(env), hi = c.s1(env);
    let prev: ReturnType<typeof proj> | null = null;
    for (let i = 0; i <= 240; i++) {
      const s = lo + ((hi - lo) * i) / 240;
      const e = { ...env, s };
      const q = proj(c.X(e), c.Y(e), c.Z(e));
      if (prev && Number.isFinite(q.X) && Number.isFinite(prev.X))
        prims.push({ depth: (q.d + prev.d) / 2 + 0.02, node: <line key={`k${k}-${i}`} x1={prev.X} y1={prev.Y} x2={q.X} y2={q.Y} style={{ stroke: col(c.color) }} strokeWidth={2.6} strokeLinecap="round" /> });
      prev = q;
    }
  });
  const pointLabels: { X: number; Y: number; label: string; color: number }[] = [];
  m.points.forEach((p, k) => {
    const q = proj(p.X(env), p.Y(env), p.Z(env));
    if (!Number.isFinite(q.X)) return;
    prims.push({ depth: q.d + 0.05, node: <circle key={`pt${k}`} cx={q.X} cy={q.Y} r={5} style={{ fill: col(p.color) }} stroke="var(--paper)" strokeWidth={1.5} /> });
    if (p.label) pointLabels.push({ X: q.X, Y: q.Y, label: p.label, color: p.color });
  });
  prims.sort((a, b) => a.depth - b.depth);

  // axes: the floor edge along x and along y nearest the viewer, and the vertical edge at the leftmost corner.
  // Each gets min and max ticks pushed away from the floor's centre, and its name at the middle.
  const mid = proj((x0 + x1) / 2, (y0 + y1) / 2, z0);
  const xEdge = [y0, y1].map((yy) => ({ a: proj(x0, yy, z0), b: proj(x1, yy, z0) })).sort((p, q) => q.a.d + q.b.d - p.a.d - p.b.d)[0];
  const yEdge = [x0, x1].map((xx) => ({ a: proj(xx, y0, z0), b: proj(xx, y1, z0) })).sort((p, q) => q.a.d + q.b.d - p.a.d - p.b.d)[0];
  const corners = [[x0, y0], [x1, y0], [x1, y1], [x0, y1]].map(([xx, yy]) => ({ xx, yy, p: proj(xx, yy, z0) })).sort((p, q) => p.p.X - q.p.X);
  const zc = corners[0];
  const zEdge = { a: zc.p, b: proj(zc.xx, zc.yy, z1) };
  const away = (pt: { X: number; Y: number }, by: number) => {
    const dx = pt.X - mid.X, dy = pt.Y - mid.Y, l = Math.hypot(dx, dy) || 1;
    return { X: pt.X + (dx / l) * by, Y: pt.Y + (dy / l) * by };
  };
  const ax = [
    { ...xEdge, lab: m.labels.x ?? "$x$", lo: x0, hi: x1, out: 1 },
    { ...yEdge, lab: m.labels.y ?? "$y$", lo: y0, hi: y1, out: 1 },
  ].map((k) => {
    const loEnd = k.a, hiEnd = k.b;
    const c = { X: (k.a.X + k.b.X) / 2, Y: (k.a.Y + k.b.Y) / 2 };
    return { ...k, ticks: [{ at: away(loEnd, 14), v: k.lo, end: loEnd }, { at: away(hiEnd, 14), v: k.hi, end: hiEnd }], name: away(c, 26) };
  });
  // corners shared by two axes get one label only (the x axis keeps its own)
  const same = (p: { X: number; Y: number }, q: { X: number; Y: number }) => Math.hypot(p.X - q.X, p.Y - q.Y) < 2;
  ax[1].ticks = ax[1].ticks.filter((t) => !ax[0].ticks.some((u) => same(u.end, t.end)));
  // the foot of the z axis belongs to z: an x/y tick there would read as a z value
  ax.forEach((k) => (k.ticks = k.ticks.filter((t) => !same(t.end, zEdge.a))));
  const zAxis = {
    ...zEdge,
    lab: m.labels.z ?? "$z$",
    ticks: [{ at: { X: zEdge.a.X - 8, Y: zEdge.a.Y }, v: z0 }, { at: { X: zEdge.b.X - 8, Y: zEdge.b.Y }, v: z1 }],
    name: { X: zEdge.b.X, Y: zEdge.b.Y - 14 },
  };
  const changed = view.az !== m.az || view.el !== m.el || m.sliders.some((s) => sl[s.name] !== s.value);

  return (
    <figure className="mt-card mt-graph mt-3d">
      <div className="mt-head">
        <span className="mt-title">{m.title && <Markdown text={m.title} inline />}</span>
        {changed && (
          <button className="mt-icon" onClick={() => { setView({ az: m.az, el: m.el }); setSl(Object.fromEntries(m.sliders.map((s) => [s.name, s.value]))); }} title="Reset">
            <RotateCcw size={14} />
          </button>
        )}
      </div>
      <div className="mt-plot">
        <svg
          viewBox={`0 0 ${W} ${H}`}
          className="mt3-svg"
          onPointerDown={(e) => {
            e.currentTarget.setPointerCapture(e.pointerId);
            drag.current = { x: e.clientX, y: e.clientY, ...view };
          }}
          onPointerMove={(e) => {
            const d = drag.current;
            if (!d) return;
            setView({ az: d.az - (e.clientX - d.x) * 0.45, el: Math.min(88, Math.max(4, d.el + (e.clientY - d.y) * 0.35)) });
          }}
          onPointerUp={() => (drag.current = null)}
          role="img"
          aria-label={m.title ?? "3-D graph"}
        >
          {floor}
          {[...ax, zAxis].map((k, i) => (
            <g key={i}>
              <line x1={k.a.X} y1={k.a.Y} x2={k.b.X} y2={k.b.Y} className="mt-axis" />
              {k.ticks.map((t, j) => (
                <text key={j} className="mt-tick" x={t.at.X} y={t.at.Y + 4} textAnchor={i === 2 ? "end" : "middle"}>{fmtNum(t.v)}</text>
              ))}
            </g>
          ))}
          {prims.map((p) => p.node)}
        </svg>
        <div className="mt-overlay">
          {[...ax, zAxis].map((k, i) => (
            <span key={i} className="mt-label mt-axis-name" style={{ left: `${(k.name.X / W) * 100}%`, top: `${(k.name.Y / H) * 100}%` }}>
              <Markdown text={k.lab} inline />
            </span>
          ))}
          {pointLabels.map((p, i) => (
            <span key={i} className="mt-label" style={{ left: `${((p.X + 8) / W) * 100}%`, top: `${((p.Y - 8) / H) * 100}%`, color: col(p.color) }}>
              <Markdown text={p.label} inline />
            </span>
          ))}
        </div>
      </div>
      {(m.surface?.label || m.plane?.label || m.curves.some((c) => c.label)) && (
        <div className="mt-legend">
          {m.surface?.label && (
            <span><i className="mt-swatch fill mt-swatch-surface" /><Markdown text={m.surface.label} inline /></span>
          )}
          {m.plane?.label && (
            <span><i className="mt-swatch" style={{ color: col(2) }} /><Markdown text={m.plane.label} inline /></span>
          )}
          {m.curves.filter((c) => c.label).map((c, i) => (
            <span key={i}><i className="mt-swatch" style={{ color: col(c.color) }} /><Markdown text={c.label!} inline /></span>
          ))}
        </div>
      )}
      {m.sliders.length > 0 && (
        <div className="mt-sliders">
          {m.sliders.map((s) => (
            <label key={s.name} className="mt-slider">
              <span className="mt-slider-name"><Markdown text={s.label} inline /></span>
              <input type="range" min={s.min} max={s.max} step={s.step} value={sl[s.name]} onChange={(e) => setSl({ ...sl, [s.name]: Number(e.target.value) })} />
              <span className="mt-slider-value">{fmtNum(sl[s.name])}</span>
            </label>
          ))}
        </div>
      )}
      <div className="mt-hint">Drag the picture to turn it.</div>
      {m.caption && (
        <figcaption>
          <Markdown text={m.caption} inline />
        </figcaption>
      )}
    </figure>
  );
}
