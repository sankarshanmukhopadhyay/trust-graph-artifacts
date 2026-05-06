# Changelog

All notable repository changes are documented here. The repository treats changelog entries as part of the governance evidence surface: they explain what changed, why it changed, and which validation surface was affected.

## [Unreleased]

## [0.2.0] - 2026-05-06

### Added

- Added formal TGA ↔ TSMM v0.20 binding metadata under `bindings/tsmm/`.
- Added TSMM alignment, decision receipt profile, layering, outcome vocabulary, assurance posture, and TGA → TSMM → TIS composition documentation.
- Added `registries/outcome-vocabulary.yaml` and `registries/assurance-vocabulary.yaml`.
- Added TSMM-profiled decision receipt schema and example.
- Added a TSMM/TIS-aligned TGA decision composition example.

### Changed

- Updated repository version to `0.2.0`.
- Updated active registry and artifact schema version markers.
- Updated decision receipt schema `$id` to a release-pinned repository URL.
- Refreshed receipt and decision-provenance documentation metadata for v0.2.0.

### Fixed

- Removed local `.DS_Store` artifacts.
- Added `.gitignore` coverage for operating-system files and build outputs.


### Added

- Expanded `scripts/validate_tsmm_native.py` to validate provenance coverage, selected semantic gates, canonical artifact YAML files, and essay-to-artifact crosswalk references.
- Added explicit `status` fields to `validation/test-matrix.yaml` so implemented checks and planned controls are no longer conflated.
- Added domain-distinguishing artifact schema constraints for authority, control-plane, delegation, legitimacy, licensing, and verification artifacts.

### Changed

- Consolidated README onboarding into a current-state description instead of announcement-style update sections.
- Reconciled `docs/quickstart.md` with README onboarding by separating the authority modeling tour from the cross-type structural tour.
- Replaced placeholder JSON Schema `$id` values with GitHub raw schema URIs.
- Renamed `patterns/your-agents-are-not-failing-your` to `patterns/agent-mandate-envelope` for navigational clarity while preserving the original essay URL.
- Moved root commit-bundle scaffolds into `docs/release-notes/`.

### Fixed

- Synchronized temporal governance packages into `provenance/essay-source-map.yaml`.
- Documented that `evidenceChecks` are declared evidence expectations, not yet machine-evaluated checks.

## [0.1.0]

### Added

- Initial TSMM-native package corpus derived from The Trust Graph essays.
- Receipt schema and example layer for authority, delegation, decision, enforcement, licensing, revocation, execution authority state, revocation propagation, and gradient exploitation signals.
- Temporal governance and revocation dynamics package cluster.
