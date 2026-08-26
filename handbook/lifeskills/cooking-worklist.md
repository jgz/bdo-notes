# Cooking & processing worklist — Jon's canonical recipes + batching

> Started 2026-08-26. The goal: a glanceable, pre-computed worklist so Jon can tab into BDO mid-workday,
> pull the exact mats for the next full-weight batch, start it, tab back, and repeat — no thinking. Built
> collaboratively: each recipe's **actual** ingredient choice is confirmed with Jon (substitutes + which
> storage), then locked here as *his* version. Data: recipes/weights from bdo-cmd + game dump; stock from
> the holdings DB (`~/.bdo-cmd/holdings.db`, Velia captured 2026-08-26).

## Batching rules (agreed 2026-08-26)

- **Every batch fills the whole bag (~1,600 usable LT** = 1,822 max − ~150 baseline), capped only by
  stock on hand. **Overshooting demand is fine** (a full Confit batch = weeks of supply → good).
- **One batch per recipe, no back-to-back repeats.** Demand sets *priority/order*, not batch size.
- **Order = dependency:** processed intermediates → cooked sub-components → final meal.
- **Mastery ~2× output** (~1,400 cooking, [mastery-yield.md](mastery-yield.md)) → a batch yields ~2× the
  crafts; overshoot even more, fewer future sessions.
- Cooking a full bag runs ~10–15 min before mats exhaust; processing a full bag ~30–45 min.

## Ingredient source legend

🌾 Farmed · 🏭 Worker/node (may live in another storage) · 🏪 Vendor (bulk-buy, keep stocked) ·
⚙️ Processed (has its own prereq step) · 💰 Bought off market · ⚠️ not in Velia (elsewhere / gap)

**⚠️ Velia ≠ full stock.** Only Velia is captured so far; an item absent from Velia may sit in another
storage (e.g. Cinnamon in Tarif). Stock caps use *known* (Velia) counts; cross-storage items are noted
from Jon until those storages are captured.

## Vendor materials (keep bulk-stocked; shopping list auto-checked from holdings)

**Salt · Sugar · Leavening Agent · Mineral Water · Deep Frying Oil · Olive Oil · Cooking Wine · Base
Sauce · Spring Water · Raw Sugar.** Reorder threshold ~10k (Jon buys 20–30k/run). _Current low (Velia,
2026-08-26): Mineral Water (7.6k), Base Sauce (4.8k), Sugar (4.3k)._

---

## Confirmed recipes

### ✅ Carrot Confit (9321) — weekly training quest → Mythical Feathers (for Courser awakening)
Per craft (~0.98 LT/craft → ~1,630 crafts fills the bag):
| Qty | Ingredient | Source |
|--:|---|---|
| 2 | Special Carrot (54005) | 🌾 Farmed (magical carrot seeds) — Special only, regular carrots don't work |
| 4 | Cinnamon (7348) | 🏭 Node → **Tarif storage** (~31k) ⚠️ not in Velia |
| 3 | Lump of Raw Sugar (54003) | ⚙️ Processed: **10 Raw Sugar + 1 Mineral Water** (HEAT). Also wild-horse capture bait → keep a buffer |
| 6 | Mineral Water (9059) | 🏪 Vendor |
| 2 | Salt (9001) | 🏪 Vendor |

_Prereq: process Lump of Raw Sugar first (Velia has 499 + 47k Raw Sugar = ~4,700 Lumps of headroom)._

### 🎯 Substitution rule (Jon's optimization heuristic, 2026-08-26)
Most cooking ingredients have **alternates**, and Jon has access to nearly all of them — so the choice is
"**use the substitute backed by the most node throughput.**" Current standing choices:
- **Pumpkin** wherever Cabbage is called for (most pumpkin nodes; ~19k across Calpheon/Heidel/Velia).
- **Wheat** (→ Wheat Flour → Wheat Dough) over Potato (most wheat nodes). _(Wheat-vs-Potato value math TODO.)_
- **Meat** = the **hunted/butchered meat group** (Rhino/Bear/Wolf/Deer/…), NOT Chicken — uses whatever's
  stocked. (Chicken Meat is only for Grilled Bird Meat below.)
