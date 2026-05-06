# Commitment Lifecycle Mediation Overlay

## Purpose

Cross-cutting overlay for commitment drift, conflict, breach, reconciliation, revocation, and retirement.

## Source essay

- Essay: *When Machines Make Commitments*
- URL: https://thetrustgraph.substack.com/p/when-machines-make-commitments
- Published: 2026-05-05

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.commitment-drift-detection` — Detect changes in conditions, policy, feasibility, or counterparties that alter commitment meaning.
- `control.conflict-detection` — Detect conflicting commitments, derived commitment chains, and incompatible obligations.
- `control.lifecycle-reconciliation` — Require reconciliation records for modified, conflicted, breached, or revoked commitments.
- `control.human-steward-escalation` — Escalate high-impact commitment conflicts to a named steward or trustee.

## Required evidence fields

- `commitment_state`
- `drift_signal`
- `conflict_check`
- `reconciliation_record`
- `escalation_owner`
- `retirement_condition`

## Threat model

- `threat.silent-commitment-drift` — Commitment meaning changes without notice or mediation.
- `threat.conflicting-obligations` — Multiple machine commitments create incompatible obligations.
- `threat.unretired-broken-commitment` — Broken commitments remain active and continue to induce reliance.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
