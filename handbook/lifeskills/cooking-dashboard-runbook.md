# Runbook — how to (re)build `cooking-dashboard.md`

Purpose: this is the **build spec + checklist** so the dashboard is regenerated the same way every time and
**no section gets dropped**. Follow it in order. Data: `~/.bdo-cmd/holdings.db` (all storages), recipes/pulls
from [cooking-batches.md](cooking-batches.md), Jon's substitutions from [cooking-worklist.md](cooking-worklist.md).

## Required sections — the dashboard MUST have all of these, in this order
1. **🏪 Buy first** — vendor mats the queues will consume that are below stock. 2-col table `Item | Buy to`.
2. **⚙️ Processing queue** — fire & forget. Ordered: recipe-short first, then surplus-convert.
3. **🔪 Cooking queue** — one queue, ordered by dependency/priority. **Carrot Confit lives here** (see gate).
4. **🌾 Farm today** — hand-farmed crops ranked lowest-stock first.

If any of the four is missing, the file is wrong. Check them off before committing.

## Format rules (non-negotiable — Jon reads this glanceably on GitHub)
- Every batch = a **2-column table: `Ingredient | Qty`**. Nothing else per card (no LT, no yields, no prose).
- **No "rotation watch" / runway / prereq-watch sections.** Deciding what's short and ordering the queue is
  Claude's job — show only the batches to actually make.
- Italic one-liner after a card title is allowed **only** to state the driver/stock (e.g. _have 499_).

## Data & sizing
- No `sqlite3` CLI on this box — query via `python3` + `sqlite3` module. Stock = `SUM(quantity)` across all
  locations for the item_id.
- Batch = **full bag (1,600 LT)** sizes from the batch book. Mastery ~2× output does **not** change pulls.
- **EVERY batch — cook AND process — is ALWAYS the full bag size from the batch book.** Never shrink to
  current stock, never size to the consumer's need. Overshoot is the goal: process/cook once, don't repeat
  for months. If Jon is short an input, the queue implies he **buys/farms up to the full batch** first
  (e.g. Lump = full 14,545 crafts / 145,450 Raw Sugar — buy the raw sugar, it's cheap; Confit = full 1,632
  crafts / 3,264 Special Carrot — farm the rest). Note the shortfall in the card's italic if useful, never
  downsize. Vendor mats are cheap and overshoot costs ~nothing, so full batch always wins on fewer reps.
- Pull quantities in tables come straight from the batch book (or scaled to need — see rules below).

## Priority rules
- **Processing queue order:** (A) intermediates SHORT for what the cooking queue will consume
  (Lump→Confit, Wheat Dough / Red Sauce → Cheese Gratin, etc.), then (B) convert big raw surpluses
  (grain→Flour/Dough, milk→Cheese). "Short" = have < one full consumer batch's need.
- **Cooking queue order:** vendor/processing prereqs handled above, then Beer/subs that are short, then
  **Balenos Meal**, then **Carrot Confit** if the quest gate trips.
- **Carrot Confit gate:** weekly training quest consumes **650 Confit**. If Confit stock < 650 → put it on
  the cooking queue (size to clear 650 + buffer). If ≥ 650 → leave it off.
- **Farm list:** only **hand-farmed** crops — Special Carrot, Onion, Special Hot Pepper (Pumpkin is
  worker-node, NOT farmed). Rank **lowest stock first**; top = farm today.

## Procedure
1. Query holdings.db for: cooked subs, processed intermediates, raws, vendor mats, Confit, farm crops.
2. Cooking queue: find subs short for one Balenos Meal batch → queue those + the meal. Apply Confit gate.
3. Processing queue: find intermediates short for the cooking queue → queue (A); add surplus note (B).
4. Buy-first: any vendor mat the two queues consume that's below stock (Mineral Water is the usual gate).
5. Farm: rank hand-farmed crops ascending by stock.
6. Write file with all 4 sections, format rules above.
7. **Commit AND push** — Jon reads on GitHub; a local commit he can't see (see the always-commit rule).

_This runbook exists because sections kept getting dropped between sessions. Update it here when the spec
changes, don't just hold it in memory._
