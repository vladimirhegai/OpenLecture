// Test 2 - Question 4: functions of a random variable, Y = g(X) (Lectures 12-15, Tutorial 6).
import { Scene, C, writeVideo } from './lib.mjs';

const S = [];
const XC = C.blue, YC = C.purple;
const phi = (x, m, s) => Math.exp(-((x - m) ** 2) / (2 * s * s)) / (s * Math.sqrt(2 * Math.PI));
const erf = (x) => { // Abramowitz-Stegun 7.1.26
  const t = 1 / (1 + 0.3275911 * Math.abs(x));
  const y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x);
  return x >= 0 ? y : -y;
};
const Phi = (z) => 0.5 * (1 + erf(z / Math.SQRT2));

/** A horizontal band on the x-axis (the x-set), revealed left to right. */
function band(s, ax, a, b, at, { color = XC, dur = 0.7 } = {}) {
  const clip = s.wipe(ax.X(a), ax.X(b), at, dur, { ease: 'power2.out' });
  return s.rect(ax.X(a), ax.Y(0) - 11, ax.X(b) - ax.X(a), 22, { fill: color, opacity: 0.55, clip });
}

// ------------------------------------------------------------------ intro
{
  const s = new Scene('q4-intro', 5.5);
  s.text('ELEC 226 · Test 2', { x: 150, y: 330, size: 38, color: C.soft, at: 0.2 });
  s.text('Question 4', { x: 150, y: 380, size: 150, weight: 500, font: 'Oswald', at: 0.35 });
  s.text('$Y=g(X)$: find its CDF and PDF', { x: 150, y: 590, w: 1000, size: 50, at: 0.7 });
  const ax = s.axes({ x: 1250, y: 300, w: 520, h: 420, xr: [-1.2, 1.2], yr: [-1.2, 1.2], yaxis: 'zero', at: 0.6 });
  s.curve(ax, (x) => x ** 3, -1.1, 1.1, { at: 1.0, dur: 1.2 });
  s.dot(ax.X(0.8), ax.Y(0), { color: XC, at: 2.2 });
  s.line(ax.X(0.8), ax.Y(0), ax.X(0.8), ax.Y(0.512), { color: C.soft, width: 3, at: 2.5, dur: 0.4 });
  s.line(ax.X(0.8), ax.Y(0.512), ax.X(0), ax.Y(0.512), { color: C.soft, width: 3, at: 2.9, dur: 0.4 });
  s.dot(ax.X(0), ax.Y(0.512), { color: YC, at: 3.3 });
  S.push(s);
}

// ------------------------------------------------------------------ the picture: x -> g(x) -> y
{
  const s = new Scene('q4-map', 14.5);
  s.title('Push every $X$ value through $g$ to get $Y$');
  const ax = s.axes({ x: 200, y: 190, w: 820, h: 640, xr: [-1.3, 1.3], yr: [-1.3, 1.3], yaxis: 'zero', at: 0.4 });
  s.text('$x$', { x: ax.x + ax.w + 14, y: ax.Y(0) - 30, w: 80, size: 42, color: XC, at: 0.8 });
  s.text('$y$', { x: ax.X(0) + 14, y: ax.y - 50, w: 80, size: 42, color: YC, at: 0.8 });
  s.curve(ax, (x) => x ** 3, -1.15, 1.15, { at: 0.8, dur: 1.0 });
  s.text('$g(x)=x^3$', { x: ax.X(-1.25), y: ax.Y(1.2), w: 300, size: 40, at: 1.6 });
  s.caption('Each $x$ goes up to the curve, then across: $y=g(x)$', 1.4, { out: 7.4 });
  [-0.9, -0.5, 0.35, 0.85].forEach((x, i) => {
    const t = 2.0 + i * 1.2, y = x ** 3;
    s.dot(ax.X(x), ax.Y(0), { color: XC, at: t });
    s.line(ax.X(x), ax.Y(0), ax.X(x), ax.Y(y), { color: C.soft, width: 3, at: t + 0.25, dur: 0.35 });
    s.dot(ax.X(x), ax.Y(y), { color: C.ink, r: 8, at: t + 0.55 });
    s.line(ax.X(x), ax.Y(y), ax.X(0), ax.Y(y), { color: C.soft, width: 3, at: t + 0.65, dur: 0.35 });
    s.dot(ax.X(0), ax.Y(y), { color: YC, at: t + 0.95 });
  });
  s.text('Step 1: what type is $Y$?', { x: 1130, y: 250, w: 740, size: 52, font: 'Oswald', color: C.orange, at: 7.6 });
  ['smooth $g$ → $Y$ continuous', 'staircase $g$ → $Y$ discrete', 'flat piece in $g$ → $Y$ mixed (a jump)'].forEach((l, i) =>
    s.text(l, { x: 1130, y: 350 + i * 80, w: 740, size: 40, at: 8.4 + i * 0.6 }));
  s.caption('Then always start from $F_Y(y)=P\\big(g(X)\\le y\\big)$', 10.6);
  S.push(s);
}

