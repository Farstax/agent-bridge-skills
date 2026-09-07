# AGENTS.md — agent-bridge-skills

This repository is the curated, optional Skill Pack content for
[Farstax/agent-bridge](https://github.com/Farstax/agent-bridge). It is not the
pack runtime. `Farstax/agent-bridge#703` shipped the mechanism that discovers,
installs, projects, and validates packs (`docs/SKILL-PACKS.md` and
`docs/skill-pack.schema.json` in that repository); this repository owns pack
*content* and the published `catalogue.json` Agent Bridge actually fetches.

## What this repository is

- A curated set of domain Skill Packs. `catalogue.json` at the repository root
  is the canonical, machine-consumed artifact — Agent Bridge fetches it from
  `https://raw.githubusercontent.com/Farstax/agent-bridge-skills/main/catalogue.json`.
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

## How metadata actually works

`catalogue.json` is generated, not hand-edited. The source of truth is
`scripts/build-catalogue.mjs`, which holds pack/Skill metadata (description,
provenance, dependencies, capabilities, tests) and computes each Skill's
`content.sha256` from its actual directory contents using the exact same
algorithm Agent Bridge uses to verify content before projection
(`scripts/hash-skill-directory.mjs`, ported from
`Farstax/agent-bridge` `src/skillPacks.ts`).

A Skill's directory under `packs/<pack-id>/skills/<skill-id>/` contains only
what should actually be installed: `SKILL.md` and any supporting
`references/`, `scripts/`, or `evals/` content. It does **not** contain a
separate `skill.yaml` — that was an earlier draft convention from before
`#703` shipped its own canonical schema, and keeping a second metadata file
next to the canonical one is exactly the kind of drift this repository's own
review process flagged and fixed once already. Metadata lives once, in
`catalogue.json`/`build-catalogue.mjs`.

### Publishing a change

1. Edit Skill content under `packs/<pack-id>/skills/<skill-id>/` and/or
   metadata in `scripts/build-catalogue.mjs`.
2. Commit that change (without touching `catalogue.json`) and push it. This
   fixes the exact commit SHA that will be `content.revision` for any Skill
   whose directory changed.
3. Regenerate the catalogue pinned to that commit:
   ```bash
   node scripts/build-catalogue.mjs --revision "$(git rev-parse HEAD)"
   ```
4. Validate and commit `catalogue.json` as a follow-up commit:
   ```bash
   python3 tests/validate.py
   git add catalogue.json && git commit -m "Publish catalogue pinned to <sha>"
   ```
5. Merge the PR with a **merge commit, not a squash**, so the pinned
   intermediate commit stays reachable from `main` — Agent Bridge fetches
   Skill content from GitHub by exact commit SHA via the GitHub API, and a
   squash merge would make that SHA unreachable.

## Mandatory rules for any change

1. **`catalogue.json` must validate against `schemas/skill-pack.schema.json`**
   (vendored byte-for-byte from `Farstax/agent-bridge` `docs/skill-pack.schema.json`
   — do not hand-edit it; if the canonical schema changes upstream, replace this
   file wholesale and re-check every skill entry against the new shape).
2. **No unattributed upstream imports.** A Skill copied or adapted from an
   external project must record `provenance.origin` (`adapted-upstream` or
   `vendored-upstream`), the exact upstream repository, revision, and SPDX
   licence, and a notice path + SHA-256. Never claim `author-created` for
   adapted third-party work — the schema fails closed on this (an
   `author-created` Skill cannot declare any upstream field).
3. **Verify upstream licences and revisions yourself.** Do not trust a prior
   PR's claim about an upstream licence — re-check the licence file at the
   exact commit you are importing.
4. **Never store credentials or client data.** No secret values, API keys,
   tokens, or customer data anywhere in this repository, including in test
   fixtures and evals. Secret *names and purposes only* — never values.
5. **Do not silently add external services.** A Skill that can call an
   external API or hosted MCP must declare it under
   `dependencies.externalServices` or `dependencies.hostedMcps`. Pack
   installation itself never configures a declared service, performs OAuth,
   or supplies a secret — that's enforced by Agent Bridge, not this
   repository, but metadata must stay honest about what a Skill can reach.
6. **Mutation and spend capabilities need explicit metadata and approval
   boundaries.** Use `capabilities.effects` honestly
   (`local-read` / `external-read` / `draft-write` / `external-write` /
   `spend-mutation`) and always fill in `capabilities.approval` — it's
   required for every Skill regardless of effect level.
7. **Keep Skills narrow.** One clear job per Skill.
8. **Prefer evidence-led instructions over prescriptive ceremony.** State the
   goal, required inputs, evidence requirements, and failure behaviour. Do not
   hardcode a specific tool, provider, or vendor when the requirement is
   "evidence of X" or "capability to do Y."
9. **Tests/evals are required for a meaningful change.** A new or materially
   changed Skill needs at least one eval or check under its `evals/`,
   referenced from that Skill's `tests` array in `build-catalogue.mjs`.
   `tests/validate.py` checks that a declared eval file exists and is
   well-formed; it does not execute evals against a model. A green `Validate`
   CI run proves catalogue/schema/provenance/hash hygiene, not that a Skill
   produces good output.
10. **Updating an upstream-derived Skill must refresh its recorded revision.**
    When you touch a Skill with `provenance.origin` of `adapted-upstream` or
    `vendored-upstream`, update `provenance.upstreamRevision` (if you
    re-pulled upstream content) and always update `provenance.lastReviewed`
    to the date you last checked the upstream source and licence.
11. **Pack-level `dependencies`/`capabilities.effects` must not omit anything
    a member Skill declares.** This is a repo curation convention on top of
    what Agent Bridge itself validates — `tests/validate.py` checks it — so a
    reader of the pack summary alone isn't misled about what it can touch.

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
2. Create `packs/<pack-id>/skills/<skill-id>/{SKILL.md,evals/...}` per Skill,
   plus `packs/<pack-id>/README.md` and, if it contains upstream-derived
   Skills, `packs/<pack-id>/NOTICE.md`.
3. Add the pack's metadata to `scripts/build-catalogue.mjs`.
4. Add or extend `THIRD_PARTY_NOTICES.md` for any upstream-derived Skill.
5. Follow "Publishing a change" above to regenerate and pin `catalogue.json`.
6. Pass `tests/validate.py` and open a PR, merged with a merge commit.
