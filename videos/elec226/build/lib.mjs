// Shared builder for the ELEC 226 Test 2 explainer videos (one HyperFrames project per test question).
// A video is a list of scenes; each scene is generated as compositions/<id>.html with static SVG, KaTeX rendered at
// build time, and one paused GSAP timeline. Usage: see q1.mjs. Run: node build/q1.mjs (from videos/elec226).
// Edit the qN.mjs scripts with an editor, not sed or JS .replace(): both mangle the doubled LaTeX backslashes
// ('\\dfrac'), and a '$' in a replace() string is a special pattern. Inline math is small: use \dfrac / \dbinom.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import katex from 'katex';

const HERE = path.dirname(fileURLToPath(import.meta.url));
export const ROOT = path.resolve(HERE, '..');

// Look: white paper, black ink, one accent per idea.
export const C = {
  ink: '#111111', soft: '#6b6b6b', faint: '#d9d9d9', ground: '#ffffff',
  orange: '#e8590c', blue: '#1c7ed6', green: '#2b8a3e', red: '#c92a2a', purple: '#7048e8',
};

export const tex = (s, display = false) => katex.renderToString(s, { displayMode: display, throwOnError: true, output: 'html' });
/** Text with inline $math$ rendered. */
export const rich = (s) => s.split(/(\$[^$]+\$)/g).map((p) => (p.startsWith('$') && p.endsWith('$') && p.length > 1 ? tex(p.slice(1, -1)) : p)).join('');

const r2 = (v) => Math.round(v * 100) / 100;

export class Scene {
  constructor(id, dur) {
    this.id = id; this.dur = dur; this.svg = []; this.defs = []; this.html = []; this.tw = []; this.n = 0;
  }
  uid(p = 'e') { return `${this.id}-${p}${this.n++}`; }
  sel(id) { return `#${id}`; }

  // ---------------------------------------------------------------- tweens (all fromTo: seek-safe)
  fromTo(id, from, to, at) { this.tw.push(`tl.fromTo(${JSON.stringify(sels(id))}, ${JSON.stringify(from)}, ${JSON.stringify(to)}, ${r2(at)});`); return this; }
  to(id, to, at) { this.tw.push(`tl.to(${JSON.stringify(sels(id))}, ${JSON.stringify(to)}, ${r2(at)});`); return this; }
  set(id, vars, at) { this.tw.push(`tl.set(${JSON.stringify(sels(id))}, ${JSON.stringify(vars)}, ${r2(at)});`); return this; }
  appear(id, at, dur = 0.22) {
    return this.fromTo(id, { opacity: 0, filter: 'blur(8px)' }, { opacity: 1, filter: 'blur(0px)', duration: dur, ease: 'power4.out' }, at);
  }
  hide(id, at, dur = 0.18) { return this.to(id, { opacity: 0, filter: 'blur(6px)', duration: dur, ease: 'power2.in' }, at); }
  pop(id, at, dur = 0.35) {
    return this.fromTo(id, { opacity: 0, scale: 0, transformOrigin: '50% 50%' }, { opacity: 1, scale: 1, duration: dur, ease: 'back.out(1.6)' }, at);
  }
  draw(id, at, dur = 0.6, ease = 'power2.inOut') {
    return this.fromTo(id, { strokeDashoffset: 1.1 }, { strokeDashoffset: 0, duration: dur, ease }, at);
  }
  /** Highlight pulse that settles: colour change on text (ink -> colour). */
  tint(id, color, at, dur = 0.25) { return this.to(id, { color, duration: dur, ease: 'power2.out' }, at); }
  move(id, x, y, at, dur = 0.7, ease = 'power3.inOut') { return this.to(id, { x, y, duration: dur, ease }, at); }

