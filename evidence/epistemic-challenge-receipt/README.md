# Epistemic Challenge Receipt

## Purpose

Records a qualifying epistemic challenge, suspension decision, review, override, and final effect disposition.

## Source essay

- Essay: *The Edge Knows First*
- URL: https://thetrustgraph.substack.com/p/the-edge-knows-first
- Published: 2026-07-22

## Authority boundary

This package is an implementation-draft governance artifact. It uses existing TSMM entities and TIS-aligned evidence conventions. It does not create canonical TSMM semantics, redefine TIS contracts, certify an institution, or establish universal thresholds.

## Core controls

- `control.trigger-evidenced` — Record the trigger and threshold evidence.
- `control.authority-separated` — Separate challenge validation, review, and override authority.
- `control.state-transitions-receipted` — Receipt suspension, review, resumption, modification, withdrawal, and override.
- `control.affected-parties-visible` — Preserve affected-party notification and redress routes.

## Required evidence fields

- `trigger`
- `threshold_evidence`
- `eligible_participant_verification`
- `suspension_state`
- `review_authority`
- `review_outcome`
- `override_evidence`
- `effect_status`
- `notification_and_redress`

## Assurance interpretation

A passing result means that the declared discovery, challenge, authority, and evidence conditions were met for the assessed scope and validity period. It does not prove that every relevant fact was discovered or that the resulting decision is correct.

## Validation posture

The package includes a TSMM-native graph, constraints, evidence requirements, positive and negative graph examples, and a repository test vector.
