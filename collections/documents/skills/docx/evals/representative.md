# Evaluation: template-preserving Word edit
**Request:** Edit an existing multi-section DOCX memo: update one date and one table entry without changing headings, page setup, footer or unrelated paragraphs; also create a clean new memo from supplied content.
**Expected:** Two valid, editable DOCX outputs. Read-back confirms requested content, table cells and preserved styles/sections. If a renderer exists, inspect rendered pages for clipping.
**Negative:** An input with complex unsupported objects must not be rewritten destructively without disclosure. Missing `python-docx` must be surfaced rather than silently substituting plain text.
**Review evidence:** Compare source and edited DOCX content/styles and inspect exported layout when available.
