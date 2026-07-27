# Epistemic Adequacy Gate

## Purpose

Determines whether a consequential decision has sufficient, contestable knowledge pathways before its effect is admitted.

## Source essay

- Essay: *The Edge Knows First*
- URL: https://thetrustgraph.substack.com/p/the-edge-knows-first
- Published: 2026-07-22

## Authority boundary

This package is an implementation-draft governance artifact. It uses existing TSMM entities and TIS-aligned evidence conventions. It does not create canonical TSMM semantics, redefine TIS contracts, certify an institution, or establish universal thresholds.

## Core controls

- `control.knowledge-dependencies-declared` — Require material situated-knowledge dependencies to be declared.
- `control.knowledge-bearers-represented` — Require relevant knowledge-bearing actor classes and channels to be evidenced.
- `control.unanticipated-input-channel` — Preserve a channel capable of receiving unanticipated operational input.
- `control.residual-uncertainty-recorded` — Record residual epistemic uncertainty and expiry conditions.

## Required evidence fields

- `knowledge_dependencies`
- `knowledge_bearer_classes`
- `consultation_channels`
- `unanticipated_input_channel`
- `residual_epistemic_risks`
- `assessment_outcome`

## Assurance interpretation

A passing result means that the declared discovery, challenge, authority, and evidence conditions were met for the assessed scope and validity period. It does not prove that every relevant fact was discovered or that the resulting decision is correct.

## Validation posture

The package includes a TSMM-native graph, constraints, evidence requirements, positive and negative graph examples, and a repository test vector.
