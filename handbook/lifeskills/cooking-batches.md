# Full-batch recipe book — Jon's canonical recipes

> **Static reference.** Every batch below fills the **1,600 usable LT** bag (1,822 max − ~150 baseline). These numbers **do not change** unless the weight cap changes — the dashboard just points here for pull amounts. `crafts` = how many times you press cook/process to fill the bag; **Pull** = exact ingredient count to grab (mastery does *not* change pulls, only output). Recipes are Jon's confirmed substitutions (see [cooking-worklist.md](cooking-worklist.md)). Stock is live in the [dashboard](cooking-dashboard.md).

## 📦 Box conversion (canonical)

**Guru's Cooking Box (Balenos)** = **24 Balenos Meal** _(normal)_ **OR 8 Special Balenos Meal** _(a Special counts ×3)_. Verified in game data: `recipe:9856:8` → 24× item 9601. Batch variants: 240→10 boxes, 2,400→100 boxes.

| | per box | per full Meal batch (2,285) |
|---|--:|--:|
| Normal meals | 24 | ≈ 95 boxes (190 w/ mastery output) |
| Target | 187 boxes/day | = **4,488 meals/day** |

---
## ⚙️ Process (fire & forget, ~30–45 min)

### Wheat Flour
`16,000` crafts/batch · 0.10 LT/craft · **Grind** · yields ≈ **32,000** (mastery ~2×)

> Bag-fill is huge because inputs are ~0.01 LT — you'll hit **raw stock on hand** before the bag fills. Treat this number as the ceiling; process what you have / what the queue needs.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat | 🏭 node | 1 | **16,000** |

### Wheat Dough
`14,545` crafts/batch · 0.11 LT/craft · **Shake** · yields ≈ **29,090** (mastery ~2×)

> Bag-fill is huge because inputs are ~0.01 LT — you'll hit **raw stock on hand** before the bag fills. Treat this number as the ceiling; process what you have / what the queue needs.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat Flour | ⚙️ process | 1 | **14,545** |
| Mineral Water | 🏪 vendor | 1 | **14,545** |

### Cheese
`160,000` crafts/batch · 0.01 LT/craft · **Dry** · yields ≈ **320,000** (mastery ~2×)

> Bag-fill is huge because inputs are ~0.01 LT — you'll hit **raw stock on hand** before the bag fills. Treat this number as the ceiling; process what you have / what the queue needs. (milk-capped in practice)

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Milk | 🏭 node | 1 | **160,000** |

### Lump of Raw Sugar
`14,545` crafts/batch · 0.11 LT/craft · **Heat** · yields ≈ **29,090** (mastery ~2×)

> Bag-fill is huge because inputs are ~0.01 LT — you'll hit **raw stock on hand** before the bag fills. Treat this number as the ceiling; process what you have / what the queue needs. Also wild-horse capture bait — keep a buffer.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Raw Sugar | 🏪 vendor | 10 | **145,450** |
| Mineral Water | 🏪 vendor | 1 | **14,545** |

### Red Sauce
`10,666` crafts/batch · 0.15 LT/craft · **Heat (craft)** · yields ≈ **21,332** (mastery ~2×)

> Bag-fill is huge because inputs are ~0.01 LT — you'll hit **raw stock on hand** before the bag fills. Treat this number as the ceiling; process what you have / what the queue needs.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Base Sauce | 🏪 vendor | 1 | **10,666** |
| Meat (hunted) | 💰 market | 1 | **10,666** |
| Mineral Water | 🏪 vendor | 2 | **21,332** |
| Sugar | 🏪 vendor | 2 | **21,332** |

---
## 🔪 Cook — sub-components (~10–15 min)

### Grilled Sausage
`1,739` crafts/batch · 0.92 LT/craft · **Cook** · yields ≈ **3,478** (mastery ~2×)

> Feeds Cheese Gratin (1 each).

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Meat (hunted) | 💰 market | 6 | **10,434** |
| Onion | 🌾 farm | 1 | **1,739** |
| Salt | 🏪 vendor | 2 | **3,478** |
| Pepper | 🌾 farm | 2 | **3,478** |

