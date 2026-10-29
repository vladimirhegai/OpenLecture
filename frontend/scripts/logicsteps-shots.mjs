// Click through every ```logicsteps card in a note, screenshot each step and the Try-inputs view.
// Usage: node scripts/logicsteps-shots.mjs <base url> <docId> <out prefix> [light|dark]
import { chromium } from "playwright-core";
const [base, docId, out, theme = "light"] = process.argv.slice(2);
const browser = await chromium.launch({ channel: "msedge" });
const page = await browser.newPage({ viewport: { width: 1100, height: 1300 }, colorScheme: theme });
const errors = [];
page.on("pageerror", (e) => errors.push(String(e)));
page.on("console", (m) => m.type() === "error" && errors.push(m.text()));
await page.goto(`${base}/courses/d0b18428-9c03-4bbf-87af-7a1169d667ab/docs/${docId}`, { waitUntil: "networkidle" });
await page.waitForTimeout(1200);
// Cards inside collapsed solutions are not rendered until their block is opened.
await page.$$eval("details.reveal", (all) => all.forEach((d) => (d.open = true)));
await page.waitForTimeout(1500);
const cards = await page.$$(".ls-card");
console.log("cards", cards.length);
for (const [c, card] of cards.entries()) {
  await card.scrollIntoViewIfNeeded();
  const steps = await card.$$(".mt-dot");
  for (let s = 0; s < steps.length; s++) {
    await page.waitForTimeout(700);
    await card.screenshot({ path: `${out}-c${c}-s${s}.png` });
    if (s < steps.length - 1) await (await card.$(".mt-primary")).click();
  }
  // Live inputs on the last step: set x1 = 1, x3 = 1 (row 101).
  await (await card.$(".ls-try")).click();
  for (const label of ["x₁", "x₃"]) {
    const bit = await card.$(`.ls-bit:has-text("${label}")`);
    if (bit) await bit.click();
  }
  await page.waitForTimeout(900);
  await card.screenshot({ path: `${out}-c${c}-try.png` });
}
console.log(errors.length ? errors : "no errors");
await browser.close();
