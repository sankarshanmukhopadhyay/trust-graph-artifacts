# Agent Accountability Edge

## Purpose

Models the accountable edge for delegated agent action: principal, controller, agent, mandate, scope, policy, revocation state, and redress before effect admission.

## Source essay

- Essay: *Your Agents Are Not Failing Your*
- URL: https://thetrustgraph.substack.com/p/your-agents-are-not-failing-your
- Published: 2026-02-26

## TSMM contribution

This package expresses the Trust Graph governance argument as a TSMM-native model with explicit authority, delegation, policy, evidence, decision, effect, revocation/status, and redress surfaces. It is aligned with TSMM v0.21.0 and can be projected into TIS v0.10.0 runtime assurance artifacts where external validation is required.

## Core controls

- `control.scoped-agent-mandate` - Require mandate, scope, expiry, and revocation state for agent action
- `control.controller-traceability` - Bind every agent action to accountable controller and principal
- `control.pre-effect-decision-receipt` - Emit decision receipt before consequential effect is admitted

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