// ------------------------------------------------------------------ type 1: increasing g, CDF method
{
  const s = new Scene('q4-up', 18);
  s.title('Type 1: $g$ only goes up');
  const ax = s.axes({ x: 150, y: 190, w: 760, h: 600, xr: [-1.3, 1.3], yr: [-1.3, 1.3], yaxis: 'zero', at: 0.3 });
  s.curve(ax, (x) => x ** 3, -1.15, 1.15, { at: 0.6, dur: 0.9 });
  s.text('$g(x)=x^3$', { x: ax.X(-1.25), y: ax.Y(1.2), w: 300, size: 40, at: 1.2 });
  const x1 = 0.7, y1 = x1 ** 3;
  s.line(ax.x, ax.Y(y1), ax.x + ax.w, ax.Y(y1), { color: YC, width: 3, at: 1.6, dur: 0.6 });
  s.text('$y$', { x: ax.X(0) - 60, y: ax.Y(y1) - 56, w: 50, size: 40, color: YC, at: 1.9 });
  s.dot(ax.X(x1), ax.Y(y1), { color: C.ink, r: 10, at: 2.4 });
  s.line(ax.X(x1), ax.Y(y1), ax.X(x1), ax.Y(0), { color: C.soft, width: 3, at: 2.7, dur: 0.4 });
  s.text('$g^{-1}(y)$', { x: ax.X(x1), y: ax.Y(0) + 18, w: 200, size: 36, align: 'center', color: XC, at: 3.0 });
  band(s, ax, -1.3, x1, 3.4);
  s.text('$X\\le g^{-1}(y)$', { x: ax.X(-1.2), y: ax.Y(0) - 64, w: 260, size: 36, color: XC, at: 3.8 });
  const R = 1000, W = 860;
  s.text('$\\{Y\\le y\\}=\\{X\\le g^{-1}(y)\\}$', { x: R, y: 200, w: W, size: 46, at: 4.2 });
  s.text('$F_Y(y)=F_X\\big(g^{-1}(y)\\big)$', { x: R, y: 290, w: W, size: 52, color: C.orange, at: 6.0 });
  s.text('Example: $X\\sim U(-1,1)$, $Y=X^3$', { x: R, y: 420, w: W, size: 40, color: C.soft, at: 7.6 });
  s.text('$F_Y(y)=F_X\\big(\\sqrt[3]{y}\\big)=\\dfrac{\\sqrt[3]{y}+1}{2}$', { x: R, y: 490, w: W, size: 46, at: 8.6 });
  s.text('then differentiate:', { x: R, y: 640, w: W, size: 40, color: C.soft, at: 10.6 });
  s.text('$f_Y(y)=\\dfrac12\\cdot\\dfrac13\\,y^{-2/3}=\\dfrac{1}{6\\sqrt[3]{y^2}}$', { x: R, y: 700, w: W, size: 46, color: C.green, at: 11.4 });
  s.caption('Invert $g$, plug into $F_X$, then differentiate.', 13.4);
  S.push(s);
}

