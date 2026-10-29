// Screenshot a whole note one screen at a time, optionally with every solution / formula-sheet block opened.
// Usage: node scripts/note-shots.mjs <base url> <courseId> <docId> <out prefix> [open|closed] [light|dark] [width]
import { chromium } from "playwright-core";
const [base, courseId, docId, out, mode = "closed", theme = "light", width = "1500"] = process.argv.slice(2);
const browser = await chromium.launch({ channel: "msedge" });
const page = await browser.newPage({ viewport: { width: Number(width), height: 1000 }, colorScheme: theme });
const errors = [];
page.on("pageerror", (e) => errors.push(String(e)));
page.on("console", (m) => m.type() === "error" && errors.push(m.text()));
await page.goto(`${base}/courses/${courseId}/docs/${docId}`, { waitUntil: "networkidle" });
await page.waitForTimeout(1500);
if (mode === "open") {
  await page.$$eval("details.reveal", (all) => all.forEach((d) => (d.open = true)));
  await page.waitForTimeout(2500); // figures and math inside the solutions render on open
}
// The note scrolls inside its own pane, not the window: find the tallest scrollable element.
const total = await page.evaluate(() => {
  const els = [...document.querySelectorAll("*")].filter((e) => e.scrollHeight > e.clientHeight + 50 && getComputedStyle(e).overflowY !== "visible");
  const el = els.sort((a, b) => b.scrollHeight - a.scrollHeight)[0] ?? document.scrollingElement;
  el.setAttribute("data-shot-scroller", "");
  return { height: el.scrollHeight, view: el.clientHeight };
});
const shots = Math.ceil(total.height / (total.view - 80));
for (let i = 0; i < shots; i++) {
  await page.$eval("[data-shot-scroller]", (el, y) => (el.scrollTop = y), i * (total.view - 80));
  await page.waitForTimeout(500);
  await page.screenshot({ path: `${out}-${String(i).padStart(2, "0")}.png` });
}
console.log(`${shots} screenshots`, errors.length ? errors : "no errors");
await browser.close();
