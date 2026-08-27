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

## Pending
- Meat Croquette (9404) — next
- Red Sauce (9004)
- Cheese Gratin (9203)
- Balenos Meal (9601)

## Implication (meat cost / box) — preliminary
Real yield ~3.66× (vs modeled 2.05×) is why hand-calc gave 71 meat/box but BDOlytics gives **16**. Plugging
3.66× into the tier-compounding model gives ~19/box; the blue-proc grade credit closes the rest to ~16.
**At 16 meat/box × 26k = ~416k cost vs 800k box = ~+384k profit/box** (buying all meat). Confirm once the
other tiers are measured.
