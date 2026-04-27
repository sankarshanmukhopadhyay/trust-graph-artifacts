# Commit Bundle: Harmonize TGA Decision Receipts with TSMM

## Commit title

Harmonize TGA decision receipts with TSMM runtime assurance model

## Commit message

Align the active Trust Graph Artifacts decision receipt schema and example with the TSMM decision receipt representation.

This commit updates TGA so decision receipts no longer use a parallel snake_case representation for active artifacts. The schema now follows the TSMM runtime assurance core: `decisionId`, `subjectRef`, `requestingActorRef`, `authorityBasis`, `policyRefs`, `evidenceRefs`, `boundaryRef`, `decision`, `effect`, `revocationStateChecked`, `assuranceLevel`, and `reviewPath`.

TGA-specific provenance remains intact through `receiptId`, `receiptType`, `sourceEssays`, and optional `signature` fields. This keeps essay-derived provenance distinct from runtime decision evidence while preserving TGA's role as an operational interpretation layer for The Trust Graph.

### Changed files

- `schemas/receipts/decision_receipt.schema.json`
- `examples/receipts/decision_receipt.example.json`
- `docs/receipts.md`
- `docs/decision-provenance.md`
- `artifacts/receipts/README.md`
- `scripts/validate_tsmm_native.py`

### Governance impact

- Eliminates representation drift between TGA and TSMM for decision receipts.
- Makes TGA decision receipts directly comparable with TSMM runtime assurance receipts.
- Preserves TGA essay provenance without treating it as runtime evidence.
- Adds receipt example validation coverage to the repository validator.

### Validation notes

- JSON syntax validation passed for the updated decision receipt schema and example.
- Python syntax compilation passed with `python3 -S -m py_compile scripts/validate_tsmm_native.py`.
- A local smoke validation confirmed the example contains all required TSMM-aligned decision receipt fields and valid enum values.
- Full repository validation via `scripts/validate_tsmm_native.py` could not be completed in this container because importing/running the local `jsonschema` validation stack timed out. The CI workflow remains wired to run the full validator.
