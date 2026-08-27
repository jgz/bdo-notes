# Meat & Fish buy-order value list — for Balenos Meal

What to keep **standing buy orders** on for the meal chain. Meat & fish are substitution groups — the
recipe count is fixed (**8 meat**/Croquette, **6 meat**/Grilled Sausage, **1 meat**/Red Sauce; **1 fish**/
Smoked Fish Steak) and the *type* doesn't change the output, so **cheapest legal fill wins.**

Prices = live `bdo-cmd market` last-sold (NA), **pulled 2026-08-27**. They drift — regenerate to refresh
(item IDs are in the tables). Best value = **low price AND real stock** (a cheap item with ~0 stock never
fills a buy order).

## 🥩 Meat — the 15-meat group (Pork's Alternative Ingredient list)
Ranked cheapest first. Stock = current CM listings.

| Meat | id | Last-sold | Stock | Note |
|---|--:|--:|--:|---|
| **Bear** | 7912 | 24,200 | 36,170 | ✅ cheap + deep stock |
| Weasel | 7911 | 25,000 | 2,116 | thin stock |
| **Fox** | 7903 | 25,300 | 18,098 | ✅ |
| **Wolf** | 7913 | 25,300 | 62,729 | ✅ deepest stock |
| **Rock Elephant** | 7962 | 25,600 | 26,860 | ✅ |
| **Lamb** | 7902 | 26,000 | 61,477 | ✅ |
| **Rhino** | 7904 | 26,600 | 20,744 | ✅ |
| Pork | 7905 | 28,100 | 52,573 | |
| Deer | 7901 | 28,400 | 7,492 | |
| Beef | 7906 | 29,100 | 10,941 | |
| Goat | 7957 | 29,900 | 17,052 | |
| Raccoon | 7910 | 30,900 | 1,394 | thin |
| Sea Lion | 7960 | 31,000 | 2,891 | thin |
| Rabbit | 7961 | 31,700 | 309 | ~none |
| Gazelle | 7925 | 40,600 | 5,235 | ❌ avoid (outlier) |

**→ Standing buy orders on the cheap cluster:** **Bear · Wolf · Fox · Rock Elephant · Lamb · Rhino**
(all 24.2–26.6k with deep stock). Take whatever fills. Bear & Wolf are both cheapest *and* deepest — lead
with those. Skip the thin-stock ones (Weasel/Raccoon/Sea Lion/Rabbit) and Gazelle.

## 🐟 Fish — Smoked Fish Steak (1 per craft)
Fish is a **rounding error** (1/meal) and your **island dried-fish nodes** already feed it — you're holding
~31k dried fish + ~50k finished steaks. So **buy orders here are low priority.**

The catch: the *cheapest* dried fish (Bass 5.9k, Catfish 7.7k, Mackerel 8k) have **~0 market stock** —
they won't fill. The only cheap fish with real liquidity are your own node fish:

| Dried Fish | id | Last-sold | Stock | Note |
|---|--:|--:|--:|---|
| Dolphinfish | 8567 | 11,500 | 4,081 | 🏭 your node |
| Filefish | 8534 | 11,900 | 10,159 | 🏭 your node |
| Flatfish | 8560 | 22,000 | 17,717 | 🏭 your node |
| Striped Catfish | 8568 | — | 0 | 🏭 node-only, not traded |
| Scorpion Fish | 8535 | — | 0 | 🏭 node-only, not traded |

**→ Don't run fish buy orders** — let the nodes + stockpile cover it. If you ever must top up, Dolphinfish/
Filefish (~11.5k) are the only cheap+liquid options, and those are already your node output.

---
_Regenerate: `bdo-cmd market price <id>` per row. Meat group from Pork (7905) item description; fish slot =
Smoked Fish Steak (9417) → item 8201 (Mudskipper / any Fish)._
