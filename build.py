#!/usr/bin/env python3
"""
Build script: Injects header.html and footer.html into all pages.
Run this after editing includes/header.html or includes/footer.html.

Usage: python build.py
"""
import re
from pathlib import Path

SITE_DIR = Path(__file__).parent / 'site'
INCLUDES_DIR = SITE_DIR / 'includes'

# Markers for injected content
HEADER_START = '<!-- HEADER_START -->'
HEADER_END = '<!-- HEADER_END -->'
FOOTER_START = '<!-- FOOTER_START -->'
FOOTER_END = '<!-- FOOTER_END -->'

# Regex patterns for the old JS fetch approach
HEADER_JS_PATTERN = re.compile(
    r'<!-- Header loaded from includes/header\.html -->\s*'
    r'<div id="site-header"></div>\s*'
    r'<script>\s*'
    r"fetch\('includes/header\.html'\).*?"
    r'</script>',
    re.DOTALL
)

FOOTER_JS_PATTERN = re.compile(
    r'<!-- Footer loaded from includes/footer\.html -->\s*'
    r'<div id="site-footer"></div>\s*'
    r'<script>\s*'
    r"fetch\('includes/footer\.html'\).*?"
    r'</script>',
    re.DOTALL
)

# Regex patterns for already-injected content (subsequent runs)
HEADER_MARKER_PATTERN = re.compile(
    rf'{re.escape(HEADER_START)}.*?{re.escape(HEADER_END)}',
    re.DOTALL
)

FOOTER_MARKER_PATTERN = re.compile(
    rf'{re.escape(FOOTER_START)}.*?{re.escape(FOOTER_END)}',
    re.DOTALL
)


def load_include(filename):
    """Load content from includes directory."""
    path = INCLUDES_DIR / filename
    if not path.exists():
        print(f"  WARNING: {path} not found")
        return None
    return path.read_text(encoding='utf-8')


def process_file(html_path, header_content, footer_content):
    """Process a single HTML file."""
    content = html_path.read_text(encoding='utf-8')
    original = content

    # Prepare wrapped content
    header_wrapped = f"{HEADER_START}\n{header_content}{HEADER_END}"
    footer_wrapped = f"{FOOTER_START}\n{footer_content}{FOOTER_END}"

    # Try to replace existing markers first (subsequent runs)
    if HEADER_START in content:
        content = HEADER_MARKER_PATTERN.sub(header_wrapped, content)
    else:
        # First run: replace JS fetch pattern
        content = HEADER_JS_PATTERN.sub(header_wrapped, content)

    if FOOTER_START in content:
        content = FOOTER_MARKER_PATTERN.sub(footer_wrapped, content)
    else:
        # First run: replace JS fetch pattern
        content = FOOTER_JS_PATTERN.sub(footer_wrapped, content)

    # Check if anything changed
    if content != original:
        html_path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("Loading includes...")
    header = load_include('header.html')
    footer = load_include('footer.html')

    if not header or not footer:
        print("ERROR: Missing include files. Aborting.")
        return

    print(f"\nProcessing HTML files in {SITE_DIR}...")

    html_files = sorted(SITE_DIR.glob('*.html'))
    updated = 0
    skipped = 0

    for html_path in html_files:
        result = process_file(html_path, header, footer)
        if result:
            print(f"  ✓ {html_path.name}")
            updated += 1
        else:
            print(f"  - {html_path.name} (no changes)")
            skipped += 1

    print(f"\nDone! Updated: {updated}, Unchanged: {skipped}")


if __name__ == '__main__':
    main()
