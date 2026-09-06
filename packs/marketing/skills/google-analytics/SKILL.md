---
name: google-analytics
description: Query live GA4 traffic, acquisition, engagement, and conversion data. Use for GA4 questions, traffic/conversion drops, channel attribution, or realtime activity questions.
---

# Google Analytics

Adapted from NotFair's `google-analytics` Skill (see `skill.yaml`).

## Job

Answer a specific GA4 question with live, correctly-scoped, decision-grade
data.

## Trigger

Use for a live GA4 question: traffic, acquisition, engagement, landing
pages, ecommerce, events, or conversions.

## Required inputs

- The exact GA4 property (`properties/123456789`) — never substitute a
  measurement ID (`G-...`) or account ID for the property resource.
- The business question, primary metric, conversion/key-event definition,
  property timezone, date range, and comparison window.

## Method

1. Confirm live access to the property. If missing or unauthorized, say so
   and stop rather than presenting synthetic numbers.
2. Pull the smallest report set that answers the question (channel,
   source/medium, campaign, landing page, device, geography, or event) —
   don't pull broad reports the question doesn't need.
3. Compare complete equivalent periods and show both absolute values and the
   delta.
4. Check for sampling, thresholding, or quota warnings in the response, and
   note a collapsed `(other)` row means detailed rows won't sum to the
   total.
5. Treat realtime/intraday data as provisional and state the property's
   timezone whenever a date range is reported.
6. Keep GA4 attribution separate from any ad-platform attribution figure
   pulled by `google-ads-audit`, `meta-ads-audit`, or `paid-ads-review` —
   explain a discrepancy rather than blending the two into one number.

## Evidence requirements

Every figure must be attributed to its exact property, date range, and
dimension set. Do not present a metric affected by sampling or thresholding
without noting that limitation.

## Outputs

The requested metric(s) with scope, comparison to the prior period, and any
data-quality caveats (sampling, thresholding, provisional data).

## Failure / insufficient evidence

If the property isn't connected/authorized, say so explicitly rather than
estimating GA4 data.

## Dependencies and effects

Requires a live GA4 connection (hosted MCP or direct Google API via OAuth).
Read-only in this pack version: measurement configuration changes (key
events, custom dimensions) are out of scope until this pack ships
write-capable Skills with populated approval metadata.

See `skill.yaml` for machine-readable metadata.
