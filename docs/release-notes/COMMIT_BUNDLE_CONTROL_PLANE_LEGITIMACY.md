# Commit bundle: control-plane legitimacy artifact set

## Commit title

feat: add control-plane legitimacy artifact set and TSMM-native package cluster

## Commit message

- add six new artifact manifests, schemas, examples, mappings, and tests:
  - control-plane-shift-detection
  - legitimacy-gap-evaluator
  - intermediary-governance-overlay
  - knowledge-substrate-integrity-profile
  - governed-license-authority
  - coalition-legitimacy-model
- add six aligned TSMM-native packages across patterns, overlays, and profiles
- update essay and provenance catalogs for the three newly evaluated essays
- add control-plane legitimacy design note to docs
- extend control catalog with legitimacy, intermediary, licensing, and coalition controls
- extend validation matrix with legitimacy-gap, intermediary-traceability, and coalition-capture-risk checks

This commit operationalizes three Trust Graph essays into machine-readable governance packages focused on authority relocation, legitimacy gaps, intermediary governance, governed licensing, and coalition capture resistance.

## Included paths

- `artifacts/control-plane-shift-detection/`
- `artifacts/legitimacy-gap-evaluator/`
- `artifacts/intermediary-governance-overlay/`
- `artifacts/knowledge-substrate-integrity-profile/`
- `artifacts/governed-license-authority/`
- `artifacts/coalition-legitimacy-model/`
- `patterns/control-plane-shift-detection/`
- `patterns/legitimacy-gap-evaluator/`
- `overlays/intermediary-governance-overlay/`
- `profiles/knowledge-substrate-integrity-profile/`
- `profiles/governed-license-authority/`
- `profiles/coalition-legitimacy-model/`
- `docs/control-plane-legitimacy.md`
- `essays/source-catalog.yaml`
- `provenance/essay-source-map.yaml`
- `validation/test-matrix.yaml`
- `registries/control-catalog.json`
- `README.md`
- `docs/index.md`
- `essays/index.md`

## Validation notes

- `python3 scripts/validate_tsmm_native.py` passes for all TSMM-native packages.
- Each new artifact includes valid and invalid examples plus package-local tests.
- The new packages preserve the existing repository package contract:
  - `package.json`
  - `graph.json`
  - `constraints.json`
  - `evidence.json`
  - valid and invalid graph examples
  - test vector
