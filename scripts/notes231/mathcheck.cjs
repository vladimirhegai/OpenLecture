const path = require('path');
const [, , root, docId] = process.argv;
const { chromium } = require(path.join(root, 'frontend/node_modules/playwright-core'));
(async () => {
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1300, height: 1000 } });
  await page.goto(`http://127.0.0.1:8000/courses/206af2a6-c1f1-4700-ac44-5eba708c676b/docs/${docId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
  await page.waitForTimeout(1500);
  const r = await page.evaluate(() => ({
    errors: [...document.querySelectorAll('.katex-error')].map((e) => e.textContent.slice(0, 80)),
    overflow: [...document.querySelectorAll('.katex-display')].filter((e) => e.scrollWidth > e.clientWidth + 2).map((e) => e.textContent.slice(0, 60)),
    tables: [...document.querySelectorAll('.table-wrap')].filter((e) => e.scrollWidth > e.clientWidth + 2).map((e) => e.textContent.slice(0, 60)),
    rawDollar: [...document.querySelectorAll('.sheet p, .sheet li, .sheet td')].filter((e) => /\$/.test(e.textContent)).map((e) => e.textContent.slice(0, 80)),
  }));
  console.log(JSON.stringify(r, null, 1));
  await browser.close();
})();
