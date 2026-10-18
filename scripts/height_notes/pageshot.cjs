// Whole-note screenshot (solutions closed), cut into numbered slices for review.
// usage: node pageshot.cjs <docId> <outDir> [--open]   (COURSE=<id> for courses other than ELEC 221)
const path = require('path');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
const fs = require('fs');
(async () => {
  const [, , docId, out, sliceArg] = process.argv;
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1300, height: 1000 }, deviceScaleFactor: 1 });
  await page.goto(`http://127.0.0.1:8000/courses/${process.env.COURSE || "4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b"}/docs/${docId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);
  // --open: expand every hidden solution so it is in the shot too
  if (process.argv.includes('--open')) await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
  const h = await page.evaluate(() => document.querySelector('div.scroll').scrollHeight);
  await page.setViewportSize({ width: 1300, height: Math.min(h + 200, 30000) });
  await page.waitForTimeout(2500);
  const el = await page.$('div.scroll');
  await el.screenshot({ path: `${out}/full.png` });
  console.log('height', h);
  await browser.close();
})();
