---
title: Master source catalog for Black Desert Online research
system: meta
source: seeded from general knowledge of long-standing BDO community resources
fetched: 2026-08-21
confidence: low   # SEEDED, NOT YET VETTED — verify every link is live and current before relying on it
---

# Source Catalog — Black Desert Online

The vetted list of where BDO facts come from. **This first pass is seeded from memory of
long-standing community resources and has NOT been link-checked** — treat it as a starting list to
verify, not confirmed sources. BDO is old and heavily patched, so the two failure modes to watch for
are **dead/renamed sites** and **stale guides** (top search hits are often years out of date).
Confirm each entry live, note what it currently covers, and mark it ✅ once checked.

**Legend:** ✅ = fetched & confirmed current; ◐ = live but JS-heavy / needs a browser; ⬜ = seeded,
not yet verified. All rows below are ⬜ until someone checks them.

## 1. Official (Pearl Abyss / publisher)

| Source | What it should cover | Status |
|---|---|---|
| ⬜ Official BDO site + **patch notes / update history** | The primary source for current mechanics and every balance change since Jon left. Region matters (NA/EU vs global lab/KR). **Highest-trust source — start here for anything that may have changed.** | verify URL for Jon's region |
| ⬜ Official news / event pages | Current events, catch-up campaigns, season timing, free-gear giveaways — directly relevant to re-onboarding. | verify |
| ⬜ In-game **Adventurer / character profile** (web) | Public character/gear lookup if profiles are set public — candidate for capturing Jon's gear. | confirm it still exists + what it exposes |

## 2. Databases / wikis (item, node, recipe data)

| Source | What it should cover | Status |
|---|---|---|
| ⬜ BDO Codex (bdocodex) | Long-standing item/quest/node/recipe/knowledge database. | verify live + current |
| ⬜ BDO Fandom wiki | General mechanics reference; **often stale — cross-check dates.** | verify |
| ⬜ BDOlytics | Market prices, item/node data, planners; more modern data site. | verify |

## 3. Tools / planners / calculators

| Source | What it should cover | Status |
|---|---|---|
| ◐ Garmoth | Gear planner (shareable codes), enhancement/failstack calc, node/worker and boss-timer tools. **Jon's main (Maegu) planner: https://garmoth.com/character/d690GifdPi.** **Fully Cloudflare-gated to automated tools (403 on page + API guesses, 2026-08-21) and a JS SPA — WebFetch/curl can't read it. Capture via screenshot** (or a rendered browser / Playwright if ever needed). | live, browser-only |
| ⬜ Famme's BDO tools (spreadsheets) | Community reference spreadsheets — enhancement, life-skill, profit data. | verify + check last-updated date |
| ⬜ Central Market price tools | Current prices to make market/profit calls. | verify (Garmoth/BDOlytics/official market web) |

## 4. Creators / guides / community

| Source | What it should cover | Status |
|---|---|---|
| ⬜ r/blackdesertonline (subreddit) | Current-meta discussion, returning-player threads, patch reactions — good for "what changed" sanity checks. | verify |
| ⬜ Reputable creators (life-skill + returning-player focused) | Prefer creators who **date their guides** and cover life-skilling; identify current ones (old guides mislead). | identify current names |
| ⬜ Grumpygreen / life-skill spreadsheets | Historically a strong life-skill/profit resource. | verify still maintained |

## How to use this list

- **For anything that may have changed in 2 years, official patch notes win.** Databases and creator
  guides are second, and only when dated.
- **A guide without a visible recent date is a hypothesis.** BDO's search results are full of
  pre-rework guides that read as current.
- Fill this out for real on the first research pass: check each link, mark ✅/◐, note current
  coverage, and add anything good that's missing (especially current life-skill/returning-player
  resources).
