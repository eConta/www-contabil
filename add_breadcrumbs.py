#!/usr/bin/env python3
"""
Add BreadcrumbList schema to all HTML pages
"""
import re
from pathlib import Path

# Breadcrumb structure for each page (filename -> breadcrumb data)
# Format: [(name, url), (name, url), ...]
BREADCRUMBS = {
    # Scalează container
    'scaleaza-cabinetul.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Scalează cabinetul', None)
    ],
    'studii-de-caz.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Scalează cabinetul', 'https://econta.ro/scaleaza-cabinetul.html'),
        ('Studii de caz', None)
    ],

    # Automatizare container
    'automatizare-operationala.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Automatizare operațională', None)
    ],
    'documente-anaf.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Automatizare', 'https://econta.ro/automatizare-operationala.html'),
        ('Documente & ANAF', None)
    ],
    'venituri-facturare.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Automatizare', 'https://econta.ro/automatizare-operationala.html'),
        ('Venituri & facturare', None)
    ],

    # Clienții tăi (standalone)
    'clientii-tai.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Clienții tăi', None)
    ],

    # Platformă container
    'cum-functioneaza.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Cum funcționează eConta', None)
    ],
    'aplicatie-desktop-integrari.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Platformă', 'https://econta.ro/cum-functioneaza.html'),
        ('Aplicație desktop & integrări', None)
    ],
    'securitate-gdpr.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Platformă', 'https://econta.ro/cum-functioneaza.html'),
        ('Securitate & GDPR', None)
    ],
    'clienti-noi.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Platformă', 'https://econta.ro/cum-functioneaza.html'),
        ('Clienți noi prin eConta', None)
    ],

    # Prețuri
    'preturi.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Prețuri platformă', None)
    ],

    # Comparații container
    'vs-taxdome.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Comparații', 'https://econta.ro/vs-taxdome.html'),
        ('eConta vs TaxDome', None)
    ],
    'vs-keez.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Comparații', 'https://econta.ro/vs-taxdome.html'),
        ('eConta vs Keez', None)
    ],
    'vs-huddle.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Comparații', 'https://econta.ro/vs-taxdome.html'),
        ('eConta vs Huddle', None)
    ],
    'vs-econtaai.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Comparații', 'https://econta.ro/vs-taxdome.html'),
        ('eConta vs eContaAI', None)
    ],

    # Utility pages
    'despre-noi.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Despre noi', None)
    ],
    'contact.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Contact', None)
    ],
    'programeaza-demo.html': [
        ('Acasă', 'https://econta.ro/'),
        ('Programează demo', None)
    ],
}

def generate_breadcrumb_schema(breadcrumbs):
    """Generate BreadcrumbList schema JSON"""
    items = []
    for i, (name, url) in enumerate(breadcrumbs, 1):
        item = {
            "@type": "ListItem",
            "position": i,
            "name": name
        }
        if url:
            item["item"] = url
        items.append(item)

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

    import json
    return json.dumps(schema, indent=2, ensure_ascii=False)

def add_breadcrumb_to_page(filepath, breadcrumbs):
    """Add BreadcrumbList schema to a page"""
    filename = filepath.name

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has BreadcrumbList
    if '"@type": "BreadcrumbList"' in content or '"@type":"BreadcrumbList"' in content:
        print(f"  Skipping {filename} (already has BreadcrumbList)")
        return

    # Generate schema
    schema_json = generate_breadcrumb_schema(breadcrumbs)
    schema_html = f'''
  <!-- Schema.org BreadcrumbList -->
  <script type="application/ld+json">
  {schema_json}
  </script>'''

    # Add before </body>
    if '</body>' in content:
        # Find last </script> before </body>
        last_script_pos = content.rfind('</script>\n</body>')
        if last_script_pos > 0:
            content = content[:last_script_pos + 9] + schema_html + content[last_script_pos + 9:]
        else:
            print(f"  ERROR: Could not find schema section in {filename}")
            return
    else:
        print(f"  ERROR: Could not find </body> tag in {filename}")
        return

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Added BreadcrumbList to {filename}")

def main():
    site_dir = Path('/Users/dragosn/CascadeProjects/econta-site/site')

    print(f"Adding BreadcrumbList to {len(BREADCRUMBS)} pages")
    print("=" * 70)

    for filename, breadcrumbs in BREADCRUMBS.items():
        filepath = site_dir / filename
        if filepath.exists():
            add_breadcrumb_to_page(filepath, breadcrumbs)
        else:
            print(f"ERROR: File not found: {filename}")
        print()

    print("=" * 70)
    print("Done!")

if __name__ == '__main__':
    main()
