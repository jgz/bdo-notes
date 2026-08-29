// Archive NA/EU official patch notes + GM Notes as markdown into research/patch-notes/.
// Runs inside the Playwright docker container (see run.sh). Incremental: skips already-saved articles.
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.resolve(HERE, '../../research/patch-notes');
fs.mkdirSync(OUT, { recursive: true });

const MONTHS_BACK = parseInt(process.env.MONTHS_BACK || '6', 10);
const BOARDS = { 2: 'update', 4: 'gm-note' }; // Updates (patch notes) + GM Notes/FAQs
const LIST = bt => `https://www.naeu.playblackdesert.com/en-US/News/Notice?boardType=${bt}`;
const DETAIL = id => `https://www.naeu.playblackdesert.com/en-US/News/Detail?groupContentNo=${id}&countryType=en-US`;

const cutoff = new Date();
cutoff.setMonth(cutoff.getMonth() - MONTHS_BACK);

const parseDate = s => {
  const m = s.match(/([A-Z][a-z]+ \d{1,2},? \d{4})/);
  if (m) { const d = new Date(m[1].replace(',', '')); if (!isNaN(d)) return d; }
  return null;
};

// Drop non-game / marketing posts (update-board: Pearl Shop/mobile/security; GM-board: events/promos).
const EXCLUDE = /pearl shop|black desert\+|security module|coupon|ambassador|bingo|finale|party rumble|arena of solare|tournament|content creator|giveaway|scrapbook|festa/i;
// GM-Notes board is mostly marketing — keep only titles that look like mechanics/progression.
const GMKEEP = /hyperboost|tuvala|season|gear|enhanc|\bguide\b|\bpatch\b|\bupdate\b|balance|\bclass\b|returning|\bfaq\b|\bnode\b|life ?skill|processing|central market|nerf|buff|rework|change|improv|graduation|milestone|academy/i;

const cleanTitle = s => s
  .replace(/\s*\[\d+\]\d*\s*/g, ' ')                          // [114]27 view-count widgets
  .replace(/\s*[A-Z][a-z]+ \d{1,2},? \d{4}\s*\(UTC\)\s*$/, '') // trailing date stamp
  .replace(/\s+/g, ' ').trim();

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36' });
const page = await ctx.newPage();

// --- 1) collect article list within cutoff (paginate via Next) ---
const byId = new Map();
for (const [bt, kind] of Object.entries(BOARDS)) {
  await page.goto(LIST(bt), { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  await page.waitForTimeout(4000);
  for (let pg = 1; pg <= 8; pg++) {
    const items = await page.evaluate(() =>
      [...document.querySelectorAll('a')]
        .map(a => ({ id: (a.href.match(/groupContentNo=(\d+)/) || [])[1], title: a.innerText.replace(/\s+/g, ' ').trim() }))
        .filter(x => x.id && x.title));
    const dates = [];
    for (const it of items) {
      const d = parseDate(it.title);
      if (!d) continue;
      dates.push(d);
      if (d < cutoff || byId.has(it.id)) continue;
      if (EXCLUDE.test(it.title)) continue;
      if (kind === 'gm-note' && !GMKEEP.test(it.title)) continue;
      byId.set(it.id, { id: it.id, title: cleanTitle(it.title), date: d, kind });
    }
    const oldest = dates.sort((a, b) => a - b)[0];
    if (oldest && oldest < cutoff) break;                 // past the window
    const next = await page.$('a:has-text("Next"), a[title="Next"], .paging a.next, .next');
    if (!next) break;
    await next.click().catch(() => {});
    await page.waitForTimeout(3500);
  }
}
const list = [...byId.values()].sort((a, b) => b.date - a.date);
console.log(`In range (last ${MONTHS_BACK}mo): ${list.length} articles`);

// --- 2) fetch each not-yet-saved detail ---
let saved = 0, skipped = 0;
for (const a of list) {
  const iso = a.date.toISOString().slice(0, 10);
  const file = path.join(OUT, `${iso}-${a.id}.md`);
  if (fs.existsSync(file)) { skipped++; continue; }
  await page.goto(DETAIL(a.id), { waitUntil: 'networkidle', timeout: 60000 }).catch(() => {});
  await page.waitForTimeout(3500);
  const body = await page.evaluate(() => {
    const el = document.querySelector('.contents_area.editor_area')
      || document.querySelector('.contents_area')
      || document.querySelector('.view_detail_area')
      || document.body;
    return el ? el.innerText : '';
  });
  const clean = body.split('\n').map(l => l.replace(/\s+$/, '')).join('\n').replace(/\n{3,}/g, '\n\n').trim();
  if (clean.length < 200) { console.log('!! thin/empty, skipping', a.id); continue; }
  const fm = `---\ntitle: ${JSON.stringify(a.title)}\ndate: ${iso}\ncategory: ${a.kind}\nid: ${a.id}\nsource: ${DETAIL(a.id)}\nfetched: ${new Date().toISOString().slice(0, 10)}\n---\n\n`;
  fs.writeFileSync(file, fm + clean + '\n');
  saved++;
  console.log('saved', path.basename(file), `(${clean.length} chars)`);
}

// --- 3) regenerate INDEX.md ---
const files = fs.readdirSync(OUT).filter(f => /^\d{4}-\d{2}-\d{2}-\d+\.md$/.test(f)).sort().reverse();
const rows = files.map(f => {
  const fm = fs.readFileSync(path.join(OUT, f), 'utf8');
  const title = (fm.match(/^title: "(.*)"$/m) || [])[1] || f;
  const cat = (fm.match(/^category: (.*)$/m) || [])[1] || '';
  const date = f.slice(0, 10);
  return `| ${date} | ${cat} | [${title.replace(/\|/g, '\\|')}](${f}) |`;
});
const index = `# Official patch notes / GM Notes archive (NA/EU)\n\n` +
  `> Auto-archived by \`tools/patch-notes/run.sh\` (renders the JS-gated official news via the Playwright container). ` +
  `${files.length} articles, last ~${MONTHS_BACK} months. Re-run to pull new ones (incremental).\n\n` +
  `| Date | Type | Article |\n|---|---|---|\n${rows.join('\n')}\n`;
fs.writeFileSync(path.join(OUT, 'INDEX.md'), index);

console.log(`Done. saved=${saved} skipped=${skipped} total=${files.length}`);
await browser.close();
