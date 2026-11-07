---
name: data-analysis
description: Profile datasets, validate calculations, visualise findings and report uncertainty without inventing data.
---

# Data Analysis

## Job and trigger
Use for exploratory, descriptive or comparative analysis of a supplied dataset or user-authorised data source. Do not replace existing `google-analytics`, `search-console`, `paid-ads-review` or `market-research` Skills.

## Method
1. Establish the question, grain, population, unit, time range and intended decision. Check whether access to source files, tables or services is actually available; a Skill does not grant any connection.
2. Profile schema/types, missing values, duplicates, outliers, timezone, units and potential selection bias. Record transformations reproducibly; avoid silently deleting bad rows.
3. Compute metrics using the provider's available execution tools (SQL, Python, spreadsheet). Check denominators, join cardinality, null handling and at least one independent reasonableness invariant.
4. Select tables/charts only when they improve the answer. Label units, population, method and uncertainty; distinguish correlation from causal evidence. If output is a spreadsheet use the separate `xlsx` Skill.
5. Present concise findings, supporting figures, data-quality limitations, source/provenance and a reproducible calculation trail. Save files only in the workspace and provide verified paths when requested.

## Missing tools and safety
If no runtime can read the source, state precisely what is missing; do not fabricate analysis. Avoid exposing unnecessary personal records, credentials or confidential rows in outputs. Never mutate production datasets, run external queries with side effects or claim statistical significance without appropriate evidence.

## Provenance
Provider-neutral adaptation guided by selected workflow patterns in [Anthropic Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins) and [Financial Services](https://github.com/anthropics/financial-services); see `collections/business/NOTICE.md`.
