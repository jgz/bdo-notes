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
- Batch = **full bag (1,600 LT)** sizes from the batch book.
- **Size by whichever weighs more — the INPUTS or the finished PRODUCT.** A batch fills 1,600 LT of the
  heavier side. Cooking recipes are input-heavy (output lighter than inputs) → size by inputs. But mastery
  multiplies OUTPUT, so light-input **processing** recipes (Wheat Flour, Wheat Dough, Cheese, Lump of Raw
  Sugar) produce MORE weight than they consume → size these by **output**: crafts = 1,600 ÷ (processing-yield
  × output-item-weight), so the batch finishes with a full bag of product instead of overflowing partway.
  Requires the real **processing** yield (measure it — do NOT reuse the cooking yield or the handbook table).
- **Every ingredient weight is looked up per-item (`bdo-cmd item info <id>` → `weight`) — NEVER a category
  placeholder.** A wrong weight silently corrupts every batch size (a 0.1 placeholder for Meat, real 0.03,
  made the meat recipes fill half). Confirmed weights: Meat = 0.03, Dried Fish = 0.5, grain/flour/dough/
  cooked-items = 0.1, vendor liquids/cheese/egg = 0.01 — but re-verify, don't trust this list blindly.
- **EVERY batch — cook AND process — is ALWAYS the full bag size from the batch book.** Never shrink to
  current stock, never size to the consumer's need. Overshoot is the goal: process/cook once, don't repeat
  for months. If Jon is short an input, the queue implies he **buys/farms up to the full batch** first
  (e.g. Lump = full 14,545 crafts / 145,450 Raw Sugar — buy the raw sugar, it's cheap; Confit = full 1,632
  crafts / 3,264 Special Carrot — farm the rest). Note the shortfall in the card's italic if useful, never
  downsize. Vendor mats are cheap and overshoot costs ~nothing, so full batch always wins on fewer reps.
- Pull quantities in tables come straight from the batch book (or scaled to need — see rules below).

## Priority rules
- **Processing queue order:** (A) intermediates SHORT for what the cooking queue will consume
  (Lump→Confit, Wheat Dough → Cheese Gratin, etc. — **Red Sauce is a COOK recipe, it goes in the cook
  queue, NOT here**; only Grind/Shake/Dry/Heat belong in the processing queue), then (B) convert surpluses
  (grain→Flour/Dough, milk→Cheese). "Short" = have < one full consumer batch's need.
- **Cooking queue order:** vendor/processing prereqs handled above, then Beer/subs that are short, then
  **Balenos Meal**, then **Carrot Confit** if the quest gate trips.
- **Blue-proc meal substitution (ALWAYS apply — see [cooking-proc-strategy.md](cooking-proc-strategy.md)):**
  when building the Balenos Meal card, fill slots from blue-proc stock before greens:
  - **Veg slot & Beer slot (2-qty):** 1 blue = 2 green. Pull **Crispy Stir-Fried Veg** (9284) and **Cold
    Draft Beer** (9283) at **2,285 each** (covers the 4,570 green need) if blue stock ≥ 2,285. Only queue a
    green Stir-Fried Veg / Beer cook if the blue stock can't cover 2,285.
  - **Fish slot (1-qty):** pull **Golden Smoked Fish Steak** (9445) 1:1 = 2,285 (Golden is unsellable +
    both fish steaks overstocked → never cook Smoked Fish Steak).
  - **Gratin & Croquette (1-qty):** stay **green** — a blue over-fills a 1-slot, so **sell** the blue
    Chewy Cheese Gratin (9282) & Crispy Meat Croquette (9438) instead of folding them in.
  So a "short" check for Veg/Beer/Fish uses **blue-equivalent** stock, not just the green count.
  - **RESIZE the batch when using blues — don't keep the green craft count.** Blues put fewer/lighter
    items in the bag, so the full-bag batch grows: green = 7 items/craft × 0.1 = 0.7 LT → **2,285**; blue
    = 5 items/craft × 0.1 = 0.5 LT → **3,200 crafts** (each ingredient 1/craft = 3,200 pull). Yields
    ~11,776 meals vs 8,408 — ~40% more per bag. Always re-derive crafts = 1,600 ÷ (items/craft × 0.1)
    for the actual slot mix. (Both meal variants are in [cooking-batches.md](cooking-batches.md).)
- **Carrot Confit gate:** weekly training quest consumes **650 Confit**. If Confit stock < 650 → put it on
  the cooking queue (size to clear 650 + buffer). If ≥ 650 → leave it off.
- **Farm list:** only **hand-farmed** crops — **Special Carrot (54005), Special Onion (7337), Special
  Hot Pepper (7339)** (Pumpkin is worker-node, NOT farmed). Jon farms the **Special** (magical-seed)
  versions and downgrades to the recipe grade (Special Onion → Onion; Special Hot Pepper → HQ) — so
  **rank by the SPECIAL variant's stock, NOT the downgraded/regular count** (ranking Onion by regular
  Onion 7303 is the recurring bug). Rank **lowest Special-stock first**; top = farm today.

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
