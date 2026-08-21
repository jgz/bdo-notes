# Agent Instructions — Black Desert Online Notes

This repo is Jon's personal handbook and planning space for **Black Desert Online** (BDO, Pearl
Abyss). Jon is a **returning player**: a well-developed account with many high-level characters and
strong **life skills** (guru cooking, master-tier processing, lots of accumulated progress), but
**modest combat gear** — and he's been away ~2 years. Your two jobs: **research** the game's
current systems from primary sources, and **maintain** the handbook that turns that into a plan
Jon can run.

## The prime directive: NEVER GUESS

BDO is 8+ years old, patched constantly, and has been **substantially reworked** over time. Two
things make training-data memory dangerous here:

1. **The web is full of stale guides.** A top-ranked BDO guide can be years out of date — grind
   spots, gear tiers, silver/hour, enhancement odds, and whole systems have changed. A guide
   without a recent date is a hypothesis, not a fact.
2. **Jon has a 2-year gap.** Much of what he (and you) "know" about the game may have shifted.
   Assume any specific number or mechanic needs re-verification before it's load-bearing.

When answering anything about mechanics, gear, systems, silver, prices, or progression:

1. **Check the research packet first** — `research/` holds sourced, dated evidence.
2. **If it's not there, look it up live** — official patch notes, the current wiki/databases,
   reputable creators. Do not answer from memory alone.
3. **If it can't be verified, say so explicitly** — "I couldn't verify this" beats a confident
   wrong answer. Flag confidence and note conflicting sources.
4. **Check the `fetched:` date.** BDO rebalances often. A load-bearing number (a big enhancement
   attempt, a gear purchase, a grind-spot choice, a market play) older than a patch cycle should
   be re-verified before acting.

### Every claim carries a source AND a date. No exceptions.

An answer is one of exactly three things — say which:

1. **Sourced** — cite the file, the URL, the patch note, or the screenshot you read. A claim
   without a pointer is not an answer.
2. **Inference, labelled** — "X is probably Y *because* Z," plus what would confirm it. Never let
   a hypothesis wear the clothes of a fact. If confirming it is cheap, don't label it — go confirm.
3. **Unknown** — "I couldn't verify this." Always acceptable, always better than fabrication.

Plausibility is not evidence. That a mechanic worked a certain way two years ago, or works that
way in a similar MMO, or has a name that implies a behavior — none of these are sources.

**Screenshots are ground truth.** When Jon provides an in-game screenshot (gear, stats, inventory,
worker/node empire, life-skill levels), that beats any web source for his current account and
patch — record what it shows and the date.

## No "tracks" here — but the account is the anchor

Unlike the Aion 2 and Space Engineers notes (which split into separate tracks/worlds), BDO is a
**single live game on one account.** There's nothing to keep from mixing. The organizing anchor is
instead **Jon's account state** — his characters, gear, life skills, workers/nodes, and silver.
Advice only makes sense relative to that state, so keep `handbook/status.md` and the account pages
current, and reason from them.

## Optimize for Jon's actual profile

Jon is **life-skill-rich, gear-poor, and returning after a break.** Bias recommendations
accordingly:

- **Lead with his strengths.** Guru cooking (daily guru boxes), high processing, and accumulated
  CP/workers/nodes are real, bankable advantages — a returning-player plan should exploit them,
  not start from zero.
- **Least-grind path that moves the goal.** He never got deep into combat grinding. Prefer plans
  that reach a gear/silver goal with the least tedious grind, and say when a grind is genuinely the
  fastest route past a specific wall.
- **Re-onboarding first.** Before optimizing anything, a chunk of value is just *catching up*: what
  changed, what free catch-up gear/events exist now, and what's safe to ignore.

## Repo layout — TWO AUDIENCES, know which you're writing for

- `handbook/` — **the reader layer, written for Jon in plain language.** Every durable fact or
  correction lands HERE FIRST. Short sections, tables where they help, no context-dump style.
  - `handbook/status.md` — the **living snapshot**: account state, what Jon's doing now, priorities,
    open questions. Keep it current — it's the "where am I / what's next" page.
  - `handbook/systems-overview.md` — the **map of the territory**: every major BDO system and how
    they interconnect. The index the rest of the handbook hangs off.
  - `handbook/account/` — Jon's account: character roster, gear, silver, workers/nodes. Populated
    from what Jon exports/screenshots.
  - `handbook/lifeskills/` — the life-skill economy (cooking, processing, gathering, etc.) — Jon's
    strength, so a first-class section.
  - Other domain folders (gear/, economy/, grinding/, sailing/…) get created as we deep-dive them.
- `research/` — **the evidence layer.** Dense, sourced, dated files for verification and agent
  context. Each file carries `source:` / `fetched:` / `confidence:` frontmatter. The handbook cites
  these; they are NOT the reading layer. `research/sources.md` is the vetted source catalog — keep
  it current.
- `tools/` — fetch/refresh/calculation scripts as we build them (e.g. an adventurer/gear fetcher,
  profit calculators).

## Working style

- **Always commit AND push** to `origin` (github.com/jgz/bdo-notes) after any meaningful change —
  no need to ask. Jon reads these notes on the GitHub website, so unpushed work is invisible to him.
  This is just documentation; push freely. Commit straight to `main` for normal note updates;
  branch only for a large rework you want to review before it lands.
- **Research fan-out:** use cheaper sub-agent models (haiku/sonnet) for bulk source-gathering and
  scraping; save top-tier tokens for synthesis. Bring back sourced, dated notes into `research/`,
  then distill the durable version into `handbook/`.
- Prefer "here's the plan and why" over raw data dumps.

## Open setup questions (resolve as we go)

- **Region + platform** — which BDO region (NA / EU / SEA / …) and PC (assumed) — confirm.
- **How Jon exports his account** — screenshots, the official Adventurer profile, a Garmoth gear
  planner code, etc. Figure out the best capture method and whether any of it can be automated into
  `tools/`. (First priority once Jon shares his account.)
- **Repo visibility (public vs private)** — confirm before adding anything Jon considers sensitive.
