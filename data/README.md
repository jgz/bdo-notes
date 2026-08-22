# Skill / combo data + rendering pipeline

A reusable, per-character system: keep skills as data, and generate combo / DPS-priority **graphics
in Jon's keys** from it. Guides are written in **default hotkeys**; the renderer transposes them to
Jon's ESDF layout automatically. Built 2026-08-21 for Maegu; the same shape works for any character.

## Layout

```
data/
  keybinds/account.json        Jon's account-wide default->his remap (dirs + skill keys)
  skills/<class>.json          the class skill DB — one 'command' (DEFAULT keys) per skill
  combos/<name>.json           a spec: type "combo" (ordered steps) or "priority" (ranked tiers)
assets/
  skills/<class>/<slug>.png    optional skill icons (embedded as data URIs when present)
tools/
  render_combo.py              spec + skills + keybinds  ->  self-contained HTML graphic
handbook/combat/*.html         generated output (published as Artifacts)
```

## How transposition works

`account.json` holds two maps. The renderer classifies each token of a skill's **default** command
and applies the right one:

- **Movement directions** (`W/A/S/D`) → Jon's movement (`E/S/D/F`).
- **Skill keys** (the letter that fires the skill) → Jon's relocated keys (`Q→W, E→R, F→A`).
- **Unchanged**: `Shift`, `Space`, `LMB`, `RMB`, `C`, `X`, `Z`.

So a skill stored as `"command": "W/S+E"` renders as `E/D + R` for Jon. Full rule + worked example:
[`handbook/combat/combo-transposition.md`](../handbook/combat/combo-transposition.md).

## Generate

```bash
python3 tools/render_combo.py data/combos/maegu-dps-priority.json -o handbook/combat/maegu-dps-priority.html
python3 tools/render_combo.py data/combos/maegu-infinite.json     -o handbook/combat/maegu-infinite-combo.html
```

Then publish the HTML as an Artifact (favicon in each spec's `favicon` field). A skill whose
`command` isn't confirmed for Jon's binds carries `UNVERIFIED` in its `note`; the renderer marks it
with ⚠ so it's obvious what still needs a skill-window check.

## Adding a new combo (the common case)

1. Paste the combo from Discord/guide (skill **names** + default keys, or icons that expand to names).
2. Make sure each skill exists in `data/skills/<class>.json` (add it with its default `command`).
3. Write a small spec in `data/combos/` (see the two Maegu examples for the shape).
4. Run the renderer, publish. Done — it's in Jon's keys automatically.

## Adding a new character/class

Copy `data/skills/maegu.json` to `data/skills/<class>.json`, fill in that class's skills + default
commands. `account.json` is shared (Jon's keybinds are account-wide), so combos for every character
transpose the same way.

## Icons

Drop `<slug>.png` files in `assets/skills/<class>/` matching each skill's `icon` field; the renderer
inlines them as data URIs (required — Artifacts block external images via CSP). Missing icons render
name + keys only, so the pipeline works with or without them.
