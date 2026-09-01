# Forest Path Wagon — crafting tracker

> Goal: finish upgrading all wagon gear. A full wagon = **4 gear pieces, one each**: **Wheel, Cover, Flag,
> Badge** (trains 4 horses). Jon crafts **multiples of each** as enhancement fodder — enhancing a part
> consumes duplicates to recover max durability. Current focus: **10× Wheel**.
> Crafted at the **Level 4 Wagon Part Workshop, Grána 3-2 2F**.
> Sources: [BDFoundry](https://www.blackdesertfoundry.com/forest-path-wagon-guide/) ·
> [GrumpyG](https://grumpygreen.cricket/forest-path/) · [BDO Codex Steel](https://bdocodex.com/us/mrecipe/27/) ·
> [Codex Merindora (repeat)](https://bdocodex.com/us/quest/6605/3/). Stock from holdings.db (2026-09-01).

## Merindora's Element — repeatable now (no daily cap)
Old daily quest was replaced (Jan 2024). After the one-time **Lv56+ Merindora** quest, exchange
**10 yellow-grade meals → 1 Merindora's Element** at **Merindora (Grána)**, unlimited. **Balenos Meal
counts** — Jon's cooking op feeds this directly.

## Wheel recipe (per wheel)
`30 Loopy Tree Timber + 60 Steel + 1,000 Piece of Image` — Lv4 Wagon Part Workshop.
- **Steel** — Heating: `5 Melted Iron Shard + 5 Coal → 1–4 Steel` (yield scales with mastery, ~2 avg).
- **Piece of Image** — Simple Alchemy: `1 Merindora's Element + 300 Trace of Nature + 100 Weeds → 150`.
- **Merindora's Element** — 10 Balenos Meal each (exchange at Grána).
- ⚠️ **Piece of Image & Merindora's Element are non-marketable** (bound) — must be crafted, can't buy.

## 10× Wheel — bill of materials vs. inventory (2026-09-01)
| Material | Need (×10) | Have | Gap | Source |
|---|--:|--:|--:|---|
| Loopy Tree Timber | 300 | 36,163 | ✅ | 🏭 node |
| Melted Iron Shard | ~1,500 | 4,852 | ✅ | have / from Iron Ore |
| **Coal** | ~1,500 | 0 | −1,500 | 🏭 worker node (below) |
| **Steel** (craft) | 600 | 0 | craft | ⚙️ Heating |
| **Trace of Nature** | 20,100 | 3,483 | −16,617 | 🏭 excavation nodes (below) — **the bottleneck** |
| **Weeds** | 6,700 | 397 | −6,303 | 💰 CM buy-order (~10k ea, ~63M gap) |
| **Merindora's Element** | 67 | 0 | −67 | 🍽️ 670 Balenos Meal → Grána |
| **Piece of Image** (craft) | 10,000 | 89 | craft | ⚗️ Simple Alchemy ×67 |

**Full 4-part project at ×10** (rough): ~40,000 Piece of Image → ~**80k Trace of Nature**, ~27k Weeds,
~2,670 Balenos Meals, ~267 Merindora's Elements. Trace of Nature dominates — see cost note.

## The real cost = Trace of Nature
Live NA order book (2026-09-01): sellers **293k**, buy-order wall **~265–267k**. So **buying** Trace of
Nature is ~**270k each** → **~4.4B for the 10-wheel gap alone** (~22B for the full ×10 set). **Produce
it, don't buy it.** (Confirm price in-client before trusting the billions figure.)

### Trace of Nature = excavation nodes (Jon's plan: spread free CP onto more)
All excavation sub-nodes: invest CP in the host node → talk to Node Manager → spend **35 energy** to
unlock the excavation. Usually ~5 worker slots (Trace of Nature + vendor items). **Reach-CP is
network-dependent** — ordered by tier; Jon marks which host nodes he already owns, then I pull exact
activation CP for the missing candidates.

| Tier (reach) | Node | Region | Own? | Notes |
|---|---|---|:--:|---|
| 2 mid | **Pila Fe (2 nodes)** | Valencia (border) | ✅ | workers pending — assign from **Altinova** or **Sand Grain Bazaar**; see [reminders](../reminders.md) |
| 1 old-world | Ancient Stone Chamber | Balenos | ? | |
| 1 old-world | Glish Ruins | Serendia | ? | |
| 1 old-world | Lynch Farm Ruins | Serendia | ? | |
| 1 old-world | Bernianto Farm | Calpheon | ? | |
| 1 old-world | Mansha Forest | Calpheon | ? | |
| 1 old-world | Rhua Tree Stub | Calpheon | ? | |
| 1 old-world | Ancient Ruins | Mediah | ? | |
| 2 mid | Pilgrim's Sanctum | Valencia | ? | |
| 2 mid | Tooth Fairy Forest | Kamasylvia | ? | |
| 2 mid | **Sherekhan Necropolis** | Drieghan | ? | ⭐ highest Trace-of-Nature yield; near Duvencrune |
| 2–3 mid | Star's End | Calpheon | ? | geographically remote SE — reach may be Tier 3 |
| 3 remote | Sherekhan Iron Mine | Everfrost | ? | |
| 3 remote | Zvier Highlands | Everfrost | ? | |
| 3 remote | Crypt of Resting Thoughts | Odyllita | ? | |
| 3 remote | Mountain of Division | Odyllita | ? | |
| 3 remote | Tungrad Ruins | Ulukita | ? | |
| 3 remote | Great Dark Spot | Edania | ? | |
| 3 remote | Urnas Mountains | Edania | ? | |
| 3 remote | Beombawi Valley | Morning Light | ? | |
| 3 remote | Dokkebi Forest | Morning Light | ? | |
| 3 remote | Golden Pig Cave | Morning Light | ? | |
| 3 remote | Haemo Island | Morning Light | ? | |
| 3 remote | Myeonggyun Hall | Morning Light | ? | |

_Fill the **Own?** column (✅/❌) as you check your map; hand me the ❌ candidates and I'll pull exact activation CP + cheapest connection path._
_⚠️ Not exhaustive — Pila Fe wasn't in the source list, so other Trace-of-Nature nodes may exist too._

## Coal nodes (worker)
1–2 workers trickle out the ~1,500 coal passively. See the [reminders](../reminders.md) to-do to improve
the Keplan loadout.

| Node | Region | Notes |
|---|---|---|
| **Keplan Quarry** | Calpheon | classic cheap-CP pick (also Powder of Rifts) |
| Glutoni Cave | Calpheon | also Powder of Rifts |
| Omar Lava Cave | Valencia | alternate |

## Build order (10 wheels)
1. Cook meals → hand **670 Balenos Meal** to Merindora → **67 Elements**.
2. Bulk **Trace of Nature ~16.6k** (excavation nodes) + buy-order **Weeds ~6.3k**.
3. Simple Alchemy ×67 → **10,050 Piece of Image**.
4. Worker **Coal** → Heat w/ Melted Iron Shard → **600 Steel**.
5. Craft **10 Wheels** (300 Timber + 600 Steel + 10,000 Image).

## TODO / open
- [ ] Jon: mark which Trace-of-Nature host nodes he already owns → get exact CP for the rest.
- [ ] Confirm Trace of Nature ~270k price in-client.
- [ ] Cover / Flag / Badge recipes + ×10 BOM (not yet pulled).
- [ ] Verify whether Special Balenos Meal is accepted by Merindora (would free up the 4,820 stock).
