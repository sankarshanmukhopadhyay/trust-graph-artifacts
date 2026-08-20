---
title: Release publication
layout: default
parent: Documentation
---

# Release publication

A TGA release is not complete merely because release code is merged. Publication has four distinct evidence states:

1. the release commit exists on `main`;
2. repository validation evidence exists for that release;
3. an immutable Git tag identifies the release commit;
4. a GitHub Release publishes the tag and canonical release notes.

The machine-readable state is maintained in [`governance/release-publication-ledger.yaml`]({% link governance/release-publication-ledger.yaml %}).

## Retrospective publication backlog

Versions v0.2.0 through v0.12.0 have release commits recorded in the ledger but their Git tag / GitHub Release publication status is currently `pending-publication`.

Retrospective publication must never tag the latest `main` commit for an old version. Each historical tag must point to the exact release commit recorded in the ledger.

## GitHub CLI procedure

For each historical release, verify the target first:

```bash
git show <merge-commit> --no-patch
```

Create and push the annotated tag:

```bash
git tag -a v<version> <merge-commit> -m "Trust Graph Artifacts v<version>"
git push origin v<version>
```

Then publish the GitHub Release from the canonical release note:

```bash
gh release create v<version> \
  --title "Trust Graph Artifacts v<version>" \
  --notes-file docs/release-notes/v<version>.md \
  --verify-tag
```

Do this in ascending version order. Do not use `--latest` for historical releases. Mark only the newest current release as Latest through GitHub after the historical backlog is complete.

## GitHub Web UI procedure

Where the CLI is unavailable:

1. create the tag against the exact commit SHA recorded in `governance/release-publication-ledger.yaml`;
2. open **Releases → Draft a new release**;
3. choose that exact tag;
4. use `Trust Graph Artifacts v<version>` as the release title;
5. copy the corresponding `docs/release-notes/v<version>.md` body, omitting YAML front matter;
6. keep historical releases unmarked as Latest;
7. publish in ascending version order.

## After publication

For each published release, update the ledger:

```yaml
tag_status: published
github_release_status: published
```

For the current release also replace any temporary `pending-pr-merge` or `pending-pr-validation` values with the actual merge commit and CI evidence reference.

The ledger update should go through normal PR validation so published-release evidence remains auditable.

## Integrity rule

Never move an existing published release tag to another commit. If release content is wrong, publish a new patch version and record the supersession. Release identity is evidence and must remain immutable.
