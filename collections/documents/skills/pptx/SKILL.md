---
name: pptx
description: Create, modify and validate editable PowerPoint presentations while preserving templates.
---

# PPTX documents

## Job
Produce or edit a genuinely editable PPTX, using an existing template/layout where supplied. Prefer a concise story and legible, accessible slide content over decorative filler.

## Tools
Inspect installed options first: `python-pptx` or `pptxgenjs` can author common slides, while direct OOXML changes are only appropriate for focused edits by a capable agent. Availability in an upstream Claude sandbox does not prove availability here. For rendering, use an installed office renderer when possible. No implicit `npm install`, sudo or global package changes.

## Workflow
1. Inspect any existing slides and template: layout dimensions, masters, fonts, theme, speaker notes, charts, source assets and numbering.
2. Define slide purpose, content hierarchy and number of slides; keep claims sourced and editable text/shapes wherever possible. Use images only when authorised and properly licensed.
3. For editing, prefer preserving master/layout relationships and existing theme rather than rebuilding the presentation. If the chosen library would lose unsupported media, animations or specialised charts, disclose the limitation before modifying.
4. Write a new PPTX unless overwrite was explicitly requested.
5. Validate that the PPTX opens, required slide count/text/shapes/tables exist, relationships resolve, and no intended objects are missing. If a renderer is available, render slide images and visually inspect overflow, alignment, fonts and readability, particularly on narrow layouts.
6. Return the verified PPTX path and note any unverified visual aspects or feature loss.

## Boundaries
Do not flatten content into screenshots merely to claim an editable deck; do not invent numbers, quotations or images. Do not add a rendering service, browser or additional agent framework.

## Provenance
Adapted for provider-neutral Agent Bridge from Anthropic's [pptx Skill](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/pptx) (Apache-2.0). Attribution: `collections/documents/NOTICE.md`.
