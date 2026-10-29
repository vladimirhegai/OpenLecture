// Test 2 - Question 1: discrete random variables, PMF, CDF, named families (Lectures 7-9).
import { Scene, C, writeVideo } from './lib.mjs';

const fact = (n) => (n <= 1 ? 1 : n * fact(n - 1));
const pois = (l, k) => Math.exp(-l) * l ** k / fact(k);
const S = [];

// ------------------------------------------------------------------ intro
{
  const s = new Scene('q1-intro', 5.5);
  s.text('ELEC 226 · Test 2', { x: 150, y: 330, size: 38, color: C.soft, at: 0.2 });
  s.text('Question 1', { x: 150, y: 380, size: 150, weight: 500, font: 'Oswald', at: 0.35 });
  s.text('Discrete random variables: PMF, CDF, named families', { x: 150, y: 590, w: 1000, size: 46, at: 0.7 });
  const ax = s.axes({ x: 1250, y: 360, w: 520, h: 300, xr: [-0.5, 6.5], yr: [0, 0.3], at: 0.6 });
  s.stems(ax, [0, 1, 2, 3, 4, 5, 6].map((k) => [k, pois(2, k)]), { at: 1.0, stagger: 0.12 });
  S.push(s);
}

// ------------------------------------------------------------------ outcomes -> numbers -> groups
{
  const s = new Scene('q1-rv', 15.5);
  s.title('A random variable turns each outcome into a number');
  const outs = ['hhh', 'hht', 'hth', 'thh', 'htt', 'tht', 'tth', 'ttt'];
  const xs = outs.map((_, i) => 260 + i * 200);
  const vals = outs.map((o) => [...o].filter((c) => c === 'h').length);
  const tok = outs.map((o, i) => s.text(o, { x: xs[i], y: 250, w: 180, size: 54, align: 'center', font: 'JetBrains Mono', at: 0.6 + i * 0.08 }));
  s.caption('Toss 3 coins. $X$ = number of heads.', 1.4, { out: 6.0 });
  const arrows = [], nums = [];
  vals.forEach((v, i) => {
    arrows.push(s.line(xs[i], 335, xs[i], 395, { color: C.soft, width: 3, at: 2.3 + i * 0.15, dur: 0.2 }));
    nums.push(s.text(`$${v}$`, { x: xs[i], y: 400, w: 180, size: 54, align: 'center', color: C.orange, at: 2.45 + i * 0.15 }));
  });
  s.hide([...arrows, ...nums], 6.0);
  s.caption('Group outcomes with the same value', 6.2, { out: 9.6 });
  const cols = [480, 800, 1120, 1440];
  const filled = [0, 0, 0, 0];
  outs.forEach((_, i) => {
    const v = vals[i];
    const ty = 700 - filled[v]++ * 78;
    s.move(tok[i], cols[v] - xs[i], ty - 250, 6.4 + i * 0.07, 0.9);
  });
  s.line(330, 790, 1590, 790, { width: 3, at: 7.4, dur: 0.5 });
  cols.forEach((cx, v) => s.text(`$X=${v}$`, { x: cx, y: 805, w: 220, size: 40, align: 'center', at: 7.6 + v * 0.08 }));
  s.caption('Each outcome is $\\dfrac18$, so add them up', 9.8, { out: 15.0 });
  ['\\dfrac18', '\\dfrac38', '\\dfrac38', '\\dfrac18'].forEach((p, v) => {
    const top = 700 - (filled[v] - 1) * 78;
    s.text(`$P=${p}$`, { x: cols[v], y: top - 90, w: 260, size: 46, align: 'center', color: C.orange, at: 10.4 + v * 0.25 });
  });
  S.push(s);
}

