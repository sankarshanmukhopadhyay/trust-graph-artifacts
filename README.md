# trust-graph-tsmm-native

## TSMM-native trust system profiles and patterns derived from The Trust Graph

This repository operationalizes concepts from **The Trust Graph** as **TSMM-native** packages.

The governing idea is simple:

- **TSMM** supplies the meta-model and system grammar
- **The essays** supply the problem framing, conceptual pressure, and package selection logic
- **This repository** turns those essay-derived concepts into native TSMM profiles, patterns, overlays, systems, and evidence models

That means this repository no longer treats TSMM as a secondary binding layer. TSMM is the only structural grammar used to design and validate the corpus.

## Why this repo exists

The essays argue that governance becomes real only when it is executable at the layer where systems actually decide, constrain, permit, deny, propagate, and record effects. A narrative claim is not yet infrastructure. It becomes infrastructure when it can be represented as policy, authority, evidence, decision, effect, and lifecycle semantics.

This repository exists to make that conversion explicit.

## What is in the repository

```text
.
├── profiles/     # TSMM-native profiles
├── patterns/     # TSMM-native patterns
├── overlays/     # TSMM-native overlays
├── systems/      # TSMM-native system models
├── evidence/     # TSMM-native evidence models
├── essays/       # source essay catalog and provenance
├── mappings/     # essay-to-package crosswalks
├── registries/   # shared machine-readable registries
├── schemas/      # vendored schemas used for validation
├── scripts/      # validation and index scripts
├── validation/   # validation matrix and notes
└── docs/         # methodology, taxonomy, and governance docs
```

## Package taxonomy

Every package in this repository is one of:

- **profile** — a bounded, reusable trust-system profile
- **pattern** — a recurring trust-system structure or control arrangement
- **overlay** — a policy or governance layer applied across other structures
- **system** — a worked trust-system model with named actors and effects
- **evidence-model** — an explicit model of proof, receipt, and verification expectations

## Current corpus

### Profiles
- `profiles/first-person-credentials`
- `profiles/layers-of-the-self`
- `profiles/digital-credential-verification-policy-playbook`
- `profiles/portable-eligibility`
- `profiles/trust-registry-governance-model`

### Patterns
- `patterns/delegation-after-identity`
- `patterns/your-agents-are-not-failing-your`
- `patterns/systemic-controllers`

### Overlays
- `overlays/consent-not-data-structure`
- `overlays/after-consent`
- `overlays/machine-readable-privacy-terms`
- `overlays/crisis-of-narrative-control`

### Systems
- `systems/wallet-to-agent-identity`

### Evidence models
- `evidence/the-proof-gap`
- `evidence/execution-time-delegation`

## Authoring stance

The essay is not the artifact.

The essay is the **source narrative** that qualifies a concept for formalization. The package is the **TSMM-native implementation surface**.

That distinction matters because it keeps editorial argument and machine-verifiable structure separate while preserving explicit provenance between them.

## Validation

Validation is native, not translational.

The repository validates:

- `package.json` against `schemas/tsmm-native-package.schema.json`
- `graph.json` against `schemas/tsmm-graph.schema.json`
- valid examples must pass
- invalid examples must fail

Run:

```bash
python3 scripts/validate_tsmm_native.py
```

## Start here

- `docs/methodology.md`
- `docs/essay-to-tsmm-method.md`
- `docs/profile-taxonomy.md`
- `docs/authoring-model.md`
- `mappings/essay-to-tsmm.yaml`
- `essays/source-catalog.yaml`

## Strategic position

This repository is a **standalone TSMM-native pattern and profile library**.

It is not a fork of TSMM and not a secondary binding repository. It is a distinct implementation corpus that uses TSMM as its only design grammar while remaining explicitly sourced from The Trust Graph essays.