// ------------------------------------------------------------------ decreasing g: the inequality flips
{
  const s = new Scene('q4-down', 13);
  s.title('$g$ only goes down? The inequality flips');
  const ax = s.axes({ x: 150, y: 190, w: 760, h: 600, xr: [-0.3, 2.4], yr: [-1.6, 3.6], yaxis: 'zero', at: 0.3 });
  s.curve(ax, (x) => 3 - 2 * x, 0, 2.2, { at: 0.6, dur: 0.8 });
  s.text('$g(x)=3-2x$', { x: ax.X(0.15), y: ax.Y(3.55), w: 300, size: 40, at: 1.1 });
  const y1 = 1, x1 = 1;
  s.line(ax.x, ax.Y(y1), ax.x + ax.w, ax.Y(y1), { color: YC, width: 3, at: 1.6, dur: 0.6 });
  s.text('$y$', { x: ax.x + ax.w - 50, y: ax.Y(y1) - 56, w: 50, size: 40, color: YC, at: 1.9 });
  s.dot(ax.X(x1), ax.Y(y1), { color: C.ink, r: 10, at: 2.3 });
  s.line(ax.X(x1), ax.Y(y1), ax.X(x1), ax.Y(0), { color: C.soft, width: 3, at: 2.6, dur: 0.3 });
  s.text('$g^{-1}(y)$', { x: ax.X(x1), y: ax.Y(0) + 18, w: 200, size: 36, align: 'center', color: XC, at: 2.9 });
  band(s, ax, x1, 2.4, 3.3);
  s.text('$X\\ge g^{-1}(y)$', { x: ax.X(1.55), y: ax.Y(0) - 64, w: 260, size: 36, color: XC, at: 3.7 });
  const R = 1000, W = 860;
  s.text('$3-2X\\le y\\iff X\\ge\\dfrac{3-y}{2}$', { x: R, y: 210, w: W, size: 46, at: 4.2 });
  s.text('$F_Y(y)=1-F_X\\big(g^{-1}(y)\\big)$', { x: R, y: 340, w: W, size: 52, color: C.orange, at: 6.0 });
  s.text('Example: $X\\sim\\text{Exp}(\\lambda)$, $P(X\\ge t)=e^{-\\lambda t}$', { x: R, y: 470, w: W, size: 38, color: C.soft, at: 7.6 });
  s.text('$F_Y(y)=e^{-\\lambda(3-y)/2},\\quad y\\le3$', { x: R, y: 540, w: W, size: 46, color: C.green, at: 8.6 });
  s.caption('Going down: the $X$-set is on the right.', 9.8);
  S.push(s);
}

// ------------------------------------------------------------------ a Gaussian through a line
{
  const s = new Scene('q4-gauss', 13);
  s.title('A Gaussian through a line stays Gaussian');
  s.text('$X\\sim N(\\mu,\\sigma^2)\\ \\Rightarrow\\ aX+b\\sim N(a\\mu+b,\\ a^2\\sigma^2)$', { x: 960, y: 175, w: 1600, size: 50, align: 'center', at: 0.5 });
  const ax = s.axes({ x: 200, y: 320, w: 1520, h: 440, xr: [-12, 16], yr: [0, 0.15],
    xticks: [-10, -5, 0, 5, 10, 15].map((v) => ({ v })), xlabel: '', at: 1.0 });
  s.curve(ax, (x) => phi(x, 2, 3), -12, 16, { color: XC, at: 1.6, dur: 1.0 });
  s.text('$X\\sim N(2,\\,9)$', { x: ax.X(4.6), y: ax.Y(0.134), w: 300, size: 40, color: XC, at: 2.3 });
  s.curve(ax, (x) => phi(x, 1, 6), -12, 16, { color: YC, at: 3.4, dur: 1.0 });
  s.text('$Y=2X-3\\sim N(1,\\,36)$', { x: ax.X(-11.7), y: ax.Y(0.075), w: 460, size: 40, color: YC, at: 4.1 });
  s.text('mean: $2\\cdot2-3=1$', { x: 1420, y: 410, w: 380, size: 38, at: 5.4 });
  s.text('variance: $2^2\\cdot9=36$', { x: 1420, y: 475, w: 380, size: 38, at: 6.2 });
  s.caption(`$P(Y>7)=1-\\Phi\\!\\left(\\dfrac{7-1}{6}\\right)=1-\\Phi(1)\\approx ${(1 - Phi(1)).toFixed(4)}$`, 7.8);
  S.push(s);
}

