# Candidate Pipeline

This directory governs how new essays are assessed as artifact candidates.

## Workflow

1. Record the essay in `essays/` or reference it directly.
2. Create an evaluation file in `evaluation/evaluations/`.
3. Score the essay using `evaluation/scoring-model.md`.
4. If the threshold is met, create an artifact folder from `artifacts/_template/`.
5. Add minimal schema, examples, and manifest.
6. Link the new artifact in `ARTIFACT_INDEX.md`.

## Review questions

- What exactly is changing in the system?
- Can the concept be expressed as a governed structure?
- What runtime effect would the artifact enable or constrain?
- How is revocation handled?
- What happens when the model is contested or incomplete?

## Operating rule

Default to restraint. Promote only concepts that justify formalization.
