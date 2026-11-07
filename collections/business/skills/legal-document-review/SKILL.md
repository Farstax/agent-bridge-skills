---
name: legal-document-review
description: Review supplied contracts and legal documents for clauses, obligations, risks and unanswered questions.
---

# Legal Document Review

## Job and trigger
Use for clause extraction, document comparison and risk spotting in a user-supplied legal document; not legal representation, jurisdiction-specific definitive advice or a contract-signing workflow.

## Method
1. Identify document/version, parties, jurisdiction if stated, intended transaction and requested review focus. Inspect the original document using available tools; use `pdf`/`docx` Skills for file parsing or tracked editable outputs.
2. Extract the exact relevant provision, section heading and page/paragraph reference. Separate what the document says from interpretations, assumptions and missing information.
3. Flag unusual indemnities, termination clauses, liability limits, privacy, governing law, payment terms, notice periods, variation and unresolved definitions only where genuinely relevant. Explain consequences conditionally, with clarity about missing applicable-law context.
4. Present a prioritised issue list (clause, factual text, concern, suggestion or question), plus a neutral summary. Quote accurately and keep document versions separate.
5. Mark proposed revisions as drafts for qualified human/legal review and disclose text-extraction limitations.

## Boundaries
No legal conclusions presented as professional advice, no signing or external legal filings. Do not disclose sensitive document contents beyond the authorised workspace/output. A missing clause is not the same as a successfully checked absence.

## Provenance
Provider-neutral adaptation guided by selected workflow patterns in [Anthropic Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins) and [Financial Services](https://github.com/anthropics/financial-services); see `collections/business/NOTICE.md`.
