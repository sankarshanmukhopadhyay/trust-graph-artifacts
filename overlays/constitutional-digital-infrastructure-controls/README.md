# Constitutional Digital Infrastructure Controls Overlay

## Purpose

Overlay for non-derogable constraints in high-risk digital infrastructure, including rights to context, contestability, reversibility, explanation, and human authority.

## Source essay

- Essay: *Governance for High-Risk Digital Infrastructure*
- URL: https://thetrustgraph.substack.com/p/governance-for-high-risk-digital
- Published: 2026-04-08

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.non-derogable-rights-profile` — Declare protected rights to context, contestability, reversibility, explanation, and human authority.
- `control.prohibited-inference-category` — Prohibit inference categories that exceed legitimate governance scope.
- `control.human-led-decision-class` — Require human authority for protected decision classes.
- `control.public-transparency-required` — Require public-facing control descriptions and change notices for high-risk systems.
- `control.independent-audit-access` — Require independent audit access to governance logs and boundary attestations.

## Required evidence fields

- `rights_profile`
- `prohibited_inference_categories`
- `human_led_decision_classes`
- `public_transparency_record`
- `audit_access_record`
- `change_notice_policy`

## Threat model

- `threat.rights-sensitive-automation` — System automates decisions that require human authority or contextual judgement.
- `threat.prohibited-inference-use` — System uses protected or inadmissible inference categories.
- `threat.unannounced-policy-shift` — Material control changes occur without notice or public accountability.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
