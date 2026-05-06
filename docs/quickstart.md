---
title: Quickstart
layout: default
nav_order: 2
---

# Quickstart

This repository is easiest to understand as a developer-facing library of TSMM-native trust-system packages.

## 1. Validate the repository

```bash
python3 scripts/validate_tsmm_native.py
```

This checks package schemas, graph schemas, valid/invalid examples, selected semantic gates, provenance coverage, and canonical artifact crosswalk integrity.

## 2. Choose the right first tour

### Authority modeling tour

Use this when your goal is to understand executable authority, legitimate control, and decision evidence:

- `patterns/authority-legitimacy-validation/`
- `overlays/legitimate-control-enforcement/`
- `evidence/legitimate-control-decision-receipt/`

### Cross-type structural tour

Use this when your goal is to see one example from each package class:

- `profiles/first-person-credentials/`
- `patterns/delegation-after-identity/`
- `overlays/consent-not-data-structure/`
- `systems/wallet-to-agent-identity/`
- `evidence/the-proof-gap/`

These two tours are intentionally different. The first is the canonical onboarding path for authority modeling. The second is a taxonomy tour across package types.

## 3. Read package files in this order

1. `README.md`
2. `package.json`
3. `graph.json`
4. `constraints.json`
5. `evidence.json`
6. `tests/test-vector.json`

That order separates intent, classification, structure, control, evidence, and validation expectations.

## 4. Keep the line clear

- **Essay** = why the problem matters
- **TSMM** = how the system is structurally expressed
- **Package** = the reusable implementation unit in this repository
- **Receipt** = the evidence object emitted when authority, delegation, enforcement, revocation, or decision state must be audited

This is the core adoption rule: do not flatten concept, model, package, and evidence into one narrative layer.
