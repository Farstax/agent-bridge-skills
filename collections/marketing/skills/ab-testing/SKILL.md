---
name: ab-testing
description: Design and interpret evidence-led A/B tests and growth experiments.
---

# ab-testing

Provider-neutral adaptation of Corey Haines's Marketing Skills (`skills/ab-testing/SKILL.md`, MIT). Use current repository instructions and tools already available in the agent session; never require upstream product-marketing files or uninstalled companion skills.

Design and evaluate a trustworthy experiment, not a speculative marketing claim.

## Work
1. Read existing product context and evidence; inspect available analytics through authorised tools. If a baseline is missing, label all calculations hypothetical.
2. Write one falsifiable hypothesis: audience, change, expected directional effect, and why.
3. Select ONE pre-registered primary outcome, guardrails, unit of randomisation, assignment persistence, exposure definition, event denominator, segments and instrumentation QA.
4. Specify baseline, minimum detectable effect, alpha/power or Bayesian/sequential method, sample requirement, traffic-dependent duration, multiple comparisons and decision/stopping rule. Never reuse an upstream quick-reference sample-size table without stating assumptions or recalculating.
5. Define control and one purposeful variant, rollout/QA, guardrail failure response and pre-launch checklist.
6. For actual results report observed counts, absolute/relative effect, confidence/credible interval if calculated correctly, uncertainty, contamination, guardrails and decision. Fixed-horizon peeking cannot trigger early wins; inconclusive does not mean no effect.
7. Deliver an experiment brief or results report and a clear next decision.

## Boundaries
No experiment activation, account mutation, tool installation or analytics configuration on the skill's authority. Read-only design and analysis by default. `campaign-review` diagnoses wider campaign outcomes; `cro-audit` identifies friction; this skill designs the test and evaluates its evidence.

## Output integrity
Clearly separate evidence, assumptions and recommendations. Ask only for material missing information that cannot be found in available context. Never represent a hypothetical model as real campaign or customer data.
