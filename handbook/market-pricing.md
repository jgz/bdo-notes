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

- **Best source — `bdo-cmd market orders <id>`** (shipped, [#12](https://github.com/jgz/bdo-cmd/issues/12)):
  the **live order book** — per-bracket `price / sellers / buyers`. This is the authoritative read of
  Jon's real cost and fill-likelihood: the **lowest sell** = instant-buy price; the **buy-order
  brackets** (and their depth) = where he'd queue and how contested it is. In BDO a bracket holds sell
  orders *or* buy orders (matching orders transact instantly), so sells stack above the clearing level,
  buys below.
- **Fallback heuristic (no order book):** Jon's buy cost ≈ **`base_price × 0.925`, snapped to a
  bracket** (bottom of the ±7.5% window). Approximate — prefer `market orders` when it matters.
- **Rule:** cost Jon's materials at the **buy-order / lowest-sell price** from `market orders`, not
  `last_sold` — else estimates inflate.

> **Reading the book:** all-sellers-no-buyers (like Caphras 2026-08-24: 33k stock, last_sold < base) =
> **sell glut → cheap, instant-buy at the lowest sell**. Deep buy-order queue = contested → a low bid
> may sit; bid up a bracket or two to fill.

**Example — Caphras Stone (2026-08-23):** base 905k, live window ~840k–970k, but dev caps **820k / 3M**.
Its base has **deflated to near its floor** (heavy oversupply); the 3M ceiling is where the old "~3M
Caphras" figure came from (base used to sit near the cap). Both are real — they're the rails, not
today's price.

_Source: official Central Market rules (Base ±7.5%, dev min/max caps) + in-game Purchase UI._
