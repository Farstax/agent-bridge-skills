# Grill Me acceptance cases

## Underspecified decision — one question
Prompt: "Grill me about adding notifications to the app."
Expected: inspect available context; ask exactly one consequential, answerable user decision with its relevance and a recommended answer; no implementation.

## Facts are discoverable
Prompt: "Grill me about replacing this repository's existing database migrations."
Expected: inspect existing migration code and repository instructions first; do not ask which migration system is used if inspectable.

## Fully specified
Prompt: "Grill me: keep the current UI and API, add a read-only status indicator using the existing status endpoint, no new settings, no backend changes."
Expected: avoid fabricated design decisions; offer a concise confirmation or only a genuinely consequential uncovered choice.

## Multi-turn dependencies
Prompt: "Grill me about integrating a messaging platform." User answers channel/identity choice in turn one.
Expected: retain settled choice and ask only downstream consequential decisions, one per turn, with recommendations.

## Explicit stop
Prompt: "Stop grilling me."
Expected: cease questions, summarise what is settled and label unknowns; no mutation.

## Negative implicit invocation
Prompt: "Implement the status indicator exactly as specified."
Expected: do not invoke Grill Me or block the implementation with an interview.

## No side effects
Prompt: "Grill me about a database migration."
Expected: research read-only; no file edit, GitHub issue creation, deploy or service change during interview.
