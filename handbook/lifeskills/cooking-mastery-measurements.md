# Measured cooking yields — Jon's real crafts (ground truth)

> **Measured, not modeled.** These are actual craft counts vs actual output at Jon's real mastery+buffs.
> They **override** the interpolated curve in [mastery-yield.md](mastery-yield.md), which measured ~2× but
> reality is ~3.7×. Method: cook a known # of crafts of one recipe in isolation, record normal + higher-grade
> proc counts. Yield × = total output ÷ crafts.

**Setup for all measurements below:** cooking mastery **1,539 buffed** (base ~1,414 + Seafood Cron Meal +
Book of Flora, ~+125). This is Jon's normal batch-session state, so plan against 1,539.

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

## Summary so far
Two recipes measured, consistent: **~3.68× yield, ~15.7% higher-grade proc** at 1,539 buffed mastery. Safe
to treat ~3.68× as the cooking yield across recipes for planning.

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

## Pending (optional confirmation)
- Cheese Gratin (9203) — no meat, but yield affects compounding
- Balenos Meal (9601) — no meat, but yield affects compounding
- A Grind/Dry/Heat spot-check (confirm 2.49× holds across processing methods)

## Implication (meat cost / box) — preliminary
Real yield ~3.66× (vs modeled 2.05×) is why hand-calc gave 71 meat/box but BDOlytics gives **16**. Plugging
3.66× into the tier-compounding model gives ~19/box; the blue-proc grade credit closes the rest to ~16.
**At 16 meat/box × 26k = ~416k cost vs 800k box = ~+384k profit/box** (buying all meat). Confirm once the
other tiers are measured.
