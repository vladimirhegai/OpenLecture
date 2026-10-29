// Test 2 - Question 3: expected value, variance, the rules for aX+b (Lectures 11-13).
import { Scene, C, writeVideo } from './lib.mjs';

const S = [];
// The running example (Practice question 1 in the note): x = -1, 0, 1, 2.
const PM = [[-1, 0.1], [0, 0.4], [1, 0.3], [2, 0.2]];
const MEAN = PM.reduce((a, [x, p]) => a + x * p, 0); // 0.6
const EX2 = PM.reduce((a, [x, p]) => a + x * x * p, 0); // 1.2
const VAR = EX2 - MEAN ** 2; // 0.84
const f2 = (v, d = 2) => Number(v.toFixed(d)).toString();

/** A fulcrum (triangle) whose apex sits at (x, y). */
function fulcrum(s, x, y, { color = C.green, at = null } = {}) {
  return s.path(`M${x},${y} L${x - 34},${y + 58} L${x + 34},${y + 58} Z`, { fill: color, opacity: 1, draw: false, at });
}

// ------------------------------------------------------------------ intro
{
  const s = new Scene('q3-intro', 5.5);
  s.text('ELEC 226 · Test 2', { x: 150, y: 330, size: 38, color: C.soft, at: 0.2 });
  s.text('Question 3', { x: 150, y: 380, size: 150, weight: 500, font: 'Oswald', at: 0.35 });
  s.text('Mean and variance', { x: 150, y: 590, w: 1000, size: 46, at: 0.7 });
  const ax = s.axes({ x: 1250, y: 340, w: 520, h: 280, xr: [-1.6, 2.6], yr: [0, 0.45], at: 0.6 });
  s.stems(ax, PM, { at: 1.0, stagger: 0.15 });
  fulcrum(s, ax.X(MEAN), ax.y0 + 4, { at: 1.9 });
  S.push(s);
}

// ------------------------------------------------------------------ the mean is the balance point
{
  const s = new Scene('q3-mean', 15);
  s.title('The mean is the balance point');
  const ax = s.axes({ x: 360, y: 230, w: 1200, h: 360, xr: [-1.6, 2.6], yr: [0, 0.45], xticks: [-1, 0, 1, 2].map((v) => ({ v })), at: 0.4 });
  s.stems(ax, PM, { at: 0.8, stagger: 0.3, labels: PM.map(([, p]) => `$${p}$`), labelSize: 36 });
  const tri = fulcrum(s, ax.X(-1.3), ax.y0 + 4, { at: 2.2 });
  s.move(tri, ax.X(MEAN) - ax.X(-1.3), 0, 2.8, 1.8);
  s.text(`$E[X]=${f2(MEAN)}$`, { x: ax.X(MEAN), y: ax.y0 + 75, w: 400, size: 46, align: 'center', color: C.green, at: 4.7 });
  s.text('$E[X]=\\displaystyle\\sum x\\,p(x)=(-1)(0.1)+0(0.4)+1(0.3)+2(0.2)=0.6$', { x: 960, y: 800, w: 1700, size: 44, align: 'center', at: 5.6 });
  s.caption('Each value × its chance, then add.', 8.6);
  S.push(s);
}

// ------------------------------------------------------------------ continuous mean
{
  const s = new Scene('q3-cmean', 13);
  s.title('Continuous: the sum becomes an integral');
  s.text('$E[X]=\\displaystyle\\int x\\,f(x)\\,dx$', { x: 150, y: 175, w: 900, size: 50, at: 0.5 });
  const ax = s.axes({ x: 180, y: 360, w: 820, h: 380, xr: [-0.5, 4.5], yr: [0, 0.6], xticks: [0, 1, 3, 4].map((v) => ({ v })), xlabel: '$x$', at: 1.0 });
  const tri = (v) => (v < 0 || v > 4 ? 0 : v < 2 ? v / 4 : (4 - v) / 4);
  s.area(ax, tri, 0, 4, { color: C.blue, opacity: 0.2, at: 1.6, sweep: 1.2 });
  s.curve(ax, tri, -0.5, 4.5, { color: C.blue, width: 6, at: 1.6, dur: 1.2, ease: 'none' });
  fulcrum(s, ax.X(2), ax.y0 + 4, { at: 3.2 });
  s.text('$E[X]=2$', { x: ax.X(2), y: ax.y0 + 80, w: 300, size: 44, align: 'center', color: C.green, at: 3.5 });
  s.text('Symmetric around $c$?', { x: 1120, y: 380, w: 700, size: 46, at: 4.4 });
  s.text('Then $E[X]=c$.', { x: 1120, y: 460, w: 700, size: 46, color: C.green, at: 5.2 });
  s.text('No integral needed.', { x: 1120, y: 540, w: 700, size: 46, color: C.soft, at: 6.0 });
  s.caption('Only integrate where $f(x)$ is not 0.', 8.0);
  S.push(s);
}

