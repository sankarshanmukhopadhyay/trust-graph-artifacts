# Trust Graph Artifacts

**A TSMM-native corpus for turning essay-derived governance failures into reusable, testable trust-system packages.**

This repository sits at the line between two layers that are often blurred together:

- **Trust Systems Meta Model (TSMM)** supplies the structural grammar for modeling trust systems.
- **The Trust Graph** supplies the problem corpus, conceptual pressure, and governance stance.

The repository does not treat essays as executable truth. It treats them as a source of questions, failure modes, and design pressure. It also does not treat TSMM as a loose reference. TSMM is the modeling discipline for every active package.

The result is a developer-facing library that moves from governance claims to concrete system shapes, machine-readable constraints, valid/invalid examples, and evidence-bearing decisions.

## TSMM v0.20 alignment

Version `0.3.0` preserves the TSMM v0.20 boundary and adds authority envelopes, machine commitments, fraud externalities, inference-to-verification controls, and high-risk infrastructure governance:

- **TSMM v0.20.0** is the semantic authority for trust-system modeling.
- **Trust Infrastructure Schemas v0.8.0** is the executable artifact contract layer where cross-repo validation, registry publication, or assurance-level semantics are required.
- **TGA** is the Trust Graph interpretation corpus: it turns essay-derived governance pressure into TSMM-native packages, receipts, examples, and provenance overlays.
- **v0.3.0** adds runtime authority envelopes, proof-carrying machine commitments, fraud externality verification, inference substitution detection, legibility trap detection, high-risk infrastructure assurance, and constitutional infrastructure controls.

Start with [`docs/tsmm-v0.20-alignment.md`](docs/tsmm-v0.20-alignment.md) and [`docs/bindings/tsmm-binding.md`](docs/bindings/tsmm-binding.md) for the current alignment contract.

## What is in this repository now

The active repository surface has three coherent layers:

1. **TSMM-native package corpus** — profiles, patterns, overlays, systems, and evidence models under `profiles/`, `patterns/`, `overlays/`, `systems/`, and `evidence/`.
2. **Executable governance artifact and receipt layer** — canonical artifact YAML, receipt schemas, and examples under `artifacts/`, `schemas/receipts/`, and `examples/receipts/`.
3. **Temporal governance layer** — revocation propagation, persistence traps, execution-time authority state, and gradient exploitation surfaces modeled as first-class validation targets.

Together these layers make authority, delegation, enforcement, revocation, evidence, and auditability visible as repository structure rather than narrative intent.

## Start here

Read these in order:

1. [`docs/quickstart.md`](docs/quickstart.md)
2. [`docs/architecture.md`](docs/architecture.md)
3. [`docs/tsmm-and-the-trust-graph.md`](docs/tsmm-and-the-trust-graph.md)
4. [`docs/package-anatomy.md`](docs/package-anatomy.md)
5. [`docs/authoring-model.md`](docs/authoring-model.md)

Then run the validator:

```bash
python3 scripts/validate_tsmm_native.py
```

## Recommended package tours

### Authority modeling tour

Start here when you want the cleanest view of executable authority, legitimate control, and decision evidence:

- `patterns/authority-legitimacy-validation`
- `overlays/legitimate-control-enforcement`
- `evidence/legitimate-control-decision-receipt`

### Cross-type structural tour

Start here when you want one package from each major package class:

- `profiles/first-person-credentials`
- `patterns/delegation-after-identity`
- `overlays/consent-not-data-structure`
- `systems/wallet-to-agent-identity`
- `evidence/the-proof-gap`

### Control-plane legitimacy tour

Use this cluster to study how commons governance, AI intermediaries, and licensing coalitions become TSMM-native model surfaces:

- `patterns/control-plane-shift-detection`
- `patterns/legitimacy-gap-evaluator`
- `overlays/intermediary-governance-overlay`
- `profiles/knowledge-substrate-integrity-profile`
- `profiles/governed-license-authority`
- `profiles/coalition-legitimacy-model`


