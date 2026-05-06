# Fraud Externality Verification Profile

## Purpose

Profile that treats fraud as a cost externality produced by missing verification infrastructure, weak issuer accountability, registry weakness, and governance capture.

## Source essay

- Essay: *Fraud as an Externality of Missing Infrastructure*
- URL: https://thetrustgraph.substack.com/p/fraud-as-an-externality-of-missing
- Published: 2026-05-05

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.issuer-authorization` — Verify issuer authorization, accountability, and removal route before accepting claims.
- `control.claim-provenance-verification` — Require verifiable provenance for claims, credentials, documents, or representations.
- `control.registry-governance-accountability` — Require admission, suspension, removal, appeal, and anti-capture evidence for registry authority.
- `control.externality-reduction-evidence` — Record how verification controls reduce fraud cost transfer to relying parties and victims.

## Required evidence fields

- `issuer_authorization`
- `claim_provenance`
- `registry_admission_policy`
- `removal_policy`
- `dispute_route`
- `anti_capture_controls`
- `externality_reduction_evidence`

## Threat model

- `threat.unverifiable-identity` — Actor identity is inferred or asserted without authoritative anchor.
- `threat.forged-provenance` — Claim lineage cannot be reconstructed or verified.
- `threat.governance-capture` — Registry or issuer governance is captured, weak, or non-contestable.
- `threat.cost-socialization` — Verification failure pushes fraud costs to users, institutions, or the public.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
