# Eval: google-analytics

**Input:** A GA4 measurement ID (`G-XXXX`) supplied instead of a property resource.

**Pass criteria:**
- Skill does not substitute the measurement ID for the property resource; it asks for or resolves the correct `properties/...` id.
- Any comparison uses complete equivalent periods, not partial-to-complete.
- Sampling/thresholding warnings, if present, are surfaced rather than silently dropped.