### Authority envelopes, commitments, and high-risk infrastructure tour

Use this cluster to study the v0.3.0 governance increment:

- `patterns/runtime-authority-envelope`
- `profiles/machine-commitment-governance-profile`
- `evidence/proof-carrying-commitment-receipt`
- `overlays/commitment-lifecycle-mediation`
- `profiles/fraud-externality-verification-profile`
- `patterns/inference-substitution-gap`
- `patterns/legibility-trap-detector`
- `profiles/high-risk-digital-infrastructure-governance-profile`
- `overlays/constitutional-digital-infrastructure-controls`
- `evidence/high-risk-governance-assurance-record`

### Temporal governance tour

Use this cluster to study revocation dynamics and authority state at execution time:

- `patterns/persistence-trap-detector`
- `patterns/revocation-lag-analyzer`
- `patterns/gradient-exploitation-surface`
- `profiles/compositional-revocation-profile`
- `overlays/execution-bound-revocation`

## Repository structure

```text
.
├── profiles/      # Reusable TSMM-native trust-system profiles
├── patterns/      # Recurring governance and control structures
├── overlays/      # Cross-cutting policy and governance constraints
├── systems/       # Worked system compositions with named actors and effects
├── evidence/      # Evidence and decision-receipt models
├── artifacts/     # Canonical executable-governance artifact declarations
├── essays/        # Source essay catalog
├── provenance/    # Package-to-essay provenance records
├── registries/    # Shared entity, control, evidence, decision, and lifecycle vocabularies
├── schemas/       # JSON Schemas for packages, graphs, artifacts, and receipts
├── scripts/       # Validation and repository maintenance scripts
├── validation/    # Validation matrix and execution notes
└── docs/          # Developer and architecture documentation
```

Older artifact-first and binding-transition material is retained under [`archive/legacy-artifact-model/`](archive/legacy-artifact-model/) for reference only. The active corpus is TSMM-native.

## Package taxonomy

Every active package is one of five types:

- **profile** — a bounded trust-system configuration meant for reuse
- **pattern** — a recurring control or governance arrangement
- **overlay** — a cross-cutting policy layer applied to other structures
- **system** — a composed trust-system model with concrete actors and effects
- **evidence-model** — a model of what the system must produce to justify actions and decisions

## Validation model

The validator now checks the active package corpus and the executable artifact layer:

- package metadata conforms to `schemas/tsmm-native-package.schema.json`
- graph surfaces and valid examples conform to `schemas/tsmm-graph.schema.json`
- invalid examples fail as negative conformance tests
- selected semantic gates from `validation/test-matrix.yaml` are enforced
- every active package has provenance coverage
- canonical artifact YAML validates against domain artifact schemas
- essay-to-artifact crosswalk references resolve locally

The validation matrix distinguishes `implemented` checks from `planned` checks. This prevents planned governance controls from being mistaken for exercised test coverage.

## How to read a package

Read package files in this order:

1. `README.md`
2. `package.json`
3. `graph.json`
4. `constraints.json`
5. `evidence.json`
6. `tests/test-vector.json`

Every package README separates the essay contribution, the TSMM contribution, and the implementation contribution. That separation is the adoption path: it keeps the source argument, the model grammar, and the developer-facing artifact distinct.

## Design stance

This repository assumes that governance only becomes credible when it is visible in system structure. Packages therefore favor explicit decision points, bounded scope, evidence outputs, lifecycle semantics, contestability, and revocation-aware execution over ambient authority or narrative assurance.

## Contribution model

A good contribution does not paste an essay into a schema. It identifies the trust problem, classifies it into the right package type, models it using the existing TSMM-native grammar, adds examples and validation cases, and explains what a developer or architect should learn from it.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/authoring-model.md`](docs/authoring-model.md).

## In one sentence

**TSMM provides the modeling discipline. The Trust Graph provides the reason to model these problems at all. This repository turns that relationship into reusable, testable packages.**
