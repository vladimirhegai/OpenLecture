// Screenshot every math-tool card (.mt-card) in a note, plus interaction states.
// usage: node toolshots.cjs <docId> <outDir> [--dark] [--width=1300]
// Reports tool errors (.mt-error) and KaTeX errors so a build can fail fast.
const path = require('path');
const fs = require('fs');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
(async () => {
  const [, , docId, out, ...flags] = process.argv;
  const dark = flags.includes('--dark');
  const width = Number((flags.find((f) => f.startsWith('--width=')) || '--width=1300').split('=')[1]);
  fs.mkdirSync(out, { recursive: true });
  const course = process.env.COURSE || '206af2a6-c1f1-4700-ac44-5eba708c676b';
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width, height: 1000 }, deviceScaleFactor: 1.5, colorScheme: dark ? 'dark' : 'light' });
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => m.type() === 'error' && errors.push('console: ' + m.text()));
  await page.goto(`http://127.0.0.1:8000/courses/${course}/docs/${docId}`, { waitUntil: 'networkidle' });
  if (dark) await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  await page.waitForTimeout(2000);
  // open every solution so tools inside them render too
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
  await page.waitForTimeout(800);
  const cards = await page.$$('.mt-card');
  console.log('cards', cards.length);
  for (let i = 0; i < cards.length; i++) {
    const c = cards[i];
    await c.scrollIntoViewIfNeeded();
    const cls = await c.getAttribute('class');
    await c.screenshot({ path: `${out}/card${String(i).padStart(2, '0')}.png` });
    if (cls.includes('mt-error')) errors.push(`card ${i}: ` + (await c.$eval('figcaption', (e) => e.textContent)));
    if (cls.includes('mt-stepper')) {
      const next = await c.$('.mt-btn.mt-primary');
      for (let k = 0; k < 3 && next; k++) await next.click();
      await c.screenshot({ path: `${out}/card${String(i).padStart(2, '0')}_step3.png` });
    }
    const dot = await c.$('.mt-drag-dot');
    if (dot) {
      const b = await dot.boundingBox();
      await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2);
      await page.mouse.down();
      await page.mouse.move(b.x + 60, b.y - 40, { steps: 6 });
      await page.mouse.up();
      await c.screenshot({ path: `${out}/card${String(i).padStart(2, '0')}_drag.png` });
    }
    if (cls.includes('mt-3d')) {
      const s = await c.$('svg');
      const b = await s.boundingBox();
      await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2);
      await page.mouse.down();
      await page.mouse.move(b.x + b.width / 2 + 120, b.y + b.height / 2 + 30, { steps: 6 });
      await page.mouse.up();
      await c.screenshot({ path: `${out}/card${String(i).padStart(2, '0')}_rot.png` });
    }
  }
  const katexErr = await page.$$eval('.katex-error', (els) => els.map((e) => e.getAttribute('title') || e.textContent));
  katexErr.forEach((k) => errors.push('katex: ' + k));
  const wide = await page.$$eval('.katex-display, .mt-eq', (els) => els.filter((e) => e.scrollWidth > e.clientWidth + 2).length);
  if (wide) errors.push(`${wide} equations overflow their column`);
  console.log(errors.length ? errors.join('\n') : 'no errors');
  await browser.close();
})();
