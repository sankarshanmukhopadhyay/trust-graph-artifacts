# trust-graph-artifacts

## Converting Governance from Narrative to Infrastructure

Most governance in digital systems is still expressed as narrative:

- policies describe intent
- documentation describes constraints
- audits describe outcomes

But at execution time, authority is exercised by systems that:

- validate inputs
- apply rules
- permit or deny actions
- propagate effects across boundaries

If governance claims cannot be implemented, tested, revoked, and contested at this layer, they are not infrastructure.

This repository exists to close that gap.

---

## What this repository does

This repository converts high-signal concepts from The Trust Graph into:

- schemas
- control models
- artifact definitions
- example payloads
- validation structures

Each artifact represents a governance claim that has been:

1. observed in narrative form
2. validated through audience signal
3. formalized into a machine-legible structure
4. prepared for testing and implementation

---

## What qualifies as an artifact

Artifacts are not created for every essay.

An essay must demonstrate:

- strong engagement signal (concept selection by audience)
- structural clarity (can be modeled)
- enforceability (can affect runtime behavior)
- lifecycle semantics (can be revoked or superseded)

See:

- `evaluation/`
- `SIGNAL_MODEL.md`

---

## Repository structure

```text
.
├── artifacts/
├── essays/
├── evaluation/
├── shared/
├── validation/
└── docs/
```

- `artifacts/` → executable governance constructs
- `essays/` → source narrative context
- `evaluation/` → selection and scoring of candidates
- `shared/` → vocabularies and reusable components
- `validation/` → conformance and test logic
- `docs/` → system design and lifecycle

---

## Artifact lifecycle

```text
Idea → Essay → Evaluated → Draft → Experimental → Stable → Deprecated
```

Artifacts evolve. They are not static.

Each artifact must declare:

- status
- lineage
- validation state

---

## Governance model

### Authority

Artifact creation and approval are controlled by repository maintainers.

### Delegation

Contributors may:

- propose artifacts
- refine schemas
- add examples and tests
- challenge semantics

### Enforcement

All artifacts must:

- include a manifest
- follow structural conventions
- pass validation checks when defined

### Revocation

Artifacts may be:

- deprecated
- superseded
- archived

### Redress

Disputes are handled through:

- issues
- structured discussion
- revision and versioning

---

## What this repository is not

- Not a content archive
- Not a speculative idea store
- Not a documentation-only system

This is an execution layer, not a publication layer.

---

## How to get started

1. Read `ARTIFACT_INDEX.md`
2. Explore an artifact folder
3. Review schema and examples
4. Examine validation logic

---

## Strategic position

This repository treats governance as:

> a system of enforceable constraints, not descriptive intent

It is designed to make:

- authority explicit
- delegation inspectable
- enforcement testable
- revocation possible
- redress structured

---

## Next steps

- expand artifact depth with richer examples and challenge flows
- extend TSMM projection coverage beyond the current 15-artifact set
- emit native TSMM graph JSON instances where useful
- verify and harden provisional source metadata

---


## TSMM binding layer

The repository now includes a concrete TSMM binding layer for all 15 governed artifacts. This makes the artifact layer structurally legible in terms of:

- entities and roles
- bounded authority
- relationships and delegation
- controls, threats, and evidence
- trust decisions and downstream effects
- lifecycle and revocation semantics

See:

- `bindings/tsmm/README.md`
- `bindings/tsmm/projections/`
- `entities/registry.yaml`
- `controls/registry.yaml`
- `docs/tsmm-binding-layer.md`

## Current artifact set

The repository now includes the initial Tier A set and a next-wave expansion derived from the current dataset.

### Foundational set

- `first-person-credentials`
- `consent-not-data-structure`
- `layers-of-the-self`

### Expansion set

- `after-consent`
- `delegation-after-identity`
- `your-agents-are-not-failing-your`
- `wallet-to-agent-identity`
- `digital-credential-verification-policy-playbook`
- `systemic-controllers`
- `trust-registry-governance-model`
- `machine-readable-privacy-terms`
- `portable-eligibility`
- `the-proof-gap`
- `execution-time-delegation`
- `crisis-of-narrative-control`

These are first-cut formalizations and should be treated as draft operational models rather than finished specifications.
