# Edge-Triggered Suspension

## Purpose

Allows qualifying edge-originated objections to suspend a proposed effect pending independent review.

## Source essay

- Essay: *The Edge Knows First*
- URL: https://thetrustgraph.substack.com/p/the-edge-knows-first
- Published: 2026-07-22

## Authority boundary

This package is an implementation-draft governance artifact. It uses existing TSMM entities and TIS-aligned evidence conventions. It does not create canonical TSMM semantics, redefine TIS contracts, certify an institution, or establish universal thresholds.

## Core controls

- `control.eligible-objectors-verifiable` — Verify objector eligibility without treating identity as authority.
- `control.threshold-machine-verifiable` — Make objection thresholds and windows machine-verifiable.
- `control.suspension-enforced` — Prevent effect admission while a valid suspension is active.
- `control.override-receipted` — Require bounded emergency overrides and retrospective evidence.

## Required evidence fields

- `decision_ref`
- `qualifying_effect`
- `objector_eligibility`
- `threshold_evidence`
- `suspension_window`
- `review_authority`
- `override_receipt`
- `outcome`

## Assurance interpretation

A passing result means that the declared discovery, challenge, authority, and evidence conditions were met for the assessed scope and validity period. It does not prove that every relevant fact was discovered or that the resulting decision is correct.

## Validation posture

The package includes a TSMM-native graph, constraints, evidence requirements, positive and negative graph examples, and a repository test vector.
