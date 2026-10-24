// Screenshot every step of every ```circuitsteps card in a note (solutions opened), and report errors.
// usage: node stepshots.cjs <docId> <outDir> [--dark] [--width=1300] [--mid] [--only=title]
//   --mid: also catch mid-animation; --only: just the cards whose title contains this text (e.g. "Problem 3 ·")
const path = require('path');
const fs = require('fs');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
(async () => {
  const [, , docId, out, ...flags] = process.argv;
  const dark = flags.includes('--dark');
  const width = Number((flags.find((f) => f.startsWith('--width=')) || '--width=1300').split('=')[1]);
  fs.mkdirSync(out, { recursive: true });
  const course = process.env.COURSE || '4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b';
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width, height: 1000 }, deviceScaleFactor: 1.5, colorScheme: dark ? 'dark' : 'light' });
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => m.type() === 'error' && errors.push('console: ' + m.text()));
  await page.goto(`http://127.0.0.1:8000/courses/${course}/docs/${docId}`, { waitUntil: 'networkidle' });
  if (dark) await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  await page.waitForTimeout(1500);
  await page.screenshot({ path: `${out}/page.png` });
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
  await page.waitForTimeout(1500);
  const only = (flags.find((f) => f.startsWith('--only=')) || '').slice(7).toLowerCase(); // card title substring
  const cards = await page.$$('.cs-card');
  console.log('cards', cards.length);
  for (let i = 0; i < cards.length; i++) {
    const c = cards[i];
    const title = (await c.$eval('.mt-title', (e) => e.textContent)).toLowerCase();
    if (only && !title.includes(only)) continue;
    const n = (await c.$$('.mt-dot')).length;
    for (let k = 0; k < n; k++) {
      await c.scrollIntoViewIfNeeded();
      if (flags.includes('--mid') && k > 0) {
        await page.waitForTimeout(250);
        await c.screenshot({ path: `${out}/c${i}_s${k + 1}_mid.png` });
      }
      await page.waitForTimeout(1800);
      await c.screenshot({ path: `${out}/c${i}_s${k + 1}.png` });
      // Labels that still overlap after the automatic layout (screen boxes, 1 px tolerance).
      const clash = await c.$eval('.cs-stage svg', (svg) => {
        const els = [...svg.querySelectorAll('[data-p="L"]:not(.cs-gone), .cs-ov:not(.cs-gone) .cs-label-in')]
          .map((e) => ({ e, r: e.getBoundingClientRect() }))
          .filter(({ r }) => r.width > 0);
        const bad = [];
        for (let a = 0; a < els.length; a++)
          for (let b = a + 1; b < els.length; b++) {
            const [p, q] = [els[a].r, els[b].r];
            if (p.left < q.right - 1 && q.left < p.right - 1 && p.top < q.bottom - 1 && q.top < p.bottom - 1)
              bad.push(`${(els[a].e.textContent || 'glyph').trim().slice(0, 12)} × ${(els[b].e.textContent || 'glyph').trim().slice(0, 12)}` +
                ` (${Math.round(Math.min(p.right, q.right) - Math.max(p.left, q.left))}×${Math.round(Math.min(p.bottom, q.bottom) - Math.max(p.top, q.top))}px at ${Math.round(p.left - svg.getBoundingClientRect().left)},${Math.round(p.top - svg.getBoundingClientRect().top)})`);
          }
        // Mesh rings crossing a label (the ring's own name sits inside it and is fine).
        const ctm = svg.getScreenCTM();
        for (const g of svg.querySelectorAll('.cs-ov[data-kind="mesh"]:not(.cs-gone)')) {
          const m = /A ([\d.]+) /.exec(g.querySelector('.cs-stroke')?.getAttribute('d') || '');
          if (!m) continue;
          const r = Number(m[1]) * ctm.a;
          const cx = (Number(g.dataset.cx) + Number(g.dataset.dx || 0)) * ctm.a + ctm.e;
          const cy = (Number(g.dataset.cy) + Number(g.dataset.dy || 0)) * ctm.d + ctm.f;
          const own = g.querySelector('.cs-label-in');
          for (const { e, r: b } of els) {
            if (e === own) continue;
            const near = Math.hypot(Math.max(b.left, Math.min(cx, b.right)) - cx, Math.max(b.top, Math.min(cy, b.bottom)) - cy);
            const far = Math.max(...[b.left, b.right].flatMap((x) => [b.top, b.bottom].map((y) => Math.hypot(x - cx, y - cy))));
            if (near < r - 1 && far > r + 1) bad.push(`mesh ring × ${(e.textContent || 'glyph').trim().slice(0, 12)}`);
          }
        }
        return bad;
      });
      if (clash.length) errors.push(`card ${i} step ${k + 1}: overlapping labels: ${clash.join(', ')}`);
      const next = await c.$('.mt-btn.mt-primary');
      if (next) await next.click();
    }
    await c.$eval('.mt-icon', (b) => b.click());
    await page.waitForTimeout(800);
    await c.screenshot({ path: `${out}/c${i}_all.png` });
  }
  const tool = await page.$$eval('.mt-error figcaption', (els) => els.map((e) => e.textContent));
  tool.forEach((t) => errors.push('tool: ' + t));
  const katexErr = await page.$$eval('.katex-error', (els) => els.map((e) => e.getAttribute('title') || e.textContent));
  katexErr.forEach((k) => errors.push('katex: ' + k));
  const wide = await page.$$eval('.katex-display', (els) => els.filter((e) => e.scrollWidth > e.clientWidth + 2).length);
  if (wide) errors.push(`${wide} equations overflow their column`);
  console.log(errors.length ? errors.join('\n') : 'no errors');
  await browser.close();
})();
