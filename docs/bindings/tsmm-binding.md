---
owner: maintainers
last_reviewed: 2026-06-30
applicable_version: v0.4.0
title: TSMM Binding
layout: default
parent: TSMM alignment
nav_order: 1
---

# TSMM Binding

The active binding declaration is available at:

```text
bindings/tsmm/tga-tsmm-binding.json
```

The binding constraints are available at:

```text
bindings/tsmm/constraints.json
```

## Binding purpose

The binding makes explicit that Trust Graph Artifacts is an interpretation corpus aligned to TSMM v0.21.0.

TGA owns package interpretation and essay provenance. TSMM owns the trust-system semantic grammar, including authority graphs, runtime governance envelopes, decision receipts, and task evidence lifecycle semantics. TIS owns executable artifact contracts when artifacts need external validation, registry publication, evidence bundles, evaluation envelopes, decision receipts, or assurance-level semantics.

## Runtime assurance projection

The active v0.4.0 release also includes a TIS binding:

```text
bindings/tis/tga-tis-binding.json
bindings/tis/constraints.json
```

Use this binding when a TGA package must produce evidence that can be consumed outside this repository.

## Validation

Run:

```bash
python3 scripts/validate_tsmm_native.py
python3 scripts/validate_tis_alignment.py
```
