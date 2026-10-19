#!/usr/bin/env node
// End-to-end smoke test for docs/explorer: drives headless Chrome over the
// DevTools protocol (Node >= 22, no npm packages), visits every view, performs
// a few interactions, and fails on any uncaught exception or console error.
//
//   node viz/smoke_test_explorer.mjs [screenshot_dir]
//   CHROME=/path/to/chrome node viz/smoke_test_explorer.mjs
//   WIDTH=820 FULL=1 node viz/smoke_test_explorer.mjs /tmp/narrow

import { spawn } from "node:child_process";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync, existsSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PAGE = pathToFileURL(path.join(HERE, "..", "docs", "explorer", "index.html")).href;
const SHOTS = process.argv[2] || path.join(tmpdir(), "sdx_shots");
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const PORT = 9333;
const WIDTH = Number(process.env.WIDTH) || 1400;  // e.g. WIDTH=820 for the stacked layout
const FULL = process.env.FULL === "1";             // full-page screenshots
const SETTLE_MS = 700;

// [name, hash, javascript that must evaluate truthy afterwards]
const STEPS = [
  ["overview", "#overview", "document.querySelectorAll('td.heat').length === 24"],
  ["classes", "#classes?cond=C", "document.querySelectorAll('td.heat').length === 20"],
  ["ledger-lenient", "#ledger?cond=B_lenient", "document.querySelectorAll('svg rect.seg').length >= 20"],
  ["ledger-from-episodes", "#ledger?cond=E", "document.body.textContent.includes('computed here from the core episodes')"],
  ["pivot", "#pivot", "document.querySelectorAll('td.heat').length > 20"],
  ["pivot-domain", "#pivot?rows=domain&cols=model&metric=wrong&battery=core", "document.querySelectorAll('td.heat').length >= 40"],
  ["episodes", "#episodes?model=openai%2Fgpt-5.6-luna&cond=C", "document.querySelectorAll('tbody tr.click').length === 50"],
  ["episode-click", null, "(document.querySelector('tbody tr.click').click(), true)"],
  ["episode-detail", null, "document.querySelector('.detail h2') && document.body.textContent.includes('What the model saw')"],
  ["episode-next-key", null, "(document.dispatchEvent(new KeyboardEvent('keydown', {key: 'j'})), true)"],
  ["episode-after-j", null, "location.hash.includes('i=')"],
  ["episodes-lenient", "#episodes?cond=B_lenient&class=rename&outcome=ACCEPTED_WRONG", "(document.querySelector('tbody tr.click').click(), true)"],
  ["episode-lenient", null, "document.querySelectorAll('td.st-dropped').length > 0 && document.querySelectorAll('td.st-wrong').length > 0"],
  ["dataset-tools", "#dataset/tools/book_flight", "document.body.textContent.includes('v1 parameters')"],
  ["dataset-tasks", "#dataset/tasks/bmk01", "document.body.textContent.includes('Phrasings')"],
  // baseline episodes count toward every class their model ran for that task (analysis.json pairing)
  ["baseline-pairing", "#pivot", "['rename','enum_tighten','required','type_change','default_change'].every((k) => SDXFields.filterIndices({cond: 'A', class: k, battery: 'core'}).length === SDXFields.filterIndices({cond: 'B_strict', class: k, battery: 'core'}).length)"],
  ["pivot-battery-clear", "#pivot", "(document.querySelector('.controls label .chip.on').click(), true)"],
  ["pivot-battery-cleared", null, "location.hash.includes('battery=all') && document.body.textContent.includes('4,800 episodes match')"],
  ["search-roundtrip", "#episodes?q=" + encodeURIComponent("a&b?c+d"), "document.querySelector('input[type=search]').value === 'a&b?c+d'"],
  ["malformed-hash", "#episodes?q=%E0%A4%A", "document.querySelector('#view h2') !== null"],
  ["stats", "#stats", "document.querySelectorAll('tbody tr').length >= 112"],
  ["stats-bh", "#stats?bh=1", "document.body.textContent.includes('74 tests shown')"],
  ["audit", "#audit", "document.querySelectorAll('.grid2 > .card').length === 24"],
  ["toggle-model", "#overview", "(document.querySelector('#modelbar .chip').click(), true)"],
  ["after-toggle", null, "document.querySelectorAll('td.heat').length === 18"],
  ["restore-model", null, "(document.querySelector('#modelbar .chip').click(), document.querySelectorAll('td.heat').length === 24)"],
];

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function waitForTarget() {
  for (let i = 0; i < 50; i++) {
    try {
      const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
      const page = list.find((t) => t.type === "page");
      if (page) return page.webSocketDebuggerUrl;
    } catch { /* chrome not up yet */ }
    await sleep(200);
  }
  throw new Error("Chrome DevTools endpoint did not come up");
}

