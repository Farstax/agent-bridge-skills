# AGENTS.md — agent-bridge-skills

This repository curates optional Skills for Agent Bridge. Agent Bridge is the runtime and installed-state authority. This repository publishes only immutable Skill content plus lightweight Collections.

## Model

- **Skill** is the actual reusable capability. Every Skill is independently installable.
- **Collection** is only a named group of Skill ids for discovery and installation convenience.
- Stacks may recommend Skills or Collections. They never own them.
- Connections, OAuth, tools, providers and external services are separate runtime concerns. Do not encode them as Skill dependencies or installation side effects.

`catalogue.json` is the canonical machine-consumed schema-v2 artefact. `catalogue.source.json` is its curation source. Skill content lives under `collections/<collection-id>/skills/<skill-id>/`; the directory grouping is editorial only.

## Publishing

1. Edit Skill content and/or `catalogue.source.json`. Keep one clear job per Skill and preserve provenance/licensing. Never add secrets or customer data.
2. Commit the source/content change.
3. Run `node scripts/build-catalogue.mjs --revision "$(git rev-parse HEAD)"`.
4. Run `python3 -m pip install -r tests/requirements.txt && python3 tests/validate.py`.
5. Commit `catalogue.json` separately. Merge with a merge commit, not squash, so the pinned source revision remains reachable.

The schema is vendored from Agent Bridge `docs/skill-collection.schema.json`; replace it wholesale when the canonical schema changes.
