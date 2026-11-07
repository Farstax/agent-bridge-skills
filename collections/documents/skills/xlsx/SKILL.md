---
name: xlsx
description: Create, inspect, edit and validate Excel workbooks; preserve existing formulas and formatting.
---

# XLSX documents

## Job
Produce a real, editable spreadsheet file from user data or modify a supplied workbook without silently changing unrelated sheets. This Skill covers XLSX/CSV; do not invoke it for plain SQL, HTML dashboards or calculations that need no file.

## Discover the available tools
Use the workspace's provider-native terminal/file tools. Check whether Python and `openpyxl` are available before choosing them; use `pandas` for large tabular ingestion if installed. Do **not** assume Anthropic's hosted environment, preinstalled office tooling, network access or permissions. For files with formula recalculation, check for a compatible spreadsheet engine (such as LibreOffice) if available. Never install anything globally or with sudo as a Skill side effect. If a necessary tool is absent, explain the precise blocker or ask for authorisation for a workspace-local installation.

## Workflow
1. Locate the input file and determine workbook/sheet structure, required outputs, formula cells, named ranges, charts, formatting and external links. Never replace an existing source file without the user's request.
2. For edits, read the existing file with `openpyxl.load_workbook` (preserve `keep_vba` when editing macro-enabled sources, where supported). Match established conventions and change only authorised cells. Preserve formulas, comments, styles, worksheets and macros where possible. If a feature cannot be round-tripped, stop and disclose it before overwriting.
3. For new workbooks, organise sheets with explicit units, dates, labelled inputs and assumptions. Use actual formulas for derived values, not pasted results; avoid hard-coded, invented financial figures.
4. Use a new output path unless overwrite was explicitly requested; save atomically where feasible. When formulas were written, recalculate in an available compatible engine and reopen cached values. If no recalculator is available, flag that cached results are unverified rather than claiming they were calculated.
5. Reopen and verify sheet count, required cells, formulas, expected formats and key totals; check for formula errors where a calculation engine is present. Give the exact file path and a brief description of what changed.

## Validation / failure modes
A successful Python save is **not** sufficient evidence. Compare edits to the original for scope, check the ZIP/OOXML container and read back expected values/formulas. If `openpyxl` cannot preserve a feature (e.g. some drawings or specialised Excel features), do not silently degrade the original. Never treat `data_only=True` values as guaranteed current unless recalculation has occurred.

## Boundaries
No upload to third-party services without the user's direction. No speculative formulas, market prices or source figures. This Skill grants no new shell, file or external-account permissions.

## Provenance
Adapted for provider-neutral Agent Bridge from Anthropic's [xlsx Skill](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/xlsx) (Apache-2.0). Attribution: `collections/documents/NOTICE.md`.
