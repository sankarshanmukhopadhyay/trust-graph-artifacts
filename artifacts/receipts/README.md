# Receipt Artifacts

Receipts are the repository's first-class evidence layer. They prove that authority, delegation, revocation, licensing, enforcement, and decisions were evaluated at execution time.

Schemas live under `schemas/receipts/` and examples live under `examples/receipts/`.

## Decision receipt alignment

The active TGA decision receipt uses the TSMM decision receipt structure as its runtime assurance core. TGA-specific provenance is carried through `sourceEssays`, while authority, policy, evidence, revocation, boundary, decision, effect, assurance, and review fields remain TSMM-aligned.

Use `examples/receipts/decision_receipt.example.json` as the canonical active representation.
