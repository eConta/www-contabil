#!/usr/bin/env python3
"""
Add page-specific schemas to HTML files
"""
import re
from pathlib import Path

# SoftwareApplication schema
SOFTWARE_APP_SCHEMA = '''
  <!-- Schema.org SoftwareApplication -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "eConta",
    "applicationCategory": "BusinessApplication",
    "operatingSystem": "Web, Windows",
    "offers": {
      "@type": "Offer",
      "price": "0.99",
      "priceCurrency": "EUR",
      "billingIncrement": "P1M",
      "description": "Per firmă activă pe lună"
    },
    "description": "Platformă de automatizare operațională pentru cabinete contabile"
  }
  </script>'''

# Product schema for preturi.html
PRODUCT_SCHEMA = '''
  <!-- Schema.org Product -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "eConta - Platformă pentru cabinete contabile",
    "description": "Model pricing flexibil: abonament lunar 0,99€/firmă SAU pay-per-document începând de la 0,99€/document",
    "offers": [
      {
        "@type": "Offer",
        "name": "Abonament lunar per firmă",
        "price": "0.99",
        "priceCurrency": "EUR",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "0.99",
          "priceCurrency": "EUR",
          "unitText": "firmă activă",
          "billingIncrement": "P1M"
        }
      },
      {
        "@type": "Offer",
        "name": "Pay-per-document",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "minPrice": "0.99",
          "priceCurrency": "EUR",
          "unitText": "document"
        },
        "description": "Pricing pe document, începând de la 0,99€"
      }
    ]
  }
  </script>'''

# ContactPage schema
CONTACT_PAGE_SCHEMA = '''
  <!-- Schema.org ContactPage -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "ContactPage",
    "name": "Contact eConta",
    "mainEntity": {
      "@type": "Organization",
      "name": "eConta",
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+40784242424",
        "email": "office@econta.ro",
        "contactType": "Customer Service",
        "areaServed": "RO",
        "availableLanguage": "ro"
      }
    }
  }
  </script>'''

# AboutPage schema
ABOUT_PAGE_SCHEMA = '''
  <!-- Schema.org AboutPage -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "AboutPage",
    "name": "Despre eConta",
    "mainEntity": {
      "@type": "Organization",
      "name": "eConta",
      "founder": [
        {"@type": "Person", "name": "Claudiu", "jobTitle": "CEO"},
        {"@type": "Person", "name": "Petrișor", "jobTitle": "Expert fiscal-contabil"},
        {"@type": "Person", "name": "Dragoș", "jobTitle": "Tech Lead"}
      ]
    }
  }
  </script>'''

# Page-specific schemas mapping
PAGE_SCHEMAS = {
    'cum-functioneaza.html': SOFTWARE_APP_SCHEMA,
    'aplicatie-desktop-integrari.html': SOFTWARE_APP_SCHEMA,
    'preturi.html': PRODUCT_SCHEMA,
    'contact.html': CONTACT_PAGE_SCHEMA,
    'despre-noi.html': ABOUT_PAGE_SCHEMA,
}

def add_schema_to_page(filepath, schema):
    """Add schema to a page before </body>"""
    filename = filepath.name

    print(f"Processing {filename}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if schema already exists
    schema_type = schema.split('"@type":')[1].split('"')[1]
    if f'"@type": "{schema_type}"' in content or f'"@type":"{schema_type}"' in content:
        print(f"  Skipping {filename} (already has {schema_type} schema)")
        return

    # Add schema before </body>
    if '</body>' in content:
        # Find Organization schema closing tag
        org_schema_end = content.rfind('</script>\n</body>')
        if org_schema_end > 0:
            # Insert after Organization schema
            content = content[:org_schema_end + 9] + schema + content[org_schema_end + 9:]
        else:
            print(f"  ERROR: Could not find Organization schema in {filename}")
            return
    else:
        print(f"  ERROR: Could not find </body> tag in {filename}")
        return

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Added {schema_type} schema to {filename}")

def main():
    site_dir = Path('/Users/dragosn/CascadeProjects/econta-site/site')

    print(f"Adding page-specific schemas to {len(PAGE_SCHEMAS)} pages")
    print("=" * 70)

    for filename, schema in PAGE_SCHEMAS.items():
        filepath = site_dir / filename
        if filepath.exists():
            add_schema_to_page(filepath, schema)
        else:
            print(f"ERROR: File not found: {filename}")
        print()

    print("=" * 70)
    print("Done!")

if __name__ == '__main__':
    main()
