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
                                 and the Skill Pack mechanism.

Farstax/agent-bridge-skills     Curated optional domain Skill content
(this repository)               (this repository). A Skill Pack is a
                                 manifest over ordinary Agent Bridge
                                 Skills — not a plugin runtime, daemon,
                                 or second execution engine.

Farstax Stacks                  Business/application catalogue that can
                                 recommend packs by id. Agent Bridge has
                                 no dependency on Stacks.
```

See `Farstax/agent-bridge#703` for the pack mechanism design and
`nickconstantinou/agent-bridge-platform#699` for how Stacks reference packs.

## Installation status

**Pending.** `Farstax/agent-bridge#703` — the pack install/update/remove
mechanism — has not shipped yet. Every pack's `compatibility.status` is
`pending` and `compatibility.agentBridge` is `null` until that mechanism
lands and this repository's schema is reconciled with it.

Until then, this repository is developed and validated on its own:

```bash
git clone https://github.com/Farstax/agent-bridge-skills.git
cd agent-bridge-skills
python3 -m pip install -r tests/requirements.txt
python3 tests/validate.py
```

A Skill's `SKILL.md` can also be read and manually copied into a provider's
Skill directory today; the pack manifest exists so that once #703 ships,
installing the whole pack or a single Skill from it becomes a supported
Agent Bridge operation with provenance preserved.

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
  knowledge than a competing Farstax version would. Only audit/analysis
  Skills are included in this initial release — see
  `packs/marketing/README.md` for what was deliberately left out and why.

No Skill Pack install grants permission to spend money, publish content, send
messages, or mutate a third-party account. External services (including
NotFair's hosted MCP) are declared per-Skill and must be explicitly
authorized by the operator before any live-data feature is used.

## Provenance model

Every Skill carries a `skill.yaml` next to its `SKILL.md` recording who wrote
it, where it came from, the exact upstream revision (if any), its licence,
what it depends on, what it can touch, and what approvals it needs. See
`schemas/skill.schema.json` and `AGENTS.md`.

## Contributing a pack or Skill

See `AGENTS.md` for the mandatory provenance, licensing, and safety rules,
and the steps for proposing a new pack or Skill.
