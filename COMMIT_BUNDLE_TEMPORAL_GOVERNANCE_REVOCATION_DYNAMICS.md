# Commit Bundle: Temporal Governance and Revocation Dynamics

## Commit title

Add temporal governance and revocation dynamics artifacts

## Commit message

Introduce Temporal Governance and Revocation Dynamics artifacts derived from The Persistence Trap, Exploiting the Revocation Lag Gradient, and When the Gradient Is the Attack Surface.

This commit adds artifact packages for persistence detection, revocation lag analysis, gradient exploitation surfaces, compositional revocation, and execution-bound revocation. It also introduces new receipt schemas for revocation propagation, execution authority state, and gradient exploitation signals.

The update extends the repository from static authority validation toward distributed execution-time governance assurance, making persistence, revocation delay, delegation contamination, and adversarial timing modelable, testable, and auditable.

## Files added

- `patterns/persistence-trap-detector/`
- `patterns/revocation-lag-analyzer/`
- `patterns/gradient-exploitation-surface/`
- `profiles/compositional-revocation-profile/`
- `overlays/execution-bound-revocation/`
- `schemas/receipts/revocation_propagation_receipt.schema.json`
- `schemas/receipts/execution_authority_state_receipt.schema.json`
- `schemas/receipts/gradient_exploitation_signal_receipt.schema.json`
- `examples/receipts/revocation_propagation_receipt.example.json`
- `examples/receipts/execution_authority_state_receipt.example.json`
- `examples/receipts/gradient_exploitation_signal_receipt.example.json`
- `docs/temporal-governance.md`
- `docs/revocation-dynamics.md`
- `docs/preservation-authority-divergence.md`
- `docs/gradient-exploitation-model.md`

## Files updated

- `README.md`
- `docs/index.md`
- `crosswalks/essay_to_artifact.yaml`
- `essays/source-catalog.yaml`
- `registries/evidence-types.json`
- `registries/decision-types.json`
- `registries/lifecycle-types.json`
- `validation/test-matrix.yaml`

## Validation notes

- JSON files parse successfully.
- YAML files parse successfully.
- New packages follow the existing TSMM-native package anatomy: `README.md`, `package.json`, `graph.json`, `constraints.json`, `evidence.json`, `examples/`, and `tests/`.
- Receipts are intentionally evidence-bounded: gradient exploitation receipts flag suspicious timing/routing signals without asserting actor intent.
