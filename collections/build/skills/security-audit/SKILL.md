---
name: security-audit
description: Use for defensive source-grounded security questions and focused vulnerability reviews. Run a full multi-phase codebase audit only when explicitly requested and when independent reviewers and an OS-enforced offline sandbox are available. Never test live systems without separate authority.
---

# Security audit

This is an optional defensive Skill. It borrows the coverage-led hunting, adversarial verification, and honest finding-status distinctions of Cloudflare's `security-audit` Skill. See `NOTICE.md` and `LICENSE`. It does **not** provide privileged tooling, network access or authorization to test production.

## Operating modes and authorization

**Focused guidance (default):** For a security question, change review, suspected issue or one component, inspect the relevant code and trust boundary. Return a concise finding with source evidence, or say what is unknown. Do not launch the full audit, create report files, run a scanner or claim comprehensive coverage.

**Full audit (explicit opt-in):** Only for a request to conduct a full security audit/penetration test of a specified codebase or to produce complete audit artifacts. Do not interpret an ordinary `review it` or `ship it` as such a request. Scope repository/revision and output directory, check actual tool and safety capabilities, and then execute the six phases below only to the extent proved safe. This Skill never grants further implementation, deployment or spending authority.

## Mandatory safety preflight

Source inspection is read-only. **Before any target-controlled executable action** (tests, builds, scripts, generated commands, browsers, fuzzers, servers, fixture execution), establish an OS-enforced sandbox with **all** of:

- target repository/toolchain read-only, and only a dedicated per-check scratch path writable by the target-controlled process; no host home, other workspace, service socket, credential or peer audit folder exposure;
- an empty environment rebuilt from a minimal explicit allowlist, with scratch-local `HOME`, temp directories and caches; no secrets;
- disabled external networking, allowing isolated local loopback only if the check needs it;
- strict CPU, memory, process, file, disk and wall-clock limits, including normal-looking quick checks;
- no package downloads, global installers, privileged helpers or production identities; tests use dummy principals and synthetic data only.

Do not probe live services, customer tenants, public endpoints or shared infrastructure, test availability against shared processes, or extract customer data. Use only already available local tooling. Independently confirm fresh reviewer contexts and their read-only/advisory boundary before representing findings as independently verified.

If **any** control is missing, stop executable testing. A safe **source-only** examination may continue; classify execution-dependent claims as `needs_validation` and disclose that the full audit and its execution coverage were **not completed**. Do not weaken the sandbox, attempt to acquire privileges or substitute a prompt saying "be careful" for enforcement.

## Six-phase full audit procedure (when prerequisites pass)

1. **Reconnaissance.** Identify the fixed target revision, actor/resource/authority boundaries, trusted/untrusted inputs, storage, credentials, message/HTTP protocols, release and tenancy model. Create a scoped coverage ledger with unit ID, file/path boundary, attack class, status (`covered`, `deferred`, `blocked`), evidence and unresolved work. Limit investigation to the requested source.
2. **Coverage-led hunt.** Assign independent bounded read-only reviewers by truly disjoint security surfaces, using provider-native subagents if supported; do not create a new orchestrator. Examine reachable paths and threat classes relevant to that target (authentication, authorization, isolation, injection, persistence, supply chain, concurrency, resource exhaustion, LLM/tool boundary). Record what was actually inspected, not only proposed.
3. **Candidate validation.** For each distinct candidate, ask a fresh independent verifier to **try to disprove it** against the actual source/reproduction evidence. A finder cannot independently verify itself. Use sandboxed, non-destructive synthetic reproductions only when permitted. A mere checklist deviation is not a vulnerability if an existing boundary blocks exploitation.
4. **Structured findings.** Record findings in machine-readable `findings.json` with `id`, `status` (`confirmed`, `needs_validation`, `rejected`), `title`, `source` (file/line/revision), `actor`, `resource`, `boundary`, `evidence`, `verification`, `impact`, `remediation`, and `unresolved` (for needs-validation). Severity is only assigned to `confirmed` cases with demonstrated impact. Do not manufacture severity or successful exploit claims.
5. **Independent record check.** A different fresh reviewer checks each confirmed record's source trace and observed result. If a material claim changes, independently recheck the replacement. If a trustworthy independent reviewer is unavailable, record `needs_validation`, not `confirmed` by fiat.
6. **Reporting.** From actual ledger and records, produce `REPORT.md` summarizing audited revision, boundaries, confirmed findings, unresolved leads, rejected false positives, tested vs untested surfaces, safety limitations and minimal fix direction. Include the ledger and findings JSON, keeping sensitive evidence out of chat and version control.

Use existing files/JSON tooling to check structured output for parseability, stable unique IDs, valid statuses, and complete evidence fields; do not install a new validator or copy a whole harness just to format a report. A run may find zero confirmed vulnerabilities without proving absence of vulnerabilities.

## Output location and contamination control

Default full-audit output is an unused directory **outside** the target checkout, scoped to that audit run. Write inside the repository only if the user expressly authorizes a directory that is demonstrably version-control ignored. Keep scratch outputs isolated from report outputs, never copy untrusted generated files into trusted reports without validating type, path, size and contents. Never include secrets, unredacted auth headers or customer data.

## Focused finding format

For each finding: **Status**, **affected actor/resource/boundary**, **source reference**, **observed or safely demonstrated result**, **independent verification (or lack thereof)**, **impact when confirmed**, **smallest effective fix**, and **unknowns**. Explain if hardening advice is not an exploitable boundary failure.

## Relationship to other Skills

`systematic-debugging` diagnoses ordinary defects; `requirements-to-acceptance` frames code changes; `release-readiness-review` alone owns exact-head `review it`/merge readiness. This optional security Skill does not replace those procedures or require Cloudflare's complete external harness.
