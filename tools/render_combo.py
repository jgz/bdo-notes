#!/usr/bin/env python3
"""Render a BDO combo / DPS-priority spec into a self-contained HTML graphic,
transposing default-hotkey skill commands into Jon's ESDF keys.

Inputs (all JSON):
  - data/keybinds/account.json   his default->his keybind remap
  - data/skills/<class>.json     the class skill database (default 'command' per skill)
  - a spec file                  type "combo" or "priority" (data/combos/*.json)

Icons: if a skill's "icon" names a file under assets/skills/<class>/, it's embedded
as a data URI. Missing icons just render name + keys (graceful).

Usage:
  python3 tools/render_combo.py data/combos/maegu-dps-priority.json \
      -o handbook/combat/maegu-dps-priority.html

  # override skill DB / keybinds if needed:
  python3 tools/render_combo.py <spec> --skills data/skills/maegu.json \
      --keybinds data/keybinds/account.json -o out.html
"""
import argparse
import base64
import html
import json
import mimetypes
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MOUSE = {"LMB", "RMB"}
MOD = {"Shift", "Space"}
DIRS = {"W", "A", "S", "D"}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_maps(kb):
    d_def, d_his = kb["default_directions"], kb["directions"]
    dir_map = {d_def[k]: d_his[k] for k in ("forward", "left", "back", "right")}
    skill_map = kb.get("skill_key_remap", {})
    return dir_map, skill_map


def transpose_token(tok, dir_map, skill_map):
    """Return (rendered_key, category) for a single default token."""
    if tok in MOUSE:
        return tok, "mouse"
    if tok in MOD:
        return tok, "mod"
    if tok in DIRS:
        return dir_map[tok], "move"
    # otherwise a skill key (single letter etc.)
    return skill_map.get(tok, tok), "skill"


def transpose_command(cmd, dir_map, skill_map):
    """Parse a default command like 'W/S+E' -> list of parts; each part is a list
    of (key, category) alternatives. Returns None for a null/empty command."""
    if not cmd:
        return None
    parts = []
    for part in cmd.split("+"):
        alts = [transpose_token(t.strip(), dir_map, skill_map) for t in part.split("/")]
        parts.append(alts)
    return parts


def caps_html(parts):
    """Render transposed command parts into keycap HTML."""
    if parts is None:
        return '<span class="followup">follow-up</span>'
    out = []
    for i, alts in enumerate(parts):
        if i:
            out.append('<span class="plus">+</span>')
        alt_html = []
        for j, (key, cat) in enumerate(alts):
            if j:
                alt_html.append('<span class="slash">/</span>')
            alt_html.append(f'<span class="cap {cat}">{html.escape(key)}</span>')
        out.append("".join(alt_html))
    return '<span class="combo">' + "".join(out) + "</span>"


def icon_data_uri(icon, cls):
    if not icon:
        return None
    path = os.path.join(ROOT, "assets", "skills", cls, icon)
    if not os.path.isfile(path):
        return None
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def skill_chip(slug, skills, cls, dir_map, skill_map):
    """One skill: icon (if any) + name + transposed keys."""
    sk = skills.get(slug)
    if not sk:
        return f'<span class="skill-chip missing">?{html.escape(slug)}?</span>'
    warn = "UNVERIFIED" in (sk.get("note") or "")
    uri = icon_data_uri(sk.get("icon"), cls)
    icon = (f'<img class="ico" src="{uri}" alt="">' if uri
            else '<span class="ico ph"></span>')
    keys = caps_html(transpose_command(sk.get("command"), dir_map, skill_map))
    warn_html = ' <span class="warn" title="command unverified — confirm in skill window">&#9888;</span>' if warn else ""
    return (
        f'<span class="skill-chip">{icon}'
        f'<span class="body"><span class="nm">{html.escape(sk["name"])}{warn_html}</span>'
        f'{keys}</span></span>'
    )


def slot_html(slot, skills, cls, dir_map, skill_map):
    """A slot = list of alternative skill slugs, rendered slug1 / slug2."""
    chips = [skill_chip(s, skills, cls, dir_map, skill_map) for s in slot]
    return '<span class="or-sep">or</span>'.join(chips)


def sequence_html(slots, skills, cls, dir_map, skill_map):
    """A sequence of slots, joined by an arrow."""
    return '<span class="seq-arrow">&rarr;</span>'.join(
        slot_html(s, skills, cls, dir_map, skill_map) for s in slots)


