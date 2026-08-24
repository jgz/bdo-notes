# bdo-cmd — design & build plan

> Last updated: 2026-08-23. The plan for the BDO tool. This lives in **bdo-notes** (the documentation +
> agent-working repo); the tool itself is a **separate repo**. This doc is the reference we cut issues
> from.

## Purpose

A **private CLI tool** that wraps the **official BDO Central Market API** + deterministic game-logic
workflows. Agents (Claude working in `bdo-notes`) call it — **JSON on stdout** — to answer "what should
I do with X." The tool is the deterministic backbone; the agent is the driver.

## Repos & workflow

- **`bdo-cmd`** — the tool. **Jon's personal GitHub, private**, checked out at `~/projects/jgz/bdo-cmd`
  (sibling of `bdo-notes`). Poetry src-layout package, **AWK-installed**, TDD. Owns the tool's
  **structured data** (item maps, enhancement/pity/cron tables, recipes, market cache, inventory).
- **`bdo-notes`** (this repo) — **documentation + Jon's agent-working repo.** Human-readable game
  knowledge; where Jon works with agents; the **source of issues** for `bdo-cmd`. Consumes `bdo-cmd`.
- **Dev flow:** changes to `bdo-cmd` come in as **GitHub issues** → developed by a separate **AWK
  repo-manager agent** (test-writer → implementer → reviewer → finalize), one vertical slice per PR,
  gated by `.awk-cmd.json` `validate.checks`. Jon owns direction/merge. This session (in `bdo-notes`)
  helps design, seed issues, and *use* the tool — not hand-build it.

## Architecture (mirrors `pmt-api-cmd`)

3-layer, strict boundaries. Stack: **Typer + Rich + httpx + pydantic-settings + tenacity; ruff +
pytest (+pytest-httpx)**; Python 3.12; console script `bdo-cmd`.

```
bdo-cmd/ src/bdo_cmd/
  clients/market/     # official Central Market API (na-trade.naeu…): httpx, tenacity retries, RATE_* consts, factory
  services/
    market/           # price normalization, item lookup
    enhance/          # THE math: expected_attempts, failstack_value, optimal_fs, upgrade_cost  ← pure, TDD
    inventory/        # value holdings, sell/process/break/use decisions
    recipes/          # "what can I make", processing profit
  commands/           # thin Typer, mirrors services; registered in cli.py
  config/ models/ output/ exceptions/ utils/
  data/               # awk-data-store YAML (store-config.yaml): game/ (item map, chance curves, pity, cron), market/ (cached snapshots), inventory/
  tests/ (mirror src, pytest-httpx — never live)   docs/ (CONTEXT, adr, architecture, commands, workflows)
  .awk-cmd.json .claude/   # AWK install (tooling Poetry group + awk-install; CodeArtifact token flow)
```

**Agent contract (non-negotiable):** every data command defaults `--output json`, **structured data on
stdout, logs/progress on stderr**, `--quiet/--verbose` don't touch stdout. That's what makes it
agent-consumable.

## The payoff workflows

> ⭐ **North star (Jon, 2026-08-24):** *"I can never find a good tool for estimating the cost of buying
> stuff off the market and then crafting it with the different workshops using workers and then selling
> it."* Jon has the basic life-skill loops mastered for years (Imperial Balenos cooking at the 800k box
> cap, gathering empire). His actual interest is the **advanced production economy** — **workshop
> crafting profit, market arbitrage, and enhancing for profit.** Workflow #4 below is *the* thing.

1. **`enhance upgrade-path`** — ranked upgrades like Garmoth, but **personalized**: prices *Jon's* Crons
   / Advice of Valks / self-produced mats at **$0 (or opportunity cost)**, so the ranking reflects his
   *real* cost, not market. This is the thing a generic site can't do.
2. **`inventory cleanout-plan`** — value years of node mats + event/quest items (Jon's stockpile from a
   ~200–250 CP gathering empire) → **sell / process-then-sell / break-down / use** recommendations.
3. **`recipes can-make` / processing profit** — what's profitable to make, and what he can make with
   what he already holds.
4. **⭐ `craft profit` — workshop crafting profitability.** For a craftable item: **input cost** (buy
   mats at Jon's real buy-order price via `market orders`) + **workshop/worker process** (which workshop,
   worker time/labor) → **output value** (sell at realistic price) ⇒ **margin & profit/hour**. Covers
   worker-crafted goods, not just Processing(L). This is the tool Jon has never been able to find, and
   the main reason to build bdo-cmd. Also feeds **arbitrage** (buy raw → convert → sell) and
   **enhance-for-profit** (buy base → enhance → sell, using the enhance math + order-book pricing).

