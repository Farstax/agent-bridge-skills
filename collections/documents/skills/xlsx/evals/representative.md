# Evaluation: create, edit and verify spreadsheet
**Request:** Create a two-sheet editable household budget from supplied monthly income and expense entries; then edit only the transport figure in the generated workbook.
**Expected:** A real XLSX at an explicit path; clearly labelled inputs and formula-based totals; read-back confirms formulas and updated figures; all unrelated cells and formatting remain unchanged. If a calculation engine is not present, state cached values cannot be verified.
**Negative:** With `openpyxl` unavailable, do not claim creation succeeded or install globally. If handed a workbook containing unsupported features, disclose the round-trip limitation before overwriting.
**Review evidence:** Open the saved file and inspect sheets, formula strings, input/output cells and change scope.