- **Fish** = any — Jon picks from node/market stock. Until storages are captured, the worklist gives the
  **quantity needed** and Jon fills it from whatever he has.

_This substitution optimization (which alternate per node throughput) is where a future tool could help —
for now, the heuristic above is the rule._

### ✅ Balenos Meal tree (9601) — Jon's confirmed recipes
Per craft. **Balenos Meal** = 1 Cheese Gratin + 1 Meat Croquette + 1 Smoked Fish Steak + 2 Stir-Fried Veg + 2 Beer.

| Recipe | Ingredients (per craft) | Notes |
|---|---|---|
| **Meat Croquette** (9404) | 8 **Meat**(hunted) · 5 Wheat Flour · 2 Cheese · 2 Egg · 4 Deep Frying Oil🏪 | meat = hunted group, uses stock |
| **Grilled Sausage** (9427) | 6 **Meat**(hunted) · 1 Onion · 2 Salt🏪 · 2 Pepper | |
| **Smoked Fish Steak** (9417) | 1 **Fish**(any) · 2 Salt🏪 · 1 Olive Oil🏪 | Jon fills fish from stock/market; 52k already made |
| **Cheese Gratin** (9203) | 5 Wheat Dough⚙️ · 4 **Pumpkin**🌾(subs Cabbage) · 1 Grilled Sausage · 3 Cheese⚙️ · 3 Red Sauce⚙️ | |
| **Stir-Fried Veg** (9241) | 5 **Pumpkin**🌾(subs Cabbage) · 2 Olive Oil🏪 · 2 **HQ Hot Pepper** · 1 Salt🏪 | HQ Hot Pepper = **downgraded** from Special (NPC) — maintenance reminder |
| **Beer** (9213) | 5 Wheat🏭 · 6 Mineral Water🏪 · 2 Leavening Agent🏪 · 1 Sugar🏪 | |
| **Red Sauce** (9004) ⚙️craft | 1 Base Sauce🏪 · 1 **Meat**(hunted) · 2 Mineral Water🏪 · 2 Sugar🏪 | Jon crafts it (not vendor/market) |
| **Wheat Flour** (7101) ⚙️grind | 1 Wheat🏭 | over Potato Flour |
| **Wheat Dough** (7201) ⚙️shake | 1 Wheat Flour · 1 Mineral Water🏪 | over Potato Dough |
| **Cheese** (9062) ⚙️dry | 1 Milk🏭 | |

**Meat is consumed in Croquette (8) + Sausage (6) + Red Sauce (1)** — the hunted-meat group, **bought off
market** (Jon's known recurring cost). Uses whatever's stocked (Velia: Rhino 8.6k, Bear 3.2k, Wolf 639).

### Side products (worker/pet food — keep a small stockpile, not bulk)
- **Grilled Bird Meat** (9492) — worker food. 2 **Chicken Meat** · 6 Deep Frying Oil🏪 · 2 Cooking Wine🏪 ·
  1 Salt🏪. Velia has 33.8k — keep topped up.
- **Organic Feed** (54018) — pet food, keep ~1,000. 2 dried fish · 5 Meat · 1 Mudskipper · 4 Chicken Meat.

### Maintenance reminders (feed the recipes above)
- ⚙️ **Process Lump of Raw Sugar** (Confit + wild-horse capture bait).
- 🌶️ **Downgrade Special Hot Pepper → HQ Hot Pepper** at the NPC (for Stir-Fried Veg).
- ⚙️ Keep **Wheat Flour / Wheat Dough** and **Cheese** processed ahead of the sub-components that need them.

### The 4-stream dashboard (the deliverable)
For each work cycle, generated from demand targets + current stock:
1. 🌾 **Farm** — plant priority (Special Carrot, Special Hot Pepper→downgrade, Onion; Pumpkin is worker-node)
2. ⚙️ **Process** — Wheat Flour/Dough, Cheese, Red Sauce, Lump of Raw Sugar (full-bag batches)
3. 🏪 **Vendor** — bulk-buy shopping list (threshold ~10k)
4. 💰 **Market** — hunted meat (+ fish as needed)
   → **Cook** — sub-components → Balenos Meals; Carrot Confit; side products. Full-bag batches, one each.
