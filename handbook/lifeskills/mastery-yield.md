# Life Mastery → yield multiplier (where crafting "profit" actually comes from)

> Last updated 2026-08-24. Jon's observation — *"the profit is the mastery; high cooking mastery makes
> way more than the recipe says"* — is exactly right and quantifiable. Numbers below are the **authoritative
> per-bracket curves straight from the NA client** (`mastery.json` → `{cooking, alchemy, processing}`),
> the same data BDOlytics' mastery calculator runs on. Column meanings interpreted + cross-checked against
> the known community figure (~2.5× cook yield at 2000 mastery).

## The point

Mastery does **not** change the recipe inputs — it multiplies the **output** per craft. Same mats in,
~2× the items out. That's why crafting is profitable **when you self-supply** (free/cheap worker mats,
doubled) and still a wash when you buy mats at market (the multiplier applies, but market mats already
cost more than the sell price). Mastery is the lever; cheap inputs are the fuel.

## Cooking (Jon: ~1,400 mastery unbuffed → ~2.05× per cook)

Average items per cook = **1 + `rates[4]`** (the bonus-yield coefficient); rare proc = **`rates[2]`**
(chance of the higher-grade dish, e.g. *Chewy* Cheese Gratin instead of Cheese Gratin).

| Cooking Mastery | Avg yield ×/cook | Higher-grade proc |
|--:|--:|--:|
| 0 | 1.00× | 0% |
| 500 | 1.21× | 2.0% |
| 1,000 | 1.67× | 5.8% |
| 1,250 | 1.96× | 8.4% |
| **1,400 (Jon)** | **2.05×** | **10.2%** |
| 1,500 | 2.11× | 11.6% |
| 1,750 | 2.28× | 15.2% |
| 2,000 | 2.45× | 19.4% |
| 2,500 | 2.63× | 21.8% |
| 3,000 | 2.81× | 24.2% |

So at 1,400 mastery Jon gets **~2 Balenos-meal components per cook** for one recipe's inputs — that's the
"more than it says" effect. Pushing mastery higher keeps raising it (diminishing but real), and the rare
proc climbs too. Mastery can exceed the table's 3,000 with food/gear buffs (curve caps at 3,000).

## Processing (same mechanic, two levers)

- **Yield ×** = 1 + `procRate` — the chance of a bonus item per unit processed. Climbs fast then plateaus
  near **~1.97×**.
- **Batch** = how many units one mass-process action consumes (throughput / clicks saved), **10 → 315**.

| Processing Mastery | Avg yield × | Batch (per action) |
|--:|--:|--:|
| ~1 | 1.00× | 10 |
| 500 | 1.71× | 35 |
| 1,000 | 1.88× | 85 |
| 1,400 | 1.94× | 162 |
| 2,000 | 1.96× | 250 |
| ~3,000 | 1.97× | 315 |

Processing hits ~1.9× yield by ~1,000 mastery — most of the *yield* gain is early; past that you're
mainly buying **throughput** (bigger batches = less clicking for the same volume).

## Why this matters for the money question

- **Confirms the craft-profit reality check** ([bdo-cmd-plan](../../research/bdo-cmd-plan.md)): the real
  margin is the mastery multiplier applied to **near-free self-supplied inputs**. Buying mats at market
  and reselling the craft stays a wash — the ~2× doesn't beat the market's own markup + tax.
- **A nuance to bank for the eventual `craft profit` tool — not to build yet.** Any real profit calc must
  use **real yield = recipe output × mastery multiplier**, not the raw recipe number, or it undercounts
  cooking/processing output by ~2×. The curve data is in `~/.bdo-cmd/dumps/mastery.json`. Per Jon's
  build sequence (data commands first; reason out the nuances with the data before crystallizing logic),
  this stays **agent-reasoned for now** — captured here, not filed as a build issue.
- **Imperial cooking:** the ~2× cooking yield is *the* reason the Balenos box loop stays cheap — one
  batch of worker mats makes roughly twice the meals the recipe implies. See
  [balenos-cooking.md](balenos-cooking.md).

_Source: NA client `mastery.json` (2026-08-24). Column mapping interpreted (cooking `rates[4]`=avg bonus
yield, `rates[2]`=rare proc; processing `procRate`=bonus chance, `batch`=throughput) and cross-checked
against community-cited yields. BDOlytics' mastery calculator is the definitive online quantifier and
uses the same bracket data._
