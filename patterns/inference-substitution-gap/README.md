# Inference Substitution Gap Pattern

## Purpose

Pattern for detecting when institutions substitute behavioral inference for verifiable identity, claims, authority, or provenance.

## Source essay

- Essay: *Before the Graph*
- URL: https://thetrustgraph.substack.com/p/before-the-graph
- Published: 2026-04-13

## TSMM contribution

This package converts the essay-derived governance pressure into a TSMM-native surface with explicit authority, scope, evidence, decision, effect, and lifecycle semantics. It is intended for reuse by architects, standards authors, assurance teams, and repository maintainers who need governance controls that can be tested rather than merely described.

## Core controls

- `control.inference-verification-classification` — Classify each decision input as inferred, asserted, verified, or authoritative.
- `control.authority-inference-prohibition` — Prohibit inferred authority where delegated mandate or registry evidence is required.
- `control.accountability-dissolution-signal` — Flag decisions where inferred signals prevent accountability reconstruction.
- `control.verification-migration-path` — Declare a path from inference-based acceptance to verification-based acceptance.

## Required evidence fields

- `input_classification`
- `inference_basis`
- `verification_alternative`
- `authority_boundary`
- `accountability_record`
- `migration_path`

## Threat model

- `threat.identity-by-behavior` — Behavioral signals are used as a substitute for anchored identity.
- `threat.claim-by-correlation` — Claims are inferred from proxies rather than provenance-backed evidence.
- `threat.authority-by-context` — System context is treated as permission without mandate evidence.
- `threat.corrupted-feedback-loop` — Inference outputs become future governance data without validation.

## Validation posture

The package includes:

- `graph.json` for the TSMM graph surface
- `constraints.json` for control and lifecycle expectations
- `evidence.json` for evidence artifacts, verification expectations, and receipt fields
- `examples/valid-graph.json` and `examples/invalid-graph.json` for positive and negative validation
- `tests/test-vector.json` for repository validation expectations

## Governance impact

This artifact makes the relevant governance claim operational: authority is bounded, delegation is explicit, enforcement is receipt-bearing, revocation is lifecycle-aware, and redress remains visible to affected or relying parties.
