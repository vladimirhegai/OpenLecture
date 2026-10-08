// Capture UI screenshots from a running server and report console errors.
// Usage: npm run screenshot -- [scenarios.json] [outdir]
// Env: OPENLECTURE_URL (default http://127.0.0.1:8000), PW_CHANNEL (installed browser: msedge, chrome).
// Scenario fields: name, path, theme ("light"|"dark"), viewport, scale, wait, storage (localStorage
// entries), mocks ([{url, method?, status?, json}]), steps ([{click|fill|type|press|hover|upload|wait|waitFor}]).
import fs from "node:fs";
import { chromium } from "playwright-core";

const [specPath = "scripts/scenarios.json", out = "screenshots"] = process.argv.slice(2);
const base = process.env.OPENLECTURE_URL ?? "http://127.0.0.1:8000";
const channel = process.env.PW_CHANNEL ?? (process.platform === "win32" ? "msedge" : "chrome");
const scenarios = JSON.parse(fs.readFileSync(specPath, "utf8"));
fs.mkdirSync(out, { recursive: true });

const browser = await chromium.launch({ channel });
let failed = 0;
for (const s of scenarios) {
  const context = await browser.newContext({
    viewport: s.viewport ?? { width: 1440, height: 900 },
    deviceScaleFactor: s.scale ?? 1,
    colorScheme: s.theme ?? "light",
  });
  await context.addInitScript((state) => {
    for (const [key, value] of Object.entries(state)) localStorage.setItem(key, value);
  }, s.storage ?? {});
  const page = await context.newPage();
  for (const mock of s.mocks ?? []) {
    await page.route(mock.url, (route) =>
      mock.method && route.request().method() !== mock.method
        ? route.continue()
        : route.fulfill({ status: mock.status ?? 200, contentType: "application/json", body: JSON.stringify(mock.json) }),
    );
  }
  const errors = [];
  page.on("console", (message) => message.type() === "error" && errors.push(message.text()));
  page.on("pageerror", (error) => errors.push(String(error)));
  try {
    await page.goto(base + (s.path ?? "/"), { waitUntil: "networkidle" });
    await page.waitForTimeout(s.wait ?? 600);
    for (const step of s.steps ?? []) {
      if (step.click) await page.click(step.click, { timeout: 5000 });
      if (step.fill) await page.fill(step.fill[0], step.fill[1]);
      if (step.type) await page.keyboard.type(step.type);
      if (step.press) await page.keyboard.press(step.press);
      if (step.hover) await page.hover(step.hover);
      if (step.upload) await page.setInputFiles(step.upload[0], step.upload[1]);
      if (step.wait) await page.waitForTimeout(step.wait);
      if (step.waitFor) await page.waitForSelector(step.waitFor, { timeout: step.timeout ?? 10000 });
    }
    await page.screenshot({ path: `${out}/${s.name}.png` });
  } catch (error) {
    errors.push(String(error));
  }
  if (errors.length) failed++;
  console.log(s.name, errors.length ? `ERRORS: ${errors.join(" | ")}` : "ok");
  await context.close();
}
await browser.close();
process.exit(failed ? 1 : 0);