// ------------------------------------------------------------------ variance is the spread
{
  const s = new Scene('q3-var', 17);
  s.title('The variance is the spread');
  const mk = (x, label, d, at) => {
    const ax = s.axes({ x, y: 250, w: 760, h: 220, xr: [-1, 21], yr: [0, 0.65], xticks: [0, 10, 20].map((v) => ({ v })), at });
    s.text(label, { x: x + 10, y: 175, w: 600, size: 40, color: C.orange, at: at + 0.2 });
    s.line(ax.X(10), ax.y0, ax.X(10), ax.Y(0.62), { color: C.green, width: 3, dash: '8 8', at: at + 0.9 });
    s.stems(ax, [[10 - d, 0.5], [10 + d, 0.5]], { at: at + 0.4, stagger: 0.2 });
    return ax;
  };
  mk(150, '$X$: 9 or 11', 1, 0.5);
  mk(1010, '$Y$: 0 or 20', 10, 1.3);
  s.text('same mean 10', { x: 960, y: 545, w: 600, size: 38, align: 'center', color: C.green, at: 2.6 });
  s.text('$\\mathrm{Var}=1$', { x: 530, y: 545, w: 300, size: 40, align: 'center', at: 3.4 });
  s.text('$\\mathrm{Var}=100$', { x: 1390, y: 545, w: 300, size: 40, align: 'center', at: 3.8 });
  s.text('$\\mathrm{Var}(X)=E[X^2]-(E[X])^2$', { x: 150, y: 640, w: 1000, size: 46, at: 5.6 });
  s.text(`$E[X^2]=(1)(0.1)+0(0.4)+(1)(0.3)+(4)(0.2)=${f2(EX2)}$`, { x: 150, y: 720, w: 1200, size: 44, at: 7.2 });
  s.text(`$\\mathrm{Var}(X)=${f2(EX2)}-${f2(MEAN)}^2=${f2(VAR)}$`, { x: 150, y: 800, w: 1000, size: 44, color: C.green, at: 8.8 });
  s.text(`$\\sigma_X=\\sqrt{${f2(VAR)}}\\approx${Math.sqrt(VAR).toFixed(3)}$`, { x: 150, y: 880, w: 1000, size: 44, color: C.green, at: 10.0 });
  s.text('$E[X^2]$ ≠ $(E[X])^2$', { x: 1380, y: 720, w: 440, size: 44, color: C.red, at: 11.4 });
  s.text('square inside the sum', { x: 1380, y: 790, w: 440, size: 34, color: C.red, at: 11.7 });
  S.push(s);
}

