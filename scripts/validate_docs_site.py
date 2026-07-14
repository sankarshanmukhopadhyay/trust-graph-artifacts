#!/usr/bin/env python3
"""Validate Jekyll documentation structure without requiring a site build."""
from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
errors=[]
permalinks={}
markdown=list(ROOT.rglob('*.md'))
excluded={'archive'}
for p in markdown:
    rel=p.relative_to(ROOT)
    if rel.parts and rel.parts[0] in excluded:
        continue
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        # Repository control files need not be Pages documents.
        if rel.parts[0] == 'guides' or str(rel) == 'index.md':
            errors.append(f'{rel}: missing YAML front matter')
        continue
    end=text.find('\n---\n',4)
    if end<0:
        errors.append(f'{rel}: unclosed front matter')
        continue
    try:
        data=yaml.safe_load(text[4:end]) or {}
    except Exception as e:
        errors.append(f'{rel}: invalid front matter: {e}')
        continue
    if not data.get('title'):
        errors.append(f'{rel}: missing title')
    if 'permalink' in data:
        pl=data['permalink']
        if pl in permalinks: errors.append(f'{rel}: duplicate permalink with {permalinks[pl]}: {pl}')
        permalinks[pl]=rel
    for m in re.finditer(r'{%\s*link\s+([^\s%]+)\s*%}',text):
        target=ROOT/m.group(1)
        if not target.exists(): errors.append(f'{rel}: missing Jekyll link target {m.group(1)}')
    # conventional relative markdown links (new guide surface only)
    if rel.parts and rel.parts[0] != 'guides':
        continue
    for m in re.finditer(r'\[[^\]]*\]\((?!https?://|mailto:|#|\{)([^)]+)\)',text):
        raw=m.group(1).split('#',1)[0].strip()
        if not raw or raw.startswith('/') or raw.startswith('<'): continue
        target=(p.parent/raw).resolve()
        if not target.exists(): errors.append(f'{rel}: missing relative link {raw}')
# machine-readable crosswalk and all yaml templates
for p in [ROOT/'guides/agentic-systems-architecture-and-governance/crosswalk.yaml', *sorted((ROOT/'guides/agentic-systems-architecture-and-governance/templates').glob('*.yaml'))]:
    try: yaml.safe_load(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p.relative_to(ROOT)}: invalid YAML: {e}')
if errors:
    print('\n'.join(f'ERROR: {e}' for e in errors))
    sys.exit(1)
print(f'Documentation validation passed: {len(markdown)} Markdown files, {len(permalinks)} explicit permalinks.')
