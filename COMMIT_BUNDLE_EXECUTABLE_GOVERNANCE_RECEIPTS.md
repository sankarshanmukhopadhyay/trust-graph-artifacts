# GitHub Commit Content

## Commit title

feat: add executable governance artifacts and receipt evidence model

## Commit message

Introduce a TSMM-aligned executable governance artifact layer derived from three Trust Graph essays:

- The Control Plane Has Already Shifted
- The Commons After the Control Plane Shifts
- Who Holds the License

This commit adds authority, control-plane, legitimacy, delegation, licensing, and verification artifacts; introduces first-class decision, authority, delegation, revocation, licensing, and enforcement receipts; adds JSON Schemas and example receipt chains; and documents the execution, governance, provenance, and walkthrough model.

### Proposed changes

- Add artifact YAMLs for authority topology, execution flow, legitimacy gap, delegation chain, license authority, and verification profile.
- Add receipt taxonomy under artifacts, schemas, and examples.
- Add crosswalks mapping essays to artifacts and risks to controls/tests/evidence.
- Add end-to-end scenario examples with receipt chains.
- Add documentation for methodology, execution model, governance model, receipts, decision provenance, and walkthrough.
- Add provenance map for the executable governance artifact expansion.
- Update README and docs index to surface the new layer.

### Validation/testing notes

- Existing TSMM package validator was run successfully.
- Receipt schemas and examples were generated consistently.
- The new receipt tests are documented as conformance targets in `validation/executable-governance-receipt-tests.md`.

### Documentation updates

- `docs/artifact-methodology.md`
- `docs/execution-model.md`
- `docs/governance-model.md`
- `docs/receipts.md`
- `docs/decision-provenance.md`
- `docs/walkthrough.md`
