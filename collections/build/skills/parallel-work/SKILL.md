---
name: parallel-work
description: Use when a task contains multiple independent scopes that can run concurrently inside one normal agent Run without sharing mutable state.
---

# Parallel work

Use this Skill to remove unnecessary waiting from substantial work. Keep the work inside the active provider's normal Run and native task/subagent facilities. Do not create a second scheduler, worker lifecycle, daemon, swarm runtime, or durable task graph.

## Decide the graph before running it

Break the task into the smallest useful work units. For each unit, identify:

- the input it needs;
- the result or artifact it must produce;
- the files, records, or other mutable state it may write;
- whether another unit truly consumes its output.

Add a dependency edge only when a later unit needs an earlier unit's output or both require exclusive access to the same mutable state. Mere ordering in a written plan is not a dependency.

Run independent units in parallel when the active provider has a safe native mechanism for it and the saved waiting time is worth the coordination cost. Keep work sequential when the task is small, tightly coupled, or mostly shares one working set.

If provider-native parallel execution is unavailable, run the same graph sequentially. Do not invent Bridge-side orchestration to compensate.

## Isolate mutation

Two parallel workers must not edit the same mutable scope.

For repository work, give mutating workers separate worktrees/branches or disjoint file ownership. If two units need the same file or shared state, serialize them or give one worker ownership and make the other read-only.

Never use parallelism to widen authority. Every worker remains bound by the root Run's user instructions, repository rules, tool permissions, approval boundaries, and external-action limits.

## Give workers a bounded contract

Each worker gets only the context needed for its scope and returns a compact result:

- conclusion or completed artifact;
- evidence actually observed, such as commands/tests run, source locations, or record identifiers;
- changed files or artifact paths when it mutated local state;
- blockers or uncertainty.

Do not merge full worker transcripts into the root context when a short result plus evidence is enough. For large outputs, keep the detail in files/artifacts and return a manifest or concise index.

## Verify important claims independently

A worker checking its own conclusion is not independent verification. When a finding is consequential enough to verify, give a fresh verifier only the claim, required source-of-record context, and evidence needed to test it. The verifier should re-open the source of record or rerun the relevant check and return `VERIFIED`, `REFUTED`, or `UNKNOWN` with concise evidence.

This is a general execution pattern. It does not replace repository-specific adversarial review, release-readiness review, exact-head CI, or any other required gate.

## Reconcile once at the root

The root agent owns integration and the final answer. Before synthesis:

1. collect terminal worker results;
2. deduplicate overlapping findings or artifacts;
3. resolve contradictions from evidence rather than vote-counting;
4. re-open current source-of-record state when worker evidence may have become stale;
5. integrate only compatible mutations, preserving the repository's normal merge/test rules.

Do not ask another agent to synthesize duplicate raw outputs when deterministic reduction can shrink them first.

## Completion

The parallel pass is done when every required unit is complete or explicitly blocked, required independent verification has settled, conflicting writes are reconciled safely, and the root has produced the requested final result. Parallel execution is an implementation detail; report the outcome and material evidence rather than narrating the worker topology unless it matters to the user.
