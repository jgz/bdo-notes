# Horse Training — pipeline reference

> Last updated 2026-08-23. The T8→T9→T10 horse pipeline (a system Jon didn't know well) + the key
> corrections. Reference data — not an AFK-training how-to.

## Corrections to common assumptions

- **A finished horse (e.g. Doomeezy, T10) does nothing on a wagon team.** Wagon Mount EXP is **split**
  across the hitched horses, and **skills are NOT shared between horses** (per-horse RNG). Also **never
  wagon a Dream/Mythical horse** (wagons nullify costume-set effects). Doomeezy = personal mount only.
- **T8 → T9 uses ONE courser**, awakened repeatedly (it survives failures). The "two same-type horses"
  rule is only the **T9 → T10 Mythical** step.
- **A horse's skill-slot COUNT is fixed at birth** — but *which* skills fill those slots is re-rollable
  now (see Level Down Ticket below). So a horse with enough slots for the 7 courser skills can be
  *finished* by re-rolling; only a horse with too few slots is a true dud. Level candidates solo;
  Imperial-Deliver the genuine duds.

## The ladder

1. **Breed to Tier 8.** Male breeds 2×, female 1×; when spent, **Exchange** (35k silver, destroys both
   parents → one higher-tier shot). Offspring tier scales with parent levels + **Training Mastery**.
2. **Courser awaken** the T8 = learn all **7 courser skills** + reach **Lv 30**.
3. **Courser-train to 200%** across Skill / Elegance / Strength (green mats +1%, blue +2%; each caps 180%).
4. **Awaken → T9 Dream Horse** at Gula (Stonetail) or Melabee (Grána). **1% + 0.2%/failstack**; ~30
   Agris stacks = guaranteed; Cron makes a fail drop to 100% instead of wiping. **~15–35 attempts**
   typical (courser survives fails). **Highest stat picks the type: Skill→Arduanatt, Elegance→Diné,
   Strength→Doom.**
5. **T9 → T10 Mythical:** two same-type **Lv 30** T9s (M + F) + a **Mythical Censer**, **3% + 0.2%/fail**;
   success consumes both, failure returns both. All three Mythicals → **Krogdalo's Sanctuary**.

**Krogdalo's Origin Stone** (id 50801, for Courser awakening): **buy off the Central Market** — **~40M
each, deep supply** (~278 listed, 2026-08-25). It also appears in the **Atanis' Element** exchange
(Merindora), but that is **NOT** its main source — **don't grind Atanis dailies for these**; the market
is cheap and unlimited. Only convert *leftover* Atanis' Elements (e.g. Jon's ~30 post-infinite-potion)
since they'd otherwise sit unused.

**Method:** wagon (Forest Path, 4 horses) = bulk-level breeding fodder; **solo** = courser candidates &
leveling a Dream/Mythical (keeps costume set + full per-level skill rolls). Mount EXP scales with
distance/speed. Training Guru 20 ≈ ~100% skill-learn per level.

### Wagon vs solo — the rule
- **Wagon = throughput.** 4 horses at once; aggregate EXP ~5% *better* than solo, but split 4 ways so
  each horse levels ~4× slower **and learns fewer skills**. Right tool for the fodder factory.
- **Solo = one horse, fast, full skill rolls.** Use for **any T8 you want to courser** and for
  **all T9/T10** (wagon also nullifies the Dream/Mythical costume set).
- **Never wagon a courser candidate.** Skills are per-horse RNG on level-up; fewer level-ups = fewer of
  the 7 courser skills. _(Source: [GrumpyG leveling](https://grumpygreen.cricket/horse-leveling-routes-methods/).)_

### Keep-or-deliver triage (at the "out of breed charges" gate)
Don't auto-deliver everything. For each spent T8, check its **skills + gender**:
- **Strong skills (esp. the `S:` ones) →** pull it out, **solo to Lv 30**, finish the 7 courser skills,
  awaken → courser → T9. Steer the stat you train toward the type you need — **Elegance → Diné**
  (Jon's current bottleneck), Skill → Arduanatt, Strength → Doom.
- **Weak / duplicate / wrong type →** Imperial-deliver (banks Golden Seals + Flowers of Oblivion) or
  Exchange for a tier-up shot.

**AFK route:** base out of **Stonetail Horse Ranch** (by Heidel). Loop a **straight, low-turn road** —
classics: **Heidel↔Velia** or **Heidel→above Lynch Farm Ruins**; a **city loop** is safest overnight
(open roads aren't a safe zone). Turns slow the horse → less EXP, so straighter = better. Drag the
auto-path marker to empty minimap space to force an infinite **green** back-and-forth.

**⚠️ Leveling is now BANKED (early-2026 rework) — horses don't auto-level.** Riding/AFK accumulates
training EXP into a **pool** on the horse; you must **manually apply it via the Harnessed Horse List →
"Level Up"**. The auto-loop still earns the XP — but there's now a follow-up step to apply the levels
(and the XP bar shows partial progress poorly). So an overnight loop = a morning "Level Up" pass.

**Mount Level Down Ticket — the skill/stat re-roll.** Drops a checked-in mount **1 level** at the Stable
Keeper, reverting the **stat + skill learned at that level**; re-leveling gives a **fresh RNG roll**.
Use it to **fish for a missing courser skill** (level a near-30 candidate down/up until it learns the
last skill it needs — turns former "duds" into finishable coursers) or to re-roll a Dream/Mythical's
stat gain. Rules: **1 level per ticket**, can't reuse until it levels up again, **Lv 2–30 only**, and
it's a **consumable ticket** (Pearl/loyalty/events) — spend it on the one stubborn skill, not casually.
_(Source: [official Mount Level Down Ticket](https://www.naeu.playblackdesert.com/en-us/Wiki?wikiNo=420).)_

## Training-EXP boosts (reference)

Value Pack +30% mount EXP · Fiery Celerity Draught +30/+30 (600 min) · Trainer's Clothes (Loggia ~28% →
Manos ~40% Training EXP at TET) · Stonetail Wind's Meal · Secret Book of Old Moon +50% Life EXP.

## Imperial Horse Delivery (reject sink)

Stable → Check In → Imperial Horse Delivery (horse **Lv 15+**). Pays ~50% of market (**don't deliver
good coursers** — market ≈ 2×). Gives **Golden Seals = horse's TIER** (T8 = 8) and **Flowers of
Oblivion** (1 @T1 → 20 @T8). **100 Flowers per T10 Mythical attempt** — so delivering high-tier rejects
banks them for the Krogdalo grind.

## Jon's Krogdalo path

Has **Doomeezy (T10) free** + **two T9 Arduanatts** (the original + **Peggers**, Lv 24, found
2026-08-29 — see [account/horses.md](../account/horses.md)). So the **Arduanatt pair may already be
complete** — pending three checks: both at **Lv 30**, **opposite genders** (M + F), and neither being a
restricted event/coupon variant. Still to produce via the ladder: **two T9 Dinés** → T10 Diné → then
T10 Arduanatt + T10 Diné + Doomeezy → Krogdalo's Sanctuary. Long-haul overnight project.
_(Open: confirm Peggers is genuinely a 2nd Arduanatt, not the one already counted; and event/coupon
eligibility as awakening material — verify in-game.)_

_Sources: GrumpyG, BDFoundry, official wiki (2026). Ballpark figures (imperial silver, ~15–35 attempts)
vary by patch/RNG._
