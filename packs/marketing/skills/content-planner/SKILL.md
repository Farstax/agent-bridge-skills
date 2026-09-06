---
name: content-planner
description: Build a dated content calendar from real Search Console demand data — striking-distance queries and unanswered intent — ready to hand to conversion-copy or content-atomisation. Use for "plan my content", "content calendar", or "what should I write next" grounded in existing search performance.
---

# Content Planner

Adapted from NotFair's `content-planner` Skill (see `skill.yaml`). Distinct
from `keyword-research`: this mines the site's *own* Search Console data for
scheduling, rather than seed-driven topic discovery for a new area.

## Job

Turn a site's actual Search Console performance into a prioritized, dated
content calendar targeting realistic quick wins.

## Trigger

Use when asked to plan content, build an editorial calendar, or find
quick-win topics grounded in the site's own search data.

## Required inputs

- Live Search Console access for the site (connector, API, or operator
  export). Without it, this Skill cannot do its job — say so and suggest
  `keyword-research` for a seed-driven alternative instead.
- Publishing cadence and capacity from the operator (how many pieces per
  period) — don't assume a fixed cadence.

## Method

1. Pull queries where the site already ranks in a recoverable range
   (typically positions 5-20) with real impression volume — these convert to
   traffic fastest with the least new authority required.
2. Identify query intent the site doesn't currently answer at all (queries
   with impressions but no matching content).
3. Prioritize by realistic click potential (current position, impression
   volume, competition) over raw volume alone.
4. Assign each prioritized topic a date based on the operator's stated
   cadence and capacity — do not invent a publishing frequency.

## Evidence requirements

Every topic in the calendar must trace to a specific Search Console query,
position, and impression figure. Do not include a topic based on a hunch the
data doesn't support.

## Outputs

A dated, prioritized content calendar (topic, target query, current
position, estimated click potential, publish date) plus a short summary.

## Failure / insufficient evidence

If Search Console isn't connected, say so explicitly rather than producing a
calendar from guessed topics.

## Dependencies and effects

Requires a Search Console connector (hosted MCP or direct Google API);
external-read only. Produces a calendar artifact only — it does not publish
or schedule content itself.

See `skill.yaml` for machine-readable metadata.
