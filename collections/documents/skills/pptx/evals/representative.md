# Evaluation: presentation creation and update
**Request:** Create a six-slide project update with supplied facts, then change one metric on slide three while preserving theme and slide order.
**Expected:** Editable PPTX with six slides and matching source data, validated by reopening and inspecting editable text/shapes. Render/inspect every slide for overflow when an office renderer exists.
**Negative:** A supplied deck with unsupported transitions or embedded objects is not silently flattened or rewritten. If no renderer exists, state that visual QA remains unverified.
**Review evidence:** Compare slide texts, XML relationships and (where possible) rendered images before and after editing.
