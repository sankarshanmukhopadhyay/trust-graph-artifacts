#!/usr/bin/env python3
"""Validate the Jekyll documentation graph without requiring a Ruby build.

The checks mirror the failure modes that most commonly become GitHub Pages 404s:
invalid front matter, unresolved Liquid links, unsafe source-file Markdown links,
missing navigation parents, and duplicate output routes.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_TOP_LEVEL = {"archive", "vendor", "node_modules", ".git"}
CONTROL_MARKDOWN = {
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "README.md",
}
errors: list[str] = []
pages: list[tuple[Path, dict, str]] = []
routes: dict[str, Path] = {}


def read_front_matter(path: Path) -> tuple[dict, str] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        errors.append(f"{path.relative_to(ROOT)}: unclosed front matter")
        return None
    try:
        data = yaml.safe_load(text[4:end]) or {}
    except Exception as exc:  # pragma: no cover - defensive reporting
        errors.append(f"{path.relative_to(ROOT)}: invalid front matter: {exc}")
        return None
    return data, text[end + 5 :]


def output_route(path: Path, data: dict) -> str:
    permalink = data.get("permalink")
    if permalink:
        route = str(permalink)
        if not route.startswith("/"):
            route = "/" + route
        return route
    rel = path.relative_to(ROOT).with_suffix(".html")
    return "/" + rel.as_posix()


for path in sorted(ROOT.rglob("*.md")):
    rel = path.relative_to(ROOT)
    if rel.parts and rel.parts[0] in EXCLUDED_TOP_LEVEL:
        continue
    parsed = read_front_matter(path)
    if parsed is None:
        # Guide files and the root entry point are intended publication pages.
        if rel.parts and rel.parts[0] == "guides":
            errors.append(f"{rel}: missing YAML front matter")
        continue
    data, body = parsed
    if not data.get("title"):
        errors.append(f"{rel}: missing title")
    pages.append((path, data, body))
    route = output_route(path, data)
    if route in routes:
        errors.append(f"{rel}: duplicate output route with {routes[route].relative_to(ROOT)}: {route}")
    routes[route] = path

# Just the Docs resolves parent and grand_parent by exact title match.
titles = {str(data.get("title")): path for path, data, _ in pages if data.get("title")}
for path, data, body in pages:
    rel = path.relative_to(ROOT)
    for field in ("parent", "grand_parent"):
        value = data.get(field)
        if value and str(value) not in titles:
            errors.append(f"{rel}: {field} title does not exist exactly: {value!r}")

    # Jekyll link tags fail the build when their source target is missing.
    for match in re.finditer(r"{%\s*link\s+([^\s%]+)\s*%}", body):
        target_text = unquote(match.group(1))
        target = ROOT / target_text
        if not target.exists():
            errors.append(f"{rel}: missing Jekyll link target {target_text}")

    # Source-file links such as page.md are not rewritten by kramdown. They
    # therefore point at non-existent files in _site and become Pages 404s.
    for match in re.finditer(r"\[[^\]]*\]\((?!https?://|mailto:|#|\{)([^)]+)\)", body):
        raw = match.group(1).strip().strip("<>")
        target_text = raw.split("#", 1)[0].split("?", 1)[0]
        if not target_text or target_text.startswith("/"):
            continue
        if target_text.lower().endswith((".md", ".markdown")):
            errors.append(
                f"{rel}: unsafe source Markdown link {raw}; use {{% link ... %}} so Jekyll emits the published URL"
            )
            continue
        target = (path.parent / unquote(target_text)).resolve()
        if not target.exists():
            errors.append(f"{rel}: missing relative link target {raw}")

# Validate machine-readable guide surfaces.
yaml_targets = [
    ROOT / "guides/agentic-systems-architecture-and-governance/crosswalk.yaml",
    *sorted((ROOT / "guides/agentic-systems-architecture-and-governance/templates").glob("*.yaml")),
]
for path in yaml_targets:
    try:
        yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    sys.exit(1)

print(
    f"Documentation validation passed: {len(pages)} published Markdown pages, "
    f"{len(routes)} unique output routes, and {len(titles)} navigation titles."
)
