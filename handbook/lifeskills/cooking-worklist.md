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

_(Balenos tree recipes get confirmed next.)_
