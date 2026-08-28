# Cooking proc strategy — sell the valuable procs, use the cheap ones in meals

> Every dish cooks a **blue (grade-2) proc** ~15% of the time (e.g. Chewy Cheese Gratin, Crispy Meat
> Croquette). Decide per-proc: **sell it, or fold it back into meals.** Prices drift — check the market
> before a big sell, but the tiers below are stable. (Analysis 2026-08-28, [measurements](cooking-mastery-measurements.md).)

## The mechanic
Normal subs are **green (g1)**, procs are **blue (g2)**, and **1 blue = 2 green** (grade value white 1 / green 4 / blue 8).
So it depends on the meal slot size:
- **1-per-meal slots** (Cheese Gratin, Meat Croquette, Smoked Fish Steak): meal needs 1 green → a blue
  *over-fills* it (1 blue used for 1 slot, half its value wasted). No quantity saving → **sell the blue, cook a normal.**
- **2-per-meal slots** (Stir-Fried Veg, Beer): meal needs 2 green = exactly 1 blue → **1 blue replaces 2 normal.**

## Verdict
**SELL (high value — dwarfs the cost of cooking a normal replacement):**
- **Crispy Meat Croquette** — highest value, thousands of buyers queued
- **Chewy Cheese Gratin** — high value (sells slower, no queue)
- **Smoked Sausage** (from Grilled Sausage) — high value, sells instantly at the price cap

**USE in meals (cheap / unsellable — folding them in beats the tiny sale):**
- **Golden Smoked Fish Steak** — floor-stacked, nobody buys; and you're sitting on ~50k Smoked Fish Steak
  + ~9k Golden → **don't cook Smoked Fish Steak for a long time; use Golden in the fish slot (1:1).**
- **Cold Draft Beer** — low value; 1 replaces 2 Beer in the meal.
- **Crispy Stir-Fried Veg** — low value (~12k if sold); 1 replaces 2 Veg. Sell if you want the silver, else use.

## Bottom line
Your **meat-heavy** cooking (Croquette, Sausage) throws off a valuable sellable byproduct → **sell those.**
Your **cheap** cooking (Fish, Beer, Veg) throws off procs best folded back into meals → **use those.**
Net: byproduct sales stack on top of the ~+448k/box meal profit.
