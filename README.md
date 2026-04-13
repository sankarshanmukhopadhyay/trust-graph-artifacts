# Trust Graph TSMM Patterns

**A TSMM-native pattern and profile library derived from The Trust Graph.**

This repository sits at the line between two things that are often blurred together:

- **Trust Systems Meta Model (TSMM)** provides the structural grammar for modeling trust systems
- **The Trust Graph** provides the conceptual pressure, problem selection, and architectural stance

This repository exists to make that line explicit and useful.

It does **not** treat essays as executable truth. It treats them as a source of questions and design pressure.
It does **not** treat TSMM as a loose reference. It treats TSMM as the only modeling language allowed in the repository.

The result is a corpus of **TSMM-native packages** that help developers and software architects move from:

- interesting governance claims
- to concrete system shapes
- to testable structures
- to evidence-bearing decisions

## The core distinction

### What TSMM does

TSMM is the **meta model**.
It gives this repository a shared vocabulary for expressing:

- entities and roles
- authority and delegation
- controls and constraints
- decisions and effects
- evidence and auditability
- lifecycle and revocation

TSMM answers the question:

> **What is the structure of a trust system?**

### What The Trust Graph does

The Trust Graph is the **concept source**.
It frames the operational problems that matter:

- why identity without authority is insufficient
- why revocation that does not propagate is governance theater
- why logs are not the same as decision evidence
- why contestability must exist at execution time, not only in policy language

The essays answer the question:

> **Which trust problems are worth modeling, and why do they fail in practice?**

### What this repository does

This repository is the implementation layer between the two.

It answers the question:

> **How do we express an essay-derived trust problem as a TSMM-native, developer-usable package?**

That is the repository’s real intent.

## Who this repository is for

### For developers

Use this repository when you need examples of how governance-heavy concepts can be represented as machine-readable trust-system components.

A package gives you:

- a `graph.json` describing the TSMM-native structure
- a `constraints.json` describing operational controls and failure boundaries
- an `evidence.json` describing the proof surfaces the system must emit
- valid and invalid examples
- a test vector the validator can exercise

### For software architects

Use this repository to study how architectural choices become governance choices.

The packages are intentionally opinionated. They foreground:

- bounded authority
- constrained delegation
- verification and admissibility
- evidence-bearing trust decisions
- revocation and lifecycle semantics

The point is not just to model systems. The point is to model systems in a way that makes governance legible at execution time.

## Start here

If you are new to the repository, read these in order:

1. [`docs/quickstart.md`](docs/quickstart.md)
2. [`docs/architecture.md`](docs/architecture.md)
3. [`docs/tsmm-and-the-trust-graph.md`](docs/tsmm-and-the-trust-graph.md)
4. [`docs/package-anatomy.md`](docs/package-anatomy.md)
5. [`docs/methodology.md`](docs/methodology.md)
6. [`docs/authoring-model.md`](docs/authoring-model.md)

Then browse:

- [`profiles/`](profiles/)
- [`patterns/`](patterns/)
- [`overlays/`](overlays/)
- [`systems/`](systems/)
- [`evidence/`](evidence/)

The newest addition is a three-package set derived from *Enforceable Authority Without Legitimate Control*:

- `patterns/authority-legitimacy-validation`
- `overlays/legitimate-control-enforcement`
- `evidence/legitimate-control-decision-receipt`

## Repository structure

```text
.
├── profiles/      # Reusable TSMM-native trust system profiles
├── patterns/      # Recurring governance and control structures
├── overlays/      # Cross-cutting policy and governance constraints
├── systems/       # Worked system compositions with named actors and effects
├── evidence/      # Evidence and decision-receipt models
├── essays/        # Catalog of source essays from The Trust Graph
├── provenance/    # Essay-to-package provenance records
├── registries/    # Shared entity, control, evidence, decision, and lifecycle vocabularies
├── schemas/       # JSON Schemas for package and graph validation
├── scripts/       # Validation and repository maintenance scripts
├── validation/    # Validation matrix and execution notes
└── docs/          # Developer and architecture documentation
```

## Streamlining and archive policy

The active repository surface is the TSMM-native package corpus and its supporting docs, schemas, provenance, and validation layers.
Older material from the artifact-first and binding-transition phases is retained under [`archive/legacy-artifact-model/`](archive/legacy-artifact-model/) for reference only.

## Package taxonomy

Every package in this repository is one of the following:

- **profile** — a bounded trust-system configuration meant for reuse
- **pattern** — a recurring control or governance arrangement
- **overlay** — a cross-cutting policy layer applied to other structures
- **system** — a composed trust-system model with concrete actors and effects
- **evidence-model** — a model of what the system must produce to justify actions and decisions

The important point is that these are all **TSMM-native package types**.
They are not artifacts waiting to be translated.

## Validation model

Validation is intentionally simple and developer-friendly.

The repository checks that:

- `package.json` conforms to the native package schema
- `graph.json` conforms to the TSMM graph schema
- the valid example passes schema validation
- the invalid example fails schema validation
- references between package surfaces resolve locally

Run locally:

```bash
python3 scripts/validate_tsmm_native.py
```

See [`validation/README.md`](validation/README.md) for the execution model and what is currently in scope.

## How to read a package

Every package README now explains three different things separately:

1. **The essay contribution** — what conceptual pressure came from The Trust Graph
2. **The TSMM contribution** — how that pressure is expressed structurally
3. **The implementation contribution** — what a developer can reuse, inspect, validate, or extend

That separation is deliberate. It is the fastest way to understand what belongs to the essay, what belongs to TSMM, and what belongs to the package authoring layer.

## Design stance

This repository is opinionated.

It assumes that governance only becomes credible when it is visible in system structure.
That means packages in this repository favor:

- explicit decision points over implied behavior
- bounded scope over ambient authority
- evidence outputs over narrative assertions
- lifecycle semantics over static eligibility
- contestability and reviewability over silent automation

## Contribution model

Contributions should preserve the line between concept and model.

A good contribution does not paste an essay into a schema.
A good contribution does not invent new package structure when TSMM-native structure already exists.
A good contribution:

- identifies the trust problem clearly
- classifies it into the right package type
- models it using the existing TSMM-native grammar
- adds examples and validation cases
- explains what a developer or architect should learn from it

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/authoring-model.md`](docs/authoring-model.md).

## In one sentence

**TSMM provides the modeling discipline. The Trust Graph provides the reason to model these problems at all. This repository turns that relationship into reusable, testable packages.**
