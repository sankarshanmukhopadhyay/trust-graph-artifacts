# Proof-Carrying Commitment Receipt

## Purpose

Evidence model that records why a machine-generated commitment was authorized, what terms were bound, which constraints were evaluated, and how it can be challenged or reconciled.

## Source essay

- Essay: *When Machines Make Commitments*
- URL: https://thetrustgraph.substack.com/p/when-machines-make-commitments
- Published: 2026-05-05

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.commitment-receipt-completeness` — Require all commitment, authority, terms, constraint, revocation, attestation, and contestability fields.
- `control.execution-attestation-present` — Bind the commitment to execution evidence and the evaluated policy version.
- `control.reliance-record-required` — Capture counterparty reliance and intended operational effect.
- `control.contestability-route-required` — Record the dispute, reconciliation, or remediation endpoint.

## Required evidence fields

- `commitment_id`
- `technical_actor`
- `accountable_controller`
- `principal`
- `mandate_reference`
- `policy_version`
- `commitment_terms`
- `activation_conditions`
- `constraint_checks`
- `authority_validation`
- `revocation_state`
- `execution_attestation`
- `counterparty_reliance`
- `reconciliation_route`
- `contestability_route`

## Threat model

- `threat.missing-commitment-proof` — Commitment exists without durable proof of authority and evaluated constraints.
- `threat.unbound-terms` — Terms are human-readable but not machine-checkable.
- `threat.no-reconciliation-route` — Affected parties cannot resolve conflict or breach.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
