// Flags display math wider than its box (cut off or scrolling) at a given viewport width, with solutions open.
// usage: node clipcheck.cjs <docId> [width]
const path = require('path');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
(async () => {
  const [, , docId, width] = process.argv;
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: Number(width || 1300), height: 1000 } });
  await page.goto(`http://127.0.0.1:8000/courses/${process.env.COURSE || "4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b"}/docs/${docId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
  for (const b of await page.$$('button')) {
    const t = ((await b.textContent()) || '').trim().toLowerCase();
    if (/^(show|reveal|view) (solution|answer)|^solution$/.test(t)) await b.click().catch(() => {});
  }
  await page.waitForTimeout(2500);
  const bad = await page.evaluate(() =>
    [...document.querySelectorAll('.equation, .katex-display')]
      .filter((e) => e.scrollWidth > e.clientWidth + 2)
      .map((e) => `${e.scrollWidth - e.clientWidth}px | ${e.textContent.slice(0, 80)}`),
  );
  console.log([...new Set(bad)].length, 'clipped');
  [...new Set(bad)].forEach((b) => console.log(' ', b));
  await browser.close();
})();
