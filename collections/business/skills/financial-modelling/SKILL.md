---
name: financial-modelling
description: Build auditable financial models with formulas, assumptions, sensitivities and reconciliation checks.
---

# Financial Modelling

## Job and trigger
Use when a user needs a spreadsheet model (budget, forecast, 3-statement, DCF or scenario). Do not treat this as permission to execute trades, create financial-account connections or offer personalised investment advice.

## Method
1. Define purpose, timeframe, currency, fiscal calendar and model type. Separate supplied historical figures, externally verified inputs and assumptions. Ask only for missing consequential assumptions.
2. Establish clearly marked input, calculation and output sections. Build formulas using the `xlsx` Skill for actual workbook operations, rather than hardcoding expected values.
3. Check unit/currency consistency, sign conventions, circular references, date alignment, balance-sheet balancing when relevant, forecast roll-forward and sensitivity to key assumptions.
4. State the scenario range and do not present one forecast as certainty. Link market data to dated sources or label it illustrative.
5. Recalculate where tooling allows, reopen the workbook, inspect critical formulas/results and deliver the verified artifact with explicit caveats if cached formulas cannot be checked.

## Boundaries
Draft analytical work for human evaluation only. No trades, external orders, ledger posting, client approvals or unsourced investment promises. Missing sources must remain missing, not filled with plausible figures.

## Provenance
Provider-neutral adaptation guided by selected workflow patterns in [Anthropic Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins) and [Financial Services](https://github.com/anthropics/financial-services); see `collections/business/NOTICE.md`.
