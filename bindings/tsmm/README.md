
# TSMM Binding Layer

This directory binds selected Trust Graph artifacts to the Trust Systems Meta Model (TSMM) so the repository can express not only artifact content, but also the trust-system structure each artifact depends on.

## What the binding layer does

For each artifact in the current 12-artifact expansion set, the binding layer adds a machine-readable projection covering:

- governance context
- profile
- entities, roles, and bounded authority
- relationships
- policy and controls
- threats and mitigations
- evidence and verification
- trust decisions and downstream effects
- lifecycle and revocation semantics

## Structure

```text
bindings/tsmm/
├── README.md
├── schema.yaml
└── projections/
    ├── after-consent.yaml
    ├── delegation-after-identity.yaml
    └── ...
```

## Binding status

- Scope: the 12-artifact expansion set in this repository
- Status: draft but fully implemented
- Validation: `scripts/validate_tsmm_bindings.py`

## Design intent

The binding layer treats TGA artifacts as executable governance components that can be projected into a TSMM-style system graph. This makes authority, delegation, enforcement, evidence, and revocation inspectable across artifacts instead of remaining local to each schema.
