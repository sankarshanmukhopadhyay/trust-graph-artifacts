# Epistemic Impact Assessment

## Purpose

Portable evidence package for evaluating whether a proposed decision can access the situated knowledge it materially depends upon.

## Source essay

- Essay: *The Edge Knows First*
- URL: https://thetrustgraph.substack.com/p/the-edge-knows-first
- Published: 2026-07-22

## Authority boundary

This package is an implementation-draft governance artifact. It uses existing TSMM entities and TIS-aligned evidence conventions. It does not create canonical TSMM semantics, redefine TIS contracts, certify an institution, or establish universal thresholds.

## Core controls

- `control.decision-and-effect-bound` — Bind the assessment to a specific decision and proposed effect.
- `control.knowledge-path-evidenced` — Evidence dependencies, bearers, channels, and contested findings.
- `control.independent-authority` — Identify assessor authority and conflicts of interest.
- `control.freshness-and-appeal` — Declare validity, expiry, challenge, and appeal paths.

## Required evidence fields

- `decision_ref`
- `effect_ref`
- `knowledge_dependencies`
- `knowledge_bearer_classes`
- `consultation_channels`
- `prior_incident_retrieval`
- `contested_findings`
- `residual_epistemic_risks`
- `assessment_outcome`
- `assessor_authority`
- `validity_period`
- `appeal_or_challenge_path`

## Assurance interpretation

A passing result means that the declared discovery, challenge, authority, and evidence conditions were met for the assessed scope and validity period. It does not prove that every relevant fact was discovered or that the resulting decision is correct.

## Validation posture

The package includes a TSMM-native graph, constraints, evidence requirements, positive and negative graph examples, and a repository test vector.
