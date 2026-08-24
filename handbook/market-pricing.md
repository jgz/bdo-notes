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
| `base_price` | current market center | rough current price; basis for Jon's buy-cost estimate (↓) |
| `last_sold_price` + `last_sold_time` | most recent real trade + when | **market value** (what it sold for) — but see below, it's NOT Jon's cost |
| `price_min` / `price_max` | **dev hard caps** (outer rails) | **NOT the price** — ignore as "cost" |
| `current_stock` | listed units at API snapshot | approximate; API lags live ([#11](https://github.com/jgz/bdo-cmd/issues/11)) |

## ⭐ Jon's real cost = the lowest buy-order bracket, not last-sold

Jon is a **patient buy-order trader**: for anything bought in bulk (Caphras, cooking ingredients like
meat), he **places buy orders at the lowest bracket price and waits** — on liquid commodities they fill
within hours (sellers dump for instant silver). So **his effective cost ≈ the bottom of the Base ±7.5%
window**, well below `last_sold_price`.

- **Interim heuristic (works with current tool):** Jon's buy cost ≈ **`base_price × 0.925`, snapped up
  to the nearest bracket.** Caphras: 905k × 0.925 = 837,125 → **~840k** (vs ~970k last-sold — ~13% less).
- **Caveat:** this gives the *price*, not the *fill-time*. Whether a bottom bid fills fast depends on
  buy-queue depth — for less-liquid items Jon may need to bid a bracket or two higher. The tool doesn't
  expose the order book yet → **[#12](https://github.com/jgz/bdo-cmd/issues/12)** (add buy/sell order
  counts per bracket). Until then, use the heuristic for staples and sanity-check thin items in-game.
- **Rule:** cost Jon's materials at the **buy-order price** (≈ base × 0.925), not `last_sold` — else
  every estimate is inflated.

**Example — Caphras Stone (2026-08-23):** base 905k, live window ~840k–970k, but dev caps **820k / 3M**.
Its base has **deflated to near its floor** (heavy oversupply); the 3M ceiling is where the old "~3M
Caphras" figure came from (base used to sit near the cap). Both are real — they're the rails, not
today's price.

_Source: official Central Market rules (Base ±7.5%, dev min/max caps) + in-game Purchase UI._
