---
name: docx
description: Create and edit structured Word documents with faithful formatting and read-back verification.
---

# DOCX documents

## Job
Create, review or revise an editable DOCX document, preserving the supplied structure and formatting when the task is an edit. Do not treat a Word deliverable as plain text pasted into chat.

## Tools and preparation
Locate files using available provider-native file tools. Check for `python-docx` or another suitable local DOCX writer; never assume it is installed. Check for a compatible document renderer (e.g. LibreOffice) only if visual verification is required. Do not invoke sudo, install software globally or send documents to external converters without permission.

## Workflow
1. Identify whether the job is new authoring or an edit. For edits, inspect headings, paragraphs, tables, styles, headers, footers, section breaks, numbering, links and embedded objects.
2. Preserve supplied document templates, brand styles, page setup, tables and user content outside the requested change. For a new document, use semantic heading/paragraph styles and consistent margins; preserve citations and source attribution.
3. Make the smallest change with a DOCX-capable library. `python-docx` can create and edit many common documents but cannot safely round-trip all complex Word features: if unsupported elements are material, stop before destructive modification and explain.
4. Write the result to an explicit output file, normally separate from the original. Reopen with the library and inspect all requested text, table structure, styles and changed paragraphs.
5. When a renderer is available, render to PDF/images and inspect page breaks, clipping, tables and headings; otherwise disclose the missing visual pass. Deliver the editable DOCX path and validation status.

## Evidence / boundaries
Use only facts provided by the user or named sources; never invent credentials, legal conclusions or branding. A valid ZIP container does not prove correct layout. Do not claim page-perfect fidelity without rendering. No credential acquisition, network upload or new permission is implied by using this Skill.

## Provenance
Adapted for provider-neutral Agent Bridge from Anthropic's [docx Skill](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/docx) (Apache-2.0). Attribution: `collections/documents/NOTICE.md`.
