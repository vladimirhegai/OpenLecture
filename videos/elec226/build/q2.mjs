// Test 2 - Question 2: continuous random variables, PDF, CDF, uniform, exponential, Gaussian, mixed (Lectures 9-11).
import { Scene, C, writeVideo } from './lib.mjs';

// Abramowitz-Stegun 7.1.26 erf, good to ~1e-7: enough for on-screen 4-decimal values.
const erf = (x) => {
  const s = Math.sign(x), a = Math.abs(x), t = 1 / (1 + 0.3275911 * a);
  return s * (1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-a * a));
};
const Phi = (z) => 0.5 * (1 + erf(z / Math.SQRT2));
const npdf = (m, sd) => (x) => Math.exp(-((x - m) ** 2) / (2 * sd * sd)) / (sd * Math.sqrt(2 * Math.PI));
const gam = (x) => (x <= 0 ? 0 : (x * x * Math.exp(-x)) / 2); // Gamma(3,1) PDF: a smooth one-hump density
const gamF = (x) => (x <= 0 ? 0 : 1 - Math.exp(-x) * (1 + x + (x * x) / 2));
const fact = (n) => (n <= 1 ? 1 : n * fact(n - 1));
const pois = (l, k) => Math.exp(-l) * l ** k / fact(k);
const f4 = (v) => v.toFixed(4);
const S = [];

// ------------------------------------------------------------------ intro
{
  const s = new Scene('q2-intro', 5.5);
  s.text('ELEC 226 · Test 2', { x: 150, y: 330, size: 38, color: C.soft, at: 0.2 });
  s.text('Question 2', { x: 150, y: 380, size: 150, weight: 500, font: 'Oswald', at: 0.35 });
  s.text('Continuous random variables: PDF, CDF, uniform, exponential, Gaussian', { x: 150, y: 590, w: 1000, size: 46, at: 0.7 });
  const ax = s.axes({ x: 1250, y: 360, w: 520, h: 300, xr: [-3.4, 3.4], yr: [0, 0.45], at: 0.6 });
  s.area(ax, npdf(0, 1), -3.4, 3.4, { color: C.blue, opacity: 0.18, at: 1.0, sweep: 1.4 });
  s.curve(ax, npdf(0, 1), -3.4, 3.4, { color: C.blue, width: 6, at: 1.0, dur: 1.4, ease: 'none' });
  S.push(s);
}

// ------------------------------------------------------------------ discrete stems -> continuous curve, probability = area
{
  const s = new Scene('q2-area', 14.5);
  s.title('Continuous: probability is area under the curve');
  s.text('Discrete: a chance at each point', { x: 150, y: 190, w: 700, size: 38, color: C.orange, at: 0.6 });
  const l = s.axes({ x: 150, y: 290, w: 680, h: 400, xr: [-0.6, 7.6], yr: [0, 0.32], xticks: [0, 2, 4, 6].map((v) => ({ v })), at: 0.5 });
  s.stems(l, [0, 1, 2, 3, 4, 5, 6, 7].map((k) => [k, pois(2, k)]), { at: 1.0, stagger: 0.12 });
  s.text('Continuous: a smooth curve, the PDF $f_X(x)$', { x: 1000, y: 190, w: 820, size: 38, color: C.blue, at: 2.6 });
  const r = s.axes({ x: 1040, y: 290, w: 720, h: 400, xr: [0, 8], yr: [0, 0.32], xticks: [0, 1, 2, 3, 4, 6].map((v) => ({ v })), xlabel: '$x$', at: 2.5 });
  s.curve(r, gam, 0, 8, { color: C.blue, width: 6, at: 3.0, dur: 1.2 });
  const p13 = gamF(3) - gamF(1);
  s.area(r, gam, 1, 3, { color: C.blue, opacity: 0.3, at: 4.8, sweep: 0.9 });
  s.text(`$P(1<X<3)$<br>= area $\\approx ${p13.toFixed(2)}$`, { x: 1440, y: 360, w: 360, size: 36, color: C.blue, at: 5.8 });
  s.caption('Probability = area under the PDF.', 5.6, { out: 9.4 });
  s.line(r.X(2), r.Y(0), r.X(2), r.Y(gam(2)), { color: C.green, width: 5, at: 9.6, dur: 0.4 });
  s.text('$P(X=2)=0$', { x: r.X(2), y: r.Y(gam(2)) - 66, w: 300, size: 38, align: 'center', color: C.green, at: 9.9 });
  s.caption('One point has no width, so no area: $<$ is the same as $\\le$.', 9.8);
  S.push(s);
}

