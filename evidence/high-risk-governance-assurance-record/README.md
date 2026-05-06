# High-Risk Governance Assurance Record

## Purpose

Evidence model for recording risk classification, boundary conditions, reversibility, contestability, auditability, oversight, and remediation for high-risk infrastructure.

## Source essay

- Essay: *Governance for High-Risk Digital Infrastructure*
- URL: https://thetrustgraph.substack.com/p/governance-for-high-risk-digital
- Published: 2026-04-08

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.assurance-record-completeness` — Require classification, consequence, coupling, delegation, reversibility, contestability, audit, oversight, and remediation fields.
- `control.boundary-condition-evidence` — Record boundary conditions and non-automatable decision classes.
- `control.reversibility-proof-present` — Require evidence that material effects can be halted, corrected, or reversed.
- `control.independent-audit-reference` — Record the audit or assessment reference used to substantiate governance posture.

## Required evidence fields

- `system_risk_classification`
- `consequence_analysis`
- `coupling_analysis`
- `interpretive_authority_analysis`
- `dependency_lock_in_assessment`
- `delegation_boundary_declaration`
- `reversibility_proof`
- `contestability_proof`
- `governance_log_reference`
- `public_oversight_record`
- `independent_audit_reference`
- `remediation_route`

## Threat model

- `threat.assurance-by-prose` — High-risk governance is asserted in narrative without testable evidence.
- `threat.boundary-omission` — Protected decision classes and boundary conditions are not declared.
- `threat.ineffective-contestability` — Challenge rights exist procedurally but not operationally.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
