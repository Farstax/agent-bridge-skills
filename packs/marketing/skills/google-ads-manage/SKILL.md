---
name: google-ads-manage
description: Operate an authorized Google Ads account using live evidence, including keywords, bids, budgets, campaign state, targeting, and other supported mutations. Use when the task calls for changing or optimizing Google Ads rather than only auditing it.
---

# Google Ads Manage

Adapted from NotFair's `google-ads/manage` Skill (see this Skill's entry in the repository root `catalogue.json`).

## Job

Diagnose and operate a connected Google Ads account using the authority the workspace owner has already granted to the agent and connected tool/service.

This Skill does not grant account access, OAuth scope, budget authority, or a separate Farstax approval. The connected account/tool and workspace owner's configuration remain authoritative.

## Required inputs

- Live, authorized Google Ads access through a connected capability.
- A clear target: account, campaign, ad group, keyword, asset, or other supported object.
- Enough current account evidence to justify the requested change.

If access is unavailable or the connected capability does not permit the requested write, do not work around that boundary. Return the evidence and the exact proposed change instead.

## Method

1. Read the current state and recent performance relevant to the task. Check conversion-tracking quality before treating CPA/ROAS as decision-grade.
2. Identify the bottleneck from evidence rather than generic best practice: query quality, rank, budget, bidding, targeting, creative, landing page, tracking, or demand.
3. Choose the smallest useful change. Prefer reversible, narrowly scoped mutations over broad restructuring when the evidence does not justify a larger intervention.
4. Respect the authority already present in the workspace and connected service. Do not request, create, or bypass broader OAuth scopes, credentials, account roles, budgets, native approval controls, or other authority just to complete the Skill.
5. When the task authorizes action and the connected capability permits it, execute the supported mutation. Do not invent an additional Farstax confirmation ceremony merely because a change can affect spend.
6. Read back the resulting state when the capability supports it. Report what changed, the affected object, relevant before/after values, and any operation identifier actually returned.
7. If the write is denied, unavailable, stale, or fails, stop mutation attempts. Explain the boundary or failure and return a proposed change the owner can apply or authorize through their normal tool/service controls.

## Spend changes

Budget, bid, and other spend-affecting changes are allowed only within the authority and limits already granted by the workspace owner and connected Google Ads tooling. Treat configured budgets, account limits, and native approval controls as constraints. Never expand them from this Skill.

Do not infer that a large budget change is justified just because write access exists. Base spend changes on current evidence and the stated business objective.

## Evidence requirements

For any material recommendation or mutation, report the account currency, date range, relevant denominator, target object, current value/state, and evidence supporting the change. Thin data should produce a watch/proposal result rather than forced optimization.

## Failure behaviour

- No authorized account access: stop and say what access is missing.
- Read access but no write access: provide the proposed mutation; do not attempt a bypass.
- Tool/service rejects the mutation: report the rejection and leave state unchanged unless the tool explicitly reports a partial result.
- Current state differs materially from the state used to plan the change: re-evaluate rather than blindly applying a stale mutation.

## Dependencies and effects

Requires an authorized Google Ads connection for live work. It can read and mutate external account state, including changes that may affect spend. Installation alone grants none of that authority.

See this Skill's entry in the repository root `catalogue.json` for machine-readable metadata.