  // ---------------------------------------------------------------- HTML text
  /** Positioned text. align: left | center | right (x is the left edge, centre or right edge). */
  text(html, { id = this.uid('t'), x = 192, y = 200, w = 1536, size = 40, weight = 400, color = C.ink, align = 'left',
    font = 'Inter', at = null, out = null, lh = 1.25, z = 2, style = '', hold = false } = {}) {
    const left = align === 'center' ? x - w / 2 : align === 'right' ? x - w : x;
    this.html.push(`<div id="${id}" class="t"${hold ? ' data-hold' : ''} style="left:${r2(left)}px;top:${r2(y)}px;width:${r2(w)}px;font-size:${size}px;` +
      `font-weight:${weight};color:${color};text-align:${align};font-family:'${font}',sans-serif;line-height:${lh};z-index:${z};${style}">${rich(html)}</div>`);
    if (at !== null) this.appear(id, at);
    if (out !== null) this.hide(id, out);
    return id;
  }
  /** Scene heading, top-left in Oswald. */
  title(s, at = 0.1, opts = {}) { return this.text(s, { x: 150, y: 70, size: 66, weight: 500, font: 'Oswald', at, ...opts }); }
  /** Bottom caption line (the line to read). */
  caption(s, at, opts = {}) { return this.text(s, { x: 960, y: 935, w: 1700, size: 44, align: 'center', at, hold: true, ...opts }); }
  math(t, opts = {}) { return this.text(`$${t}$`, opts); }

  // ---------------------------------------------------------------- SVG primitives
  line(x1, y1, x2, y2, { id = this.uid('l'), color = C.ink, width = 4, at = null, dur = 0.5, draw = true, dash = null, cap = 'round' } = {}) {
    const d = dash ? `stroke-dasharray="${dash}"` : (draw ? 'pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"' : '');
    this.svg.push(`<line id="${id}" x1="${r2(x1)}" y1="${r2(y1)}" x2="${r2(x2)}" y2="${r2(y2)}" stroke="${color}" stroke-width="${width}" stroke-linecap="${cap}" ${d}/>`);
    if (at !== null) (draw && !dash ? this.draw(id, at, dur) : this.appear(id, at));
    return id;
  }
  path(d, { id = this.uid('p'), color = C.ink, width = 5, fill = 'none', at = null, dur = 0.9, draw = true, ease = 'power2.inOut', opacity = 1, clip = null, join = 'round' } = {}) {
    const dd = draw && fill === 'none' ? 'pathLength="1" stroke-dasharray="1 1.2" stroke-dashoffset="1.1"' : '';
    this.svg.push(`<path id="${id}" d="${d}" stroke="${fill === 'none' ? color : 'none'}" stroke-width="${width}" fill="${fill}" ` +
      `fill-opacity="${opacity}" stroke-linejoin="${join}" stroke-linecap="round" ${dd} ${clip ? `clip-path="url(#${clip})"` : ''}/>`);
    if (at !== null) (draw && fill === 'none' ? this.draw(id, at, dur, ease) : this.appear(id, at, Math.min(dur, 0.35)));
    return id;
  }
  dot(cx, cy, { id = this.uid('d'), r = 11, color = C.ink, open = false, at = null, width = 4 } = {}) {
    this.svg.push(`<circle id="${id}" cx="${r2(cx)}" cy="${r2(cy)}" r="${r}" fill="${open ? C.ground : color}" stroke="${color}" stroke-width="${width}"/>`);
    if (at !== null) this.pop(id, at);
    return id;
  }
  rect(x, y, w, h, { id = this.uid('r'), fill = C.blue, opacity = 0.25, stroke = 'none', width = 0, at = null, rx = 0, clip = null } = {}) {
    this.svg.push(`<rect id="${id}" x="${r2(x)}" y="${r2(y)}" width="${r2(w)}" height="${r2(h)}" rx="${rx}" fill="${fill}" fill-opacity="${opacity}" ` +
      `stroke="${stroke}" stroke-width="${width}" ${clip ? `clip-path="url(#${clip})"` : ''}/>`);
    if (at !== null) this.appear(id, at);
    return id;
  }
  /** A left-to-right reveal window (a clipPath whose rect grows). Returns the clip id to pass as `clip`. */
  wipe(x0, x1, at, dur = 1.2, { ease = 'none', y0 = 0, y1 = 1080 } = {}) {
    const id = this.uid('cp');
    this.defs.push(`<clipPath id="${id}"><rect id="${id}-r" x="${r2(x0)}" y="${y0}" width="0" height="${y1 - y0}"/></clipPath>`);
    this.fromTo(`${id}-r`, { attr: { width: 0 } }, { attr: { width: x1 - x0 }, duration: dur, ease }, at);
    return id;
  }
  /** Group of ids that should leave together. */
  hideAll(ids, at) { return this.hide(ids, at); }

