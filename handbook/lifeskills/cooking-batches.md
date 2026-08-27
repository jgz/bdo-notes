# Full-batch recipe book — Jon's canonical recipes

> **Static reference.** Every batch fills the **1,600 usable LT** bag (1,822 max − ~150). Numbers change only if the weight cap changes. `crafts` = presses to fill the bag; **Pull** = exact ingredient count (mastery changes output, not pulls). **All ingredient weights looked up per-item via `bdo-cmd item info` — no placeholders** (Meat = **0.03** LT, Dried Fish = **0.5**, grain/flour/dough/cooked = 0.1, vendor liquids/cheese/egg = 0.01). Recipes = Jon's subs ([worklist](cooking-worklist.md)); live stock in the [dashboard](cooking-dashboard.md).

## 📦 Box conversion (canonical)

**Guru's Cooking Box (Balenos)** = **24 Balenos Meal** _(normal)_ **OR 8 Special** _(Special ×3)_. Verified: `recipe:9856:8` → 24× item 9601. Target 187 boxes/day = **4,488 meals/day**.

---
## ⚙️ Process (fire & forget, ~30–45 min)

### Wheat Flour
`16,000` crafts/batch · 0.100 LT/craft · **Grind** · yields ≈ **32,000** (mastery ~2×)

> Ultra-light inputs (~0.01 LT) → bag-fill is huge; you'll hit raw stock on hand first. This is the ceiling.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat | 🏭 node | 1 | **16,000** |

### Wheat Dough
`14,545` crafts/batch · 0.110 LT/craft · **Shake** · yields ≈ **29,090** (mastery ~2×)

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat Flour | ⚙️ process | 1 | **14,545** |
| Mineral Water | 🏪 vendor | 1 | **14,545** |

### Cheese
`160,000` crafts/batch · 0.010 LT/craft · **Dry** · yields ≈ **320,000** (mastery ~2×)

> Ultra-light inputs (~0.01 LT) → bag-fill is huge; you'll hit raw stock on hand first. This is the ceiling. (milk-capped in practice)

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Milk | 🏭 node | 1 | **160,000** |

### Lump of Raw Sugar
`14,545` crafts/batch · 0.110 LT/craft · **Heat** · yields ≈ **29,090** (mastery ~2×)

> Ultra-light inputs (~0.01 LT) → bag-fill is huge; you'll hit raw stock on hand first. This is the ceiling. Also horse-capture bait.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Raw Sugar | 🏪 vendor | 10 | **145,450** |
| Mineral Water | 🏪 vendor | 1 | **14,545** |

### Red Sauce
`20,000` crafts/batch · 0.080 LT/craft · **Heat (craft)** · yields ≈ **40,000** (mastery ~2×)

> ⚠️ Full bag = 20,000 crafts → **20,000 Meat** (market cost). Big silver — consider a partial batch.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Base Sauce | 🏪 vendor | 1 | **20,000** |
| Meat (hunted, 0.03 LT) | 💰 market | 1 | **20,000** |
| Mineral Water | 🏪 vendor | 2 | **40,000** |
| Sugar | 🏪 vendor | 2 | **40,000** |

---
## 🔪 Cook — sub-components (~10–15 min)

### Grilled Sausage
`3,200` crafts/batch · 0.500 LT/craft · **Cook** · yields ≈ **6,400** (mastery ~2×)

> Feeds Cheese Gratin (1 each).

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Meat (hunted, 0.03 LT) | 💰 market | 6 | **19,200** |
| Onion | 🌾 farm | 1 | **3,200** |
| Salt | 🏪 vendor | 2 | **6,400** |
| Pepper | 🌾 farm | 2 | **6,400** |

### Beer
`2,711` crafts/batch · 0.590 LT/craft · **Cook** · yields ≈ **5,422** (mastery ~2×)

> 2 per Balenos Meal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Potato | 🏭 node | 5 | **13,555** |
| Mineral Water | 🏪 vendor | 6 | **16,266** |
| Leavening Agent | 🏪 vendor | 2 | **5,422** |
| Sugar | 🏪 vendor | 1 | **2,711** |

### Stir-Fried Vegetables
`2,191` crafts/batch · 0.730 LT/craft · **Cook** · yields ≈ **4,382** (mastery ~2×)

> 2 per Meal. HQ Hot Pepper = downgrade Special at NPC first.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Pumpkin | 🌾 subs Cabbage | 5 | **10,955** |
| Olive Oil | 🏪 vendor | 2 | **4,382** |
| HQ Hot Pepper | 🌾↓ downgrade | 2 | **4,382** |
| Salt | 🏪 vendor | 1 | **2,191** |

### Smoked Fish Steak
`3,018` crafts/batch · 0.530 LT/craft · **Cook** · yields ≈ **6,036** (mastery ~2×)

> 1 per Meal. Dried fish (0.5 LT) from island nodes.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Dried Fish (0.5 LT) | 🏭 island node | 1 | **3,018** |
| Salt | 🏪 vendor | 2 | **6,036** |
| Olive Oil | 🏪 vendor | 1 | **3,018** |

### Meat Croquette
`1,951` crafts/batch · 0.820 LT/craft · **Cook** · yields ≈ **3,902** (mastery ~2×)

> 1 per Meal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Meat (hunted, 0.03 LT) | 💰 market | 8 | **15,608** |
| Wheat Flour | ⚙️ process | 5 | **9,755** |
| Cheese | ⚙️ process | 2 | **3,902** |
| Egg | 🏭 node | 2 | **3,902** |
| Deep Frying Oil | 🏪 vendor | 4 | **7,804** |

### Cheese Gratin
`1,509` crafts/batch · 1.060 LT/craft · **Cook** · yields ≈ **3,018** (mastery ~2×)

> 1 per Meal. Deepest chain.

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
`2,285` crafts/batch · 0.700 LT/craft · **Cook** · yields ≈ **4,570** (mastery ~2×)

> The goal.

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
`1,632` crafts/batch · 0.980 LT/craft · **Cook** · yields ≈ **3,264** (mastery ~2×)

> Weekly quest (needs 650). Special-Carrot-capped.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Special Carrot | 🌾 farm | 2 | **3,264** |
| Cinnamon | 🏭 Tarif | 4 | **6,528** |
| Lump of Raw Sugar | ⚙️ process | 3 | **4,896** |
| Mineral Water | 🏪 vendor | 6 | **9,792** |
| Salt | 🏪 vendor | 2 | **3,264** |
