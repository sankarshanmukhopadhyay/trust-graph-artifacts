# Changelog

All notable repository changes are documented here. The repository treats changelog entries as part of the governance evidence surface: they explain what changed, why it changed, and which validation surface was affected.

## [Unreleased]

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
