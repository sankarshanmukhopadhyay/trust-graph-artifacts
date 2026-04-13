# Developer guide

## Local setup

Requirements:

- Python 3.11+
- `jsonschema`

Install:

```bash
pip install jsonschema
```

## Validate changes

```bash
python3 scripts/validate_tsmm_native.py
```

## Recommended workflow for adding or revising a package

1. Update the package README first so intent is clear
2. Update `package.json` classification and metadata
3. Update `graph.json`
4. Update `constraints.json` and `evidence.json`
5. Refresh examples
6. Confirm the invalid example still fails for the right reason
7. Run validation

## Design review questions

Before merging, ask:

- Is the package type correct?
- Is the trust problem clearly bounded?
- Are decision points explicit?
- Are control surfaces visible?
- Does evidence describe what the system must emit, not just what we hope to log?
- Does the README explain the line between essay pressure and TSMM structure?