// ------------------------------------------------------------------ PDF area sweep in sync with the CDF drawing in
{
  const s = new Scene('q2-pdfcdf', 15.5);
  s.title('CDF = area so far.  PDF = slope of the CDF.');
  const m = 3.5, sd = 0.75, f = npdf(m, sd), F = (x) => Phi((x - m) / sd);
  const top = s.axes({ x: 520, y: 190, w: 1100, h: 270, xr: [0, 7], yr: [0, 0.6], xticks: [1, 2, 3, 4, 5, 6].map((v) => ({ v })), at: 0.4, tickSize: 30 });
  s.text('PDF', { x: 150, y: 230, size: 52, font: 'Oswald', color: C.blue, at: 0.5 });
  s.text('$f_X(x)$', { x: 150, y: 300, w: 340, size: 36, at: 0.6 });
  const bot = s.axes({ x: 520, y: 560, w: 1100, h: 290, xr: [0, 7], yr: [0, 1.08], xticks: [1, 2, 3, 4, 5, 6].map((v) => ({ v })),
    yticks: [{ v: 1, label: '$1$', guide: true }], at: 0.5, tickSize: 30 });
  s.text('CDF', { x: 150, y: 600, size: 52, font: 'Oswald', color: C.blue, at: 0.6 });
  s.text('$F_X(x)=P(X\\le x)$', { x: 150, y: 670, w: 360, size: 38, at: 0.7 });
  s.curve(top, f, 0, 7, { color: C.blue, width: 6, at: 0.9, dur: 1.2 });
  const at = 2.4, dur = 6.0;
  s.area(top, f, 0, 7, { color: C.blue, opacity: 0.25, at, sweep: dur });
  const clip = s.wipe(bot.X(0), bot.X(7) + 6, at, dur);
  s.path(s.fpath(bot, F, 0, 7), { color: C.blue, width: 6, draw: false, clip });
  const mk = s.line(top.X(0), top.y - 10, top.X(0), bot.y0, { color: C.soft, width: 2, dash: '6 8', at });
  s.fromTo(mk, { x: 0 }, { x: top.X(7) - top.X(0), duration: dur, ease: 'none' }, at);
  s.caption('As $x$ moves right, the shaded area is $F_X(x)$.', at + 0.2, { out: 8.8 });
  s.text('$F_X(x)=\\displaystyle\\int_{-\\infty}^{x} f_X(t)\\,dt$', { x: 130, y: 760, w: 380, size: 36, at: 9.0 });
  s.caption('CDF = area so far.   PDF = slope of the CDF: $f_X=F_X\'$.', 9.0);
  S.push(s);
}

// ------------------------------------------------------------------ find c: total area 1
{
  const s = new Scene('q2-c', 12.5);
  s.title('Type 1: find $c$.  The total area must be 1.');
  const I = 4 - 8 / 3, c = 1 / I; // integral of x(2-x) over [0,2] = 4/3
  s.text('$f_X(x)=c\\,x(2-x)$ on $[0,2]$', { x: 150, y: 190, w: 1200, size: 50, at: 0.5 });
  const ax = s.axes({ x: 250, y: 330, w: 820, h: 450, xr: [-0.2, 2.3], yr: [0, 0.95], xticks: [0, 1, 2].map((v) => ({ v })), xlabel: '$x$', at: 1.0 });
  const g = (x) => c * x * (2 - x);
  s.curve(ax, g, 0, 2, { color: C.blue, width: 6, at: 1.5, dur: 1.0 });
  s.area(ax, g, 0, 2, { color: C.blue, opacity: 0.25, at: 2.6, sweep: 1.2 });
  s.text('area $=1$', { x: ax.X(1), y: ax.Y(0.3), w: 300, size: 46, align: 'center', color: C.blue, at: 3.8 });
  s.text('$\\displaystyle\\int_0^2 c\\,x(2-x)\\,dx=1$', { x: 1220, y: 340, w: 640, size: 46, at: 4.2 });
  s.text('$c\\cdot\\dfrac43=1$', { x: 1220, y: 490, w: 640, size: 52, at: 5.6 });
  s.text(`$c=\\dfrac34$`, { x: 1220, y: 630, w: 640, size: 66, color: C.green, at: 6.8 });
  if (Math.abs(c - 0.75) > 1e-12) throw new Error('c should be 3/4');
  s.caption('Integrate, set it equal to 1, solve for $c$.', 7.8);
  S.push(s);
}