CSS = """
:root{--ground:#151109;--panel:#1c1810;--panel-2:#221d13;--edge:#3c3220;
--cap:#2a2417;--cap-hi:#332c1c;--cap-edge:#493d26;--gold:#e2c06d;--gold-dim:#a98f4e;
--ink:#efe6d2;--muted:#9d927b;--faint:#6b6353;--move:#e2c06d;--skill:#6f9fc4;--mouse:#c8b489;--mod:#8f866f;
--top:#d98b57;--core:#8fb17a;--filler:#7f93b8;}
*{box-sizing:border-box}
body{margin:0;color:var(--ink);font-family:"Barlow Semi Condensed",system-ui,sans-serif;
background:radial-gradient(120% 80% at 50% -10%,#241d10 0%,var(--ground) 60%) fixed;
padding:clamp(14px,3vw,40px);display:flex;justify-content:center}
.sheet{width:100%;max-width:1120px}
header{margin-bottom:1.2rem}
.rule{height:2px;background:linear-gradient(90deg,transparent,var(--gold-dim),var(--gold),var(--gold-dim),transparent);opacity:.8;margin-bottom:1rem}
h1{font-family:"Cinzel",serif;font-weight:700;color:var(--gold);margin:0;font-size:clamp(1.5rem,3.6vw,2.2rem);text-shadow:0 1px 0 #000;text-wrap:balance}
.sub{color:var(--muted);font-size:.95rem;margin-top:.25rem}.sub b{color:var(--ink);font-weight:600}
.src{color:var(--faint);font-size:.8rem;margin-top:.35rem;font-style:italic}
.legend{display:flex;flex-wrap:wrap;gap:.4rem .9rem;align-items:center;background:linear-gradient(180deg,var(--panel-2),var(--panel));
border:1px solid var(--edge);border-radius:10px;padding:.6rem .9rem;margin:1rem 0 1.5rem;font-size:.8rem;color:var(--muted)}
.legend .lb{color:var(--gold-dim);text-transform:uppercase;letter-spacing:.12em;font-size:.7rem;font-weight:600}
.legend .sw{display:inline-block;width:.7rem;height:.7rem;border-radius:2px;vertical-align:-1px;margin-right:.3rem}
.notes{margin:0 0 1.4rem;padding-left:1.1rem;color:var(--muted);font-size:.86rem}.notes li{margin:.2rem 0}
.notes b{color:var(--ink);font-weight:600}
/* skill chip */
.skill-chip{display:inline-flex;align-items:center;gap:.5rem;vertical-align:middle}
.skill-chip .ico{width:2.1rem;height:2.1rem;border-radius:7px;border:1px solid var(--cap-edge);flex:none;object-fit:cover;background:#0003}
.skill-chip .ico.ph{background:linear-gradient(135deg,#2c2519,#211c14)}
.skill-chip .body{display:flex;flex-direction:column;gap:.2rem;min-width:0}
.skill-chip .nm{font-weight:600;font-size:.9rem;color:var(--ink);line-height:1.05}
.warn{color:var(--top)}
.combo{display:inline-flex;flex-wrap:wrap;align-items:center;gap:.24rem}
.cap{display:inline-flex;align-items:center;justify-content:center;min-width:1.55rem;height:1.55rem;padding:0 .4rem;border-radius:6px;
font-weight:700;font-size:.8rem;line-height:1;background:linear-gradient(180deg,var(--cap-hi),var(--cap));border:1px solid var(--cap-edge);
border-bottom-width:3px;color:var(--ink);box-shadow:0 1px 0 #0006}
.cap.move{border-bottom-color:var(--move);color:#ffe9a8;background:linear-gradient(180deg,#4a3d1e,#37301b);border-color:#7a6533;box-shadow:0 0 0 1px #e2c06d44}
.cap.skill{border-bottom-color:var(--skill);color:#c9e0f2}
.cap.mouse{border-bottom-color:var(--mouse)}
.cap.mod{border-bottom-color:var(--mod);color:var(--muted);font-size:.72rem}
.plus{color:var(--muted);font-weight:700;font-size:.82rem}.slash{color:var(--faint);font-weight:600;font-size:.8rem}
.followup{color:var(--faint);font-style:italic;font-size:.82rem}
.or-sep{display:inline-block;margin:0 .5rem;font-size:.66rem;text-transform:uppercase;letter-spacing:.12em;color:var(--faint)}
.seq-arrow{margin:0 .5rem;color:var(--gold-dim);font-size:1rem}
/* combo steps */
.flow{display:flex;flex-wrap:wrap;gap:.7rem;align-items:stretch}
.step{position:relative;flex:1 1 160px;min-width:150px;display:flex;flex-direction:column;justify-content:center;
background:linear-gradient(180deg,var(--panel-2),var(--panel));border:1px solid var(--edge);border-radius:11px;padding:.85rem .7rem .8rem}
.step.opt{border-style:dashed;border-color:#4a4636}
.step .no{position:absolute;top:-.6rem;left:-.6rem;width:1.5rem;height:1.5rem;border-radius:50%;background:var(--gold);color:#1a1509;
font-weight:700;font-size:.8rem;display:grid;place-items:center;font-family:"Cinzel",serif;box-shadow:0 1px 4px #0007}
.step .opttag{position:absolute;top:-.55rem;right:.5rem;font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);background:var(--panel);padding:0 .3rem}
.step .note{color:var(--muted);font-size:.76rem;margin-top:.45rem}
.step .alt{display:flex;flex-direction:column;gap:.35rem}
/* priority tiers */
.tier{margin-bottom:1.3rem;background:linear-gradient(180deg,var(--panel-2),var(--panel));border:1px solid var(--edge);border-radius:12px;overflow:hidden}
.tier>.head{display:flex;align-items:center;gap:.6rem;padding:.6rem .95rem;border-bottom:1px solid var(--edge)}
.tier>.head .dot{width:.65rem;height:.65rem;border-radius:50%}
.tier>.head h2{font-family:"Cinzel",serif;font-size:.95rem;letter-spacing:.04em;margin:0;color:var(--ink)}
.tier>.head .cnt{margin-left:auto;color:var(--faint);font-size:.72rem;text-transform:uppercase;letter-spacing:.12em}
.entries{display:flex;flex-direction:column}
.entry{display:flex;align-items:center;gap:.7rem;padding:.6rem .95rem;border-left:3px solid transparent}
.entry+.entry{border-top:1px solid #ffffff08}
.entry .rank{font-family:"Cinzel",serif;color:var(--faint);font-size:.82rem;min-width:1.2rem;text-align:right}
.entry .body{display:flex;flex-wrap:wrap;align-items:center;gap:.3rem .5rem}
.entry .enote{color:var(--muted);font-size:.76rem;font-style:italic;margin-left:.3rem}
.tier.top .entry{border-left-color:var(--top)}.tier.core .entry{border-left-color:var(--core)}.tier.filler .entry{border-left-color:var(--filler)}
.tier.top .dot{background:var(--top)}.tier.core .dot{background:var(--core)}.tier.filler .dot{background:var(--filler)}
/* extras */
.extras{margin-top:1.5rem;display:grid;gap:.7rem;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.ex{background:linear-gradient(180deg,var(--panel-2),var(--panel));border:1px solid var(--edge);border-radius:10px;padding:.75rem .9rem}
.ex h3{font-family:"Cinzel",serif;font-size:.76rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--gold-dim);margin:0 0 .5rem}
.ex p{margin:.4rem 0 0;color:var(--muted);font-size:.82rem}
footer{margin-top:1.5rem;padding-top:.9rem;border-top:1px solid var(--edge);color:var(--faint);font-size:.78rem}
footer b{color:var(--muted);font-weight:600}
""".strip()

