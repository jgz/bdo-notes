# Measured cooking yields — Jon's real crafts (ground truth)

> **Measured, not modeled.** These are actual craft counts vs actual output at Jon's real mastery+buffs.
> They **override** the interpolated curve in [mastery-yield.md](mastery-yield.md), which measured ~2× but
> reality is ~3.7×. Method: cook a known # of crafts of one recipe in isolation, record normal + higher-grade
> proc counts. Yield × = total output ÷ crafts.

**Setup for all measurements below:** cooking mastery **1,539 buffed** (base ~1,414 + Seafood Cron Meal +
Book of Flora, ~+125). This is Jon's normal batch-session state, so plan against 1,539.

## 🌾 Farming — Magical Carrot Seeds → Special Carrot — 2026-08-28
One full farm batch = **9,662 Special Carrots**. ≈ 3 full Carrot Confit batches (3,264 each), or ~14 weeks
of the 650/quest need. Confit is no longer carrot-capped after one farm run.

---

## Grilled Sausage (9427) — 2026-08-27
| | |
|---|--:|
| Crafts (19,200 Deer ÷ 6) | 3,200 |
| Normal Grilled Sausage | 9,816 |
| Blue proc (Smoked Sausage) | 1,891 |
| **Total output** | **11,707** |
| **Yield ×/craft** | **3.66×** |
| Higher-grade proc rate | 16.2% |
| Deer per sausage produced | 1.64 |

## Meat Croquette (9404) — 2026-08-27
| | |
|---|--:|
| Crafts (15,608 Wolf ÷ 8) | 1,951 |
| Normal Meat Croquette | 6,111 |
| Blue proc (Crispy Meat Croquette) | 1,101 |
| **Total output** | **7,212** |
| **Yield ×/craft** | **3.70×** |
| Higher-grade proc rate | 15.3% |
| Wolf per croquette produced | 2.16 |

_(Prediction from sausage's 3.66× was ~7,140 total — actual 7,212, within ~1%.)_

## Summary so far (1,539 buffed mastery)
- **Dishes ~3.7× yield, ~15% higher-grade proc:** Grilled Sausage 3.66×/16.2%, Meat Croquette 3.70×/15.3%,
  Cheese Gratin 3.80×/14.5%, Stir-Fried Veg 3.69×/13.6%. Use ~3.7× for dish planning / the box math.
- **Base sauces lower, no proc:** Red Sauce 2.93× (→ buy, don't craft).
- **Processing 2.49×** (Grind/Shake/Dry/Heat).
Yield is recipe-type-specific — don't assume one number for everything.

## Wheat Dough (7201, SHAKE) — 2026-08-27 — PROCESSING yield
| | |
|---|--:|
| Crafts (5,000 Flour + 5,000 Water) | 5,000 |
| Wheat Dough out | 12,454 |
| **Processing yield ×/craft** | **2.49×** |

Processing yield (2.49×) is **lower than cooking (3.68×)** and applies to all processing methods via the
shared processing-mastery stat — Grind / Shake / Dry / Heat (Wheat Flour, Wheat Dough, Cheese, Lump). It's
what makes those four **output-heavier than their inputs**, so they're **output-sized** in the batch book
(6,425 crafts → ~16k product = a full bag). Measured on SHAKE; assumed same for Grind/Dry/Heat (same stat).

## Red Sauce (9004, COOK) — 2026-08-27 — buy, don't craft
| | |
|---|--:|
| Crafts (20,000 meat − 664 left) | 19,336 |
| Red Sauce out | 56,566 |
| **Yield ×/craft** | **2.93×** |
| Higher-grade proc | none (no blue) |

**Cooking yield is NOT uniform:** dishes ~3.68×, but Red Sauce (a base sauce, no blue proc) only **2.93×**.
So don't assume 3.68× for every COOK recipe. **Buy-vs-craft:** craft cost is meat-driven = 25,300 ÷ 2.93 ≈
**8,600/sauce** (breakeven yield would be ~3.3×; 2.93 is below it), vs market **~7,600 buy order** / 8,800
instant. → **Buy Red Sauce, don't cook it** — removed from the cook queue; frees ~20k meat/batch.

## Cheese Gratin (9203, COOK) — 2026-08-28
| | |
|---|--:|
| Crafts (full dashboard batch) | 1,509 |
| Normal Cheese Gratin | 4,902 |
| Blue proc (Chewy Cheese Gratin) | 830 |
| **Total output** | **5,732** |
| **Yield ×/craft** | **3.80×** |
| Higher-grade proc rate | 14.5% |

## Stir-Fried Vegetables (9241, COOK) — 2026-08-28
| | |
|---|--:|
| Crafts (old 2-HQ-pepper batch) | 2,191 |
| Normal Stir-Fried Veg | 6,983 |
| Blue proc (crispy variant) | 1,101 |
| **Total output** | **8,084** |
| **Yield ×/craft** | **3.69×** |
| Higher-grade proc rate | 13.6% |

## Balenos Meal (9601, COOK) — 2026-08-28 — final tier ✅
| | |
|---|--:|
| Crafts (full batch) | 2,285 |
| Normal Balenos Meal | 6,994 |
| Special Balenos Meal | 1,501 |
| **Total output** | **8,495** |
| **Yield ×/craft** | **3.72×** |
| Special-meal rate | 17.7% |
| Box-equiv (Special ×3) | 6,994 + 1,501×3 = **11,497** → **479 boxes/batch** (5.03 box-meals/craft) |

## Pending (optional confirmation)
- A Grind/Dry/Heat spot-check (confirm 2.49× holds across processing methods)

## Meat cost / box — FINAL (all tiers measured)
Traced with measured yields (Croq 3.70×, Gratin 3.80×, Sausage 3.66×) and the meal tier's Special-meal ×3
box credit (5.03 box-meals/craft):
- Meat Croquette: 8 ÷ 3.70 per croq × (4.77 croq/box) = **~10.3 meat/box**
- Grilled Sausage → Gratin: 6 ÷ 3.66 × (1.255 gratin-crafts/box) = **~2.1 meat/box**
- Red Sauce: **0** (bought, not cooked)
- **Total ≈ 12.4 raw meat/box** (down from the ~16 estimate — specials stretch each craft + Red Sauce bought)

**Profit/box (buy everything):** 12.4 meat × 26k ≈ 322k + ~3.8 Red Sauce × ~8k ≈ 30k → **~352k cost vs 800k
box = ~+448k profit/box.** Plus byproduct income from selling Crispy Croquette / Chewy Gratin / Smoked
Sausage procs (see [proc strategy](cooking-proc-strategy.md)). Loop is solidly profitable even buying all inputs.
