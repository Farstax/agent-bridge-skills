# Third-party notices

`agent-bridge-skills` is licensed under MIT for Farstax-authored content
(see `LICENSE`). Some Skills are adapted or vendored from third-party
upstream projects and retain their own licence.

Per-pack notices live at `packs/<pack-id>/NOTICE.md`. Per-Skill provenance
(exact upstream repository, path, commit, licence, and modification status)
lives in each Skill's entry in the repository root `catalogue.json` (generated from `scripts/build-catalogue.mjs`).

## Design collection

The `impeccable` skill is adapted from [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0); see `collections/design/NOTICE.md` and `collections/design/LICENSE` for details.

## marketing pack

See `packs/marketing/NOTICE.md`. Includes Skills adapted from
[`nowork-studio/notfair-plugin`](https://github.com/nowork-studio/notfair-plugin)
(MIT licence).


## Grill Me (Build collection)

- Upstream repository: https://github.com/mattpocock/skills
- Revision: `49dd158d1076134a641b33efb035946536778336`
- Upstream paths: `skills/productivity/grill-me/SKILL.md` and `skills/productivity/grilling/SKILL.md`
- Author: Matt Pocock; copyright (c) 2026 Matt Pocock
- Licence: MIT; full licence included at `collections/build/LICENSE`
- Modified: flattened upstream delegation into one portable skill, changed rounds to one decision per turn, tightened opt-in, factual research and no-side-effect boundaries.
