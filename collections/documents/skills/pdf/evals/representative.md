# Evaluation: PDF generation, extraction and limitations
**Request:** Generate a two-page event brief from supplied text, extract the title and a cited fact from page two, then rotate a copy of page two.
**Expected:** Valid PDF, correct text/page count on reopening, and page-specific citations. Render/check pages where possible. Preserve the source while producing the rotated copy.
**Negative:** For a scanned PDF without OCR capability, report that accurate text extraction is unavailable rather than inventing text. For a signed PDF, warn that writing changes may invalidate its signature.
**Review evidence:** Reopen with a local PDF reader, validate pages/text/rotation and inspect rendered pages if available.
