---
name: investment-research
description: Prepare evidence-linked company and sector investment research for human review, not trading.
---

# Investment Research

## Job and trigger
Use to investigate a named company, security, fund or industry and produce a sourced research memorandum. For general multi-topic investigation use `deep-research`; for financial model creation use `financial-modelling`.

## Method
1. Define issuer/asset identity, market and as-of date. Distinguish legal entity, ticker, listing, fund share class and currency.
2. Prefer issuer filings, audited financials, regulatory disclosures, exchange releases and dated primary information. Then review independent commentary for challenges to the thesis.
3. Summarise business model, competitive context, major financial figures, capital structure, cash flows, risks and plausible bullish/bearish cases. Cite material facts with document/section/date; expose assumptions and unknowns.
4. Where figures permit, compute comparisons with consistent periods/units. Avoid live-price claims unless a current data source was actually consulted.
5. Produce an investment research note including sources, uncertainties, conflicts, sensitivity and reasons the thesis may fail. Use `xlsx`/`pdf` only when a file deliverable is requested.

## Boundaries
Research is not a trade recommendation or regulated investment advice. No order execution, portfolio mutation or assumed brokerage access. Do not silently fill stale or unavailable numbers.

## Provenance
Provider-neutral adaptation guided by selected workflow patterns in [Anthropic Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins) and [Financial Services](https://github.com/anthropics/financial-services); see `collections/business/NOTICE.md`.
