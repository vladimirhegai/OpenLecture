// Screenshot a long note in viewport-sized chunks by scrolling div.scroll (no texture-size cap).
// usage: node chunkshot.cjs <repoRoot> <docId> <outDir> [courseId]
const path = require('path');
const fs = require('fs');
const [, , root, docId, out, course = '206af2a6-c1f1-4700-ac44-5eba708c676b'] = process.argv;
const { chromium } = require(path.join(root, 'frontend/node_modules/playwright-core'));
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1300, height: 1400 }, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:8000/courses/${course}/docs/${docId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);
  if (process.env.OPEN) {  // OPEN=1: open every solution first, so the steps get screenshotted too
    await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
    await page.waitForTimeout(1500);
  }
  const info = await page.evaluate(() => {
    const s = document.querySelector('div.scroll');
    const r = s.getBoundingClientRect();
    return { h: s.scrollHeight, top: r.top, x: r.x, w: r.width, vh: s.clientHeight };
  });
  const step = info.vh - 40;
  let i = 0;
  for (let y = 0; y < info.h; y += step, i++) {
    await page.evaluate((y) => { document.querySelector('div.scroll').scrollTop = y; }, y);
    await page.waitForTimeout(250);
    await page.screenshot({ path: `${out}/c${String(i).padStart(2, '0')}.png`, clip: { x: info.x, y: info.top, width: info.w, height: info.vh } });
  }
  console.log('chunks', i, 'height', info.h, 'width', info.w);
  await browser.close();
})();