// ------------------------------------------------------------------ type 2: turns around, DAD
{
  const s = new Scene('q4-dad', 18.5);
  s.title('Type 2: $g$ turns around (the DAD method)');
  const ax = s.axes({ x: 150, y: 190, w: 760, h: 600, xr: [-1.3, 1.3], yr: [-0.3, 1.3], yaxis: 'zero', at: 0.3 });
  s.curve(ax, (x) => x * x, -1.1, 1.1, { at: 0.6, dur: 0.9 });
  s.text('$g(x)=x^2$', { x: ax.X(0.1), y: ax.Y(1.22), w: 300, size: 40, at: 1.2 });
  const y1 = 0.36, r = Math.sqrt(y1);
  s.line(ax.x, ax.Y(y1), ax.x + ax.w, ax.Y(y1), { color: YC, width: 3, at: 1.6, dur: 0.6 });
  s.text('$y$', { x: ax.x + ax.w - 50, y: ax.Y(y1) - 56, w: 50, size: 40, color: YC, at: 1.9 });
  [-r, r].forEach((x, i) => {
    s.dot(ax.X(x), ax.Y(y1), { color: C.ink, r: 10, at: 2.4 + i * 0.15 });
    s.line(ax.X(x), ax.Y(y1), ax.X(x), ax.Y(0), { color: C.soft, width: 3, at: 2.7 + i * 0.15, dur: 0.3 });
  });
  s.text('$-\\sqrt y$', { x: ax.X(-r), y: ax.Y(0) + 26, w: 160, size: 36, align: 'center', color: XC, at: 3.0 });
  s.text('$\\sqrt y$', { x: ax.X(r), y: ax.Y(0) + 26, w: 160, size: 36, align: 'center', color: XC, at: 3.1 });
  band(s, ax, -r, r, 3.4);
  const R = 1000, W = 880;
  s.text('Example: $X\\sim U(-1,1)$, $Y=X^2$', { x: R, y: 190, w: W, size: 38, color: C.soft, at: 3.8 });
  s.text('<b>D</b>istribution: the range is $0\\le Y\\le1$', { x: R, y: 260, w: W, size: 40, at: 4.6 });
  s.text('<b>A</b>ccumulate: $X^2\\le y\\iff-\\sqrt y\\le X\\le\\sqrt y$', { x: R, y: 350, w: W, size: 40, at: 6.2 });
  s.text('$F_Y(y)=F_X(\\sqrt y)-F_X(-\\sqrt y)$', { x: R, y: 430, w: W, size: 48, color: C.orange, at: 7.8 });
  s.text('$=2\\sqrt y\\cdot\\dfrac12=\\sqrt y$',{ x: R + 125, y: 515, w: W - 125, size: 48, at: 9.6 });
  s.text('<b>D</b>ifferentiate: $f_Y(y)=\\dfrac{1}{2\\sqrt y},\\ \\ 0<y<1$', { x: R, y: 620, w: W, size: 44, color: C.green, at: 11.6 });
  s.caption('Find every $x$ with $g(x)\\le y$, then add up their chance.', 13.6);
  S.push(s);
}