  // ---------------------------------------------------------------- plots
  /** Axes box. Returns mappers X(v), Y(v) and the frame. ticks: [{v, label}] (label may hold $math$). */
  axes({ x, y, w, h, xr, yr, xticks = [], yticks = [], xlabel = '', ylabel = '', at = 0.2, color = C.ink, tickSize = 32, yaxis = 'left' }) {
    const X = (v) => x + ((v - xr[0]) / (xr[1] - xr[0])) * w;
    const Y = (v) => y + h - ((v - yr[0]) / (yr[1] - yr[0])) * h;
    const y0 = yr[0] <= 0 && yr[1] >= 0 ? Y(0) : y + h;
    const x0 = yaxis === 'zero' && xr[0] <= 0 && xr[1] >= 0 ? X(0) : x; // 'left' keeps the axis off the stem at 0
    const ids = [];
    ids.push(this.line(x, y0, x + w, y0, { color, width: 3, at, dur: 0.6 }));
    ids.push(this.line(x0, y + h, x0, y, { color, width: 3, at: at + 0.1, dur: 0.6 }));
    xticks.forEach((t, i) => {
      ids.push(this.text(t.label ?? `$${t.v}$`, { x: X(t.v), y: y0 + 14, w: 160, size: tickSize, align: 'center', color: C.soft, at: at + 0.3 + i * 0.03 }));
    });
    yticks.forEach((t, i) => {
      ids.push(this.line(x0 - 8, Y(t.v), x0, Y(t.v), { color, width: 3, draw: false, at: at + 0.3 }));
      ids.push(this.text(t.label ?? `$${t.v}$`, { x: x0 - 18, y: Y(t.v) - tickSize * 0.65, w: 200, size: tickSize, align: 'right', color: C.soft, at: at + 0.3 + i * 0.03 }));
      if (t.guide) ids.push(this.line(x0, Y(t.v), x + w, Y(t.v), { color: C.faint, width: 2, dash: '8 8', at: at + 0.4 }));
    });
    if (xlabel) ids.push(this.text(xlabel, { x: x + w + 18, y: y0 - 26, w: 200, size: 36, color, at: at + 0.4 }));
    if (ylabel) ids.push(this.text(ylabel, { x: x0 - 20, y: y - 62, w: 600, size: 36, color, at: at + 0.4 }));
    return { X, Y, x, y, w, h, y0, x0, ids };
  }
  /** PMF stems; each grows from the axis then its dot pops. Returns ids per stem. */
  stems(ax, pts, { color = C.orange, at = 0.5, stagger = 0.35, width = 6, r = 12, labels = null, labelColor = C.ink, labelSize = 32, labelGap = 1.9 } = {}) {
    return pts.map(([v, p], i) => {
      const t = at + i * stagger;
      const l = this.line(ax.X(v), ax.Y(0), ax.X(v), ax.Y(p), { color, width, at: t, dur: 0.35 });
      const d = this.dot(ax.X(v), ax.Y(p), { color, r, at: t + 0.28 });
      let lab = null;
      if (labels) lab = this.text(labels[i], { x: ax.X(v), y: ax.Y(p) - labelSize * labelGap, w: 220, size: labelSize, align: 'center', color: labelColor, at: t + 0.3 });
      return { l, d, lab, t };
    });
  }
  /** Step CDF from sorted [v, p] masses over [x0, x1] on axes. Pieces appear in order; returns their start times. */
  staircase(ax, pts, x0, x1, { color = C.orange, at = 0.5, stagger = 0.35, width = 6, labels = null, labelSize = 30, labelGap = 1.6 } = {}) {
    let total = 0; let prev = x0; const out = [];
    const seg = (a, b, yv, t) => this.line(ax.X(a), ax.Y(yv), ax.X(b), ax.Y(yv), { color, width, at: t, dur: 0.3 });
    out.push(seg(x0, pts[0][0], 0, at));
    pts.forEach(([v, p], i) => {
      const t = at + (i + 1) * stagger;
      const before = total; total += p;
      this.dot(ax.X(v), ax.Y(before), { color, r: 10, open: true, at: t });
      this.dot(ax.X(v), ax.Y(total), { color, r: 11, at: t + 0.05 });
      const next = i + 1 < pts.length ? pts[i + 1][0] : x1;
      out.push(seg(v, next, total, t + 0.1));
      if (labels) this.text(labels[i], { x: ax.X(v) + 10, y: ax.Y(total) - labelSize * labelGap, w: 200, size: labelSize, color, at: t + 0.15 });
      prev = v;
    });
    return out;
  }
  /** Polyline path of f over [a, b] on axes (n samples). */
  fpath(ax, f, a, b, n = 160) {
    const pts = [];
    for (let i = 0; i <= n; i++) { const v = a + ((b - a) * i) / n; pts.push([ax.X(v), ax.Y(f(v))]); }
    return 'M' + pts.map(([px, py]) => `${r2(px)},${r2(py)}`).join(' L');
  }
  /** Closed area under f over [a, b] down to y=0 on axes. */
  fareaPath(ax, f, a, b, n = 160) {
    return this.fpath(ax, f, a, b, n) + ` L${r2(ax.X(b))},${r2(ax.Y(0))} L${r2(ax.X(a))},${r2(ax.Y(0))} Z`;
  }
  curve(ax, f, a, b, opts = {}) { return this.path(this.fpath(ax, f, a, b, opts.n ?? 160), opts); }
  area(ax, f, a, b, { color = C.blue, opacity = 0.25, at = null, sweep = 0, ...rest } = {}) {
    const clip = sweep ? this.wipe(ax.X(a), ax.X(b), at, sweep) : null;
    const id = this.path(this.fareaPath(ax, f, a, b), { fill: color, opacity, draw: false, at: sweep ? null : at, clip, ...rest });
    if (sweep) this.set(id, { opacity: 1 }, at);
    return id;
  }

