# Public repository baseline completion evidence

Tracking issue: #19

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| README purpose, maturity, authority and limits | PASS | `README.md` states flagship role, current version, canonical validation, TSMM/TIS authority boundaries, TGA ownership and non-certification limits. | None identified in this tranche. |
| Quick-start / reproducible validation | PASS | `README.md` identifies `make validate`, validation evidence output, golden-path guide and direct validation command. | Environment dependencies remain those declared by repository tooling. |
| LICENSE | PASS | Repository-local `LICENSE` present. | None identified. |
| CONTRIBUTING / CODE_OF_CONDUCT / SECURITY / SUPPORT / templates | PASS | Existing `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`; strengthened `SECURITY.md`; added `SUPPORT.md`, engineering issue template and PR template. | GitHub private vulnerability reporting availability remains a repository setting outside file content. |
| Security supported-version policy | PASS | `SECURITY.md` now identifies the current release line as supported and historical/archive material as unsupported runtime baselines. | No LTS branch is claimed. |
| Workflow least privilege | PASS | Validation workflow explicitly uses `contents: read`; Pages workflow already scopes `contents: read`, `pages: write`, `id-token: write` for deployment. | GitHub-owned actions still use maintained major tags. |
| Third-party action immutability | PASS | `ruby/setup-ruby` pinned to `95ef2b042f9d7a56d8268cba8559e2842e2ad01b` (observed `v1` head on 2026-09-03). | GitHub-owned actions remain major-tag references; update policy should continue to monitor them. |
| Privileged workflow / untrusted code boundary | PASS | Pages deploy runs only on `main` push/manual dispatch; pull requests run validation workflow without write privileges. | Manual dispatch retains normal repository maintainer authority. |
| Protected main | PASS | Active `protect-main` ruleset targets default branch; deletion/non-fast-forward prohibited; linear history and PR required; review threads resolved; `validate` required; no bypass actors; current user cannot bypass. | Zero approving reviews is intentional for the current single-maintainer repository. |
| Deterministic consequential CI | PASS | `make validate` is canonical in README and both validation/Pages workflows; validation evidence is uploaded as an artifact. | Full independence is not claimed. |
| Release/version/provenance | PASS | README current release posture plus `CHANGELOG.md`, `PROJECT-STATUS.yaml`, provenance and current-release catalog surfaces. | Release publication remains maintainer-controlled. |
| Docs/Pages alignment | PASS subject to CI | Pages publication executes the same `make validate` gate before Jekyll build/deploy. | Final PR CI is the completion gate for this tranche. |
| Authority and scope boundaries | PASS | README explicitly separates Trust Graph source pressure, TSMM semantic authority, TIS contract authority and TGA executable-governance ownership. | External authority remains external by design. |
| Experimental / historical distinction | PASS | README identifies historical material in `docs/release-notes/` and `archive/` and distinguishes it from the current compatibility baseline. | Individual historical files may retain release-specific terminology. |

## Completion gate

Merge only after the repository `validate` check is green on this PR. The merge does not claim external certification, independent security review, or authority beyond TGA's repository-local scope.