### Beer
`2,711` crafts/batch · 0.59 LT/craft · **Cook** · yields ≈ **5,422** (mastery ~2×)

> 2 per Balenos Meal — the heaviest-consumed sub.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Potato | 🏭 node | 5 | **13,555** |
| Mineral Water | 🏪 vendor | 6 | **16,266** |
| Leavening Agent | 🏪 vendor | 2 | **5,422** |
| Sugar | 🏪 vendor | 1 | **2,711** |

### Stir-Fried Vegetables
`2,191` crafts/batch · 0.73 LT/craft · **Cook** · yields ≈ **4,382** (mastery ~2×)

> 2 per Balenos Meal. HQ Hot Pepper = **downgrade Special Hot Pepper at NPC** first.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Pumpkin | 🌾 subs Cabbage | 5 | **10,955** |
| Olive Oil | 🏪 vendor | 2 | **4,382** |
| HQ Hot Pepper | 🌾↓ downgrade | 2 | **4,382** |
| Salt | 🏪 vendor | 1 | **2,191** |

### Smoked Fish Steak
`12,307` crafts/batch · 0.13 LT/craft · **Cook** · yields ≈ **24,614** (mastery ~2×)

> 1 per Meal. Fill Fish from stock/market.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Fish (any) | 💰/node | 1 | **12,307** |
| Salt | 🏪 vendor | 2 | **24,614** |
| Olive Oil | 🏪 vendor | 1 | **12,307** |

### Meat Croquette
`1,159` crafts/batch · 1.38 LT/craft · **Cook** · yields ≈ **2,318** (mastery ~2×)

> 1 per Meal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Meat (hunted) | 💰 market | 8 | **9,272** |
| Wheat Flour | ⚙️ process | 5 | **5,795** |
| Cheese | ⚙️ process | 2 | **2,318** |
| Egg | 🏭 node | 2 | **2,318** |
| Deep Frying Oil | 🏪 vendor | 4 | **4,636** |

### Cheese Gratin
`1,509` crafts/batch · 1.06 LT/craft · **Cook** · yields ≈ **3,018** (mastery ~2×)

> 1 per Meal. Deepest chain (needs Dough+Sausage+Cheese+Red Sauce).

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat Dough | ⚙️ process | 5 | **7,545** |
| Pumpkin | 🌾 subs Cabbage | 4 | **6,036** |
| Grilled Sausage | ⚙️ cook | 1 | **1,509** |
| Cheese | ⚙️ process | 3 | **4,527** |
| Red Sauce | ⚙️ process | 3 | **4,527** |

---
## 🍽️ Cook — the meal

### Balenos Meal
`2,285` crafts/batch · 0.70 LT/craft · **Cook** · yields ≈ **4,570** (mastery ~2×)

> The goal. 1 Gratin + 1 Croq + 1 FishSteak + 2 Veg + 2 Beer.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Cheese Gratin | ⚙️ cook | 1 | **2,285** |
| Meat Croquette | ⚙️ cook | 1 | **2,285** |
| Smoked Fish Steak | ⚙️ cook | 1 | **2,285** |
| Stir-Fried Vegetables | ⚙️ cook | 2 | **4,570** |
| Beer | ⚙️ cook | 2 | **4,570** |

---
## 🥕 Cook — side stream (Mythical Feathers)

### Carrot Confit
`1,632` crafts/batch · 0.98 LT/craft · **Cook** · yields ≈ **3,264** (mastery ~2×)

> Weekly training quest → Mythical Feathers (Courser awakening). Special Carrot-capped.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Special Carrot | 🌾 farm | 2 | **3,264** |
| Cinnamon | 🏭 Tarif | 4 | **6,528** |
| Lump of Raw Sugar | ⚙️ process | 3 | **4,896** |
| Mineral Water | 🏪 vendor | 6 | **9,792** |
| Salt | 🏪 vendor | 2 | **3,264** |
