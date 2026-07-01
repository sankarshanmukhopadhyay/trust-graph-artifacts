# Registry Gatekeeper Risk Profile

## Purpose

Models registry admission and suspension as market-shaping governance power with appeal, anti-capture controls, revocation evidence, and publication transparency.

## Source essay

- Essay: *Trust Lists as Market Gatekeepers*
- URL: https://thetrustgraph.substack.com/p/trust-lists-as-market-gatekeepers
- Published: 2026-05-04

## TSMM contribution

This package expresses the Trust Graph governance argument as a TSMM-native model with explicit authority, delegation, policy, evidence, decision, effect, revocation/status, and redress surfaces. It is aligned with TSMM v0.21.0 and can be projected into TIS v0.10.0 runtime assurance artifacts where external validation is required.

## Core controls

- `control.admission-criteria-public` - Publish admission and suspension criteria
- `control.appeal-route-required` - Provide appeal and review route for exclusion or downgrade
- `control.capture-risk-monitor` - Monitor concentration, conflicts, and anti-competitive registry behavior

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
