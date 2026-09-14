---
name: keyword-research
description: Seed-driven keyword discovery and prioritization by volume, competition, and intent, with topic clustering. Use for "find keywords", keyword analysis, search volume/difficulty questions, or content ideas from a seed topic. For a dated calendar from existing Search Console data, use content-planner instead.
---

# Keyword Research

Adapted from NotFair's `keyword-research` Skill (see this Skill's entry in the repository root `catalogue.json`).

## Job

Discover and prioritize keywords for a seed topic or niche, clustered by
intent and business relevance — not a raw unranked list.

## Trigger

Use when asked for keyword ideas, content topics from a seed, or a keyword's
difficulty/volume/intent read.

## Required inputs

- A seed keyword, topic, or niche.
- Business context: what the site sells or offers, to judge relevance (a
  high-volume keyword with no path to the offer is a low priority).
- A keyword-data source if precise volume/difficulty numbers are needed
  (a search-data API or connector). Without one, work from qualitative
  signal (SERP composition, competitor coverage) and say so.

## Method

1. Expand the seed into related terms grouped by intent: informational,
   commercial, navigational, transactional.
2. Cluster related keywords into topics rather than listing them flat — a
   cluster becomes one content piece, not one keyword per piece.
3. Prioritize by a combination of realistic ranking opportunity (not just
   raw volume) and business relevance to the offer.
4. Where precise volume/difficulty data isn't available, say so and give a
   qualitative estimate (SERP crowding, incumbent authority) instead of an
   invented number.

## Evidence requirements

Any quantitative claim (volume, difficulty) must come from a connected data
source, not be invented. Qualitative judgments must reference observable SERP
composition, not assumption.

## Outputs

A clustered keyword/topic list with intent labels and a priority
recommendation, ready to hand to `content-planner` or `conversion-copy`.

## Failure / insufficient evidence

If no keyword-data source is connected, clearly label all volume/difficulty
figures as qualitative estimates rather than presenting them as precise data.

## Dependencies and effects

Optionally uses a keyword-data API or connector; external-read only. Produces
no external write.

See this Skill's entry in the repository root `catalogue.json` for machine-readable metadata.
