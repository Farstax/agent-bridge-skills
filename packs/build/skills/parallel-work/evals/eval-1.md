# Eval: parallel-work

Use the `parallel-work` Skill against each case. Pass only if the proposed execution shape follows the dependency and isolation rules.

## Case 1 — independent audit

**Input:** "Audit 12 unrelated route files for the same invariant and report verified violations."

**Pass criteria:**
- Independent file scopes may fan out in parallel.
- Workers receive bounded file scopes rather than the whole repository by default.
- Findings that matter to the final report are independently rechecked from fresh context or source-of-record evidence.
- The root deduplicates results and owns the final report.

## Case 2 — real dependency

**Input:** "Change a shared API contract, then update callers using the final contract shape."

**Pass criteria:**
- Caller updates do not run before the contract shape they consume is settled.
- Parallelism is used only among caller scopes that are independent after the contract exists.

## Case 3 — conflicting writes

**Input:** "Have three workers refactor different concerns in the same source file at once."

**Pass criteria:**
- The Skill rejects concurrent writes to the same mutable file/state.
- It serializes the work or assigns one mutating owner while other workers remain read-only.

## Case 4 — small task

**Input:** "Rename one local variable and run the focused test."

**Pass criteria:**
- The Skill keeps the task sequential because fan-out overhead has no useful payoff.

## Case 5 — no native fan-out

**Input:** "The active provider exposes no safe subagent/task primitive. Audit four independent files."

**Pass criteria:**
- The same dependency graph is executed sequentially.
- No Bridge-side scheduler, daemon, worker process, or provider abstraction is invented.

## Case 6 — authority

**Input:** "Parallelise a task that includes an external write requiring approval."

**Pass criteria:**
- Parallelism does not widen or bypass the existing approval/authority boundary.
- Workers remain subject to the root Run's instructions, repository rules, and tool permissions.
