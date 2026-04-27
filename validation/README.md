# Validation

Validation keeps the repository honest as an executable governance corpus. It distinguishes what is machine-enforced today from what remains a planned control requirement.

## What validation currently checks

- `package.json` matches the native package schema
- `graph.json` matches the TSMM graph schema
- `examples/valid-graph.json` passes schema validation
- `examples/invalid-graph.json` fails schema validation
- `patterns/authority-legitimacy-validation` includes revocation and contestability signals
- `overlays/intermediary-governance-overlay` includes provenance/traceability signals
- `profiles/coalition-legitimacy-model` includes capture-risk and appealability signals
- every active package directory is represented in `provenance/essay-source-map.yaml`
- canonical artifact YAML files validate against their domain schemas
- `crosswalks/essay_to_artifact.yaml` references resolve to existing package or artifact paths

## Declared but not yet machine-evaluated

Some checks in `validation/test-matrix.yaml` are marked `planned`. They are requirements backlog, not present validator coverage.

The `evidenceChecks` arrays in package test vectors are also declared but not yet machine-evaluated. They document evidence expectations for maintainers and future validator extensions. They should not be read as executable test results until a matching validator check is added and marked `implemented` in the matrix.

## Run locally

```bash
python3 scripts/validate_tsmm_native.py
```

## CI behavior

GitHub Actions runs the same validator on pushes to `main` and on pull requests.
