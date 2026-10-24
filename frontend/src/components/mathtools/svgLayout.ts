import { useLayoutEffect, type RefObject } from "react";
import { schematicImage } from "../../api";

/*
 * Inline circuit SVGs and the automatic label layout that keeps their text from overlapping.
 *
 * The server draws a schematic as an SVG whose top-level children are strokes (paths, circles: wires and
 * element bodies) and labels (one <g> of glyphs per label). `autoLayout` runs in the browser after each
 * render: it measures every label, and any label that overlaps a stroke or another label moves to the
 * nearest free spot (tried in rings of growing distance, preferring spots inside the frame). Overlays from
 * ```circuitsteps follow: mesh arrows shrink until their ring clears every label and element, then overlay
 * labels (callouts, mesh names, path labels) move clear of everything placed before them. It is plain
 * geometry, run again whenever the drawing changes size, so a new drawing needs no hand tuning.
 */

export type Box = { x: number; y: number; w: number; h: number };
export type Parsed = { box: Box; parts: { html: string; label: boolean }[] };

/** Split the server's SVG into its top-level parts, recoloured to follow the theme. */
function splitSvg(text: string): Parsed {
  const doc = new DOMParser().parseFromString(text, "image/svg+xml");
  const svg = doc.documentElement;
  const [x, y, w, h] = (svg.getAttribute("viewBox") ?? "0 0 0 0").split(/\s+/).map(Number);
  const parts: Parsed["parts"] = [];
  for (const el of Array.from(svg.children)) {
    if (["script", "foreignObject", "style"].includes(el.tagName)) continue;
    for (const node of [el, ...Array.from(el.querySelectorAll("*"))]) {
      if (["script", "foreignObject"].includes(node.tagName)) {
        node.remove();
        continue;
      }
      for (const attr of Array.from(node.attributes)) {
        // glyphs are <use href="#glyph">: keep in-document links only
        if (/^on/i.test(attr.name) || (/href/i.test(attr.name) && !attr.value.startsWith("#"))) node.removeAttribute(attr.name);
        else node.setAttribute(attr.name, attr.value.replace(/\bblack\b/g, "currentColor").replace(/\bwhite\b/g, "var(--raised)"));
      }
    }
    parts.push({ html: el.outerHTML, label: el.tagName === "g" });
  }
  return { box: { x, y, w, h }, parts };
}

const svgCache = new Map<string, Promise<Parsed>>();
export function loadSvg(drawing: string) {
  if (!svgCache.has(drawing)) {
    const p = schematicImage(drawing).then(async (url) => splitSvg(await (await fetch(url)).text()));
    p.catch(() => svgCache.delete(drawing));
    svgCache.set(drawing, p);
  }
  return svgCache.get(drawing)!;
}

/** A part wrapped so the layout knows what it is: data-p="L" labels move, "S" strokes are obstacles. */
export const wrapPart = (part: Parsed["parts"][number], cls = "") =>
  `<g data-p="${part.label ? "L" : "S"}"${cls ? ` class="${cls}"` : ""}>${part.html}</g>`;

type Pt = [number, number];

export function arrowHead(tip: Pt, dir: Pt, size: number) {
  const len = Math.hypot(dir[0], dir[1]) || 1;
  const [ux, uy] = [dir[0] / len, dir[1] / len];
  const back: Pt = [tip[0] - ux * size, tip[1] - uy * size];
  const side: Pt = [-uy * size * 0.55, ux * size * 0.55];
  return `${tip[0]},${tip[1]} ${back[0] + side[0]},${back[1] + side[1]} ${back[0] - side[0]},${back[1] - side[1]}`;
}

/** A 300° mesh arrow: the arrowhead sits at the lower right (ccw) or lower left (cw), like a hand-drawn one. */
export function meshGeometry(cx: number, cy: number, r: number, ccw: boolean) {
  const end = ((ccw ? 45 : 135) * Math.PI) / 180;
  const start = end + ((ccw ? 300 : -300) * Math.PI) / 180;
  const p = (t: number): Pt => [cx + r * Math.cos(t), cy + r * Math.sin(t)];
  const [x0, y0] = p(start);
  const [x1, y1] = p(end);
  const dir: Pt = ccw ? [Math.sin(end), -Math.cos(end)] : [-Math.sin(end), Math.cos(end)];
  return {
    d: `M ${x0} ${y0} A ${r} ${r} 0 1 ${ccw ? 0 : 1} ${x1} ${y1}`,
    head: arrowHead([x1 + dir[0] * 4, y1 + dir[1] * 4], dir, Math.min(11, r * 0.45)),
  };
}

// ------------------------------------------------------------------ layout

type R = { x0: number; y0: number; x1: number; y1: number };
type Ring = { cx: number; cy: number; r: number };

const hit = (a: R, b: R, pad: number) => a.x0 < b.x1 + pad && b.x0 < a.x1 + pad && a.y0 < b.y1 + pad && b.y0 < a.y1 + pad;
const shift = (a: R, dx: number, dy: number): R => ({ x0: a.x0 + dx, y0: a.y0 + dy, x1: a.x1 + dx, y1: a.y1 + dy });

