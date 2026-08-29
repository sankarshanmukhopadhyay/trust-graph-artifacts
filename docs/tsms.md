---
title: TSMS executable golden path
---
# TGA in the Trust Systems Modelling Stack (TSMS)

TGA is the **executable governance and implementation layer** of TSMS.

The first stack-qualified golden path is `examples/tsms/golden-path.json`. It makes the dependency chain inspectable:

```text
TSMM canonical concepts
  authority · delegation · scope · evidence · decision · effect
        ↓
TIS portable contracts
  authority boundary · evidence bundle · decision receipt
        ↓
TGA executable artifact
  delegated-authority decision
        ↓
make validate
        ↓
artifacts/validation/tsms-golden-path.json
```

## What “stack-qualified” means

A TGA artifact may claim `stackQualified: true` only when it:

1. declares the exact TSMM semantic authority version and concept identifiers it uses;
2. declares the exact TIS contract authority version and portable contract paths it uses;
3. declares its TGA version;
4. survives both positive and negative conformance cases;
5. does not imply external certification or compatibility with unreviewed future versions.

## Run it

```bash
python3 scripts/validate_tsms_golden_path.py
```

or run the complete repository gate:

```bash
make validate
```

## Falsification cases

The validator includes three boundary cases:

- a nonexistent TSMM concept → `reject`;
- a nonexistent TIS contract → `reject`;
- an unknown TSMM version → `unsupported`.

This is intentionally stronger than “the JSON parses.” It tests the claim that the artifact is bound to known semantic and portable-contract authorities.

## Non-claims

A passing result is repository conformance evidence. It is not external certification and it does not establish that remote repositories have not changed since the reviewed baseline.
