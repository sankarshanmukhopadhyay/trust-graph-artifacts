# Trust Graph Artifacts

> **Flagship repository**  
> **Role:** `executable-governance-and-implementation-layer`  
> **Current version:** `0.12.1`  
> **Canonical validation:** `make validate`  
> **Semantic authority:** `trust-systems-meta-model@v0.24.0`  
> **Portable contract authority:** `trust-infrastructure-schemas@v0.14.1`

**Trust Graph Artifacts (TGA) converts high-signal governance arguments from The Trust Graph into machine-readable, testable trust-system artifacts without taking semantic authority away from TSMM or portable-schema authority away from TIS.**

## Authority model

The repository operates as an executable-governance incubation and implementation layer:

- **The Trust Graph** provides source arguments, failure modes, and design pressure.
- **TSMM v0.24.0** is the canonical semantic authority for subjects, agents, authority, policy, evidence, assessment, trust decisions, effects, delegation, lifecycle, and related trust-system concepts.
- **TIS v0.14.1** is the portable artifact-contract authority for authority boundaries, evidence bundles, evaluation envelopes, decision receipts, registry records, and other interoperable assurance artifacts.
- **TGA** owns project-local governance patterns, system compositions, mappings, examples, provenance, and negative-assurance tests.

TGA artifacts are therefore implementation and assurance inputs. They are not independent certification, canonical semantic definitions, or substitutes for the authority of external protocols, institutions, or legal regimes.

## TGA in the Trust Systems Modelling Stack (TSMS)

TGA is the **executable governance and implementation layer** of TSMS. The first stack-qualified golden path binds explicit TSMM concept identifiers to existing TIS portable contracts and produces machine-readable local conformance evidence.

- [TSMS executable golden-path guide](docs/tsms.md)
- Golden-path artifact: `examples/tsms/golden-path.json`
- Validation: `python3 scripts/validate_tsms_golden_path.py`
- Evidence: `artifacts/validation/tsms-golden-path.json`
- Governing workstream: [#16](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts/issues/16)


## Current release posture

The v0.6.0–v0.11.0 release train added six current artifact families:

| Release | Artifact | Governance surface |
|---|---|---|
| v0.6.0 | `provenance-backed-reputation` | provenance-bearing and context-bounded reliance on reputation signals |
| v0.7.0 | `context-bound-identifier-use` | purpose limitation and authority for cross-context correlation |
| v0.8.0 | `verifiable-trade-corridor` | cross-border trust composition using authority, provenance, status and receipts |
| v0.9.0 | `agent-capability-accreditation` | task-class, configuration-bound and revocable agent market participation |
| v0.10.0 | `issuer-incentive-inversion` | issuer-level correction, revocation, redress and institutional legibility |
| v0.11.0 | `autonomy-native-institution` | mandate, runtime authority, delegation, accreditation, contestability and redress composition |

v0.12.0 consolidated repository assurance and repaired validation/build drift. v0.12.1 aligns the public documentation, source catalog, provenance and crosswalk surfaces with that executable baseline.

## Start here

1. [`docs/index.md`](docs/index.md) — documentation map and active release surfaces.
2. [`docs/architecture.md`](docs/architecture.md) — repository and authority boundaries.
3. [`docs/adoption.md`](docs/adoption.md) — adoption guidance.
4. [`essays/index.md`](essays/index.md) — current source-to-artifact entry points.
5. [`essays/current-release-catalog.yaml`](essays/current-release-catalog.yaml) — current machine-readable source catalog.
6. [`provenance/current-release-map.yaml`](provenance/current-release-map.yaml) — source interpretation and assurance provenance.
7. [`crosswalks/current-release-essay-to-artifact.yaml`](crosswalks/current-release-essay-to-artifact.yaml) — essay → TGA artifact → TSMM semantics → TIS contracts.

## Repository structure

```text
profiles/      reusable TSMM-native trust-system profiles
patterns/      recurring governance and control structures
overlays/      cross-cutting governance constraints
systems/       worked trust-system compositions
evidence/      evidence and decision-receipt models
artifacts/     executable-governance artifact declarations and assurance cases
essays/        source catalogs and essay mappings
provenance/    source-to-artifact provenance records
crosswalks/    essay, risk, control and interoperability mappings
bindings/      explicit TGA → TIS runtime-assurance bindings
schemas/       project-local schemas and receipt contracts
scripts/       canonical validation and maintenance scripts
validation/    validation matrices and test cases
docs/          publication and implementation guidance
```

## Assurance model

Run the canonical gate with:

```bash
make validate
```

The gate exercises package validation, authority envelopes, delegation lineage, receipts, TIS alignment, artifact assurance cases, documentation integrity, repository governance, portfolio relationships, and current-release publication/provenance surfaces.

CI writes a machine-readable result to:

```text
artifacts/validation/latest.json
```

A failed gate is evidence too: the record identifies passed, failed and skipped checks and the GitHub commit evaluated. GitHub Pages publication is gated on the same repository-wide validation contract.

## Current artifact assurance cases

The release train includes executable admit/reject cases for:

- provenance completeness and contextual reputation use;
- identifier purpose expansion and unauthorized correlation;
- issuer authority, status freshness and primary-evidence reconstruction in trade;
- agent capability/configuration mismatch and revoked accreditation;
- issuer-level lifecycle opacity and voluntary-pilot generalization;
- orphan agent actions, stale runtime authority, absent contestability/redress and broken receipt chains.

These cases are repository assurance evidence, not external certification.

## Contribution discipline

A contribution should not paste an essay into a schema. It should:

1. identify a governable failure mode, authority boundary, evidence requirement, control surface, or system composition;
2. reuse TSMM semantics wherever possible;
3. project portable artifacts through TIS rather than creating project-local alternatives;
4. declare provenance and authority explicitly;
5. add positive and negative assurance cases;
6. pass `make validate` before merge.

See [`CONTRIBUTING.md`](CONTRIBUTING.md), [`GOVERNANCE.md`](GOVERNANCE.md), and [`docs/authoring-model.md`](docs/authoring-model.md).

## Historical material

Earlier release documentation and transition material remain available in `docs/release-notes/` and `archive/`. Historical version references should be read as release-specific context, not as the current repository compatibility baseline.

## In one sentence

**The Trust Graph supplies design pressure, TSMM supplies canonical trust-system semantics, TIS supplies portable contracts, and TGA turns the relationship into executable governance and assurance evidence.**
