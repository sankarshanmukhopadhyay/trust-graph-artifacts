# Commit bundle: Just the Docs / Jekyll publication readiness

## Commit title

Enable Just the Docs publication without release version change

## Commit message

Prepare the Trust Graph Artifacts repository for GitHub Pages publication using Jekyll and the Just the Docs theme without issuing a new release.

This commit adds the site configuration, local build dependency contract, Pages deployment workflow, homepage, navigation parent pages, and maintainer publication guidance required to display the documentation corpus as a structured Just the Docs site.

The change preserves the repository's executable governance model. It does not move or flatten schemas, packages, registries, evidence models, or validation assets. Instead, it creates a navigable publication layer over the existing repository structure while keeping machine-verifiable artifacts in their canonical paths.

## Proposed changes

- Add `_config.yml` for Just the Docs / Jekyll configuration.
- Add `Gemfile` for local and CI documentation builds.
- Add `.github/workflows/pages.yml` for GitHub Pages publication through Actions.
- Add `index.md` as the Jekyll homepage.
- Add `docs/jekyll-publication.md` with publication and navigation discipline.
- Add parent navigation pages for TSMM alignment, authoring, executable governance, authority/governance, temporal governance, governance/release, and release notes.
- Add/refresh front matter across documentation pages so the corpus can be rendered in the Just the Docs sidebar.
- Update `README.md` with documentation-site usage instructions.
- Update `CHANGELOG.md` with an unreleased publication-readiness entry.

## Validation notes

- Ran `python3 scripts/validate_tsmm_native.py`.
- Result: `TSMM-native validation passed for all packages and artifact crosswalks (39 packages).`
- Parsed `_config.yml`, `index.md`, and all `docs/**/*.md` front matter successfully with PyYAML.

## Documentation updates

- `README.md` now explains the Jekyll/Just the Docs publication surface.
- `docs/jekyll-publication.md` documents local preview, GitHub Pages settings, navigation front matter, and assurance expectations.
- Documentation navigation now separates publication concerns into parent sections without changing the active package corpus.

## Release notes

No GitHub release is required for this change. This is a documentation publication-readiness commit only.
