---
title: Jekyll publication
layout: default
parent: Governance and release
nav_order: 3
---

# Jekyll publication

This repository can be published as a Just the Docs site using GitHub Pages and GitHub Actions.

## Publication model

The repository root is the Jekyll source. The `docs/` directory is the primary documentation surface. Source artifacts, schemas, examples, registries, validation inputs, and evidence packages remain in their existing repository paths so that the site does not collapse the executable corpus into prose-only documentation.

## Build files

| File | Purpose |
| --- | --- |
| `_config.yml` | Defines the Just the Docs theme, navigation behavior, search, callouts, footer content, and site defaults. |
| `Gemfile` | Pins the local Jekyll, Just the Docs, remote theme, and SEO dependencies used by maintainers and CI. |
| `.github/workflows/pages.yml` | Builds the site through GitHub Actions and deploys the `_site` artifact to GitHub Pages. |
| `index.md` | Provides the site homepage and routes readers into the documentation corpus. |

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

For GitHub Pages, set **Settings → Pages → Build and deployment → Source** to **GitHub Actions**.

## Navigation discipline

Documentation pages intended for publication must include Jekyll front matter with at least:

```yaml
---
title: Page title
layout: default
nav_order: 10
---
```

Child pages should also declare a `parent` value that matches one of the parent navigation pages. Pages that are not intended for sidebar navigation may set `nav_exclude: true`.

## Assurance expectations

Publication readiness is not just cosmetic. A documentation page is considered ready when it preserves the executable governance chain:

1. **Authority:** states which actor, policy, package, or registry controls the relevant decision surface.
2. **Scope:** identifies the package, profile, overlay, receipt, or validation target affected.
3. **Evidence:** links to machine-readable schemas, examples, or validation inputs where applicable.
4. **Revocation/change control:** states how drift, stale references, or invalid examples should be detected.