/** Does a ring of radius r (stroke about 3 wide) cross the rectangle? */
function ringHits(g: Ring, b: R, pad = 2) {
  const nx = Math.max(b.x0, Math.min(g.cx, b.x1)) - g.cx;
  const ny = Math.max(b.y0, Math.min(g.cy, b.y1)) - g.cy;
  const near = Math.hypot(nx, ny);
  const far = Math.max(...[b.x0, b.x1].flatMap((x) => [b.y0, b.y1].map((y) => Math.hypot(x - g.cx, y - g.cy))));
  return near <= g.r + pad && far >= g.r - pad;
}

// Candidate moves, nearest first: rings of 2, 4, ... 48 units, 16 directions each, straight up/down/left/right first.
const OFFSETS: Pt[] = [[0, 0]];
for (let d = 2; d <= 48; d += 2)
  for (const a of [270, 90, 0, 180, 315, 225, 45, 135, 292.5, 247.5, 67.5, 112.5, 337.5, 202.5, 22.5, 157.5])
    OFFSETS.push([d * Math.cos((a * Math.PI) / 180), d * Math.sin((a * Math.PI) / 180)]);

// Ring centre slides: none first, then 3, 6, ... 18 units in 8 directions.
const RING_OFFSETS: Pt[] = [[0, 0]];
for (let d = 3; d <= 18; d += 3)
  for (const a of [0, 180, 270, 90, 315, 225, 45, 135])
    RING_OFFSETS.push([d * Math.cos((a * Math.PI) / 180), d * Math.sin((a * Math.PI) / 180)]);

function place(b: R, blocked: (r: R) => boolean, bounds: R): Pt {
  let outside: Pt | null = null;
  for (const [dx, dy] of OFFSETS) {
    const m = shift(b, dx, dy);
    if (blocked(m)) continue;
    if (m.x0 >= bounds.x0 && m.x1 <= bounds.x1 && m.y0 >= bounds.y0 && m.y1 <= bounds.y1) return [dx, dy];
    outside ??= [dx, dy];
  }
  return outside ?? [0, 0];
}

