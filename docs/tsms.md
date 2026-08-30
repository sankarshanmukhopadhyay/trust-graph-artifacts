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

## First evidence-backed stack release

TGA `v0.12.1` participates in **`tsms-stack-2026.1 — Cashew-Nut`** through the accepted immutable TSMS baseline:

- TSMM `v0.24.0` — commit `2867010121e8a61971184d8fe7d3306b985e5884`
- TIS `v0.14.1` — commit `d25539932181e6d883f5bec261daaf011f740059`
- TGA `v0.12.1` — commit `f0bdc309a691a7be8dca3b48fed8ac1555219bec`

The stack release coordinates evidence through TSMM. It does not transfer TGA's authority over executable governance compositions.

Complete-stack adopters should start with the TSMS adopter guide:

https://sankarshanmukhopadhyay.github.io/trust-systems-meta-model/tsms-adopter-guide.html

## What “stack-qualified” means

A TGA artifact may claim `stackQualified: true` only when it:

1. declares the exact TSMM semantic authority version and concept identifiers it uses;
2. declares the exact TIS contract authority version and portable contract paths it uses;
3. declares its TGA version;
4. survives both positive and negative conformance cases;
5. does not imply external certification or compatibility with unreviewed future versions.

Cross-repository TSMS compatibility is additionally governed by the accepted baseline and drift evidence. A green local TGA validation does not override `REVIEW_REQUIRED`, `UNSUPPORTED`, or `INDETERMINATE` at stack level.

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

A passing result is repository conformance evidence. It is not external certification, does not establish that remote repositories are unchanged, and does not transfer TSMM semantic or TIS portable-contract authority into TGA.
