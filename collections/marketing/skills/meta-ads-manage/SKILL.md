---
name: meta-ads-manage
description: Operate an authorized Meta Ads account using live evidence, including campaigns, ad sets, budgets, targeting, delivery state, and other supported mutations. Use when the task calls for changing or optimizing Facebook or Instagram ads rather than only auditing them.
---

# Meta Ads Manage

Adapted from NotFair's `meta-ads/manage` Skill (see this Skill's entry in the repository root `catalogue.json`).

## Job

Diagnose and operate a connected Meta Ads account using the authority the workspace owner has already granted to the agent and connected tool/service.

This Skill does not grant account access, OAuth scope, budget authority, or a separate Farstax approval. The connected account/tool and workspace owner's configuration remain authoritative.

## Required inputs

- Live, authorized Meta Ads access through a connected capability.
- A clear target: account, campaign, ad set, ad, audience, budget, or other supported object.
- Enough current delivery and conversion evidence to justify the requested change.

If access is unavailable or the connected capability does not permit the requested write, do not work around that boundary. Return the evidence and the exact proposed change instead.

## Method

1. Read the current state and performance needed for the task. Verify the relevant attribution window and tracking quality before treating CPA/ROAS as decision-grade.
2. Diagnose from evidence: delivery/learning state, frequency and creative fatigue, audience overlap, CPM/CPC, conversion rate, budget pacing, or another supported factor.
3. Choose the smallest useful change. Avoid stacking unnecessary edits during learning or making broad restructures from thin data.
4. Respect the authority already present in the workspace and connected service. Do not request, create, or bypass broader OAuth scopes, credentials, account roles, budgets, native approval controls, or other authority just to complete the Skill.
5. When the task authorizes action and the connected capability permits it, execute the supported mutation. Do not invent an additional Farstax confirmation ceremony merely because a change can affect spend.
6. Read back the resulting state when supported. Report what changed, the affected object, relevant before/after values, attribution context, and any operation identifier actually returned.
7. If the write is denied, unavailable, stale, or fails, stop mutation attempts. Explain the boundary or failure and return a proposed change the owner can apply or authorize through their normal tool/service controls.

## Spend changes

Budget and other spend-affecting changes are allowed only within the authority and limits already granted by the workspace owner and connected Meta tooling. Treat configured budgets, account limits, and native approval controls as constraints. Never expand them from this Skill.

Write access is not evidence that scaling is sensible. Check frequency, CPM trend, attribution context, learning state, and conversion economics before changing spend.

## Evidence requirements

For any material recommendation or mutation, report account currency, date range, attribution window, target object, current value/state, and evidence supporting the change. If the data is too thin to distinguish signal from noise, return a watch/proposal result rather than forcing a mutation.

## Failure behaviour

- No authorized account access: stop and say what access is missing.
- Read access but no write access: provide the proposed mutation; do not attempt a bypass.
- Tool/service rejects the mutation: report the rejection and leave state unchanged unless the tool explicitly reports a partial result.
- Current state differs materially from the state used to plan the change: re-evaluate rather than blindly applying a stale mutation.

## Dependencies and effects

Requires an authorized Meta Ads connection for live work. It can read and mutate external account state, including changes that may affect spend. Installation alone grants none of that authority.

See this Skill's entry in the repository root `catalogue.json` for machine-readable metadata.
