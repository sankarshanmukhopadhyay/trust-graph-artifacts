# Redress Rails for Machine Decisions

## Purpose

Adds machine-readable redress requirements to automated or agentic decisions so review authority, evidence disclosure, correction, and state repair are part of the execution surface.

## Source essay

- Essay: *Redress at Machine Speed*
- URL: https://thetrustgraph.substack.com/p/redress-at-machine-speed
- Published: 2026-05-01

## TSMM contribution

This package expresses the Trust Graph governance argument as a TSMM-native model with explicit authority, delegation, policy, evidence, decision, effect, revocation/status, and redress surfaces. It is aligned with TSMM v0.21.0 and can be projected into TIS v0.10.0 runtime assurance artifacts where external validation is required.

## Core controls

- `control.redress-route-required` - Require visible redress route for every consequential decision
- `control.evidence-disclosure` - Disclose decision basis and evidence references to authorized reviewers
- `control.state-repair` - Record correction, reversal, compensation, or downstream state repair

## Required runtime evidence

- `actor`
- `authority_boundary`
- `policy_evaluated`
- `evidence_bundle`
- `revocation_or_status_check`
- `decision_receipt`
- `effect_admission`
- `redress_route`

## TIS projection

The package can be projected into the following TIS v0.10.0 artifact contracts:

- `governance/authority-boundary.schema.json`
- `evidence/evidence-bundle-manifest.schema.json`
- `oasf/oasf-evaluation-envelope.schema.json`
- `decision/decision-receipt.schema.json`
- `registry/registry-publication-profile.schema.json`

## Validation posture

The package includes schema-valid `package.json`, `graph.json`, `constraints.json`, `evidence.json`, valid and invalid graph examples, and a test vector. The invalid example deliberately uses an unsupported relation type so negative validation remains executable.

## Governance impact

This package makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation/status is checked before effect, evidence is auditable, and redress remains visible to affected or relying parties.
