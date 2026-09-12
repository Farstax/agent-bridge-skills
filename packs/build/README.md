# Build pack

Provider-neutral engineering methods for agents doing substantial implementation, audit, and codebase work. This pack is intentionally instruction-only: it does not add a scheduler, daemon, worker runtime, provider abstraction, or new authority model.

## Skills

| Skill | Origin | Job |
|---|---|---|
| `parallel-work` | Farstax-authored | Turn genuinely independent work into safe provider-native fan-out, isolate mutation, independently verify important claims, and reconcile once at the root. |

## Architecture boundary

`parallel-work` operates inside one normal agent Run. It uses the active provider's native task/subagent/async capability when available and falls back to sequential execution when it is not. Agent Bridge continues to own only its existing durable cross-provider boundaries.

The Skill does not replace repository-specific review, release qualification, CI, approval, or deployment rules. It also does not grant any worker more authority than the root Run already has.

This pack is kept deliberately small so it can migrate cleanly to the lightweight Collection model being designed in `Farstax/agent-bridge#764` without turning grouping metadata into a second capability runtime.