LEGEND = (
    '<div class="legend"><span class="lb">Your keys</span>'
    '<span><span class="sw" style="background:var(--move)"></span>Move E S D F</span>'
    '<span><span class="sw" style="background:var(--skill)"></span>Skill keys (Q&rarr;W E&rarr;R F&rarr;A)</span>'
    '<span><span class="sw" style="background:var(--mouse)"></span>LMB / RMB</span>'
    '<span><span class="sw" style="background:var(--mod)"></span>Shift / Space</span></div>'
)


def header_html(spec):
    src = spec.get("source")
    return (
        '<header><div class="rule"></div>'
        f'<h1>{html.escape(spec["title"])}</h1>'
        f'<div class="sub">Converted to your <b>ESDF</b> keys &middot; {html.escape(spec.get("subtitle",""))}</div>'
        + (f'<div class="src">Source: {html.escape(src)}</div>' if src else "")
        + "</header>"
    )


def notes_html(spec):
    ns = spec.get("notes") or []
    if not ns:
        return ""
    items = "".join(f"<li>{html.escape(n)}</li>" for n in ns)
    return f'<ul class="notes">{items}</ul>'


def render_combo(spec, skills, cls, dm, sm):
    steps = []
    for i, st in enumerate(spec["steps"], 1):
        opt = st.get("optional")
        inner = sequence_html(st["slots"], skills, cls, dm, sm)
        note = f'<div class="note">{html.escape(st["note"])}</div>' if st.get("note") else ""
        tag = '<span class="opttag">optional</span>' if opt else ""
        steps.append(
            f'<div class="step{" opt" if opt else ""}"><span class="no">{i}</span>{tag}'
            f'<div class="alt">{inner}</div>{note}</div>'
        )
    flow = f'<div class="flow">{"".join(steps)}</div>'
    extras = ""
    if spec.get("extras"):
        cards = []
        for ex in spec["extras"]:
            body = sequence_html(ex["slots"], skills, cls, dm, sm)
            cards.append(
                f'<div class="ex"><h3>{html.escape(ex["title"])}</h3>{body}'
                + (f'<p>{html.escape(ex["text"])}</p>' if ex.get("text") else "")
                + "</div>"
            )
        extras = f'<div class="extras">{"".join(cards)}</div>'
    footer = ('<footer><b>Optional</b> steps only pay off with high attack speed (BSR / Shai buffs). '
              'Gold caps are movement; blue caps are the skill keys you relocated '
              '(<b>Q&rarr;W, E&rarr;R, F&rarr;A</b>).</footer>')
    return LEGEND + flow + extras + footer


