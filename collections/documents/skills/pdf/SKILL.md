---
name: pdf
description: Read, generate and validate PDF deliverables; disclose limits on editing scanned or protected PDFs.
---

# PDF documents

## Job
Extract/inspect PDF information or produce a verifiable PDF from user-approved content. Use an editable source file when future revision is expected. Never claim full arbitrary PDF editing/OCR support.

## Tools and classification
Determine whether the PDF is text-based, a scanned image, password-protected, a form, digitally signed or has annotations. Check installed options: `pypdf`, `PyMuPDF` or `pdftotext` for extraction; `reportlab`, installed office tools or a suitable provider-native generator for creation. Do not assume all tools exist. Do not run OCR or remote conversion without a suitable tool and user authorisation, especially for sensitive files.

## Workflow
1. Inspect page count, file restrictions, embedded fonts, form fields and available extractable text. Preserve source originals.
2. For reading, extract text with page references; distinguish missing text from blank pages, failed extraction or scans. Summaries and quotations must be traceable to pages.
3. For generation, choose a layout that supports headings, tables, pagination, margins and Unicode. Generate a real PDF at a user-visible path.
4. For permitted modifications, prefer regenerating from the original authoring source. Direct merging, annotations, page rotation, extraction or form edits are acceptable only when supported by a verified local tool. Warn that rewriting a signed PDF may invalidate signatures.
5. Reopen to confirm a valid document, expected page count and nonempty intended content; render pages/images when tooling permits and inspect clipping/overlap.
6. Return the PDF path, page count and any extraction, OCR, signature or visual-verification limitations.

## Boundaries
No silent redaction by drawing black rectangles over original text: redaction requires confirmed removal of underlying content. Do not upload confidential PDFs to third-party sites or alter legal/financial content beyond instructions.

## Provenance
Adapted for provider-neutral Agent Bridge from Anthropic's [pdf Skill](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/pdf) (Apache-2.0). Attribution: `collections/documents/NOTICE.md`.
