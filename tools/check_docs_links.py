#!/usr/bin/env python3
"""Check local Markdown links and same-file heading anchors for repository docs."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINKS = re.compile(r'!?(?:\[[^\]]*\])\(([^)]+)\)')
HEADING = re.compile(r'^#{1,6}\s+(.*?)\s*$', re.M)

def slug(s):
    s = re.sub(r'<[^>]+>', '', s).lower()
    s = re.sub(r'[^\w\s-]', '', s, flags=re.UNICODE)
    return re.sub(r'\s+', '-', s.strip())

def anchors(path):
    # GitHub auto-adds suffixes for duplicate headings.
    names = {}
    result = set()
    for match in HEADING.finditer(path.read_text(encoding='utf-8')):
        key = slug(match.group(1))
        i = names.get(key, 0)
        names[key] = i+1
        result.add(key if i == 0 else f'{key}-{i}')
    return result

def check():
    broken = []
    scanned = 0
    for page in ROOT.rglob('*.md'):
        for ref in LINKS.findall(page.read_text(encoding='utf-8')):
            url = ref.strip('<>').split(' ', 1)[0]
            if url.startswith(('https://','http://','mailto:','#not-an-anchor')):
                continue
            path, sep, fragment = url.partition('#')
            target = (page.parent/unquote(path)).resolve() if path else page
            scanned += 1
            if not target.is_file():
                broken.append(f'{page.relative_to(ROOT)}: missing {url}')
            elif fragment and target.suffix.lower() == '.md' and unquote(fragment) not in anchors(target):
                broken.append(f'{page.relative_to(ROOT)}: missing anchor {url}')
    for problem in broken:
        print('BROKEN:', problem)
    print(f'Local documentation link checks: {scanned} scanned, {len(broken)} broken')
    return not broken

if __name__ == '__main__':
    sys.exit(0 if check() else 1)