// ------------------------------------------------------------------ uniform and exponential
{
  const s = new Scene('q2-uniexp', 16.5);
  s.title('Type 2: uniform and exponential');
  s.text('Bus arrives uniformly in 0–30 min', { x: 150, y: 185, w: 760, size: 38, color: C.orange, at: 0.5 });
  const u = s.axes({ x: 150, y: 330, w: 700, h: 330, xr: [-3, 34], yr: [0, 0.05], xticks: [0, 10, 30].map((v) => ({ v })), xlabel: '$x$', at: 0.6 });
  const h = 1 / 30, flat = () => h;
  s.area(u, flat, 0, 30, { color: C.blue, opacity: 0.12, at: 1.2 });
  s.line(u.X(0), u.Y(0), u.X(0), u.Y(h), { color: C.blue, width: 5, at: 1.2, dur: 0.3 });
  s.curve(u, flat, 0, 30, { color: C.blue, width: 6, at: 1.4, dur: 0.6, n: 2 });
  s.line(u.X(30), u.Y(h), u.X(30), u.Y(0), { color: C.blue, width: 5, at: 1.9, dur: 0.3 });
  s.text('height $\\dfrac{1}{b-a}=\\dfrac1{30}$', { x: u.X(15), y: u.Y(h) - 90, w: 420, size: 36, align: 'center', color: C.blue, at: 2.3 });
  s.area(u, flat, 10, 30, { color: C.green, opacity: 0.35, at: 3.4, sweep: 0.8 });
  s.text('wait $\\ge10$: $P=\\dfrac{20}{30}=\\dfrac23$', { x: 150, y: 730, w: 760, size: 40, at: 4.3 });
  s.text('length ÷ total length', { x: 150, y: 835, w: 760, size: 34, color: C.soft, at: 4.8 });

  s.text('Lifetime: exponential, $\\lambda=1$', { x: 1040, y: 185, w: 760, size: 38, color: C.orange, at: 5.8 });
  const e = s.axes({ x: 1040, y: 330, w: 700, h: 330, xr: [0, 5], yr: [0, 1.1], xticks: [0, 1, 2, 3, 4].map((v) => ({ v })), xlabel: '$x$', at: 6.0 });
  const ex = (x) => Math.exp(-x);
  s.curve(e, ex, 0, 5, { color: C.blue, width: 6, at: 6.5, dur: 1.0 });
  s.area(e, ex, 1, 5, { color: C.green, opacity: 0.35, at: 7.8, sweep: 0.9 });
  s.text('$P(X>t)=e^{-\\lambda t}$', { x: e.X(2.1), y: e.Y(0.62), w: 460, size: 44, color: C.green, at: 8.6 });
  s.text(`$t=1$: $e^{-1}\\approx ${f4(Math.exp(-1))}$`, { x: 1040, y: 730, w: 760, size: 40, at: 9.2 });
  s.caption('Memoryless: $P(X>s+t\\mid X>s)=P(X>t)$. Time already waited doesn\'t count.', 11.0, { size: 40 });
  S.push(s);
}

// ------------------------------------------------------------------ Gaussian: standardise, read Phi, symmetry
{
  const s = new Scene('q2-gauss', 17.5);
  s.title('Gaussian: standardise, then read the $\\Phi$ table');
  const mu = 80, sd = 7, x = 89, z = Math.round(((x - mu) / sd) * 100) / 100;
  const L = s.axes({ x: 150, y: 300, w: 680, h: 360, xr: [mu - 3.4 * sd, mu + 3.4 * sd], yr: [0, 0.065], xticks: [{ v: 80 }, { v: 89 }], at: 0.5 });
  s.text('$X\\sim N(80,\\,7^2)$', { x: 150, y: 190, w: 700, size: 42, color: C.orange, at: 0.7 });
  s.area(L, npdf(mu, sd), mu - 3.4 * sd, x, { color: C.blue, opacity: 0.25, at: 2.2, sweep: 1.2 });
  s.curve(L, npdf(mu, sd), mu - 3.4 * sd, mu + 3.4 * sd, { color: C.blue, width: 6, at: 0.9, dur: 1.2 });
  s.text('$P(X\\le89)$', { x: L.X(80), y: L.Y(0.024), w: 260, size: 36, align: 'center', color: C.blue, at: 3.2 });
  s.line(870, 480, 1040, 480, { color: C.ink, width: 4, at: 4.0, dur: 0.4 });
  s.path('M1020,465 L1042,480 L1020,495', { color: C.ink, width: 4, at: 4.3, dur: 0.2 });
  s.text(`$z=\\dfrac{x-\\mu}{\\sigma}=\\dfrac{89-80}{7}\\approx ${z}$`, { x: 960, y: 740, w: 1200, size: 46, align: 'center', at: 4.4 });
  const R = s.axes({ x: 1080, y: 300, w: 680, h: 360, xr: [-3.4, 3.4], yr: [0, 0.45], xticks: [{ v: 0 }, { v: z, label: `$${z}$` }], at: 5.2 });
  s.text('$Z\\sim N(0,1)$', { x: 1080, y: 190, w: 700, size: 42, color: C.orange, at: 5.4 });
  s.curve(R, npdf(0, 1), -3.4, 3.4, { color: C.blue, width: 6, at: 5.6, dur: 1.2 });
  const blue = s.area(R, npdf(0, 1), -3.4, z, { color: C.blue, opacity: 0.25, at: 6.9, sweep: 1.2 });
  const val = s.text(`$\\Phi(${z})\\approx ${f4(Phi(z))}$`, { x: R.X(0), y: R.Y(0.16), w: 340, size: 38, align: 'center', color: C.green, at: 8.2 });
  s.caption('Same area, but now you can read it from the table.', 8.4, { out: 11.6 });
  s.hide([blue, val], 11.6);
  s.area(R, npdf(0, 1), -3.4, -z, { color: C.red, opacity: 0.3, at: 11.9 });
  s.area(R, npdf(0, 1), z, 3.4, { color: C.red, opacity: 0.3, at: 12.2 });
  s.text('equal tails', { x: R.X(0), y: R.Y(0.13), w: 300, size: 36, align: 'center', color: C.red, at: 12.4 });
  s.caption('Negative $z$? Use the mirror: $\\Phi(-z)=1-\\Phi(z)$.', 12.0);
  S.push(s);
}