// ------------------------------------------------------------------ named families: read it off
{
  const s = new Scene('q3-families', 16.5);
  s.title('Named family: read the mean and variance off the table');
  // two blocks: discrete on the left, continuous on the right
  const cols = [[150, 560, 740], [1000, 1420, 1580]];
  cols.forEach(([xn, xm, xv]) => {
    s.text('Family', { x: xn, y: 185, w: 380, size: 34, color: C.soft, at: 0.4 });
    s.text('$E[X]$', { x: xm, y: 185, w: 170, size: 34, color: C.soft, at: 0.4 });
    s.text('$\\mathrm{Var}(X)$', { x: xv, y: 185, w: 200, size: 34, color: C.soft, at: 0.4 });
  });
  const rows = [
    ['Bernoulli$(p)$', 'p', 'p(1-p)', C.orange],
    ['Binomial$(n,p)$', 'np', 'np(1-p)', C.orange],
    ['Geometric$(p)$, $k\\ge1$', '\\dfrac1p', '\\dfrac{1-p}{p^2}', C.orange],
    ['Poisson$(\\lambda)$', '\\lambda', '\\lambda', C.orange],
    ['Uniform$(a,b)$', '\\dfrac{a+b}{2}', '\\dfrac{(b-a)^2}{12}', C.blue],
    ['Exponential$(\\lambda)$', '\\dfrac1\\lambda', '\\dfrac1{\\lambda^2}', C.blue],
    ['Gaussian $N(\\mu,\\sigma^2)$', '\\mu', '\\sigma^2', C.blue],
  ];
  rows.forEach(([name, m, v, col], i) => {
    const [xn, xm, xv] = cols[i < 4 ? 0 : 1];
    const y = 270 + (i < 4 ? i : i - 4) * 135, t = 0.8 + i * 1.1;
    s.text(name, { x: xn, y: y + 6, w: 400, size: 40, font: 'Oswald', color: col, at: t });
    s.text(`$${m}$`, { x: xm, y, w: 170, size: 40, at: t + 0.35 });
    s.text(`$${v}$`, { x: xv, y, w: 260, size: 40, at: t + 0.6 });
  });
  s.caption('Need $E[X^2]$? It is $\\mathrm{Var}+\\mu^2$. Poisson$(3)$: $3+3^2=12$.', 9.6);
  S.push(s);
}

// ------------------------------------------------------------------ given a CDF: tail formula
{
  const s = new Scene('q3-cdf', 15.5);
  s.title('Given a CDF? Get the PMF/PDF, or use the tail');
  s.text('Staircase: the jumps are the PMF.', { x: 150, y: 190, w: 800, size: 40, at: 0.5 });
  s.text('Smooth: the slope is the PDF.', { x: 150, y: 260, w: 800, size: 40, at: 1.0 });
  const ax = s.axes({ x: 1040, y: 330, w: 720, h: 420, xr: [-0.15, 1.45], yr: [0, 1.15], xticks: [0, 1].map((v) => ({ v })),
    yticks: [{ v: 1, label: '$1$', guide: true }], xlabel: '$t$', at: 1.4 });
  const F = (t) => (t < 0 ? 0 : t > 1 ? 1 : t * t);
  s.text('$F(t)=t^2$', { x: ax.X(0.42), y: ax.Y(0.12) - 10, w: 300, size: 38, color: C.blue, at: 2.6 });
  s.curve(ax, F, -0.15, 1.45, { color: C.blue, width: 6, at: 1.9, dur: 1.0 });
  // the area above the CDF and below 1, from 0 to 1
  const pts = []; for (let i = 0; i <= 80; i++) { const t = i / 80; pts.push(`${ax.X(t).toFixed(1)},${ax.Y(t * t).toFixed(1)}`); }
  const d = `M${ax.X(0).toFixed(1)},${ax.Y(1).toFixed(1)} L${ax.X(1).toFixed(1)},${ax.Y(1).toFixed(1)} L${pts.reverse().join(' L')} Z`;
  const clip = s.wipe(ax.X(0), ax.X(1), 3.6, 1.1);
  const a = s.path(d, { fill: C.green, opacity: 0.25, draw: false, clip });
  s.set(a, { opacity: 1 }, 3.6);
  s.text('area $=E[X]$', { x: ax.X(0.12), y: ax.Y(0.92), w: 300, size: 38, color: C.green, at: 4.6 });
  s.text('$E[X]=\\displaystyle\\int_0^{\\infty}\\big(1-F(t)\\big)\\,dt$', { x: 150, y: 400, w: 850, size: 46, at: 5.2 });
  s.text('$=\\displaystyle\\int_0^1(1-t^2)\\,dt=\\dfrac23$', { x: 150, y: 520, w: 850, size: 46, color: C.green, at: 6.9 });
  s.text('Check with the PDF $f=2t$:', { x: 150, y: 660, w: 850, size: 38, color: C.soft, at: 8.6 });
  s.text('$\\displaystyle\\int_0^1 t\\cdot2t\\,dt=\\dfrac23$ ✓', { x: 150, y: 730, w: 850, size: 44, at: 9.2 });
  s.caption('Tail formula: for $X\\ge0$ only.', 11.0);
  S.push(s);
}

