# Cooking Dashboard — live cycle (stock: all storages, 2026-08-27)

The perpetual loop: **make a full Balenos Meal batch → it drains the subs → refill whatever went short → make another meal batch → repeat.** Do the top card, let it drop off, next moves up. Full pull amounts for every recipe live in the **[batch book](cooking-batches.md)** — this page only shows *what's short and in what order*.

**Reference:** 1 Guru's Cooking Box = **24 meals** · target 187 boxes/day = 4,488 meals/day. One full meal batch = 2,285 crafts ≈ 4,570 meals ≈ **1 day of boxes** — so the meal card comes up roughly every day and the subs cycle under it.

## 🏪 Vendor restock first (gates the Beer batch)
| Item | Have | Buy to | Why |
|---|--:|--:|---|
| Mineral Water | 7,642 | ~30,000 | a full Beer batch alone needs **16,266** |
| Sugar | 4,335 | ~20,000 | in Beer + Red Sauce |
| Base Sauce | 4,846 | ~20,000 | Red Sauce |

---

## ▶ DO NOW

### 1. Beer — full batch _(only sub short for the next meal)_
Runway 0.5 batches — can't complete a meal without it. **2,711 crafts** → Potato 13,555 · Mineral Water 16,266 · Leavening 5,422 · Sugar 2,711. → yields ~5,422 Beer.

### 2. Balenos Meal — full batch
**2,285 crafts** → pulls 2,285 Gratin · 2,285 Croquette · 2,285 Fish Steak · 4,570 Veg · 4,570 Beer (all in stock once Beer is done). → ~4,570 meals = ~190 boxes.

---

## 🔁 Rotation watch (refills as the meal batch drains them)
Runway = full meal-batches of stock left before it re-enters the queue. When one drops below 1, it jumps into **DO NOW** above the meal.

| Sub-component | Stock | Runway | Status |
|---|--:|--:|---|
| **Beer** | 2,191 | 0.5 | ▶ short — batch now |
| Cheese Gratin | 4,090 | 1.8 | next up (see prereqs) |
| Stir-Fried Veg | 8,819 | 1.9 | ok — downgrade Hot Pepper to keep HQ stocked |
| Meat Croquette | 4,422 | 1.9 | ok |
| Smoked Fish Steak | 52,466 | 23 | ⏸ parked — skip for weeks |

## ⚙️ Prereq watch (needed when Cheese Gratin re-enters, ~next pass)
A full Gratin batch (1,509) needs more than we hold of these — process them *before* the Gratin batch:
| Prereq | Stock | Full Gratin batch needs | Do |
|---|--:|--:|---|
| Grilled Sausage | 750 | 1,509 | cook a batch (1,739) |
| Red Sauce | 2,287 | 4,527 | craft a batch (10,666) |
| Wheat Dough | 2,390 | 7,545 | shake a batch (Flour → Dough) |
| Cheese | 25,702 | 4,527 | ok (5+ batches) |
| Wheat Flour | 39,188 | 5,795 | ok |

---

## 🥕 Side stream — Carrot Confit (Mythical Feathers)
Special Carrot **1,208** caps this at **604 crafts** (not a full 1,632 bag). First process **Lump of Raw Sugar** — have 499, a 604-craft Confit needs 1,812. Then cook Confit 604 → ~1,208 Confit. Cinnamon (31,571) is in **Tarif**.

---

_Regenerate from `~/.bdo-cmd/holdings.db` (all storages). Pull amounts: [batch book](cooking-batches.md). Recipes/subs: [worklist](cooking-worklist.md)._
