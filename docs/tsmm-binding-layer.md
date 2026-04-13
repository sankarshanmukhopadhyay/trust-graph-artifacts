---
owner: maintainers
last_reviewed: 2026-04-13
status: draft
---

# TSMM Binding Layer

## Purpose

This document explains how the Trust Graph Artifacts repository binds selected artifacts into TSMM-aligned projections. The goal is to move from artifact-local semantics to a comparable trust-system representation.

## What this increment implements

The current increment adds a full TSMM binding layer for the 12-artifact expansion set. Each included artifact now has:

- a machine-readable projection in `bindings/tsmm/projections/`
- manifest-level binding references
- shared entity and control registries
- updated local TSMM mapping notes
- validation logic that checks projection completeness and reference integrity

## Binding model

The binding layer treats each artifact as a TSMM-relevant profile or policy surface and then makes explicit:

1. governance context
2. participating entities and roles
3. bounded authority and relationships
4. controls and threats
5. evidence and verification expectations
6. trust decision and effect path
7. lifecycle and revocation transitions

## Current scope

This increment covers the 12-artifact expansion set:

- after-consent
- delegation-after-identity
- your-agents-are-not-failing-your
- wallet-to-agent-identity
- digital-credential-verification-policy-playbook
- systemic-controllers
- trust-registry-governance-model
- machine-readable-privacy-terms
- portable-eligibility
- the-proof-gap
- execution-time-delegation
- crisis-of-narrative-control

## Validation

Use:

```bash
python scripts/validate_tsmm_bindings.py
```

Validation checks:

- projection files exist for all bound artifacts
- required sections exist
- entity and control references resolve to shared registries
- each trust decision references at least one effect
- lifecycle model includes the expected minimum states

## Why this matters

Without the binding layer, the repository can express governance artifacts but cannot yet compare them as system structures. The binding layer closes that gap and makes TGA more legible as a TSMM-adjacent repository.