// ------------------------------------------------------------------ mixed: jump + ramp
{
  const s = new Scene('q2-mixed', 13.5);
  s.title('Mixed: a jump plus a ramp');
  s.text('Signal lost with probability $0.2$ ($X=0$); otherwise uniform on $(0,10)$', { x: 150, y: 180, w: 1650, size: 40, at: 0.5 });
  const ax = s.axes({ x: 350, y: 320, w: 1050, h: 470, xr: [-2, 12], yr: [0, 1.1], xticks: [{ v: 0 }, { v: 10 }], xlabel: '$x$',
    yticks: [{ v: 0.2, label: '$0.2$' }, { v: 1, label: '$1$', guide: true }], at: 0.8 });
  s.text('$F_X(x)$', { x: 200, y: 260, w: 200, size: 38, at: 1.0 });
  s.line(ax.X(-2), ax.Y(0), ax.X(0), ax.Y(0), { color: C.blue, width: 6, at: 1.4, dur: 0.4 });
  s.dot(ax.X(0), ax.Y(0), { color: C.blue, r: 10, open: true, at: 2.2 });
  s.line(ax.X(0), ax.Y(0), ax.X(0), ax.Y(0.2), { color: C.faint, width: 3, dash: '6 6', at: 2.3 });
  s.dot(ax.X(0), ax.Y(0.2), { color: C.blue, r: 11, at: 2.4 });
  s.text('jump $=P(X=0)=0.2$', { x: ax.X(0) + 30, y: ax.Y(0.2) - 10, w: 480, size: 38, color: C.red, at: 2.7 });
  s.line(ax.X(0), ax.Y(0.2), ax.X(10), ax.Y(1), { color: C.blue, width: 6, at: 3.8, dur: 1.4 });
  s.text('ramp: slope $0.8\\cdot\\dfrac1{10}=0.08$', { x: ax.X(5.0), y: ax.Y(0.38), w: 560, size: 38, color: C.blue, at: 4.6 });
  s.line(ax.X(10), ax.Y(1), ax.X(12), ax.Y(1), { color: C.blue, width: 6, at: 5.3, dur: 0.3 });
  s.caption('Any probability = jumps inside the range + area over it.', 6.6, { out: 10.0 });
  s.caption('$P(2<X<5)=0.08\\cdot3=0.24$   (no jump inside)', 10.2);
  S.push(s);
}

// ------------------------------------------------------------------ end card
{
  const s = new Scene('q2-end', 10);
  s.title('Question 2 is one of two kinds');
  s.text('1. Given a PDF or CDF formula', { x: 150, y: 230, w: 820, size: 54, font: 'Oswald', color: C.blue, at: 0.6 });
  ['find $c$: total area $=1$', 'CDF = area so far; PDF = slope', 'mixed: jumps + area'].forEach((l, i) =>
    s.text(l, { x: 150, y: 340 + i * 95, w: 800, size: 46, at: 1.2 + i * 0.5 }));
  s.text('2. Named family word problem', { x: 1000, y: 230, w: 820, size: 54, font: 'Oswald', color: C.orange, at: 2.8 });
  ['uniform: length ÷ total length', 'exponential: $P(X>t)=e^{-\\lambda t}$', 'Gaussian: $z=\\dfrac{x-\\mu}{\\sigma}$, read $\\Phi$'].forEach((l, i) =>
    s.text(l, { x: 1000, y: 340 + i * 95, w: 820, size: 46, at: 3.4 + i * 0.5 }));
  s.caption('One point has zero area: $<$ is the same as $\\le$.', 5.6, { y: 760, size: 50 });
  S.push(s);
}

writeVideo('q2', 'ELEC 226 Test 2 - Question 2', S);
