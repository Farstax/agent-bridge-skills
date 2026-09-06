---
name: search-console
description: Query live Google Search Console data — clicks, impressions, CTR, position, indexing status, URL inspection, sitemap status. Use for live GSC questions; route full-site SEO audits to seo-analysis and demand-driven calendars to content-planner.
---

# Google Search Console

Adapted from NotFair's `search-console` Skill (see this Skill's entry in the repository root `catalogue.json`).

## Job

Answer a specific Search Console question with live, correctly-scoped data.

## Trigger

Use for a live GSC query, page-performance question, indexing-status check,
or sitemap status question. Hand off to `seo-analysis` for a full-site audit
that also needs crawling and on-page analysis.

## Required inputs

- The exact property to query. `sc-domain:example.com` and
  `https://example.com/` are different properties — confirm which one is
  intended rather than guessing.
- The metric, dimension(s), and date range (plus a comparison window if a
  change is being investigated).

## Method

1. Confirm live access to the property through whatever connector is
   available (hosted MCP or direct API). If access is missing or
   unauthorized, say so and stop rather than presenting synthetic data.
2. Pull the smallest data slice that answers the question — a single
   property/date-range read for a specific question, broader dimensions only
   when the question needs them.
3. Compare complete equivalent periods when investigating a change; do not
   compare partial to complete periods.
4. Note when recent days are still provisional (GSC data typically finalizes
   with a lag) and label fresh data as such.
5. For query-level data, note that low-volume queries are anonymized and
   query-level totals will not sum exactly to property-level totals.
6. Use URL inspection sparingly (tighter quota than Search Analytics); it
   reports index state, it does not request indexing.
7. This Skill is read-only in this pack version: it queries performance,
   indexing status, and sitemap status. Sitemap submission/removal is a
   write action and is out of scope here until this pack ships write-capable
   Skills with populated approval metadata.

## Evidence requirements

Every figure reported must be attributed to its exact property, dimension
set, and date range. Do not average pre-aggregated CTR or position values
without noting the distortion that introduces.

## Outputs

The requested metric(s) with their exact scope (property, dimensions, date
range) and, if relevant, a comparison to the prior equivalent period.

## Failure / insufficient evidence

If the property isn't connected/authorized, say so explicitly and do not
substitute an estimate for live data.

## Dependencies and effects

Requires a live Search Console connection (hosted MCP or direct Google API
via OAuth). Read-only: this Skill queries and does not modify the property.

See this Skill's entry in the repository root `catalogue.json` for machine-readable metadata.
