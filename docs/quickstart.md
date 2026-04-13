# Quickstart

This repository is easiest to understand if you treat it as a developer-facing library of trust-system packages.

## 1. Validate the repository

```bash
python3 scripts/validate_tsmm_native.py
```

This confirms that the package metadata, graph structures, and example files are internally consistent.

## 2. Open one package from each class

Recommended tour:

- `profiles/first-person-credentials/`
- `patterns/delegation-after-identity/`
- `overlays/consent-not-data-structure/`
- `systems/wallet-to-agent-identity/`
- `evidence/the-proof-gap/`

## 3. Read package files in this order

1. `README.md`
2. `package.json`
3. `graph.json`
4. `constraints.json`
5. `evidence.json`
6. `tests/test-vector.json`

That order helps separate **intent**, **classification**, **structure**, **control**, **evidence**, and **validation expectations**.

## 4. Keep the line clear

When reading the repository, use this mental model:

- **Essay** = why the problem matters
- **TSMM** = how the system is structurally expressed
- **Package** = the reusable implementation unit in this repo

If you maintain that distinction, the repository becomes much easier to navigate.

## Recommended first package set

A good starting cluster is the set derived from *Enforceable Authority Without Legitimate Control*:

- `patterns/authority-legitimacy-validation`
- `overlays/legitimate-control-enforcement`
- `evidence/legitimate-control-decision-receipt`

Together they show the difference between modeling authority, modeling control, and modeling the evidence needed to prove that control actually held.