function connect(url) {
  const ws = new WebSocket(url);
  let id = 0;
  const pending = new Map(), problems = [];
  ws.onmessage = (msg) => {
    const m = JSON.parse(msg.data);
    if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); return; }
    if (m.method === "Runtime.exceptionThrown") problems.push(`exception: ${m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text}`);
    if (m.method === "Runtime.consoleAPICalled" && ["error", "warning"].includes(m.params.type))
      problems.push(`console.${m.params.type}: ${m.params.args.map((a) => a.value ?? a.description).join(" ")}`);
  };
  const send = (method, params = {}) => new Promise((resolve) => {
    pending.set(++id, resolve);
    ws.send(JSON.stringify({ id, method, params }));
  });
  return new Promise((resolve) => { ws.onopen = () => resolve({ ws, send, problems }); });
}

async function main() {
  if (!existsSync(CHROME)) throw new Error(`Chrome not found at ${CHROME}; set CHROME=...`);
  mkdirSync(SHOTS, { recursive: true });
  const profile = mkdtempSync(path.join(tmpdir(), "sdx-chrome-"));
  const chrome = spawn(CHROME, ["--headless=new", `--remote-debugging-port=${PORT}`, `--user-data-dir=${profile}`,
    `--window-size=${WIDTH},1000`, "--allow-file-access-from-files", "about:blank"], { stdio: "ignore" });
  let failures = 0;
  try {
    const { ws, send, problems } = await connect(await waitForTarget());
    await send("Runtime.enable");
    await send("Page.enable");
    await send("Emulation.setDeviceMetricsOverride", { width: WIDTH, height: 1000, deviceScaleFactor: 1, mobile: false });
    await send("Page.navigate", { url: PAGE + "#overview" });
    await sleep(2500); // data.js is ~5 MB
    for (const [name, hash, check] of STEPS) {
      const before = problems.length;
      if (hash) await send("Runtime.evaluate", { expression: `location.hash = ${JSON.stringify(hash)}` });
      await sleep(SETTLE_MS);
      const res = await send("Runtime.evaluate", { expression: check, returnByValue: true });
      const ok = res.result?.result?.value === true && problems.length === before;
      const shot = await send("Page.captureScreenshot", { format: "png", captureBeyondViewport: FULL });
      writeFileSync(path.join(SHOTS, `${name}.png`), Buffer.from(shot.result.data, "base64"));
      console.log(`${ok ? "ok  " : "FAIL"} ${name}${ok ? "" : "  " + JSON.stringify(res.result?.result?.value ?? res.result?.exceptionDetails?.text)}`);
      problems.slice(before).forEach((p) => console.log(`       ${p}`));
      if (!ok) failures++;
    }
    ws.close();
  } finally {
    chrome.kill();
    await sleep(300);
    rmSync(profile, { recursive: true, force: true });
  }
  console.log(`\n${STEPS.length - failures}/${STEPS.length} steps passed; screenshots in ${SHOTS}`);
  process.exit(failures ? 1 : 0);
}

main().catch((err) => { console.error(err); process.exit(2); });
