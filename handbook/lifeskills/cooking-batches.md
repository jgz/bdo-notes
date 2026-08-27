# Full-batch recipe book — Jon's canonical recipes

> **Static reference.** Each batch fills the **1,600 usable LT** bag. Sized by **whichever weighs more, inputs or the finished product** — cooking recipes are input-heavy (size by inputs), but processing (Grind/Shake/Dry/Heat) makes more weight than it consumes at Jon's mastery, so those size by **output** so the batch finishes with a full bag of product. **All weights & yields looked up / MEASURED** — Meat 0.03 LT, Dried Fish 0.5; **cook yield 3.68×**, **process yield 2.49×** (see [measurements](cooking-mastery-measurements.md)). `Pull` = exact ingredient count. Recipes = Jon's subs ([worklist](cooking-worklist.md)); live stock in the [dashboard](cooking-dashboard.md).

## 📦 Box conversion (canonical)

**Guru's Cooking Box (Balenos)** = **24 Balenos Meal** _(normal)_ **OR 8 Special** _(Special ×3)_. Verified: `recipe:9856:8` → 24× item 9601. Target 187 boxes/day = **4,488 meals/day**.

---
## ⚙️ Process (Grind/Shake/Dry/Heat — output-sized)

### Wheat Flour
`6,425` crafts/batch · Grind · **output-sized** (product heavier than inputs) · yields ≈ **15,998** (2.49× measured)

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat | 🏭 node | 1 | **6,425** |

### Wheat Dough
`6,425` crafts/batch · Shake · **output-sized** (product heavier than inputs) · yields ≈ **15,998** (2.49× measured)

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat Flour | ⚙️ process | 1 | **6,425** |
| Mineral Water | 🏪 vendor | 1 | **6,425** |

### Cheese
`64,257` crafts/batch · Dry · **output-sized** (product heavier than inputs) · yields ≈ **159,999** (2.49× measured)

> Milk-capped in practice (need 1 milk/craft).

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Milk | 🏭 node | 1 | **64,257** |

### Lump of Raw Sugar
`6,425` crafts/batch · Heat · **output-sized** (product heavier than inputs) · yields ≈ **15,998** (2.49× measured)

> Raw-sugar-capped (10/craft). Also horse-capture bait.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Raw Sugar | 🏪 vendor | 10 | **64,250** |
| Mineral Water | 🏪 vendor | 1 | **6,425** |

---
## 🔪 Cook — sub-components & Red Sauce (input-sized)

### Red Sauce
`20,000` crafts/batch · Cook · input-sized · yields ≈ **73,600** (3.68× measured)

> ⚠️ 20k crafts → 20k Meat (market). Big silver.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Base Sauce | 🏪 vendor | 1 | **20,000** |
| Meat (hunted, 0.03 LT) | 💰 market | 1 | **20,000** |
| Mineral Water | 🏪 vendor | 2 | **40,000** |
| Sugar | 🏪 vendor | 2 | **40,000** |

### Grilled Sausage
`3,200` crafts/batch · Cook · input-sized · yields ≈ **11,776** (3.68× measured)

> Feeds Cheese Gratin.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Meat (hunted, 0.03 LT) | 💰 market | 6 | **19,200** |
| Onion | 🌾 farm | 1 | **3,200** |
| Salt | 🏪 vendor | 2 | **6,400** |
| Pepper | 🌾 farm | 2 | **6,400** |

### Beer
`2,711` crafts/batch · Cook · input-sized · yields ≈ **9,976** (3.68× measured)

> 2 per Meal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Potato | 🏭 node | 5 | **13,555** |
| Mineral Water | 🏪 vendor | 6 | **16,266** |
| Leavening Agent | 🏪 vendor | 2 | **5,422** |
| Sugar | 🏪 vendor | 1 | **2,711** |

### Stir-Fried Vegetables
`2,191` crafts/batch · Cook · input-sized · yields ≈ **8,062** (3.68× measured)

> 2 per Meal. Downgrade Special Hot Pepper → HQ first.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Pumpkin | 🌾 subs Cabbage | 5 | **10,955** |
| Olive Oil | 🏪 vendor | 2 | **4,382** |
| HQ Hot Pepper | 🌾↓ downgrade | 2 | **4,382** |
| Salt | 🏪 vendor | 1 | **2,191** |

### Smoked Fish Steak
`3,018` crafts/batch · Cook · input-sized · yields ≈ **11,106** (3.68× measured)

> Dried fish (0.5 LT) from island nodes.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Dried Fish (0.5 LT) | 🏭 island node | 1 | **3,018** |
| Salt | 🏪 vendor | 2 | **6,036** |
| Olive Oil | 🏪 vendor | 1 | **3,018** |

### Meat Croquette
`1,951` crafts/batch · Cook · input-sized · yields ≈ **7,179** (3.68× measured)

> 1 per Meal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Meat (hunted, 0.03 LT) | 💰 market | 8 | **15,608** |
| Wheat Flour | ⚙️ process | 5 | **9,755** |
| Cheese | ⚙️ process | 2 | **3,902** |
| Egg | 🏭 node | 2 | **3,902** |
| Deep Frying Oil | 🏪 vendor | 4 | **7,804** |

### Cheese Gratin
`1,509` crafts/batch · Cook · input-sized · yields ≈ **5,553** (3.68× measured)

> 1 per Meal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Wheat Dough | ⚙️ process | 5 | **7,545** |
| Pumpkin | 🌾 subs Cabbage | 4 | **6,036** |
| Grilled Sausage | ⚙️ cook | 1 | **1,509** |
| Cheese | ⚙️ process | 3 | **4,527** |
| Red Sauce | ⚙️ cook | 3 | **4,527** |

---
## 🍽️ Cook — the meal

### Balenos Meal
`2,285` crafts/batch · Cook · input-sized · yields ≈ **8,408** (3.68× measured)

> The goal.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Cheese Gratin | ⚙️ cook | 1 | **2,285** |
| Meat Croquette | ⚙️ cook | 1 | **2,285** |
| Smoked Fish Steak | ⚙️ cook | 1 | **2,285** |
| Stir-Fried Vegetables | ⚙️ cook | 2 | **4,570** |
| Beer | ⚙️ cook | 2 | **4,570** |

---
## 🥕 Cook — side stream

### Carrot Confit
`1,632` crafts/batch · Cook · input-sized · yields ≈ **6,005** (3.68× measured)

> Weekly quest (650). Special-Carrot-capped.

| Ingredient | Source | /craft | **Pull** |
|---|---|--:|--:|
| Special Carrot | 🌾 farm | 2 | **3,264** |
| Cinnamon | 🏭 Tarif | 4 | **6,528** |
| Lump of Raw Sugar | ⚙️ process | 3 | **4,896** |
| Mineral Water | 🏪 vendor | 6 | **9,792** |
| Salt | 🏪 vendor | 2 | **3,264** |
