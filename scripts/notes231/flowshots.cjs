// Exercise every current-flow circuit (.flow) in a note: steady state, flip each switch, watch the transient.
// usage: node flowshots.cjs <docId> <outDir> [--dark]   Prints the readouts at each moment so values can be checked.
const path = require('path');
const fs = require('fs');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
(async () => {
  const [, , docId, out, ...flags] = process.argv;
  fs.mkdirSync(out, { recursive: true });
  const course = process.env.COURSE || '206af2a6-c1f1-4700-ac44-5eba708c676b';
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1300, height: 1000 }, deviceScaleFactor: 1.5, colorScheme: flags.includes('--dark') ? 'dark' : 'light' });
  const errors = [];
  page.on('pageerror', (e) => errors.push('pageerror: ' + e.message));
  await page.goto(`http://127.0.0.1:8000/courses/${course}/docs/${docId}`, { waitUntil: 'commit' });
  await page.waitForSelector('.flow', { timeout: 30000 }).catch(() => {});
  if (flags.includes('--dark')) await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  await page.waitForTimeout(1500);
  const flows = await page.$$('figure.schematic:has(.flow)');
  console.log('flow circuits', flows.length);
  // readout text, then [switch label] and {box widths in px}: the widths must not change while numbers run
  const readouts = async (f) =>
    (await f.$$eval('.mt-readout, .flow-time', (els) => els.map((e) => e.textContent.trim()))).join(' | ') +
    ' [' + (await f.$$eval('.flow-labels > span .katex-mathml annotation', (els) => els.map((e) => e.textContent)).then((x) => x.join(','))) + ']' +
    ' {' + (await f.$$eval('.mt-readout', (els) => els.map((e) => Math.round(e.getBoundingClientRect().width)).join(','))) + '}';
  for (let i = 0; i < flows.length; i++) {
    const f = flows[i];
    await f.scrollIntoViewIfNeeded();
    await page.waitForTimeout(1200);
    await f.screenshot({ path: `${out}/flow${i}_steady.png` });
    console.log(`#${i} steady:`, await readouts(f));
    const btn = await f.$('.flow-controls .mt-btn');
    if (!btn) continue;
    await btn.click();
    for (const ms of [300, 2000, 6000]) {
      await page.waitForTimeout(ms === 300 ? 300 : ms === 2000 ? 1700 : 4000);
      await f.screenshot({ path: `${out}/flow${i}_after${ms}.png` });
      console.log(`#${i} +${ms}ms:`, await readouts(f));
    }
    // click the drawn switch itself to flip it back
    const sw = await f.$('.flow-switch .flow-hit');
    if (sw) {
      await sw.click();
      await page.waitForTimeout(2500);
      await f.screenshot({ path: `${out}/flow${i}_back.png` });
      console.log(`#${i} back:`, await readouts(f));
    }
  }
  console.log(errors.length ? errors.join('\n') : 'no errors');
  await browser.close();
})();