// ------------------------------------------------------------------ Type 2: the rules for aX + b
{
  const s = new Scene('q3-rules', 19.5);
  s.title('Type 2: shift by $b$, stretch by $a$');
  const ax = s.axes({ x: 160, y: 200, w: 1600, h: 230, xr: [-2, 9], yr: [0, 0.5], xticks: [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8].map((v) => ({ v })), at: 0.3, tickSize: 30 });
  const st = s.stems(ax, PM, { at: 0.7, stagger: 0.15 });
  const tri = fulcrum(s, ax.X(MEAN), ax.y0 + 54, { at: 1.4 });
  const lab = s.text('$X$', { x: 200, y: 200, w: 200, size: 46, color: C.orange, at: 1.2 });
  const stage1 = 2.8, stage2 = 7.0;
  // shift: x -> x + 3
  st.forEach(({ l, d }, i) => s.move([l, d], ax.X(PM[i][0] + 3) - ax.X(PM[i][0]), 0, stage1, 1.0));
  s.move(tri, ax.X(MEAN + 3) - ax.X(MEAN), 0, stage1, 1.0);
  s.caption('$X+3$: the mean moves 3. The spread stays.', stage1 + 0.3, { y: 560, out: stage2 - 0.2 });
  s.hide(lab, stage1);
  // stretch: x + 3 -> 2x + 3 (moves are absolute offsets from the start)
  st.forEach(({ l, d }, i) => s.move([l, d], ax.X(2 * PM[i][0] + 3) - ax.X(PM[i][0]), 0, stage2, 1.0));
  s.move(tri, ax.X(2 * MEAN + 3) - ax.X(MEAN), 0, stage2, 1.0);
  s.caption('$2X+3$: the spread doubles, so the variance ×4.', stage2 + 0.3, { y: 560 });
  s.text('$E[aX+b]=a\\,E[X]+b$', { x: 150, y: 680, w: 800, size: 48, at: 10.8 });
  s.text('$\\mathrm{Var}(aX+b)=a^2\\,\\mathrm{Var}(X)$', { x: 1000, y: 680, w: 800, size: 48, at: 11.6 });
  s.text(`$E[2X+3]=2(${f2(MEAN)})+3=${f2(2 * MEAN + 3)},\\qquad \\mathrm{Var}(2X+3)=4(${f2(VAR)})=${f2(4 * VAR)}$`,
    { x: 960, y: 790, w: 1700, size: 44, align: 'center', color: C.green, at: 13.0 });
  s.caption('The $+b$ drops out of Var. The $a$ gets squared.', 15.0);
  S.push(s);
}

// ------------------------------------------------------------------ end card
{
  const s = new Scene('q3-end', 10.5);
  s.title('Question 3 is one of two kinds');
  s.text('1. Mean & variance from the distribution', { x: 150, y: 220, w: 820, size: 50, font: 'Oswald', color: C.orange, at: 0.6 });
  ['value × chance, add ($\\int$ for a PDF)', '$\\mathrm{Var}=E[X^2]-(E[X])^2$', 'family? read the table', 'CDF? jumps, slope, or the tail'].forEach((l, i) =>
    s.text(l, { x: 150, y: 320 + i * 90, w: 800, size: 44, at: 1.2 + i * 0.5 }));
  s.text('2. Use the rules', { x: 1050, y: 220, w: 760, size: 50, font: 'Oswald', color: C.blue, at: 3.2 });
  ['$E[aX+b]=aE[X]+b$', '$\\mathrm{Var}(aX+b)=a^2\\mathrm{Var}(X)$', '$E[X^2]=\\mathrm{Var}+\\mu^2$'].forEach((l, i) =>
    s.text(l, { x: 1050, y: 320 + i * 90, w: 760, size: 44, at: 3.8 + i * 0.5 }));
  s.caption('$E[X^2]$ ≠ $(E[X])^2$, every time.', 6.2, { y: 790, size: 50, color: C.red });
  S.push(s);
}

writeVideo('q3', 'ELEC 226 Test 2 - Question 3', S);
