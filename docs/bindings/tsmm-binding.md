---
owner: maintainers
last_reviewed: 2026-08-22
applicable_version: v0.12.1
title: TSMM Binding
layout: default
parent: TSMM alignment
nav_order: 1
---

# TSMM Binding

The active binding declaration is:

```text
bindings/tsmm/tga-tsmm-binding.json
```

The binding constraints are:

```text
bindings/tsmm/constraints.json
```

## Binding purpose

Trust Graph Artifacts is an interpretation and assurance corpus aligned to **TSMM v0.24.0**. The alignment direction is deliberately asymmetric:

- **TSMM owns canonical trust-system semantics and stable semantic identifiers.**
- **TGA consumes and profiles those semantics into essay-derived implementation, governance, and assurance artifacts.**
- **TIS owns portable executable contracts when evidence, authority boundaries, decisions, registry publication, or assurance objects must travel across repository boundaries.**

TGA does not create a semantic dependency from TSMM back to TGA.

## Stable semantic identifiers

Active TGA mappings use TSMM v0.24.0 identifiers such as:

```text
urn:tsmm:concept:authority
urn:tsmm:concept:delegation
urn:tsmm:concept:scope
urn:tsmm:concept:policy
urn:tsmm:concept:evidence-artifact
urn:tsmm:concept:trust-decision
urn:tsmm:concept:effect
urn:tsmm:concept:revocation
urn:tsmm:concept:assurance-profile
urn:tsmm:concept:redress
```

The binding pins the TSMM source commit used for the current alignment review while treating the released v0.24.0 semantic registry, rather than a copied local vocabulary, as semantic authority.

## Runtime assurance projection

The corresponding TIS binding is:

```text
bindings/tis/tga-tis-binding.json
bindings/tis/constraints.json
```

The current compatibility baseline is:

```text
TGA  v0.12.1
TSMM v0.24.0
TIS  v0.14.1
```

## Validation

Run:

```bash
python3 scripts/validate_tsmm_alignment.py
make validate
```

The alignment validator fails if the TGA version, TSMM binding version, TIS semantic-authority declaration, stable semantic identifiers, or active binding documentation drift from the declared baseline.

{: .assurance }
> This is repository-level compatibility evidence, not external certification. TSMM remains authoritative for semantic definitions; TGA validation proves that the local binding contract is internally consistent with the reviewed TSMM baseline.
