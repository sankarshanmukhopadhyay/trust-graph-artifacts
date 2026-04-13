# Trust Graph TSMM Patterns

## TSMM-native trust system profiles, patterns, overlays, systems, and evidence models derived from The Trust Graph

This repository operationalizes concepts from **The Trust Graph** as **TSMM-native packages**.

The governing idea is simple:

- **TSMM** supplies the meta-model and system grammar
- **The essays** supply the problem framing, conceptual pressure, and package selection logic
- **This repository** turns those essay-derived concepts into native TSMM profiles, patterns, overlays, systems, and evidence models

There is no secondary structural model in this repository. TSMM is the only grammar used to design, describe, and validate the corpus.

## Why this repo exists

The essays argue that governance becomes real only when it is executable at the layer where systems decide, constrain, permit, deny, propagate, and record effects. A narrative claim is not yet infrastructure. It becomes infrastructure when it can be represented as policy, authority, evidence, decision, effect, and lifecycle semantics.

This repository exists to make that conversion explicit.

## Repository structure

```text
.
├── profiles/      # TSMM-native profiles
├── patterns/      # TSMM-native patterns
├── overlays/      # TSMM-native overlays
├── systems/       # TSMM-native system models
├── evidence/      # TSMM-native evidence models
├── essays/        # source essay catalog
├── provenance/    # essay-to-package provenance records
├── registries/    # shared machine-readable registries
├── schemas/       # validation schemas
├── scripts/       # validation and maintenance scripts
├── validation/    # validation matrix and notes
└── docs/          # methodology, taxonomy, and governance docs
```

## Package taxonomy

Every package in this repository is one of:

- **profile** — a bounded, reusable trust-system profile
- **pattern** — a recurring trust-system structure or control arrangement
- **overlay** — a policy or governance layer applied across other structures
- **system** — a worked trust-system model with named actors and effects
- **evidence-model** — an explicit model of proof, receipt, and verification expectations

## Validation

Validation is native.

The repository validates:

- `package.json` against `schemas/tsmm-native-package.schema.json`
- `graph.json` against `schemas/tsmm-graph.schema.json`
- valid examples must pass
- invalid examples must fail
- package references must resolve to local TSMM-native files

Run:

```bash
python3 scripts/validate_tsmm_native.py
```

## Start here

- `docs/methodology.md`
- `docs/essay-to-tsmm-method.md`
- `docs/profile-taxonomy.md`
- `docs/authoring-model.md`
- `provenance/essay-source-map.yaml`
- `essays/source-catalog.yaml`

## Strategic position

This repository is a **standalone TSMM-native pattern and profile library**.

It is not a fork of TSMM and not a translation repository. It is a distinct implementation corpus that uses TSMM as its only design grammar while remaining explicitly sourced from The Trust Graph essays.
