# Validation

Validation in this repository serves two goals:

- keep TSMM-native package surfaces structurally consistent
- give developers confidence that examples and tests reflect the package contract

## What validation currently checks

- `package.json` matches the native package schema
- `graph.json` matches the TSMM graph schema
- `examples/valid-graph.json` passes schema validation
- `examples/invalid-graph.json` fails schema validation

## What validation does not yet do

The current validator is intentionally lightweight. It does not yet perform deep semantic checks such as:

- registry reference completeness
- control-to-decision coverage
- lifecycle transition integrity
- evidence-field conformance to decision surfaces

Those would be strong future increments.

## Run locally

```bash
python3 scripts/validate_tsmm_native.py
```

## CI behavior

GitHub Actions runs the same validator on pushes to `main` and on pull requests.
