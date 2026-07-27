# Situated-Knowledge-Dependent Infrastructure Profile

## Purpose

Classifies and protects functions whose value materially depends on tacit knowledge, operational proximity, or community-maintained context.

## Source essay

- Essay: *The Edge Knows First*
- URL: https://thetrustgraph.substack.com/p/the-edge-knows-first
- Published: 2026-07-22

## Authority boundary

This package is an implementation-draft governance artifact. It uses existing TSMM entities and TIS-aligned evidence conventions. It does not create canonical TSMM semantics, redefine TIS contracts, certify an institution, or establish universal thresholds.

## Core controls

- `control.classification-criteria` — Apply explicit situated-knowledge dependency criteria.
- `control.protection-lifecycle` — Provide protected, review, suspension, withdrawal, and retirement states.
- `control.appeal-and-revalidation` — Provide appeal, periodic revalidation, and revocation.
- `control.change-impact-gate` — Require an epistemic impact assessment before material change.

## Required evidence fields

- `function_ref`
- `dependency_criteria`
- `classification_decision`
- `protection_state`
- `review_date`
- `appeal_path`
- `change_assessment_ref`

## Assurance interpretation

A passing result means that the declared discovery, challenge, authority, and evidence conditions were met for the assessed scope and validity period. It does not prove that every relevant fact was discovered or that the resulting decision is correct.

## Validation posture

The package includes a TSMM-native graph, constraints, evidence requirements, positive and negative graph examples, and a repository test vector.
