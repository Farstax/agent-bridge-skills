# AGENTS.md — agent-bridge-skills

This repository is the curated, optional Skill Pack content for
[Farstax/agent-bridge](https://github.com/Farstax/agent-bridge). It is not the
pack runtime. See `Farstax/agent-bridge#703` for the mechanism that installs,
projects, and validates packs; this repository owns pack *content* only.

## What this repository is

- A curated set of domain Skill Packs, each a manifest (`pack.yaml`) over
  ordinary Agent Bridge Skills.
- Farstax-qualified, not an open marketplace. Contributions are reviewed for
  provenance, licensing, safety metadata, and quality before merge.
- Standalone-usable. A pack must work for an operator running plain OSS Agent
  Bridge with no Farstax Stacks account.

## What this repository is not

- Not a plugin runtime, daemon, or dynamic loader. Skills here install and
  project through Agent Bridge's existing Skill mechanism.
- Not a place for Farstax Stacks business logic. Stacks may recommend a pack
  id; they do not own or duplicate pack content.
- Not a home for unreviewed third-party imports.

## Mandatory rules for any change

1. **Metadata and provenance are mandatory.** Every Skill needs a `skill.yaml`
   next to its `SKILL.md` that validates against `schemas/skill.schema.json`.
   Every pack needs a `pack.yaml` that validates against
   `schemas/pack.schema.json`.
2. **No unattributed upstream imports.** A Skill copied or adapted from an
   external project must record `origin.type` (`adapted-upstream` or
   `vendored-upstream`), the exact upstream repository, path, and commit SHA,
   and its licence. Never claim `farstax-authored` for adapted third-party
   work.
3. **Verify upstream licences and revisions yourself.** Do not trust a prior
   PR's claim about an upstream licence — re-check the licence file at the
   exact commit you are importing.
4. **Never store credentials or client data.** No secret values, API keys,
   tokens, or customer data anywhere in this repository, including in test
   fixtures and evals.
5. **Do not silently add external services.** A Skill that can call an
   external API, hosted MCP, or account-connected service must declare it
   under `dependencies.externalServices` or `dependencies.mcp` in its
   `skill.yaml`, and the pack must not authorize that service on install.
6. **Mutation and spend capabilities need explicit metadata and approval
   boundaries.** Use `effects.level` honestly. Anything above
   `external-read` needs a populated `approvals` list describing what
   confirmation the operator or resident agent must obtain before acting.
   No Skill Pack install may itself grant permission to spend money, publish
   content, send messages, or mutate a third-party account.
7. **Keep Skills narrow.** One clear job per Skill. Prefer several small,
   addressable Skills over one omnibus Skill — this lets the resident agent
   load only what the task needs (progressive disclosure).
8. **Prefer evidence-led instructions over prescriptive ceremony.** State the
   goal, required inputs, evidence requirements, and failure behaviour. Do not
   add step-by-step scripts where a competent agent only needs the invariant.
   Do not hardcode a specific tool, provider, or vendor when the requirement
   is "evidence of X" or "capability to do Y."
9. **Tests/evals are required for a meaningful change.** A new or materially
   changed Skill needs at least one eval or check under its `evals/` and a
   reference from `skill.yaml.evals` and the pack's `tests` list.
10. **Updating an upstream-derived Skill must refresh its recorded revision.**
    When you touch a Skill with `origin.type` of `adapted-upstream` or
    `vendored-upstream`, update `origin.upstream.commit` (if you re-pulled
    upstream content) and always update `origin.lastUpstreamReview` to the
    date you last checked the upstream source and licence.

## Validation

Run before opening a PR:

```bash
python3 -m pip install -r tests/requirements.txt
python3 tests/validate.py
```

CI runs the same script on every PR and on `main`.

## Adding a new pack

1. Open an issue describing the proposed capability set, why it's coherent,
   and which upstream sources (if any) it draws from.
2. Create `packs/<pack-id>/` with `pack.yaml`, `README.md`, `NOTICE.md` (if it
   contains upstream-derived Skills), and `skills/<skill-id>/{SKILL.md,skill.yaml}`
   per Skill.
3. Add the pack to `catalog.yaml`.
4. Add or extend `THIRD_PARTY_NOTICES.md` for any upstream-derived Skill.
5. Pass `tests/validate.py` and open a PR.
