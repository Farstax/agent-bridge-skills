# Farstax Agent Bridge Skill Packs

Agent Bridge runs Skills. This repository provides optional, curated domain
Skill Packs that install into a resident Agent Bridge agent. Farstax Stacks
may recommend these packs, but the packs also work standalone — you do not
need a Farstax account or any Farstax product to use them.

Farstax curates and qualifies everything here. This is not an open Skill
marketplace: packs are reviewed for provenance, licensing, safety metadata,
and quality before they ship.

## Architecture

```
Farstax/agent-bridge            Skill runtime, installation, projection,
                                 and the Skill Pack mechanism (#703).

Farstax/agent-bridge-skills     Curated optional domain Skill content
(this repository)               (this repository). A Skill Pack is a
                                 manifest over ordinary Agent Bridge
                                 Skills — not a plugin runtime, daemon,
                                 or second execution engine.

Farstax Stacks                  Business/application catalogue that can
                                 recommend packs by id. Agent Bridge has
                                 no dependency on Stacks.
```

## Installation

`Farstax/agent-bridge#703` has shipped. Agent Bridge fetches this
repository's `catalogue.json` directly from
`https://raw.githubusercontent.com/Farstax/agent-bridge-skills/main/catalogue.json`
through its existing Skill manager:

```bash
# From an Agent Bridge checkout
npm run skills -- packs list
npm run skills -- packs show marketing
npm run skills -- packs install marketing
npm run skills -- packs install-skill marketing positioning
npm run skills -- packs status
npm run skills -- packs update marketing
npm run skills -- packs remove marketing
```

See `Farstax/agent-bridge`'s `docs/SKILL-PACKS.md` for the full command
reference, installed-state layout, and update/removal semantics. Installing a
pack never authorizes an external account, performs OAuth, supplies a secret,
or grants spend/mutation authority. The workspace owner and connected
tool/account permissions, budgets, and native controls remain authoritative.

The Marketing pack currently requires Agent Bridge `2026.9.6-2` or newer via
`compatibility.minAgentBridgeVersion`. Keep that pin aligned with the oldest
released Agent Bridge version that implements the catalogue contract the pack
uses.

To develop or qualify changes to this repository itself:

```bash
git clone https://github.com/Farstax/agent-bridge-skills.git
cd agent-bridge-skills
python3 -m pip install -r tests/requirements.txt
python3 tests/validate.py
```

## Initial pack: `marketing`

Strategy, acquisition, conversion, distribution, and measurement capabilities
for a resident business agent. See `packs/marketing/README.md` for the full
Skill list and provenance.

Conceptual flow:

```
Research → Positioning → Offer → Brand/Creative
  → Acquisition (SEO / GEO / paid media)
  → Conversion (landing copy, lead magnets, email)
  → Distribution (content atomisation, newsletters)
  → Measurement (GA4, Search Console, ad performance)
  → Campaign review → next hypothesis
```

The pack combines two complementary sources:

- **Farstax-authored** strategy and conversion Skills, modernised from
  Farstax's private Antigravity marketing work — stale assumptions (fixed
  send times, hardcoded providers, unsupported "vibe" statistics) and
  manipulative copy prescriptions (fake scarcity, manufactured urgency) were
  removed. What's kept: clear positioning, specific offers, a human brand
  voice, channel-native distribution, and evidence-led iteration.
- **NotFair-derived** operational SEO/GEO/analytics/paid-media Skills,
  selected from [`nowork-studio/notfair-plugin`](https://github.com/nowork-studio/notfair-plugin)
  (MIT licence) where it has stronger current, evidence-led operational
  knowledge than a competing Farstax version would. The pack includes both
  read-only analysis and a small curated write-capable layer for Google Ads
  and Meta Ads; see `packs/marketing/README.md` for the exact boundary.

No Skill Pack install grants permission to spend money, publish content, send
messages, or mutate a third-party account. External services (including
NotFair's hosted MCP) are declared per-Skill and must be explicitly
authorized by the workspace owner before any live-data or mutation capability
is available.

## Provenance model

Every Skill's metadata (who wrote it, exact upstream revision if any, licence,
dependencies, capabilities, approvals) lives in `catalogue.json`, generated
from `scripts/build-catalogue.mjs`. See `schemas/skill-pack.schema.json` and
`AGENTS.md`.

## Contributing a pack or Skill

See `AGENTS.md` for the mandatory provenance, licensing, and safety rules,
and the steps for proposing a new pack or Skill.