export function autoLayout(svg: SVGSVGElement) {
  const ctm = svg.getScreenCTM();
  if (!ctm || !svg.getBoundingClientRect().width) return; // hidden (e.g. a closed solution): try again when shown
  const inv = ctm.inverse();
  const pt = svg.createSVGPoint();
  const user = (el: Element): R | null => {
    const r = el.getBoundingClientRect();
    if (!r.width && !r.height) return null;
    pt.x = r.left;
    pt.y = r.top;
    const a = pt.matrixTransform(inv);
    pt.x = r.right;
    pt.y = r.bottom;
    const b = pt.matrixTransform(inv);
    return { x0: Math.min(a.x, b.x), y0: Math.min(a.y, b.y), x1: Math.max(a.x, b.x), y1: Math.max(a.y, b.y) };
  };
  const live = (el: Element) => !el.closest(".cs-gone");
  const vb = svg.viewBox.baseVal;
  const bounds: R = { x0: vb.x, y0: vb.y, x1: vb.x + vb.width, y1: vb.y + vb.height };

  // Start from the drawing as authored.
  svg.querySelectorAll('[data-p="L"], .cs-mov').forEach((g) => g.removeAttribute("transform"));
  const meshes = Array.from(svg.querySelectorAll<SVGGElement>('.cs-ov[data-kind="mesh"]')).filter(live);
  const setMesh = (g: SVGGElement, r: number, dx = 0, dy = 0) => {
    const geo = meshGeometry(Number(g.dataset.cx) + dx, Number(g.dataset.cy) + dy, r, g.dataset.ccw === "1");
    g.querySelector(".cs-stroke")?.setAttribute("d", geo.d);
    g.querySelector(".cs-head")?.setAttribute("points", geo.head);
    // the mesh's name rides along with the ring (step 4 starts placing it from here)
    g.dataset.dx = `${dx}`;
    g.dataset.dy = `${dy}`;
  };
  meshes.forEach((g) => setMesh(g, Number(g.dataset.r)));

  // 1. Strokes of the drawing and fixed overlay marks (polarity boxes, path segments) are obstacles.
  const strokes: R[] = [];
  svg.querySelectorAll('[data-p="S"]').forEach((g) => {
    if (live(g)) g.querySelectorAll("path, circle, polygon, rect, line").forEach((el) => strokes.push(...[user(el)].filter((b): b is R => !!b)));
  });
  const marks: R[] = [];
  svg.querySelectorAll(".cs-ov").forEach((g) => {
    if (!live(g)) return;
    if (g.querySelector(".cs-plus, .cs-minus")) marks.push(...[user(g)].filter((b): b is R => !!b));
    const pts = (g as SVGGElement).dataset.pts?.split(" ").map((p) => p.split(",").map(Number) as Pt);
    pts?.slice(1).forEach(([x, y], i) => {
      const [px, py] = pts[i];
      marks.push({ x0: Math.min(x, px) - 3, y0: Math.min(y, py) - 3, x1: Math.max(x, px) + 3, y1: Math.max(y, py) + 3 });
    });
    // a dashed region's outline (not its inside): text crossed by the dashes is hard to read
    const rect = g.querySelector("rect.cs-region");
    const r = rect && user(rect);
    if (r)
      marks.push(
        { x0: r.x0, y0: r.y0 - 1, x1: r.x1, y1: r.y0 + 1 },
        { x0: r.x0, y0: r.y1 - 1, x1: r.x1, y1: r.y1 + 1 },
        { x0: r.x0 - 1, y0: r.y0, x1: r.x0 + 1, y1: r.y1 },
        { x0: r.x1 - 1, y0: r.y0, x1: r.x1 + 1, y1: r.y1 },
      );
  });

  // 2. The drawing's own labels: clear of strokes (a small overlap is tolerated) and of each other.
  const labels: R[] = [];
  svg.querySelectorAll<SVGGElement>('[data-p="L"]').forEach((g) => {
    const b = live(g) && user(g);
    if (!b) return;
    // A label drawn inside an element body (the A of an ammeter, a source's sign) belongs there: that body is not an obstacle.
    const around = strokes.filter((s) => s.x0 <= b.x0 && s.y0 <= b.y0 && s.x1 >= b.x1 && s.y1 >= b.y1);
    const [dx, dy] = place(
      b,
      (m) =>
        strokes.some((s) => !around.includes(s) && hit(m, s, -1.5)) || labels.some((l) => hit(m, l, 1.5)) || marks.some((s) => hit(m, s, 0.5)),
      bounds,
    );
    if (dx || dy) g.setAttribute("transform", `translate(${dx} ${dy})`);
    labels.push(shift(b, dx, dy));
  });

  // 3. Mesh arrows shrink, and if that is not enough slide off-centre, until the ring crosses no element,
  //    label or polarity box (nor another ring). Smallest change first: shrink in place, then nearer slides.
  const rings: Ring[] = [];
  for (const g of meshes) {
    const [cx, cy, r0] = [Number(g.dataset.cx), Number(g.dataset.cy), Number(g.dataset.r)];
    const obstacles = [...strokes, ...labels, ...marks];
    const count = (x: number, y: number, r: number) =>
      obstacles.filter((o) => ringHits({ cx: x, cy: y, r }, o)).length +
      rings.filter((q) => Math.hypot(q.cx - x, q.cy - y) < q.r + r + 3).length;
    // never shrink below the mesh's own name (it sits in the middle of the ring)
    const name = g.querySelector(".cs-label-in");
    const nb = name && user(name);
    const floor = Math.max(9, r0 * 0.4, nb ? Math.hypot(nb.x1 - nb.x0, nb.y1 - nb.y0) / 2 + 3 : 0);
    let best = { dx: 0, dy: 0, r: r0, c: count(cx, cy, r0) };
    search: for (const [dx, dy] of RING_OFFSETS)
      for (let r = r0; r >= floor; r -= 1) {
        const c = count(cx + dx, cy + dy, r);
        if (c < best.c) best = { dx, dy, r, c };
        if (c === 0) break search;
      }
    if (best.r !== r0 || best.dx || best.dy) setMesh(g, best.r, best.dx, best.dy);
    rings.push({ cx: cx + best.dx, cy: cy + best.dy, r: best.r });
  }

  // 4. Overlay labels (callouts, mesh names, path and region labels) clear of everything above and each other.
  const placed: R[] = [];
  svg.querySelectorAll<SVGGElement>(".cs-mov").forEach((g) => {
    const inner = g.querySelector(".cs-label-in, text");
    const measured = live(g) && inner && user(inner);
    if (!measured) return;
    const host = g.closest<SVGGElement>('.cs-ov[data-kind="mesh"]');
    const [bx, by] = [Number(host?.dataset.dx ?? 0), Number(host?.dataset.dy ?? 0)];
    const b = shift(measured, bx, by);
    const blocked = (m: R) =>
      strokes.some((s) => hit(m, s, 0.5)) ||
      labels.some((l) => hit(m, l, 2)) ||
      marks.some((l) => hit(m, l, 1)) ||
      placed.some((l) => hit(m, l, 2)) ||
      rings.some((r) => ringHits(r, m, 1.5));
    const [dx, dy] = place(b, blocked, bounds);
    if (dx + bx || dy + by) g.setAttribute("transform", `translate(${dx + bx} ${dy + by})`);
    placed.push(shift(b, dx, dy));
  });
}

/** Run autoLayout after every render of the SVG, again when it changes size (shown, resized) and once fonts load. */
export function useAutoLayout(ref: RefObject<SVGSVGElement | null>, deps: unknown[]) {
  useLayoutEffect(() => {
    const svg = ref.current;
    if (!svg) return;
    let live = true;
    const run = () => live && autoLayout(svg);
    run();
    const seen = new ResizeObserver(run);
    seen.observe(svg);
    document.fonts?.ready.then(run);
    return () => {
      live = false;
      seen.disconnect();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
}
