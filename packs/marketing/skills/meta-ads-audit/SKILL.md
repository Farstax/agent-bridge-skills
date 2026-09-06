---
name: meta-ads-audit
description: Read-only Meta (Facebook + Instagram) Ads account health audit and business-context capture. Use for "audit my Meta/Facebook ads", account-health checks, or onboarding a new Meta Ads account.
---

# Meta Ads Audit

Adapted from NotFair's `meta-ads-audit` Skill (see `skill.yaml`).
**Read-only** — this Skill never mutates the account.

## Job

Diagnose Meta (Facebook and Instagram) Ads account health and capture
reusable business context for future work on the account.

## Trigger

Use for a Meta Ads account-health audit, or when onboarding a Meta account
for the first time.

## Required inputs

- Live, authorized access to the Meta Ads account. Without it, say so rather
  than inferring health from indirect signals.
- Existing business context from a prior `google-ads-audit`, if any — most
  fields (services, differentiators, seasonality) are platform-agnostic and
  should be reused rather than re-derived.

## Method

1. Pull account structure and recent performance: campaigns, ad sets, spend,
   conversions, and conversion-tracking (Pixel/Conversions API) health.
   Verify tracking is actually firing before treating downstream CPA/ROAS as
   decision-grade.
2. Check for common health issues: creative fatigue (declining frequency
   performance), audience overlap, disapproved ads, and delivery/learning
   phase problems.
3. Capture or update business context with any Meta-specific differences
   from a prior platform audit (different creative angles, different
   audiences, different funnel events).
4. Report findings ranked by likely impact: what's healthy, what's broken,
   what to fix first.

## Evidence requirements

Every finding must cite the actual account data it's drawn from. Do not
report a generic Meta Ads best-practice gap the account data doesn't show.

## Outputs

A ranked health report plus captured/updated business context.

## Failure / insufficient evidence

If account access isn't authorized, say so and do not fabricate findings.

## Dependencies and effects

Requires live, authorized Meta Ads account access (OAuth); external-read
only. This Skill never changes budgets, targeting, or creative — any fix it
identifies is a recommendation for the operator or a separate,
approval-gated Skill to execute.

See `skill.yaml` for machine-readable metadata.
