#!/usr/bin/env python3
"""
Fix 8 page titles that are too short (SEO optimization)
"""
import re
from pathlib import Path

# New titles mapping (filename -> new title)
NEW_TITLES = {
    'studii-de-caz.html': 'Studii de caz automatizare contabilitate România - eConta',
    'securitate-gdpr.html': 'Securitate GDPR platformă cabinete contabile - eConta',
    'clientii-tai.html': 'Platform comunicare client - CRM contabilitate - eConta',
    'documente-anaf.html': 'Documente ANAF eFactura - Automatizare contabilitate - eConta',
    'scaleaza-cabinetul.html': 'Platformă cabinete contabile - Scalare fără angajări - eConta',
    'automatizare-operationala.html': 'Automatizare contabilitate - Declarații și obligații - eConta',
    'venituri-facturare.html': 'CRM contabilitate - Facturare automată cabinete - eConta',
    'programeaza-demo.html': 'Demo platformă cabinete contabile - Automatizare - eConta'
}

def fix_title(filepath, new_title):
    """Fix title in HTML file"""
    filename = filepath.name

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract old title
    old_title_match = re.search(r'<title>(.*?)</title>', content)
    if not old_title_match:
        print(f"  ERROR: Could not find title in {filename}")
        return

    old_title = old_title_match.group(1)
    print(f"  Old: {old_title} ({len(old_title)} chars)")
    print(f"  New: {new_title} ({len(new_title)} chars)")

    # Replace in <title> tag
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{new_title}</title>',
        content,
        count=1
    )

    # Replace in OG title
    content = re.sub(
        r'<meta property="og:title" content=".*?">',
        f'<meta property="og:title" content="{new_title}">',
        content,
        count=1
    )

    # Replace in Twitter title
    content = re.sub(
        r'<meta name="twitter:title" content=".*?">',
        f'<meta name="twitter:title" content="{new_title}">',
        content,
        count=1
    )

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Updated title in {filename}")

def main():
    site_dir = Path('/Users/dragosn/CascadeProjects/econta-site/site')

    print(f"Fixing {len(NEW_TITLES)} page titles")
    print("=" * 70)

    for filename, new_title in NEW_TITLES.items():
        filepath = site_dir / filename
        if filepath.exists():
            fix_title(filepath, new_title)
        else:
            print(f"ERROR: File not found: {filename}")
        print()

    print("=" * 70)
    print("Done!")

if __name__ == '__main__':
    main()
