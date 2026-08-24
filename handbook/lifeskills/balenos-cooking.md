# Balenos Meal — Imperial cooking loop (full audit)

> Last updated 2026-08-24. The complete recipe tree for Jon's Imperial-delivery income loop, sourced
> from `bdo-cmd item recipe` + `market price` (NA, prices are base / last-sold, 2026-08-24). Jon is
> **Cooking Guru ~1,400 mastery**; boxes sell for **exactly 800k** at the Imperial Delivery NPC.
> Reference — see [overview.md](overview.md) for where this sits in the wider empire.

## The loop in one line

**24 Balenos Meals → 1 Guru's Cooking Box → 800,000 silver (NPC, no market tax).**

- **Box (Guru's Cooking Box, id 9856)** ← 24× Balenos Meal (recipe `9856:8`). Bulk variants just save
  clicks: **+1 Heavy Duty Packaging Cord (8198) per 10 boxes** (240 meals, `9856:39`); **+10 Cord + 1
  Black Stone Powder per 100 boxes** (2,400 meals, `9856:70`). The cord is the only "extra" item.
- **Why box instead of selling meals:** NPC pays **33,333/meal** (800k ÷ 24), tax-free. Selling the meal
  on the CM (31,500 last-sold) nets only **20,475** (×0.65 tax) / 26,617 with Value Pack. Boxing wins by
  25–60% **and** doesn't flood the market. This is the whole reason the loop exists.
- **Daily throughput:** ~**184 boxes/day** (CP-gated, ≈ half of Jon's 369 CP) = **~147M/day**, needing
  ~4,416 meals/day. Hence "one day of crafting = ~2 weeks of deliveries."

## The Balenos Meal (id 9601) — recipe `9601:0`

One meal = **5 cooked sub-components** (not raw mats — you cook these first):

| Qty | Sub-component | id | Market (base/last) |
|--:|---|--:|--:|
| 1 | **Cheese Gratin** | 9203 | 48,400 / 51,500 |
| 1 | **Meat Croquette** | 9404 | 47,000 / 50,500 |
| 1 | **Smoked Fish Steak** | 9417 | 5,350 / 5,700 |
| 2 | **Stir-Fried Vegetables** | 9241 | 7,650 / 8,050 |
| 2 | **Beer** | 9213 | 3,050 / 3,270 |

_(Recipe variant `9601:1` swaps Cheese Gratin → **Chewy Cheese Gratin** (9282) — the higher-grade proc
of the same recipe; either makes a standard Balenos Meal.)_

## Sub-component recipes → raws

| Sub-component | Recipe (raw inputs) |
|---|---|
| **Cheese Gratin** (9203) | 5 Wheat Dough (7201) · 4 Cabbage (7318) · 1 Grilled Sausage (9427) · 3 Cheese (9062) · 3 Red Sauce (9004) |
| **Meat Croquette** (9404) | **8 Meat** (any, see below) · 5 Wheat Flour (7101) · 2 Cheese (9062) · 2 Egg (9064) · 4 Deep Frying Oil (9016) |
| **Smoked Fish Steak** (9417) | **1 Fish** (any, see below) · 2 Salt (9001) · 1 Olive Oil (9015) |
| **Stir-Fried Vegetables** (9241) | 5 Cabbage (7318) · 2 Olive Oil (9015) · 2 Hot Pepper (7305) · 1 Salt (9001) |
| **Beer** (9213) | 5 Wheat (7001) · 6 Mineral Water (9059) · 2 Leavening Agent (9005) · 1 Sugar (9002) |

**Meat & fish are substitution groups — buy the cheapest.** Confirmed from the dump (`recipes.json` +
item descriptions, 2026-08-24): the recipe count is **fixed** — **8 meat** / **1 fish** — regardless of
type; only the item swaps (the "Select Material" popup just re-prices the same slot). Cheapest legal fill
wins.

- **Meat Croquette accepts 15 meats** (Pork's "Alternative Ingredient" list — *not* the whole "Meat"
  market subcategory, which mixes in unrelated cooking groups like Chicken/Whale). Live cheap cluster
  (base price, 2026-08-24): **Rhino 26,100 · Weasel 26,300 · Rock Elephant 26,700 · Bear 27,400 · Deer
  28,800 · Beef 28,600 · Goat 28,100.** Mid: Pork 30,700 · Wolf 31,300 · Rabbit 31,500 · Fox 31,900.
  Outlier: **Gazelle ~46k (avoid).** → run standing buy orders on the **~26–28k cluster** (Rhino /
  Weasel / Rock Elephant / Bear / Deer), take whatever fills.
- **Smoked Fish Steak accepts fish broadly** (Fish category; recipe rep = Mudskipper). Only **1 per
  meal**, so it's a rounding error next to the 14 meat — any cheap common fish is fine. Fish is also
  **worker-producible** (Mudskipper `gatheredFrom`: Fish Net / Fish Drying Rack), so his coastal workers
  can feed this slot directly.

**Jon's workflow:** keep **standing buy orders on several cheap meats + fish at once** (the CM caps
per-order quantity), relist-to-collect when filled, pull from the market warehouse when cooking.

### Crafted intermediates (cook these *before* the sub-components)

| Item | id | Recipe | Type |
|---|--:|---|---|
| **Wheat Flour** | 7101 | 1 Wheat (7001) | Grind |
| **Wheat Dough** | 7201 | 1 Wheat Flour (7101) + 1 Mineral Water (9059) | Shake/mix |
| **Cheese** | 9062 | 1 Milk (9065) | Dry/heat |
| **Grilled Sausage** | 9427 | 6 Pork (7905) · 1 Onion (7303) · 2 Salt (9001) · 2 Pepper (7301) | Cook |

## Where every raw comes from (Jon's setup)

| Source | Items |
|---|---|
| 🏭 **Workers** (his empire) | Wheat (7001), Cabbage (7318), Egg (9064), Fish (worker/coastal nodes) |
| 🌾 **Farmed** (his crop plots) | **Hot Pepper (7305)**, **Onion (7303)** |
| 💰 **Bought — meat + fish** | **Cheapest of the meat group** (~26–33k) + **fish** — standing buy orders on several types, pulled from warehouse. His main recurring silver cost. |
| 🥛 **Milk (9065) → Cheese** | **Free.** Jon takes **Milk as the daily Imperial Delivery quest reward** and has a **25,000+ stockpile** → make Cheese from his own milk (do **not** buy Cheese). |
| 🏪 **Vendor** (cooking NPC, ~trivial) | Salt (9001), Pepper (7301), Sugar (9002), Leavening Agent (9005), Mineral Water (9059), Olive Oil (9015), Deep Frying Oil (9016), Red Sauce (9004 — also on CM ~9.25k), Heavy Duty Packaging Cord (8198) |

## Cost notes (from the 2026-08-24 price pull)

- **Meat is the one real silver cost.** Per meal you burn **14 meat** (8 in Croquette + 6 in Sausage) —
  everything else Jon self-supplies or buys from a vendor for pennies. Buy the **cheapest of the meat
  group** (Weasel ~26.3k beats Pork ~28.6k), via standing buy orders. Fish (1/meal) is trivial by
  comparison. The loop's margin *is* "workers/farm cover the rest; I only pay for meat."
- **Make Cheese from your milk stockpile — it's free.** Jon banks Milk daily from the Imperial quest
  (25k+ on hand), so making Cheese costs nothing. _(Buying Cheese at 14k only beats buying Milk at 23k —
  irrelevant when the milk is free. Don't buy either.)_
- **Grind your own flour/dough.** Wheat Flour and Wheat Dough both sell at **4,190** vs Wheat at
  **2,410** — from worker wheat, grinding/shaking is ~free and roughly halves the cost vs buying dough.
  If you must buy, buy **Flour**, not Wheat+grind (same price, saves the step).
- **Never buy the sub-components at market.** At market prices the mats for one meal (~650k+) dwarf the
  33.3k box value — the loop is only profitable because the inputs are worker-gathered/farmed and
  **1,400 mastery multiplies output ~2.05× per cook** ([mastery-yield.md](mastery-yield.md)), so a stack of free wheat/cabbage/eggs stretches
  across thousands of meals.

## Build order (batch-cook top to bottom)

1. **Wheat Flour** (grind worker Wheat) → **Wheat Dough** (Flour + Mineral Water)
2. **Grilled Sausage** (Pork + farmed Onion + vendor Salt/Pepper)
3. **Cheese** — dry it from the free Milk stockpile
4. The **5 sub-components** (Cheese Gratin, Meat Croquette, Smoked Fish Steak, Stir-Fried Vegetables, Beer)
5. **Balenos Meal** (24 → 1 box)
6. **Guru's Cooking Box** → hand in at the **Imperial Crafting Delivery** NPC (800k/box, CP-capped/day)

## To finish the audit — what Jon still needs to supply

The "what do I already have" column needs Jon's **cooking-storage / inventory** (screenshot). With that,
this becomes a shopping list: how many of each intermediate + raw are on hand vs needed for a target
box count, and which sub-components to batch first.
