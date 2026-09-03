# Security policy

## Supported versions

Security fixes are applied to the current release line. Historical releases and archived material are retained for provenance and are not maintained as supported runtime baselines.

## Reporting a vulnerability

Report unsafe governance patterns, validator bypasses, misleading assurance claims, authority-escalation defects, revocation failures, workflow privilege problems, integrity/provenance defects, or dependency vulnerabilities through a **private GitHub security advisory** where possible.

Please do not open a public issue when disclosure could expose users, credentials, integrity evidence, workflow privileges, or supply-chain controls before a fix is available.

Include:

- the affected package, workflow, artifact, or release;
- the security property you believe is violated;
- reproduction steps or a minimal proof of concept;
- expected versus observed behaviour;
- known impact, preconditions, and containment guidance.

If private reporting is unavailable, contact the repository maintainer through the contact information associated with the GitHub account and avoid publishing exploit details until a coordinated disclosure path is established.

## Authority boundary

This policy covers code, validation scripts, GitHub Actions, published artifacts, and provenance/integrity mechanisms owned by TGA. Vulnerabilities in TSMM, TIS, external protocols, institutions, or third-party services should be reported to their respective authorities unless the defect is specifically in TGA's integration or use of them.
