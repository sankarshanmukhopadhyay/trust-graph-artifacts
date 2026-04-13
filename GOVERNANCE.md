# Governance Model

This repository is governed as an operational system, not a documentation space.

---

## 1. Authority

Authority to:

- create artifacts
- approve structural models
- assign lifecycle status

rests with maintainers.

Artifacts represent enforceable claims and must meet structural criteria before inclusion.

---

## 2. Delegation

Contributors may:

- propose new artifacts
- refine schemas
- add examples and tests
- challenge assumptions

All contributions must:

- include justification
- reference source essay
- follow manifest structure

---

## 3. Enforcement

Artifacts must include:

- artifact manifest (`artifact.yaml`)
- schema or model definition
- example instances
- declared lifecycle status

CI enforcement, when introduced, should validate:

- structure
- completeness
- consistency

---

## 4. Revocation

Artifacts may transition to:

- deprecated
- superseded

All revocation actions must:

- identify successor artifact, if applicable
- include rationale
- preserve lineage

---

## 5. Redress

Disputes are first-class.

Use issues with labels:

- `semantic-dispute`
- `enforcement-gap`
- `model-incomplete`

Resolution requires:

- structured argument
- possible artifact revision
- documentation of decision

---

## 6. Lifecycle Control

Artifacts move through:

```text
Draft → Experimental → Stable → Deprecated
```

No artifact is assumed stable by default.

---

## 7. Design Principle

If a governance claim cannot be:

- implemented
- validated
- revoked
- contested

it does not belong in this repository.
