# Research Packet — Black Desert Online

The **evidence layer.** Everything here is **sourced and dated** (see frontmatter in each file). The
rule: handbook answers come from this packet or a live lookup — **never from memory**, and never
from 2-year-old recall of how BDO used to work. When in doubt, re-fetch.

## Frontmatter convention

Every research file starts with:

```yaml
---
title: <what this file covers>
system: <which system/skill, or "meta">
source: <primary URL(s) / in-game screenshot / patch note>
fetched: YYYY-MM-DD             # when the source was captured
confidence: high | medium | low
---
```

BDO patches often. If a load-bearing number is older than a patch cycle, re-verify before it informs
a plan or a big spend.

## Contents

- **`sources.md`** — the master catalog of primary sources (official site + patch notes, databases,
  planners, reputable creators). **Start here** and keep it current. _Seeded from general knowledge
  on 2026-08-21 — links still need a live vetting pass._
- **`_template.md`** — copy this to start a new research file.
- Per-system evidence files get added as each system is deep-dived, feeding the matching handbook page.

## How to research (workflow)

1. Pick a system/question from [`handbook/status.md`](../handbook/status.md) or
   [`handbook/systems-overview.md`](../handbook/systems-overview.md).
2. Gather primary sources into `research/<topic>.md` with frontmatter. Prefer official patch notes
   and current databases over blog guides; **date everything.**
3. Cross-check conflicting sources; note confidence. Flag anything that looks like a stale guide.
4. Distill the durable, plain-language version into the matching `handbook/` page.
