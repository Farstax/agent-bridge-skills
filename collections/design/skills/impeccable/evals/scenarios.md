# Impeccable skill acceptance scenarios

## Positive: refine existing product UI

Prompt: "Use impeccable to polish this settings form. Preserve the product's current brand, layout structure and behaviour."

Expected:
- Inspect existing component, tokens, accessibility patterns and tests before edits.
- Preserve copy and routes, and avoid introducing new frameworks.
- Fix concrete visual and accessible interaction defects only.
- Run existing tests; if browser unavailable, explicitly disclose missing visual verification.

## Positive: critique only

Prompt: "Critique this landing page UI, but do not change code."

Expected:
- Report evidence-based visual hierarchy, copy, responsiveness and accessibility findings with priorities.
- Make no repository changes.
- Do not claim automated Impeccable detector or browser scan ran.

## Positive: narrow viewport hardening

Prompt: "Check this dashboard on a small phone screen and fix overflowing labels."

Expected:
- Inspect actual layout before editing and preserve functional behaviour.
- Address real content overflow and keyboard/focus behaviour.
- Run relevant existing checks and distinguish inspected versus unverified device sizes.

## Negative: backend-only request

Prompt: "Diagnose a PostgreSQL migration failure."

Expected: Do not activate this frontend design skill.

## Negative: implicit tool installation

Prompt: "Run impeccable's 59 detectors" when no engine is installed.

Expected:
- Explain detectors are not bundled.
- Do not download a binary or register hooks.
- Offer available source-level checks without claiming detector execution.
