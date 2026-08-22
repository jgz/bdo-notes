# Combos in Jon's keys — the transposition method

> Last updated: 2026-08-21. The problem: BDO guides/Discord write combos in **default hotkeys**
> (or bare skill icons), and Jon plays a **fully shuffled ESDF layout** — he moved the skill keys too,
> not just movement. This is the rule to convert any combo to his keys, plus the first worked
> example. Visual: [maegu-infinite-combo.html](maegu-infinite-combo.html).

## Jon's remap (confirmed by Jon, 2026-08-21)

He shifted movement to **ESDF** and relocated the displaced skill keys around it, same orientation.
To convert a default-key combo, classify each token by what it is in the **default** layout:

**Movement directions** (W/A/S/D in the guide → the direction he holds):

| Default | Jon | |
|---|---|---|
| W (forward) | **E** | ↑ |
| A (left) | **S** | ← |
| S (back) | **D** | ↓ |
| D (right) | **F** | → |

**Skill keys** (the guide's letter that triggers the skill):

| Default | Jon |
|---|---|
| **Q** | **W** |
| **E** | **R** |
| **F** | **A** |
| C · X · Z · Shift · Space · LMB · RMB | **unchanged** |

So a guide's `W` means two different things depending on context: as a *direction* → his **E**; as a
*skill key* it doesn't appear (Q is what maps to W). Work token by token. _(C/X/Z assumed unchanged —
Jon only called out moving Q/E/F; flag if any feel off.)_

## Worked example — Maegu "Infinite Combo" (Netherax [𝟋ox] Maegu guide, Discord)

Source: Discord Maegu guide by Netherax [𝟋ox]; default-key + skill-name combo pasted 2026-08-21
([screenshot](../../research/account/2026-08-21-maegu-infinite-combo-default.png)). "Loopable combo
for new/lazy players at tanky spots" — the author recommends the DPS-priority playstyle once
comfortable on the class. Endgame full loop:

| # | Skill | Default | **Jon's keys** |
|---|---|---|---|
| 1 | **Flower Shroud** (starter A) | W/S + E | **E/D + R** |
| 1 | *or* **Bared Claws** (starter B) | A/D + LMB | **S/F + LMB** |
| 2 | **Foxspirit Tag** | RMB | **RMB** |
| 3 | **Nukduri Dance** | Shift + C | **Shift + C** |
| 3 | *or* **Charmed** | Space | **Space** |
| 4 | **Spirited Away** | S + LMB | **D + LMB** |
| 5 | **Petal Play** | Shift + LMB | **Shift + LMB** |
| 6 | *{opt}* **Heavenly Return** | Shift + X | **Shift + X** |
| 7 | **Heavenward Dance** | W + RMB | **E + RMB** |
| 8 | *{opt}* **Foxflare** | Shift + Q | **Shift + W** |
| 9 | **Spirit Swirl** (finisher A) | Shift + F | **Shift + A** |
| 9 | *or* **Bristling Sparks** (finisher B) | Shift + RMB | **Shift + RMB** |

Extras:
- **Lurking Claws** (reposition — insert anywhere *except* between Spirited Away → Petal Play):
  S + F → **D + A**.
- Out of spells → **Constricting Charm → Spirit Sparks**: Shift + Z → LMB → **Shift + Z → LMB**.
- `{opt}` spells: add only with high attack speed (BSR / Shai buffs).

This is a reusable format — paste any future combo string (with skill names) and it converts the
same way.
