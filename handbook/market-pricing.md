# Central Market pricing — how the numbers work

> Last updated 2026-08-23. Reference for reading prices and interpreting **`bdo-cmd market price`**
> output. Confirmed against the in-game Purchase UI (Caphras Stone screenshots, 2026-08-23).

## Three different price concepts

1. **Base Price** — the white number (Caphras: 905,000); the current market "center." **Fluctuates with
   supply/demand:** sells at the low end push it down, buys at the high end push it up.
2. **Live listable window = Base Price ±7.5%** (was ±10%), snapped to bracketed increments. You can
   **only** list a sell/buy order within this window — no custom price outside it. Increments are
   **graduated by price tier** (≈5,000 at the ~900k tier; larger steps at higher prices). The window
   drifts as the base moves.
   - Caphras check: 905,000 × 1.075 ≈ 972,875 → top bracket **970,000**; × 0.925 ≈ 837,125 → bottom
     **840,000**. Matches the in-game brackets exactly.
3. **Developer hard caps (MIN / MAX)** — absolute floor/ceiling the *base price* can ever drift
   between, set by devs. **These are what `bdo-cmd` returns as `price_min` / `price_max`.** They are
   **NOT** the live window.

## Reading `bdo-cmd market price`

| Field | Meaning | Use it for? |
|---|---|---|
| `base_price` | current market center | rough current price |
| `last_sold_price` + `last_sold_time` | most recent real trade + when | **the number to trust** (check freshness) |
| `price_min` / `price_max` | **dev hard caps** (outer rails) | **NOT the price** — ignore as "cost" |
| `current_stock` | listed units at API snapshot | approximate; API lags live ([#11](https://github.com/jgz/bdo-cmd/issues/11)) |

**Example — Caphras Stone (2026-08-23):** base 905k, live window ~840k–970k, but dev caps **820k / 3M**.
Its base has **deflated to near its floor** (heavy oversupply); the 3M ceiling is where the old "~3M
Caphras" figure came from (base used to sit near the cap). Both are real — they're the rails, not
today's price.

_Source: official Central Market rules (Base ±7.5%, dev min/max caps) + in-game Purchase UI._
