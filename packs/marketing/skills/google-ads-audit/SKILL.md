---
name: google-ads-audit
description: Read-only Google Ads account health audit and business-context capture. Use for "audit my ads", account-health checks, or onboarding a new Google Ads account before any optimization work.
---

# Google Ads Audit

Adapted from NotFair's `google-ads-audit` Skill (see `skill.yaml`).
**Read-only** — this Skill never mutates the account.

## Job

Diagnose Google Ads account health and capture reusable business context
(audience, offers, differentiators) for any future work on the account.

## Trigger

Use for an account-health audit, or when onboarding an account for the first
time.

## Required inputs

- Live, authorized access to the Google Ads account (via connector or API).
  Without it, say so — do not infer account health from indirect signals.
- Basic business context if not already known: what's sold, target
  audience, typical offers — ask rather than guess.

## Method

1. Pull account structure and recent performance: campaigns, spend,
   conversions, and the account's conversion-tracking setup. Verify
   conversion tracking is actually firing correctly before treating any
   downstream CPA/ROAS figure as decision-grade.
2. Check for common health issues: wasted spend on irrelevant search terms,
   disapproved ads, low quality scores, budget-limited campaigns, and
   missing conversion actions.
3. Capture durable business context (industry, services, target audience,
   brand voice, differentiators, competitors, seasonality, high-intent
   keyword landscape) so future work on this account doesn't start from
   zero.
4. Report findings as: what's healthy, what's broken, and what to fix first
   — ranked by likely impact, not an unranked list.

## Evidence requirements

Every finding must cite the actual account data it's drawn from (specific
campaign, metric, date range). Do not report a generic best-practice gap the
account data doesn't actually show.

## Outputs

A ranked health report plus captured business context for reuse by future
account work.

## Failure / insufficient evidence

If account access isn't authorized, say so and do not fabricate account
health findings.

## Dependencies and effects

Requires live, authorized Google Ads account access (OAuth); external-read
only. This Skill never changes budgets, bids, ads, or targeting — any fix it
identifies is a recommendation for the operator or a separate,
approval-gated Skill to execute.

See `skill.yaml` for machine-readable metadata.
