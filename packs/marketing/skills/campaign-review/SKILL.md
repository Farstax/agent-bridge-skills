---
name: campaign-review
description: Turn real campaign performance data into a diagnosis and one recommended next experiment, and check drafted marketing assets against the brand voice and offer before they ship. Use for a post-campaign retro, a performance review, or a pre-publish quality check on marketing copy.
---

# Campaign Review

## Job

Two related checks, both evidence-led: (1) review a drafted asset against
the brand voice and offer before it ships, and (2) after a campaign runs,
diagnose what the performance data actually shows and recommend one next
experiment.

## Trigger

Use before publishing a marketing asset (pre-publish check), or after a
campaign, email, or content piece has run and has real performance data
(post-campaign review).

## Required inputs

**Pre-publish check:** the drafted asset, the brand voice profile, and the
offer/positioning it's meant to reflect.

**Post-campaign review:** the actual performance numbers (traffic, opens,
clicks, conversions — whatever the channel reports) and what was published.

## Method — pre-publish check

1. Compare the draft against the brand voice profile's concrete attributes
   and avoid-list — not a generic "sounds corporate" impression.
2. Check the draft still matches the offer and positioning it's derived
   from; flag any claim that's drifted from what was confirmed.
3. Check structural basics: does the headline's promise hold by the first
   paragraph; is there one clear call to action; would a specific named
   audience member recognize themselves in this.
4. Give a clear pass/fail with the specific line and reason — not a vague
   "maybe punchier" suggestion.

## Method — post-campaign review

1. Compare against the prior equivalent period or a stated baseline, not an
   isolated absolute number.
2. Diagnose the likely driver only when the data supports it: high
   traffic/low conversion points at the offer or page friction; low traffic
   points at distribution or the hook; state which pattern applies and why.
3. Recommend exactly one next experiment tied to the diagnosis (for example,
   "traffic was fine, conversion was the problem — next test is the
   offer's risk reversal"), not a list of unranked ideas.

## Evidence requirements

Every diagnosis must cite the actual numbers it's based on. Do not name a
likely driver the data doesn't support, and say so explicitly when the data
is inconclusive.

## Outputs

Pre-publish: a pass/fail with specific line-level feedback. Post-campaign: a
short diagnosis grounded in the numbers, plus one recommended next
experiment.

## Failure / insufficient evidence

If performance data is incomplete or not comparable to a baseline, say so and
avoid manufacturing a confident diagnosis from partial numbers.

## Dependencies and effects

No external service is required if performance data is supplied directly.
This Skill only reads and reasons over supplied material — it does not
change, publish, or spend anything itself.

See this Skill's entry in the repository root `catalogue.json` for machine-readable metadata.
