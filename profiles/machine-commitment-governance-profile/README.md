# Machine Commitment Governance Profile

## Purpose

Governance profile for machine-generated commitments that create institutional obligations, reliance, or future-state expectations.

## Source essay

- Essay: *When Machines Make Commitments*
- URL: https://thetrustgraph.substack.com/p/when-machines-make-commitments
- Published: 2026-05-05

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.commitment-authority-binding` — Bind every commitment to an accountable controller, delegated mandate, policy version, and commitment class.
- `control.intent-binding-schema` — Represent terms, activation conditions, constraints, counterparties, and reliance assumptions in machine-verifiable form.
- `control.proof-carrying-commitment` — Require a proof-carrying commitment receipt before external reliance is permitted.
- `control.reconciliation-route-required` — Declare reconciliation, dispute, and retirement paths for commitments that conflict, drift, or fail.

## Required evidence fields

- `commitment_id`
- `delegated_authority`
- `commitment_terms`
- `activation_conditions`
- `constraint_checks`
- `execution_attestation`
- `counterparty_reliance`
- `reconciliation_route`
- `contestability_route`

## Threat model

- `threat.commitment-without-authority` — A machine creates reliance without an accountable authority chain.
- `threat.commitment-drift` — The commitment changes meaning or feasibility without mediation.
- `threat.unreviewable-breach` — A breached machine commitment lacks reconciliation or dispute handling.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
