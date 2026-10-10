---
name: impeccable
description: Design, critique, audit, polish and harden existing frontend interfaces. Use for UI work including accessibility, responsive layout, visual hierarchy, typography, interactions and design-system consistency; not backend-only or marketing positioning.
---

# Impeccable — frontend design quality

Adapted from [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus (Apache-2.0). This is a portable instructions-only adaptation for Agent Bridge. It does **not** include Impeccable's engine, browser extension, native hooks, installers or deterministic detector suite.

## Job

Produce or improve a functioning frontend that respects product truth, user goals, existing code conventions and the requested scope. Choose evidence-backed design over template decoration. For brand positioning and a marketing creative brief, use `creative-strategy` instead.

## Start

1. Identify the surface and user goal: **persuade** (landing pages), **operate** (app workflows), **read** (documentation) or **experience** (portfolio/showcase).
2. Inspect the existing app, design tokens, layout primitives, copy, assets, responsive breakpoints, accessibility conventions and available tests before proposing changes.
3. Separate a **refinement** (preserve design identity, behaviour and out-of-scope content) from a **redesign** (new visual language, preserve product truth and function). Do not silently turn one into the other.
4. Ask only for missing consequential product decisions. Never fabricate claims, research findings or brand assets.

## Select the smallest workflow

- **Shape:** describe user task, information hierarchy, navigation, primary action, constraints and edge states before writing UI.
- **Critique:** assess hierarchy, clarity, focus, visual rhythm, density, typography, consistency and usability. Prioritise actionable findings, citing code or inspected screens.
- **Audit:** check keyboard navigation, contrast, focus, semantics, labels, errors, small screens, overflow, loading/empty/error states and performance. Distinguish observed findings from untested hypotheses; do not claim an automated audit ran unless tools actually ran.
- **Polish:** fix a bounded set of obvious visual defects while preserving existing interactions, routes and content.
- **Harden:** verify long text, locale expansion, validation, failures, asynchronous states and narrow viewports.
- **Adapt:** make layouts work on relevant mobile, tablet and desktop sizes, respecting reduced-motion preferences.
- **Extract:** when duplication exists, consolidate existing components and tokens instead of adding an unnecessary design-system layer.
- **Typeset / layout / colourize / clarify:** apply only the requested typography, spacing, colour or UX-copy improvement. Prefer a coherent visual hierarchy to arbitrary decorative effects.

## Implementation rules

- Preserve working paths and interactions. Prefer current components, tokens and styling patterns; do not add a framework for a visual task.
- Ensure accessible names, visible focus, usable target sizes, text reflow, sufficient contrast, semantic elements and keyboard operation.
- Use meaningful type scales, intentional whitespace, restrained colour, clear selected/error/success states and responsive content priority. Do not make a universal rule out of a fashionable aesthetic.
- Animations must communicate state or orientation, respect reduced motion and avoid disrupting core tasks.
- Use only tools already available and authorised in the active provider. Do not install software, download binaries, register hooks, access browser profiles or publish anything on the skill's authority.
- A tool's absence limits the verification claim, not the ability to carry out source-level design work.

## Verify and deliver

1. Run the existing relevant build, lint and tests if available.
2. When screenshot/browser access exists, inspect desktop and mobile in one bounded pass, fix observed defects, then confirm at most once. Otherwise inspect code and clearly state what remains unverified.
3. Report the exact changed surface, functional/accessibility checks, evidence and remaining limitations. A visual audit is not automatically certified by this skill.

## Upstream boundary

The upstream `/impeccable` command router, `PRODUCT.md` / `DESIGN.md` automation, live-browser variations, hooks and 59 deterministic detectors require upstream tooling and are **not** provided by this skill. Never claim those commands or detectors ran. See `collections/design/NOTICE.md` for provenance and licensing.
