---
name: attribution
description: Reconcile marketing channel attribution with observed conversion truth and uncertainty.
---

# attribution

Provider-neutral adaptation of Corey Haines's Marketing Skills (`skills/attribution/SKILL.md`, MIT). Use current repository instructions and tools already available in the agent session; never require upstream product-marketing files or uninstalled companion skills.

Explain what marketing measurement supports and where channel credit remains uncertain.

## Work
1. Establish the decision and canonical conversion source (backend/CRM/payment as appropriate), conversion/event definitions, time zone, windows, identity and consent constraints.
2. Inventory observed channels, UTM conventions, first-party event tracking, platform-reported claims, self-reported sources, dark social and branded/direct search. Identify absent coverage.
3. Deduplicate conversion totals against the authoritative source. Never add platform claims together as if independent; compare lookback windows, view-through, cross-device, modeled events and missing records.
4. Distinguish **source attribution** (who receives reporting credit) from **incrementality** (causal lift). First/last/multi-touch models are interpretations, not proof of causation.
5. Provide an explicit discrepancy table with facts, probable explanations, uncertainties, confidence and focused validation steps. Do not invent allocation percentages or multiply an ad platform's reported contribution to reconcile totals.
6. Advise measurement improvements: UTMs, event names and consent-respecting first-party/self-report signals, with no implied deployment.

## Boundaries
Read-only analysis. `google-analytics`, `paid-ads-review` and other authorised data skills may provide observations. No new tracking, consent changes, credentials, advertising mutations or account linking without separate authorisation.

## Output integrity
Clearly separate evidence, assumptions and recommendations. Ask only for material missing information that cannot be found in available context. Never represent a hypothetical model as real campaign or customer data.
