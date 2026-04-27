# System Package Template

Use this template when adding a composed trust-system package.

A system package should show how multiple TSMM-native components operate together with named actors, decision surfaces, controls, evidence outputs, and effects.

Required active package files:

- `README.md`
- `package.json`
- `graph.json`
- `constraints.json`
- `evidence.json`
- `examples/valid-graph.json`
- `examples/invalid-graph.json`
- `tests/test-vector.json`

Minimum modeling expectations:

- identify the governing authority and relying parties
- show which policies constrain execution
- show where delegation, enforcement, revocation, and evidence are produced
- include at least one `TrustDecision` and one `EvidenceBundle`
- define what failure or quarantine looks like when authority cannot be proven
