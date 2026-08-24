# CP growth + passive-income empire

> Last updated 2026-08-24. Jon's focus: grow CP → more/better worker nodes → more passive silver
> (scales better than crafting margins). Reference for the CP methods + the node-optimizer tools.

## Growing CP (returning player, 369 CP)

- **Daily regional Contribution-EXP quests** — the sustainable grind. **Duvencrune** is the standout:
  ~15-min route, **7k+ Contribution EXP/day**. Altinova + other regions also have dailies.
- **Cooking/Alchemy byproduct → CP exchange (Olvia):** **Witch's Delicacy** (cooking byproduct) +
  **Mysterious Catalyst** (alchemy). Jon's Guru cooking already generates Witch's Delicacy — free CP
  fuel from the Balenos loop. (Same byproducts as the Floramos Liana quest.)
- **Weekly Contribution quests** — large chunks.
- **One-time regional quest CP** — 2 years away = big untapped pools (LoML, newer regions).
- **Basic resource turn-ins** (weeds/logs/rough stones) at some NPCs.

**Visibility (Jon can't tell me what he's done — solved):** the quest log (**O**) → **"Recurring" tab**
lists exactly which repeatable CP quests are available to him *now*; one-time quests only appear if
uncompleted. So no need to track history — the game filters it. Just work the Recurring tab + unrun regions.

## Node-optimizer tools (the "compute optimal, then set it up in-game" idea — already built)

- **[bdo-empire](https://github.com/Thell/bdo-empire)** (`pipx install bdo-empire`, Python 3.12+) —
  input a **CP budget + price list**, it solves the **optimal node/worker allocation from scratch** (MIP
  solver, ~exact). **Doesn't need Jon's current setup** → dodges the visibility problem entirely. Output
  imports to **Workerman**; replicate it in-game. Accounts for node chains, worker types, lodging/CP.
- **[bdo-node-ranks](https://bdo-node-ranks.treaplabs.com/)** / **[bdoworker.com](https://bdoworker.com/)**
  — live node rankings by **silver-per-CP** (the metric that matters — factors the connection chain).

**Implication for bdo-cmd:** don't rebuild the node optimizer (bdo-empire is better than we'd make).
Optional integration: bdo-cmd could generate the **price list** for bdo-empire from Jon's real
buy-order/order-book prices.

## The flywheel

Cook (already) → Witch's Delicacy → **CP** → feed **bdo-empire** → optimal nodes → passive silver →
**sell raws** (per the crafting reality-check: raws usually beat crafting). This is the passive engine.
