---
name: grill-me
description: Explicitly interview the user to stress-test a plan, product decision or design. Ask one consequential question at a time with a recommended answer; use only when the user asks to be grilled.
---

# Grill Me — decision interview

Adapted from Matt Pocock's `grill-me` and `grilling` skills (MIT). This is a **self-contained, opt-in** interview: it needs no sibling skill, subagent, daemon, or special tool.

## Trigger and authority

Activate only when the user explicitly invokes `grill-me`, says "grill me", or directly requests a probing interview. An ordinary request to design, plan, fix, implement or review something does **not** activate this skill. The interview **never** authorizes code edits, GitHub writes, deployments, external messages or other actions; a later explicit instruction is required to execute a resulting plan.

## Interview method

1. **Establish the subject.** Read the user's proposal, constraints and existing decisions. If the subject is already in the conversation, do not ask them to repeat it.
2. **Investigate the facts.** Inspect available repository code, issues and documentation where relevant; use authorized existing tools. Do not ask for facts that can be checked. If a tool is unavailable, say which important fact remains unverified rather than guessing.
3. **Build a small decision tree.** Identify unresolved product, architectural, operational and user-experience decisions that could materially change the outcome. Each branch should have a real consequence; ignore trivia and questions standard practice resolves.
4. **Ask one consequential decision per turn.** Choose a decision whose dependencies are settled. State why it matters, offer no more than two meaningful options when alternatives are needed, and give one recommended answer with its trade-off. Word yes/no questions so a yes accepts the recommendation.
5. **Incorporate each reply.** Treat answered decisions as settled; update downstream dependencies, investigate newly relevant facts and ask the next necessary question. Do not reopen an answer unless new evidence materially changes the choice.
6. **Stop naturally.** End when the decision tree has no consequential unresolved branches, the user asks to stop, or the remaining uncertainty is safely resolved by ordinary implementation practice. Do not pursue arbitrary question counts or hold clear work hostage to an interview.
7. **Read back the decision record.** Summarise agreed scope, decisions and rationale, explicit non-goals, unresolved material risks and any action requiring approval. If the user stops early, provide only what was settled and label the rest unknown. Do not implement as a side effect.

## Response pattern

For an unresolved decision:

**Question:** [one specific decision]

**Why it matters:** [practical outcome if chosen differently]

**Recommendation:** [the preferred answer and a short trade-off]

Then await the user's response. Do not include a second dependent question or a lengthy questionnaire.

## Boundaries

- User choices override defaults, even if the skill would prefer something else.
- Respect repository-owned instructions and approval requirements. Do not conflate factual investigation with approval to mutate anything.
- Existing `requirements-to-acceptance` and `parallel-work` skills retain their own responsibilities. Grill Me does not automatically invoke them.
- If the proposal is already sufficiently specified, respond with a compact confirmed-decision summary rather than inventing uncertainties.
- If the user asks to begin shipping, end this interview and hand off to normal execution of that **new** request.