def render_priority(spec, skills, cls, dm, sm):
    tiers = []
    for tier in spec["tiers"]:
        acc = tier.get("accent", "core")
        entries = []
        for k, ent in enumerate(tier["entries"], 1):
            body = sequence_html(ent["slots"], skills, cls, dm, sm)
            enote = f'<span class="enote">{html.escape(ent["note"])}</span>' if ent.get("note") else ""
            entries.append(
                f'<div class="entry"><span class="rank">{k}</span>'
                f'<span class="body">{body}{enote}</span></div>'
            )
        tiers.append(
            f'<div class="tier {acc}"><div class="head"><span class="dot"></span>'
            f'<h2>{html.escape(tier["name"])}</h2><span class="cnt">{len(tier["entries"])} entries</span></div>'
            f'<div class="entries">{"".join(entries)}</div></div>'
        )
    footer = ('<footer>Work top-down: cast the highest-tier skill that\'s off cooldown. '
              'Gold caps are movement; blue caps are the skill keys you relocated '
              '(<b>Q&rarr;W, E&rarr;R, F&rarr;A</b>). &#9888; = command not yet verified in your skill window.</footer>')
    return LEGEND + notes_html(spec) + "".join(tiers) + footer


def main():
    ap = argparse.ArgumentParser(description="Render a BDO combo/priority spec into HTML in Jon's keys.")
    ap.add_argument("spec", help="path to a combo/priority spec JSON")
    ap.add_argument("-o", "--out", required=True, help="output HTML path")
    ap.add_argument("--skills", help="skills DB (default: data/skills/<class>.json)")
    ap.add_argument("--keybinds", default=os.path.join(ROOT, "data/keybinds/account.json"))
    args = ap.parse_args()

    spec = load_json(args.spec)
    cls = spec["class"]
    skills_path = args.skills or os.path.join(ROOT, f"data/skills/{cls}.json")
    skills = {s["slug"]: s for s in load_json(skills_path)["skills"]}
    kb = load_json(args.keybinds)
    dm, sm = build_maps(kb)

    if spec["type"] == "combo":
        body = render_combo(spec, skills, cls, dm, sm)
    elif spec["type"] == "priority":
        body = render_priority(spec, skills, cls, dm, sm)
    else:
        sys.exit(f"unknown spec type: {spec['type']}")

    page = (
        f'<title>{html.escape(spec["title"])}</title>\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cinzel:wght@600;700&family=Barlow+Semi+Condensed:wght@400;500;600;700&display=swap">\n'
        f"<style>{CSS}</style>\n"
        f'<div class="sheet">{header_html(spec)}{body}</div>\n'
    )
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"wrote {args.out} ({len(page)} bytes)")


if __name__ == "__main__":
    main()
