---
title: 'Walkthrough: Commons Moderation Decision'
layout: default
parent: Executable governance
nav_order: 6
---

# Walkthrough: Commons Moderation Decision

A content input is submitted to a commons ingestion pipeline. The system resolves authority, checks delegation, checks revocation state, evaluates policy, executes enforcement, and emits a decision receipt. A reviewer can then replay the decision from the receipt chain and determine whether authority was exercised legitimately.


## TSMM v0.20 alignment checklist

Before merging a new or revised package, verify that:

1. The package has a clear Trust Graph source or governance pressure.
2. The graph models authority, evidence, policy, decision, and effect using TSMM-native concepts where applicable.
3. Any local Trust Graph vocabulary is mapped through `registries/outcome-vocabulary.yaml` or documented as narrative-only.
4. `assuranceLevel` is not treated as a TIS AL1-AL4 claim unless an explicit assurance artifact is referenced.
5. Runtime evidence is represented separately from essay provenance.
6. `python3 scripts/validate_tsmm_native.py` passes.


## v0.3.0 walkthrough path

To review the v0.3.0 increment, follow this path:

1. Read `patterns/runtime-authority-envelope` to understand the authority wrapper for agentic action.
2. Read `profiles/machine-commitment-governance-profile` and `evidence/proof-carrying-commitment-receipt` to understand commitment evidence.
3. Read `profiles/fraud-externality-verification-profile` to understand verification infrastructure as fraud-cost control.
4. Read `patterns/inference-substitution-gap` and `patterns/legibility-trap-detector` to understand migration from inference to verification.
5. Read `profiles/high-risk-digital-infrastructure-governance-profile`, `overlays/constitutional-digital-infrastructure-controls`, and `evidence/high-risk-governance-assurance-record` to understand high-risk architectural governance.
6. Run `python3 scripts/validate_tsmm_native.py` to confirm structural integrity.
