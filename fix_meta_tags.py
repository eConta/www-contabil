#!/usr/bin/env python3
"""
Script pentru a corecta meta tags în toate fișierele HTML:
1. Schimbă econta.ro în platforma.econta.ro (cu excepții)
2. Șterge liniile cu og:image și twitter:image
"""

import os
import re
from pathlib import Path

def fix_meta_tags(file_path):
    """Corectează meta tags într-un fișier HTML"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    lines = content.split('\n')
    new_lines = []

    for line in lines:
        # Skip lines cu og:image sau twitter:image
        if 'og:image' in line or 'twitter:image' in line:
            print(f"  ❌ Șterg: {line.strip()[:80]}...")
            continue

        # Înlocuiește econta.ro cu platforma.econta.ro DOAR în contextele relevante
        # Excludem: www.econta.ro, office@econta.ro, pozele fondatorilor
        new_line = line

        # Canonical links
        if 'rel="canonical"' in line:
            new_line = line.replace('https://econta.ro/', 'https://platforma.econta.ro/')

        # OG URL
        elif 'property="og:url"' in line:
            new_line = line.replace('https://econta.ro/', 'https://platforma.econta.ro/')

        # Twitter URL
        elif 'name="twitter:url"' in line:
            new_line = line.replace('https://econta.ro/', 'https://platforma.econta.ro/')

        # JSON-LD schema - url și logo
        elif '"url":' in line and 'https://econta.ro' in line and 'econta.ro/' not in line:
            # "url": "https://econta.ro" (fără trailing slash sau cu ,)
            new_line = line.replace('"https://econta.ro"', '"https://platforma.econta.ro"')

        elif '"logo":' in line and 'https://econta.ro/images/' in line:
            new_line = line.replace('https://econta.ro/images/', 'https://platforma.econta.ro/images/')

        # Breadcrumb items
        elif '"item":' in line and 'https://econta.ro/' in line:
            new_line = line.replace('https://econta.ro/', 'https://platforma.econta.ro/')

        if new_line != line:
            print(f"  ✏️  {line.strip()[:60]}...")
            print(f"     → {new_line.strip()[:60]}...")

        new_lines.append(new_line)

    new_content = '\n'.join(new_lines)

    if new_content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    site_dir = Path('/Users/dragosn/CascadeProjects/econta-site/site')

    # Găsește toate fișierele HTML (exclude includes pentru moment)
    html_files = []
    for html_file in site_dir.glob('*.html'):
        html_files.append(html_file)

    print(f"🔍 Găsite {len(html_files)} fișiere HTML\n")

    modified_count = 0
    for html_file in sorted(html_files):
        print(f"📄 {html_file.name}")
        if fix_meta_tags(html_file):
            modified_count += 1
            print(f"   ✅ Modificat\n")
        else:
            print(f"   ⏭️  Fără modificări\n")

    print(f"\n✨ Gata! {modified_count}/{len(html_files)} fișiere modificate")

if __name__ == '__main__':
    main()