  // ---------------------------------------------------------------- output
  render() {
    const svg = `<svg id="${this.id}-svg" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0;top:0;z-index:1">` +
      `<defs>${this.defs.join('')}</defs>${this.svg.join('\n')}</svg>`;
    const end = Math.max(0.1, this.dur - 0.3);
    return `<template>
<style>
  #root { position: absolute; inset: 0; background: ${C.ground}; overflow: hidden; }
</style>
<div id="root" data-composition-id="${this.id}" data-width="1920" data-height="1080">
  <div id="${this.id}-stage" style="position:absolute;inset:0">
${svg}
${this.html.join('\n')}
  </div>
</div>
<script>
  const tl = gsap.timeline({ paused: true });
  ${this.tw.join('\n  ')}
  tl.to("#${this.id}-stage", { opacity: 0, filter: "blur(8px)", duration: 0.25, ease: "power2.in" }, ${r2(end)});
  window.__timelines["${this.id}"] = tl;
</script>
</template>
`;
  }
}

function sels(id) { return Array.isArray(id) ? id.map((i) => `#${i}`).join(', ') : `#${id}`; }

/** Write a whole video: compositions/<scene>.html, index.html, KaTeX assets. */
export function writeVideo(project, title, scenes) {
  const dir = path.join(ROOT, project);
  fs.mkdirSync(path.join(dir, 'compositions'), { recursive: true });
  const kdir = path.join(dir, 'assets', 'katex');
  fs.mkdirSync(path.join(kdir, 'fonts'), { recursive: true });
  const kdist = path.join(HERE, 'node_modules', 'katex', 'dist');
  fs.copyFileSync(path.join(kdist, 'katex.min.css'), path.join(kdir, 'katex.min.css'));
  for (const f of fs.readdirSync(path.join(kdist, 'fonts'))) if (f.endsWith('.woff2')) fs.copyFileSync(path.join(kdist, 'fonts', f), path.join(kdir, 'fonts', f));
  for (const f of fs.readdirSync(path.join(dir, 'compositions'))) if (f.endsWith('.html')) fs.unlinkSync(path.join(dir, 'compositions', f));
  let t = 0; const hosts = [];
  scenes.forEach((s, i) => {
    fs.writeFileSync(path.join(dir, 'compositions', `${s.id}.html`), s.render());
    hosts.push(`      <div id="${s.id}" data-composition-id="${s.id}" data-composition-src="compositions/${s.id}.html" data-start="${r2(t)}" ` +
      `data-duration="${s.dur}" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>`);
    t += s.dur;
  });
  const total = r2(t);
  fs.writeFileSync(path.join(dir, 'index.html'), `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>${title}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link rel="stylesheet" href="assets/katex/katex.min.css" />
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: ${C.ground}; }
      #main { width: 100%; height: 100%; position: relative; }
      #bg { position: absolute; inset: 0; background: ${C.ground}; }
      .t { position: absolute; white-space: normal; }
      .t .katex { font-size: 1.08em; }
    </style>
  </head>
  <body>
    <div id="main" data-composition-id="main" data-start="0" data-duration="${total}" data-width="1920" data-height="1080">
      <div id="bg"></div>
${hosts.join('\n')}
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
`);
  console.log(`${project}: ${scenes.length} scenes, ${total}s -> ${dir}`);
}
