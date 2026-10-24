// Check and screenshot an ELEC 226 note: KaTeX errors, math overflow, tool errors; page cut into slices.
// usage: node shots.cjs <docId> <outDir> [--closed] [--dark] [--width=1300] [--slice=1600]
const path = require('path');
const fs = require('fs');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
(async () => {
  const [, , docId, out, ...flags] = process.argv;
  const opt = (k, d) => Number((flags.find((f) => f.startsWith(`--${k}=`)) || `--${k}=${d}`).split('=')[1]);
  const width = opt('width', 1300), slice = opt('slice', 1600);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width, height: 1000 }, deviceScaleFactor: 1 });
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  page.on('console', (m) => m.type() === 'error' && errors.push('console: ' + m.text()));
  await page.goto(`http://127.0.0.1:8000/courses/149e587a-a62f-415a-91de-6337ea2f0006/docs/${docId}`, { waitUntil: 'networkidle' });
  if (flags.includes('--dark')) await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  await page.waitForTimeout(2000);
  if (!flags.includes('--closed')) {
    await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
    await page.waitForTimeout(1200);
  }
  const report = await page.evaluate(() => {
    const txt = (el) => (el.closest('[id^="b-"]')?.querySelector('h1,h2,h3,summary,strong')?.textContent || '').slice(0, 60);
    return {
      katex: [...document.querySelectorAll('.katex-error')].map((e) => `${txt(e)} :: ${e.getAttribute('title') || e.textContent}`.slice(0, 220)),
      overflow: [...document.querySelectorAll('.katex-display')]
        .filter((e) => e.scrollWidth > e.clientWidth + 2)
        .map((e) => `${txt(e)} :: ${e.scrollWidth}>${e.clientWidth} :: ${e.textContent.slice(0, 80)}`),
      tools: [...document.querySelectorAll('.mt-error')].map((e) => e.textContent.slice(0, 200)),
      tables: [...document.querySelectorAll('.table-wrap')].filter((e) => e.scrollWidth > e.clientWidth + 2).length,
      height: document.querySelector('div.scroll').scrollHeight,
    };
  });
  console.log(JSON.stringify({ ...report, errors }, null, 1));
  const h = report.height;
  await page.setViewportSize({ width, height: Math.min(h + 100, 32000) });
  await page.waitForTimeout(1500);
  const el = await page.$('div.scroll');
  const box = await el.boundingBox();
  for (let y = 0, i = 1; y < Math.min(h, 32000); y += slice, i++) {
    await page.screenshot({
      path: `${out}/s${String(i).padStart(2, '0')}.png`,
      clip: { x: box.x, y: box.y + y, width: box.width, height: Math.min(slice, h - y) },
    });
  }
  console.log('slices', Math.ceil(Math.min(h, 32000) / slice));
  await browser.close();
})();
