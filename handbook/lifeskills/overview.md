# Life Skills: Overview

> Last updated: 2026-08-24. Levels/mastery captured; Imperial loop + worker empire documented below.

Life skills are **Jon's strongest axis** and the intended engine to fund everything else on a
gear-poor account. This page is the hub for the life-skill economy; each skill gets its own deep-dive
page as we work it.

**Life skills are account-wide (Family-wide), confirmed by Jon (2026-08-21).** They're no longer
tied to one character, so the life-skill grind runs off whichever character is convenient — in
practice **JGZ (Corsair)**, the original life-skill character, sits parked in **Heidel** doing the
cooking/processing loops. Any character can pick up the life-skill work.

## Levels + Life Mastery (in-game, 2026-08-21)

From the life-skill page ([evidence](../../research/account/2026-08-21-lifeskills.png)). Rank ladder:
Beginner → Apprentice → Skilled → Professional → Artisan → Master → Guru.

| Skill | Rank | Mastery | Note |
|---|---|---|---|
| **Cooking** | **Guru 1** | **~1,400** | With life gear (Jon, 2026-08-24) — the effective number; 555 was level-only. Guru boxes at the **800k cap** (maxed). |
| **Fishing** | **Master 21** | **505** | Highest *rank* on the account; low-attention income |
| **Processing** | **Master 8** | **440** | Sub-skills all 440 (shaking/grinding/chopping/drying/filtering/heating) |
| **Farming** | Artisan 9 (98.6%) | 395 | Basically about to hit Master; feeds cooking/alchemy |
| **Training** | Artisan 7 | 389 | Horse training — the AFK-training goal (see [status](../status.md)) |
| **Hunting** | Artisan 4 | 370 | Whales / matchlock |
| **Gathering** | Professional 8 (68.3%) | 330 | Sub-skills all 330; feeds processing/alchemy |
| **Alchemy** | Skilled 3 | 180 | Weakest of the "useful" skills — headroom for elixir/guru-box income |
| **Trading** | Apprentice 3 | 80 | Low; imperial delivery still works regardless |
| Sailing | Beginner 7 | 35 | Barely started |
| Barter | Beginner 1 | 0 | Not started |

**Shape of it:** cooking (Guru), fishing (Master 21), and processing (Master 8) are the mature,
bankable skills; farming/training/hunting are Artisan and close behind. Alchemy, trading, sailing,
barter are the undeveloped tail. Jon's self-description ("guru cooking, high Master processing")
checks out exactly.

## The Imperial Cooking loop (SOLVED — Jon has run this for years)

> **Full recipe tree + sourcing audit → [balenos-cooking.md](balenos-cooking.md).**
> **Weight Limit is the cooking bottleneck — free-first plan → [weight-limit.md](weight-limit.md).**
> **Why crafting pays when self-supplied: mastery ≈ 2× yield → [mastery-yield.md](mastery-yield.md).**

- Meal = **Balenos**. Guru's Cooking Boxes turn in at **800k each** (the Imperial NPC pays 250% of box
  value; **800k is the cap**, already hit at 1,400 mastery → more cooking mastery won't raise box income).
- Imperial delivery is **once/day**, **CP ÷ 2 boxes** → Jon turns in **184/day** (369 CP).
- One day of crafting while working ≈ **2 weeks** of Imperial deliveries. Prep is fast → this loop is
  "done", not where Jon's interest is.

## Worker / CP empire (Jon, 2026-08-24)

- **369 total CP.** ~**200–250 CP** of workers out **gathering**; **all the most expensive nodes worked**.
- **Mostly Artisan workers** (not fully min-maxed).
- Most gathered materials are **stockpiled, unused** (years of node mats sitting) → the `inventory
  cleanout-plan` target.
- Dedicated worker loop for **Forest Path Wagon mats** (e.g. Knot Wood).
- **Balenos ingredient setup:** workers gather everything except the **farmed** items (hot peppers,
  onions — Jon farms those); only **meat** is bought off market.

## Direction: advanced money-making (the real interest, 2026-08-24)

Jon has the basic loops solved (Imperial cooking, gathering). What he actually wants is the **production
economy**: **enhancing for profit, market arbitrage, and buy-mats → worker-craft in workshops → sell.**
He's never found a good tool to estimate **workshop crafting profit** → that's the **north-star use case
for `bdo-cmd`** (see [research/bdo-cmd-plan.md](../../research/bdo-cmd-plan.md)).
