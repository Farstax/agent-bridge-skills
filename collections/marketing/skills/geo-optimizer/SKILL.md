---
name: geo-optimizer
description: Generative Engine Optimization — audit and rewrite content to be citable by AI answer engines (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews). Use for "optimize for AI search", "rank in ChatGPT/Perplexity", GEO/AEO audits, or "get cited by AI".
---

# GEO Optimizer

Adapted from NotFair's `geo-optimizer` Skill (see this Skill's entry in the repository root `catalogue.json`). Distinct from
`seo-analysis`: this targets citation by generative answer engines, not
traditional ranked search results.

## Job

Make content more likely to be quoted, cited, or referenced by AI answer
engines, based on what's actually known about how those engines select and
attribute source material — not a guess dressed up as a ranking factor.

## Trigger

Use when asked to improve AI-search visibility, audit content for citability,
or produce a per-engine content strategy for generative search.

## Required inputs

- The URL, file, or draft content to audit or optimize.
- The target engine(s) if known (ChatGPT, Perplexity, Claude, Gemini, Google
  AI Overviews) — behavior and citation patterns differ; don't optimize for
  "AI search" as a single undifferentiated target if a specific engine
  matters to the operator.

## Method

1. Audit the content for the structural properties that make text easy for a
   retrieval system to extract cleanly: direct answers near the top,
   clear question-and-answer structure, self-contained claims that don't
   depend on surrounding context, explicit sourcing/dates for factual claims.
2. Check for the basic technical access requirements these engines' crawlers
   need (the content must be crawlable and not blocked) rather than assuming
   indexing is automatic.
3. Rewrite or restructure only what the audit identifies as a gap — don't
   rewrite content that already meets the bar.
4. State honestly that GEO outcomes (whether a specific engine actually cites
   the page) can't be verified the way a search rank can; frame
   recommendations as improving citability odds, not guaranteed citation.

## Evidence requirements

Do not claim a specific ranking or citation outcome as fact — no engine
exposes a verifiable "citation rank." Ground recommendations in structural
best practice and any available direct signal (referral traffic showing an AI
engine as a source), not invented statistics about AI search share.

## Outputs

An audit of citability gaps, a rewritten or restructured draft where useful,
and a short per-engine note where target engines were specified.

## Failure / insufficient evidence

If asked to prove content was cited by a specific engine, say that this isn't
directly verifiable and suggest checking referral traffic/analytics instead
of asserting an outcome.

## Dependencies and effects

No external service is required for the structural audit; this Skill
operates on supplied content. It does not publish changes on its own.

See this Skill's entry in the repository root `catalogue.json` for machine-readable metadata.
