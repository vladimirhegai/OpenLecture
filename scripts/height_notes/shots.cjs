// For each block whose text contains one of the given strings: screenshot the block and its figure, then open its
// height view and screenshot step 0 and the finished picture for every tab and both drawing modes.
// usage: node shots.cjs <docId> <outDir> "title1" "title2" ...   (run from this folder; server on :8000)
const path = require('path');
const { chromium } = require(path.join(__dirname, '../../frontend/node_modules/playwright-core'));
const fs = require('fs');
(async () => {
  const [, , docId, out, ...titles] = process.argv;
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const page = await browser.newPage({ viewport: { width: 1400, height: 1100 }, deviceScaleFactor: 1.5 });
  await page.goto(`http://127.0.0.1:8000/courses/${process.env.COURSE || "4f61c7c9-90ce-4e64-8e1b-b7fb2f198e0b"}/docs/${docId}`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => (d.open = true)));
  for (const b of await page.$$('button')) {
    const t = ((await b.textContent()) || '').trim().toLowerCase();
    if (/^(show|reveal|view) (solution|answer)|^solution$/.test(t)) await b.click().catch(() => {});
  }
  await page.waitForTimeout(1500);
  console.log('katex errors on page:', await page.evaluate(() => document.querySelectorAll('.katex-error').length));
  for (const [n, title] of titles.entries()) {
    const block = page.locator('section.block', { hasText: title }).first();
    await block.scrollIntoViewIfNeeded();
    await page.waitForTimeout(400);
    await block.screenshot({ path: `${out}/${n}_block.png` });
    const fig = block.locator('figure.schematic').first();
    if (await fig.count()) { await fig.scrollIntoViewIfNeeded(); await fig.screenshot({ path: `${out}/${n}_fig.png` }); }
    const btn = block.locator('.elev-open').first();
    if (!(await btn.count())) { console.log(title, 'no height button'); continue; }
    await btn.click();
    await page.waitForTimeout(700);
    const dlg = page.locator('.elev-dialog');
    const walk = dlg.getByRole('button', { name: /Walk me through it/ });
    if (await walk.count()) await walk.click();
    await page.waitForTimeout(400);
    const tabs = dlg.locator('.elev-tabs button');
    const nt = Math.max(1, await tabs.count());
    for (let t = 0; t < nt; t++) {
      if (await tabs.count()) { await tabs.nth(t).click(); await page.waitForTimeout(400); }
      const modes = dlg.locator('.elev-mode button');
      const nm = Math.max(1, await modes.count());
      for (let m = 0; m < nm; m++) {
        if (await modes.count()) { await modes.nth(m).click(); await page.waitForTimeout(300); }
        const restart = dlg.getByRole('button', { name: /Restart/ });
        if ((await restart.count()) && (await restart.isEnabled())) await restart.click();
        await page.waitForTimeout(250);
        await dlg.screenshot({ path: `${out}/${n}_t${t}_m${m}_step0.png` });
        const all = dlg.getByRole('button', { name: /Show all/ });
        if ((await all.count()) && (await all.isEnabled())) await all.click();
        await page.waitForTimeout(350);
        await dlg.screenshot({ path: `${out}/${n}_t${t}_m${m}_final.png` });
      }
    }
    await page.keyboard.press('Escape');
    await page.waitForTimeout(400);
  }
  await browser.close();
})();