// ------------------------------------------------------------------ flat piece: a jump
{
  const s = new Scene('q4-flat', 15.5);
  s.title('A flat piece in $g$ makes a jump in $F_Y$');
  s.text('$X\\sim U(-1,1)$, $Y=\\max\\{X,0\\}$', { x: 150, y: 165, w: 900, size: 40, color: C.soft, at: 0.4 });
  const ax = s.axes({ x: 150, y: 260, w: 700, h: 470, xr: [-1.3, 1.3], yr: [-0.3, 1.3], yaxis: 'zero', at: 0.6 });
  s.path(`M${ax.X(-1.1)},${ax.Y(0)} L${ax.X(0)},${ax.Y(0)} L${ax.X(1.1)},${ax.Y(1.1)}`, { at: 1.0, dur: 0.9 });
  s.text('$g(x)$', { x: ax.X(0.75), y: ax.Y(1.2), w: 200, size: 40, at: 1.6 });
  s.line(ax.X(-1), ax.Y(0), ax.X(0), ax.Y(0), { color: C.red, width: 12, at: 2.0, dur: 0.5 });
  s.text('every $X\\le0$ lands on $Y=0$', { x: ax.X(-1.25), y: ax.Y(0.5), w: 340, size: 36, color: C.red, at: 2.4 });
  const bx = s.axes({ x: 1080, y: 260, w: 700, h: 470, xr: [-0.6, 1.5], yr: [0, 1.15], yaxis: 'zero',
    xticks: [{ v: 0 }, { v: 1 }], yticks: [{ v: 0.5, label: '$\\dfrac12$' }, { v: 1, label: '$1$', guide: true }], ylabel: '$F_Y(y)$', at: 3.0 });
  const O = C.orange;
  s.line(bx.X(-0.6), bx.Y(0), bx.X(0), bx.Y(0), { color: O, width: 6, at: 3.6, dur: 0.4 });
  s.dot(bx.X(0), bx.Y(0), { color: O, r: 10, open: true, at: 4.2 });
  s.line(bx.X(0), bx.Y(0), bx.X(0), bx.Y(0.5), { color: C.red, width: 3, dash: '6 6', at: 4.3 });
  s.dot(bx.X(0), bx.Y(0.5), { color: O, r: 11, at: 4.4 });
  s.text('jump $=P(X\\le0)=\\dfrac12$', { x: bx.X(0.06), y: bx.Y(0.32), w: 420, size: 36, color: C.red, at: 4.9 });
  s.curve(bx, (y) => (y + 1) / 2, 0, 1, { color: O, width: 6, at: 6.0, dur: 0.8 });
  s.line(bx.X(1), bx.Y(1), bx.X(1.5), bx.Y(1), { color: O, width: 6, at: 6.9, dur: 0.3 });
  s.text('$\\dfrac{y+1}{2}$', { x: bx.X(0.12), y: bx.Y(0.98), w: 200, size: 38, color: O, at: 7.0 });
  s.caption('A jump, then a smooth climb → $Y$ is mixed', 8.4, { out: 11.8 });
  s.caption('$P(Y=0)=\\dfrac12$, plus density $\\dfrac12$ on $(0,1)$', 12.0);
  S.push(s);
}

// ------------------------------------------------------------------ end card
{
  const s = new Scene('q4-end', 10.5);
  s.title('Question 4 is one of two kinds');
  s.text('1. $g$ only goes up (or down)', { x: 150, y: 220, w: 820, size: 52, font: 'Oswald', color: XC, at: 0.6 });
  ['$\\{g(X)\\le y\\}=\\{X\\le g^{-1}(y)\\}$', 'flip to $\\ge$ if $g$ goes down', '$F_Y(y)=F_X\\big(g^{-1}(y)\\big)$, then differentiate', '$aX+b$: a Gaussian stays Gaussian'].forEach((l, i) =>
    s.text(l, { x: 150, y: 320 + i * 85, w: 800, size: 38, at: 1.2 + i * 0.45 }));
  s.text('2. $g$ turns around or goes flat', { x: 1010, y: 220, w: 820, size: 52, font: 'Oswald', color: YC, at: 3.0 });
  ['find the $x$-set where $g(x)\\le y$', '$Y=X^2$: $F_X(\\sqrt y)-F_X(-\\sqrt y)$', 'flat piece → a jump: $Y$ is mixed'].forEach((l, i) =>
    s.text(l, { x: 1010, y: 320 + i * 85, w: 800, size: 38, at: 3.6 + i * 0.45 }));
  s.caption('Every time: Range → CDF → PDF', 5.8, { y: 760, size: 52 });
  S.push(s);
}

writeVideo('q4', 'ELEC 226 Test 2 - Question 4', S);
