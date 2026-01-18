#!/usr/bin/env python3
"""
Add SEO meta tags and Organization schema to all HTML files in site/
"""
import os
import re
from pathlib import Path

# Organization schema template
ORGANIZATION_SCHEMA = '''
  <!-- Schema.org Organization -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "eConta",
    "legalName": "AI DIGITALTRANSFORMATION S.R.L.",
    "url": "https://econta.ro",
    "logo": "https://econta.ro/images/logo-econta.png",
    "description": "Platformă de automatizare și management pentru cabinete contabile din România",
    "email": "office@econta.ro",
    "telephone": "+40784242424",
    "address": {
      "@type": "PostalAddress",
      "addressCountry": "RO",
      "addressLocality": "București"
    },
    "taxID": "48990514",
    "vatID": "RO48990514",
    "founder": [
      {"@type": "Person", "name": "Claudiu", "jobTitle": "CEO"},
      {"@type": "Person", "name": "Petrișor", "jobTitle": "Expert fiscal-contabil"},
      {"@type": "Person", "name": "Dragoș", "jobTitle": "Tech Lead"}
    ],
    "sameAs": []
  }
  </script>'''

def get_meta_tags(filename, title, description):
    """Generate meta tags for a page"""
    # Determine URL
    if filename == 'index.html':
        url = 'https://econta.ro/'
    else:
        url = f'https://econta.ro/{filename}'

    return f'''
  <!-- Canonical -->
  <link rel="canonical" href="{url}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://econta.ro/images/og-image.png">
  <meta property="og:locale" content="ro_RO">
  <meta property="og:site_name" content="eConta">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{url}">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://econta.ro/images/twitter-card.png">
'''

def process_file(filepath):
    """Process a single HTML file"""
    filename = os.path.basename(filepath)

    # Skip index.html as it's already processed
    if filename == 'index.html':
        print(f"Skipping {filename} (already processed)")
        return

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has canonical tag (already processed)
    if 'rel="canonical"' in content:
        print(f"  Skipping {filename} (already has SEO tags)")
        return

    # Extract title and description
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)"', content)

    if not title_match or not desc_match:
        print(f"  ERROR: Could not find title or description in {filename}")
        return

    title = title_match.group(1)
    description = desc_match.group(1)

    # Add meta tags after description meta tag
    meta_tags = get_meta_tags(filename, title, description)

    # Find the position after description meta tag
    desc_pattern = r'(<meta name="description" content=".*?">)'
    if re.search(desc_pattern, content):
        content = re.sub(
            desc_pattern,
            r'\1' + meta_tags,
            content,
            count=1
        )
    else:
        print(f"  ERROR: Could not find description meta tag in {filename}")
        return

    # Add Organization schema before </body>
    if '</body>' in content:
        content = content.replace('</body>', ORGANIZATION_SCHEMA + '\n</body>', 1)
    else:
        print(f"  ERROR: Could not find </body> tag in {filename}")
        return

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Added SEO tags to {filename}")

def main():
    site_dir = Path('/Users/dragosn/CascadeProjects/econta-site/site')
    html_files = list(site_dir.glob('*.html'))

    print(f"Found {len(html_files)} HTML files")
    print("=" * 60)

    for filepath in sorted(html_files):
        process_file(filepath)

    print("=" * 60)
    print("Done!")

if __name__ == '__main__':
    main()
