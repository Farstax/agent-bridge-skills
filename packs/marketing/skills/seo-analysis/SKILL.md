---
name: seo-analysis
description: Full technical and content SEO audit using live Google Search Console data and page-performance signals. Use for "why is my traffic down", SEO audits, keyword/content-gap analysis, metadata or schema-markup review, indexing issues, or Core Web Vitals questions.
---

# SEO Analysis

Adapted from NotFair's `seo-analysis` Skill (see `skill.yaml` for exact
provenance). Condensed to be self-contained and provider-neutral for this
pack; the upstream Skill has more depth. Route ongoing Search Console queries
to `search-console` and ongoing GA4 queries to `google-analytics` in this
pack; use this Skill for a full-site or full-page audit.

## Job

Diagnose SEO health for a site or URL using real, connected data — never a
guess about ranking or traffic based on the page content alone.

## Trigger

Use for a traffic-drop investigation, a requested SEO audit, or any question
about search visibility, indexing, metadata, or schema markup that needs live
evidence to answer credibly.

## Required inputs

- The site or URL to audit.
- Access to the site's Google Search Console property (through whatever
  connector — hosted MCP, direct API credentials, or an operator-supplied
  export). If no live access exists, say so and work only from what's
  directly observable (page content, robots.txt, sitemap) rather than
  guessing at ranking data.
- A page-performance signal (PageSpeed Insights or equivalent) when Core Web
  Vitals or load-speed questions are in scope.

## Method

1. Pull recent Search Console performance (clicks, impressions, CTR,
   position) for the property or URL in question, compared against a prior
   equivalent period.
2. Crawl or fetch the page(s) in scope for on-page basics: title/meta
   description presence and length, heading structure, internal linking,
   canonical tags, and structured data.
3. Cross-reference: a traffic drop with stable rankings points at CTR/SERP
   feature changes; a position drop points at a ranking-signal or
   content-quality issue; a drop isolated to specific pages points at a
   page-level cause (deindexing, content change, technical error).
4. Check indexing status (via URL inspection or sitemap coverage) for pages
   that should be indexed but show zero impressions.
5. Summarize page-speed/Core Web Vitals findings only if the connected tool
   provides them — do not estimate them from static analysis.

## Evidence requirements

Every finding must cite the actual metric, date range, and comparison period
it's drawn from. Do not present a ranking or traffic claim without the
Search Console (or equivalent) data behind it.

## Outputs

A findings summary (quick wins, likely traffic-drop cause if applicable,
content/metadata/schema gaps) and a short, prioritized action list.

## Failure / insufficient evidence

If Search Console access isn't connected, say so explicitly, limit the audit
to directly observable page content, and stop before presenting inferred
ranking claims as verified.

## Dependencies and effects

Optionally uses a Search Console connector (hosted MCP or direct Google API)
and a page-speed API; both are external-read only. This Skill does not modify
site content, submit sitemaps, or request indexing on its own.

See `skill.yaml` for machine-readable metadata.
