---
name: paid-ads-review
description: Read-only, evidence-based paid-media performance review across connected platforms or supplied exports. Use for weekly/monthly performance reports, scorecards, CPA/ROAS/CTR/spend/pacing questions, or conversion-tracking health checks.
---

# Paid Ads Review

Adapted from NotFair's `paid-ads-review` Skill (see `skill.yaml`).
**Read-only.**

## Job

Produce a cross-channel paid-media performance review that leads with the
decision, not a dashboard transcription.

## Trigger

Use for a periodic performance review, scorecard, or a specific spend/CPA/
ROAS/pacing question across one or more paid channels.

## Required inputs

- Which platforms are actually connected or have a supplied export
  (Google Ads, Meta Ads, or others) — check rather than assume, and request
  the missing export instead of silently skipping a channel.
- The date range and, for a change investigation, a comparison window.

## Method

1. Assemble comparable evidence per platform: spend, qualified conversions,
   CPA, attributable revenue/ROAS where available, link CTR, and pace
   against any declared budget.
2. Keep currency, conversion definition, attribution window, and reporting
   lag visible per source — don't blend definitions across platforms
   silently.
3. Verify conversion tracking before treating CPA, ROAS, or revenue as
   decision-grade for any platform.
4. Compare each row to the preceding equivalent period and name the likely
   driver only when the data supports it.
5. If a cross-channel blended CPA/ROAS is useful, label its conversion
   definition, attribution source, spend-weighted formula, and included
   channels explicitly — never present an unqualified blended figure.
6. Lead the report with the strongest contributor, the largest risk, and one
   recommended next action — not a raw table dump.

## Evidence requirements

Every figure must be attributed to its source platform, date range, and
conversion definition. Mark absent tracking or data as a blocking limitation
rather than omitting it silently.

## Outputs

A platform scorecard, a labeled cross-channel view if useful, and a close of
`hold`, `investigate`, or one proposed next action.

## Failure / insufficient evidence

If a platform isn't connected and no export is supplied, request it and
exclude that platform from the review rather than estimating its numbers.

## Dependencies and effects

Optionally uses connected ad-platform data (Google Ads, Meta Ads, or others)
or an operator-supplied export; external-read only. This Skill never changes
budgets or campaigns — route any proposed mutation to a separate,
approval-gated Skill.

See `skill.yaml` for machine-readable metadata.
