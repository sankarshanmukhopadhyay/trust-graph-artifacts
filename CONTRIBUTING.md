# Contributing

## Before you contribute

Read:

- `docs/methodology.md`
- `docs/essay-to-tsmm-method.md`
- `docs/profile-taxonomy.md`

## Pull request expectations

A package addition or change should include:

- updated `package.json`
- updated or new `graph.json`
- updated constraints or evidence model where applicable
- valid and invalid examples
- test-vector updates
- refreshed mappings or essay catalog entries if the package set changes

## Validation

Run:

```bash
python3 scripts/validate_tsmm_native.py
```