> ⚠️ **Reality check — the tool is a SCREENER, not a money printer (community consensus + Jon's prior).**
> In BDO, **most crafting/processing/flipping is marginal-to-unprofitable when you buy the inputs**:
> finished goods often sell for *less* than their mats (classic example: a boat deco sells ~400k vs ~1.4M
> in mats → sell the raws); processing margins are thin (~8% seen) unless the mat was free or demand is
> real; and flipping is gutted by the **±7.5% price band + 35% tax** (65% payout, 84.5% w/ Value Pack).
> The genuinely profitable loops **bypass market pricing**: Imperial cooking/alchemy (NPC pays **250%**),
> selling **free worker-gathered raws**, and a few price-sensitive niches. **So `craft profit`'s most
> common correct answer is "don't craft — sell the raws," and its value is catching the rare positive
> margins + steering the stockpile to `cleanout-plan`/NPC loops.** Build it as a make-vs-buy-vs-sell-raw
> filter, not a "get rich crafting" engine. _(Sources: Steam/BDO forums, GrumpyG/Eminent processing,
> official CM tax/band rules — 2026-08-24.)_

### Worked example — Forest Path Wagon Wheel (first live test-case, 2026-08-24)

The tool surfaced this instantly via `item recipe 53411` + `market prices`/`orders` — and it's the
perfect illustration of the reality check.

- **Looks like a goldmine:** sells at the **800M cap**, order book = **26 buyers / 0 sellers** (real
  demand, no supply).
- **Recipe:** 30 Loopy Tree Timber + 60 Steel + **1000 Piece of Image**. Piece of Image (Simple Alchemy,
  →150) = **1 Merindora's Element** (non-tradable, ~2/day) + 100 Weeds + **300 Trace of Nature**. So one
  wheel ≈ 7 Merindora's Element + ~700 Weeds + **~2,100 Trace of Nature**.
- **Cost is ~all Trace of Nature:** ~2,100 × **286k ≈ 601M** = **98%** of the ~610M input cost.
- **After 35% tax:** net **676M** (Value Pack) / **520M** (none). Buying mats → **~+66M w/ VP, ~−90M
  LOSS without** = a wash. Self-gathering Trace → profitable, but **selling that Trace raw nets ~508M
  anyway**, so crafting adds only ~159M for the Merindora time-gate + labor.
- **Verdict:** the 800M is an illusion — it's just ~600M of Trace of Nature funneled through the recipe.
  The scarcity/demand exists *because* it's a gated, unprofitable-to-mass-produce craft, not free money.
- **Jon's takeaway:** keep such setups for **personal-use** items (make/enhance the wheels he wants),
  then **shut it down and reclaim the CP** for the passive node empire (the actually-profitable play).

## The two hard problems

1. **Enhancement success curves** — the math is only as good as `p(gear, level, failstack)`. We have
   data points + pity thresholds; we need the full curves. **Approach:** gather published tables
   (famme's / datamine / Garmoth sim) into `data/game/`, then **calibrate/validate against Garmoth's
   displayed costs** (Jon's screenshots are ground-truth targets). Prerequisite for the enhance slice.
2. **Inventory (no API)** — market is public; personal storage is not. **Decision: OCR command.**
   `bdo-cmd inventory scan <screenshot>` → reads the inventory grid (icon-matching against BDO item
   icons + stack-count OCR) → inventory records. Its own slice with real R&D; manual/screenshot entry
   is the interim fallback.

## Slice roadmap (vertical, TDD, one PR each)

- **S0** — bootstrap ✅ **DONE (2026-08-23)** → **[github.com/jgz/bdo-cmd](https://github.com/jgz/bdo-cmd)**
  (private). Poetry src-layout, Typer skeleton, 3-layer dirs, output contract, config (NA), exceptions,
  baseline tests (ruff+pytest green), `.claude/` agents+skills + `.awk-cmd.json` + AGENTS.md, AWK tooling
  group wired to CodeArtifact. Issues #1 (agent-ready) … #5 filed. **Remaining Jon step:** `poetry
  install` with CodeArtifact creds → run `awk-install` skill → start the repo-manager on issue #1.
- **S1** — market client + `market price <item>` → JSON. *Proves API access + agent contract.*
- **S2** — item-ID map + `market search <name>`.
- **S3** — enhance data (curves/pity/cron → `data/game/`) + `enhance cost` / `optimal-fs` (TDD,
  validate vs Garmoth). _Seed cron/pity/recipe data from the bdo-notes work._
- **S4** — inventory model + **OCR `inventory scan`** + `inventory value`.
- **S5** — workflows: `enhance upgrade-path` (personalized), `inventory cleanout-plan`, `recipes can-make`.

## Open items

- **Personalization order:** match Garmoth's market-priced numbers first (for validation), *then* layer
  in Jon's $0-Cron/mat pricing. (Recommended.)
- **AWK install** needs Jon's `pmt` CodeArtifact token flow (AWS creds) — a Jon step at S0.
- Data source-of-truth: cron/pity/recipe tables exist as prose in `bdo-notes`; the tool's `data/game/`
  is the machine-readable copy — accept mild duplication, or later generate one from the other.