// ------------------------------------------------------------------ PMF stems + CDF staircase (synced)
{
  const s = new Scene('q1-pmfcdf', 15.5);
  s.title('PMF = the chances.  CDF = the running total.');
  const pm = [[0, 1 / 8], [1, 3 / 8], [2, 3 / 8], [3, 1 / 8]];
  const top = s.axes({ x: 520, y: 205, w: 1100, h: 250, xr: [-0.8, 4.2], yr: [0, 0.62], xticks: [0, 1, 2, 3].map((v) => ({ v })), at: 0.4, tickSize: 30 });
  s.text('PMF', { x: 150, y: 250, size: 52, font: 'Oswald', color: C.orange, at: 0.5 });
  s.text('$p_X(x)=P(X=x)$', { x: 150, y: 320, w: 360, size: 32, at: 0.6 });
  const bot = s.axes({ x: 520, y: 560, w: 1100, h: 290, xr: [-0.8, 4.2], yr: [0, 1.08], xticks: [0, 1, 2, 3].map((v) => ({ v })),
    yticks: [{ v: 1, label: '$1$', guide: true }], at: 0.5, tickSize: 30 });
  s.text('CDF', { x: 150, y: 620, size: 52, font: 'Oswald', color: C.orange, at: 0.6 });
  s.text('$F_X(x)=P(X\\le x)$', { x: 150, y: 690, w: 360, size: 32, at: 0.7 });
  const st = 1.4;
  s.stems(top, pm, { at: 1.6, stagger: st, labels: ['$\\dfrac18$', '$\\dfrac38$', '$\\dfrac38$', '$\\dfrac18$'], labelSize: 34, labelGap: 2.9 });
  s.staircase(bot, pm, -0.8, 4.2, { at: 1.6 + 0.4 - st, stagger: st, labels: ['$\\dfrac18$', '$\\dfrac12$', '$\\dfrac78$', ''], labelSize: 34, labelGap: 3.0 });
  pm.forEach(([v], i) => s.line(top.X(v), top.Y(0) + 8, bot.X(v), bot.Y(0) - 4, { color: C.faint, width: 2, dash: '6 8', at: 1.9 + i * st }));
  s.caption('Jump size = PMF.   Running total = CDF.', 7.8, { out: 11.4 });
  s.caption('$P(a<X\\le b)=F(b)-F(a)$', 11.6, { color: C.ink });
  S.push(s);
}

// ------------------------------------------------------------------ find c
{
  const s = new Scene('q1-c', 11.5);
  s.title('Unknown constant $c$?  The total must be 1.');
  s.text('$p_X(x)=c\\,(x+1),\\quad x=0,1,2,3$', { x: 150, y: 200, w: 1200, size: 50, at: 0.5 });
  const ax = s.axes({ x: 300, y: 360, w: 780, h: 420, xr: [-0.6, 3.6], yr: [0, 0.45], xticks: [0, 1, 2, 3].map((v) => ({ v })), at: 1.0 });
  s.stems(ax, [0, 1, 2, 3].map((x) => [x, (x + 1) / 10]), { at: 1.6, stagger: 0.35, labels: ['$c$', '$2c$', '$3c$', '$4c$'], labelSize: 38, labelColor: C.orange });
  s.text('$c+2c+3c+4c=1$', { x: 1220, y: 420, w: 600, size: 52, at: 3.6 });
  s.text('$10c=1$', { x: 1220, y: 520, w: 600, size: 52, at: 4.9 });
  s.text('$c=\\dfrac{1}{10}$', { x: 1220, y: 620, w: 600, size: 64, color: C.green, at: 6.0 });
  s.caption('Add every chance, set it equal to 1, solve.', 7.2);
  S.push(s);
}

// ------------------------------------------------------------------ named families: clue -> family
{
  const s = new Scene('q1-families', 19.5);
  s.title('Type 2: the clue word tells you the family');
  const rows = [
    ['fixed $n$ tries, count successes', 'Binomial', '\\dbinom{n}{k}p^k(1-p)^{n-k}'],
    ['tries until the first success', 'Geometric', '(1-p)^{k-1}p'],
    ['tries until the $r$-th success', 'Negative Binomial', '\\dbinom{k-1}{r-1}p^r(1-p)^{k-r}'],
    ['draw $n$ without replacement', 'Hypergeometric', '\\dbinom{K}{k}\\dbinom{N-K}{n-k}\\Big/\\dbinom{N}{n}'],
    ['"on average $\\lambda$ per hour / page / year"', 'Poisson', 'e^{-\\lambda}\\dfrac{\\lambda^k}{k!}'],
    ['one yes/no try', 'Bernoulli', 'p^k(1-p)^{1-k}'],
  ];
  rows.forEach(([clue, fam, pmf], i) => {
    const y = 195 + i * 118, t = 0.8 + i * 1.9;
    s.text(clue, { x: 150, y, w: 720, size: 38, at: t });
    s.line(890, y + 26, 960, y + 26, { color: C.soft, width: 3, at: t + 0.45, dur: 0.25 });
    s.text(fam, { x: 985, y: y - 6, w: 420, size: 44, font: 'Oswald', color: C.orange, at: t + 0.7 });
    s.text(`$${pmf}$`, { x: 1390, y: y - 10, w: 500, size: 42, at: t + 1.0 });
  });
  s.caption('Spot the clue, write the PMF, plug in $k$.', 13.0);
  S.push(s);
}

