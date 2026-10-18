// Visual/content QA for the Week 0 note; uses the existing local app.
const path = require('path');
const fs = require('fs');
const { chromium } = require('../../frontend/node_modules/playwright-core');

(async () => {
  const ref = JSON.parse(fs.readFileSync(path.join(__dirname, 'out/w0-document.json'), 'utf8'));
  const out = path.join(__dirname, 'out/w0-qa');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  try {
    const page = await browser.newPage({ viewport: { width: 1300, height: 1000 }, deviceScaleFactor: 1 });
    const errors = [];
    const stability = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.goto('http://127.0.0.1:8000' + ref.route, { waitUntil: 'networkidle' });
    await page.getByRole('heading', { name: 'Calculus Refresher', exact: true }).waitFor();
    await page.screenshot({ path: path.join(out, 'opening.png') });
    const hidden = await page.locator('details:not([open])').count();
    if (hidden !== 21) errors.push('Expected 21 initially hidden solutions, found ' + hidden);
    const spec = JSON.parse(fs.readFileSync(path.join(__dirname, 'out/w0.json'), 'utf8'));
    const outline = [];
    let topic;
    for (const block of spec.blocks) {
      if (block.type !== 'heading') continue;
      if (block.level === 1) topic = block.text;
      outline.push({ level: block.level, title: block.text, topic });
    }
    for (const title of ['Chain rule', 'Product rule and second derivatives', 'Quotient rule', 'Partial derivatives', 'Implicit differentiation']) {
      if (!outline.some((h) => h.level === 2 && h.title === title && h.topic === 'Derivatives')) errors.push('Wrong heading hierarchy: ' + title);
    }
    for (const [prefix, name] of [
      ['chain', 'Chain rule'],
      ['exact', 'Exact differential equations'],
      ['complex', 'Complex roots'],
    ]) {
      await page.locator('.collapsible-heading').filter({ hasText: name }).scrollIntoViewIfNeeded();
      await page.screenshot({ path: path.join(out, prefix + '-section.png') });
    }
    await page.evaluate(() => document.querySelectorAll('details').forEach((d) => d.open = true));
    await page.locator('.mt-stepper').last().waitFor();

    async function checkNavigation(target, label) {
      await target.evaluate(() => document.querySelectorAll('details').forEach((d) => d.open = true));
      await target.evaluate(() => document.fonts.ready);
      const cards = target.locator('.mt-stepper');
      let transitions = 0;
      let maxMovement = 0;
      for (let i = 0; i < await cards.count(); i++) {
        const card = cards.nth(i);
        await card.scrollIntoViewIfNeeded();
        const measure = () => card.evaluate((e) => {
          const r = e.querySelector('.mt-nav > button:last-child').getBoundingClientRect();
          const c = e.getBoundingClientRect();
          const note = e.querySelector('.mt-step.mt-active .mt-note');
          const n = note.getBoundingClientRect();
          if (getComputedStyle(note).animationName !== 'none') throw new Error('Explanation still has an animation');
          return [r.x, r.y, r.width, r.height, c.width, c.height, n.x, n.y];
        });
        const initial = await measure();
        const steps = await card.locator('.mt-dot').count();
        for (let k = 1; k < steps; k++) {
          await card.locator('.mt-nav > button').last().click();
          const current = await measure();
          maxMovement = Math.max(maxMovement, ...current.map((n, j) => Math.abs(n - initial[j])));
          if (await card.locator('.mt-step.mt-active').count() !== 1) errors.push(label + ' card ' + i + ': active step count');
          transitions++;
        }
        // Again, Back, keyboard and direct-dot navigation share the same stable frame.
        await card.locator('.mt-nav > button').last().click();
        if (!await card.locator('.mt-nav > button').first().isDisabled()) errors.push(label + ' card ' + i + ': Again did not reset');
        if (steps > 1) {
          await card.locator('.mt-dot').last().click();
          await card.locator('.mt-nav > button').first().click();
          await card.focus();
          await card.press('ArrowLeft');
          await card.locator('.mt-dot').first().click();
        }
        const reset = await measure();
        maxMovement = Math.max(maxMovement, ...reset.map((n, j) => Math.abs(n - initial[j])));
      }
      stability.push({ viewport: label, cards: await cards.count(), transitions, maxMovement });
      console.log(label + ': checked ' + transitions + ' transitions, maximum movement ' + maxMovement + 'px (buttons and explanation)');
      if (maxMovement > 1) errors.push(label + ': navigation moved by ' + maxMovement + 'px');
    }

    await checkNavigation(page, 'desktop 1300px');
    const narrow = await browser.newPage({ viewport: { width: 390, height: 1000 } });
    narrow.on('pageerror', (e) => errors.push(e.message));
    await narrow.goto('http://127.0.0.1:8000' + ref.route, { waitUntil: 'networkidle' });
    await checkNavigation(narrow, 'narrow 390px');
    await narrow.locator('.mt-stepper').first().scrollIntoViewIfNeeded();
    await narrow.screenshot({ path: path.join(out, 'stable-narrow.png') });
    await narrow.close();

    const first = page.locator('.mt-stepper').first();
    await first.scrollIntoViewIfNeeded();
    await first.screenshot({ path: path.join(out, 'stationary-note-step0.png') });
    await first.locator('.mt-nav > button').last().click();
    await first.screenshot({ path: path.join(out, 'stationary-note-step1.png') });

    await page.evaluate(() => document.querySelectorAll('button[title="Show every step"]').forEach((b) => b.click()));
    await page.locator('.mt-all').last().waitFor();
    const result = await page.evaluate(() => ({
      allSteppers: document.querySelectorAll('.mt-all').length,
      renderedSteps: document.querySelectorAll('.mt-all .mt-eq').length,
      errors: [...document.querySelectorAll('.katex-error, .mt-error')].map((e) => e.textContent),
      overflow: [...document.querySelectorAll('.katex-display, .mt-eq')]
        .filter((e) => e.scrollWidth > e.clientWidth + 2).map((e) => e.textContent),
    }));
    errors.push(...result.errors, ...result.overflow.map((e) => 'Equation overflow: ' + e));
    if (result.allSteppers !== 42) errors.push('Expected 42 equation steppers, found ' + result.allSteppers);
    console.log(JSON.stringify({ hiddenSolutions: hidden, outline, stability, ...result, errors }, null, 2));
    fs.writeFileSync(path.join(out, 'audit.json'), JSON.stringify({ hiddenSolutions: hidden, outline, stability, ...result, errors }, null, 2));
    if (errors.length) process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