// ------------------------------------------------------------------ Poisson: scale lambda
{
  const s = new Scene('q1-poisson', 13.5);
  s.title('Poisson: scale $\\lambda$ to the time you are asked about');
  s.text('7 calls per week', { x: 150, y: 250, w: 700, size: 58, at: 0.7 });
  s.text('asked about 1 day', { x: 150, y: 340, w: 700, size: 44, color: C.soft, at: 1.4 });
  s.text('$\\lambda=\\dfrac77=1$', { x: 150, y: 440, w: 700, size: 70, color: C.orange, at: 2.2 });
  const ax = s.axes({ x: 920, y: 240, w: 820, h: 470, xr: [-0.6, 7.6], yr: [0, 0.42], xticks: [0, 1, 2, 3, 4, 5, 6, 7].map((v) => ({ v })), xlabel: '$k$', at: 2.6 });
  s.stems(ax, [0, 1, 2, 3, 4, 5, 6, 7].map((k) => [k, pois(1, k)]), { at: 3.1, stagger: 0.14 });
  s.caption(`$P(X=2)=e^{-1}\\dfrac{1^2}{2!}\\approx ${pois(1, 2).toFixed(3)}$`, 5.0, { out: 8.6, y: 860 });
  s.dot(ax.X(2), ax.Y(pois(1, 2)), { r: 26, color: C.green, open: true, at: 5.3, width: 4 });
  s.caption(`At least one: $1-P(X=0)=1-e^{-1}\\approx ${(1 - Math.exp(-1)).toFixed(3)}$`, 8.8, { y: 860 });
  s.dot(ax.X(0), ax.Y(pois(1, 0)), { r: 26, color: C.red, open: true, at: 9.1, width: 4 });
  S.push(s);
}

// ------------------------------------------------------------------ two families in one question
{
  const s = new Scene('q1-combined', 14.5);
  s.title('Two families in one question');
  s.text('Earthquakes: on average 7 per year (Poisson)', { x: 150, y: 185, w: 1600, size: 44, at: 0.6 });
  s.text('1. Inside', { x: 150, y: 275, w: 300, size: 42, font: 'Oswald', color: C.orange, at: 1.6 });
  s.text('a quiet year: $q=P(X=0)=e^{-7}$', { x: 360, y: 278, w: 1200, size: 42, at: 1.9 });
  const n = 8, bw = 130, gap = 30, x0 = 960 - (n * bw + (n - 1) * gap) / 2, quiet = [1, 4, 6];
  for (let i = 0; i < n; i++) {
    const x = x0 + i * (bw + gap);
    const r = s.rect(x, 400, bw, bw, { fill: quiet.includes(i) ? C.green : C.ground, opacity: 0, stroke: C.ink, width: 3, rx: 10, at: 3.2 + i * 0.08 });
    s.text(`year ${i + 1}`, { x: x + bw / 2, y: 445, w: bw, size: 30, align: 'center', color: C.soft, at: 3.3 + i * 0.08 });
    if (quiet.includes(i)) s.to(r, { attr: { 'fill-opacity': 0.3 }, duration: 0.3 }, 4.8 + quiet.indexOf(i) * 0.25);
  }
  s.text('2. Outside', { x: 150, y: 600, w: 300, size: 42, font: 'Oswald', color: C.orange, at: 6.0 });
  s.text('count quiet years out of 8 → Binomial$(8,q)$', { x: 360, y: 603, w: 1300, size: 42, at: 6.3 });
  s.text('$P(\\text{exactly 3 quiet})=\\dbinom83q^3(1-q)^5$', { x: 960, y: 700, w: 1400, size: 50, align: 'center', at: 8.0 });
  s.caption('The first family gives $q$. The second family uses it.', 10.0);
  S.push(s);
}

// ------------------------------------------------------------------ end card
{
  const s = new Scene('q1-end', 10);
  s.title('Question 1 is one of two kinds');
  s.text('1. PMF & CDF from scratch', { x: 150, y: 230, w: 800, size: 54, font: 'Oswald', color: C.orange, at: 0.6 });
  ['list → label → group → add', 'unknown $c$: the total = 1', 'CDF: running total; jumps = PMF'].forEach((l, i) =>
    s.text(l, { x: 150, y: 340 + i * 95, w: 800, size: 46, at: 1.2 + i * 0.5 }));
  s.text('2. Named family word problem', { x: 1000, y: 230, w: 800, size: 54, font: 'Oswald', color: C.blue, at: 2.8 });
  ['spot the clue word', 'write the PMF, plug in $k$', 'scale Poisson\'s $\\lambda$'].forEach((l, i) =>
    s.text(l, { x: 1000, y: 340 + i * 95, w: 800, size: 46, at: 3.4 + i * 0.5 }));
  s.caption('"At least one" → $1-P(0)$, every time.', 5.6, { y: 760, size: 50 });
  S.push(s);
}

writeVideo('q1', 'ELEC 226 Test 2 - Question 1', S);
