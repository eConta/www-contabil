# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the eConta website project focused on creating a new site variant targeting accountants who want to purchase the eConta platform for internal work organization. The project repositions eConta from B2B accounting services to B2B accounting software for independent accountants.

## Project Structure

```
econta-site/
├── inputs/                    # Design and content inputs
│   ├── readme.md             # Project requirements (in Romanian)
│   ├── 2025 New site.md      # Site content and sitemap (2MB, draft copy)
│   ├── eConta – Scalează cabinetul.html  # Reference layout example
│   ├── color theme.png       # UI design mockup
│   └── logo econta.png       # Company logo
└── site/                     # Implementation directory (currently empty)
```

## Key Project Information

### Target Audience
- **Primary**: Accountants who want to scale their practice using eConta's platform
- **Secondary**: Entrepreneurs seeking premium accounting services through eConta-powered accountants

### Main Product Positioning
eConta has a dual positioning:
1. **Accounting services**: Traditional B2B accounting services for small companies
2. **Platform software**: Management platform for accountants to organize their own client portfolios (focus of this project)

### Content Architecture
The main navigation structure from `2025 New site.md` includes:
- **Scalează cabinetul** (Scale your practice)
- **Automatizare operațională** (Operational automation)
- **Servicii contabile premium** (Premium accounting services)
- **Documente & ANAF** (Documents & Tax Authority)
- **Venituri & facturare** (Revenue & billing)
- **Platformă & ecosistem** (Platform & ecosystem)

### Design Reference
- Base HTML template: `inputs/eConta – Scalează cabinetul.html` (dark theme with blue/pink accents)
- UI inspiration: `inputs/color theme.png`
- Brand assets: `inputs/logo econta.png`

## Development Notes

This appears to be a content and design project rather than a traditional software development project. The main work involves:

1. **Content organization**: Converting the draft content from `2025 New site.md` into structured web pages
2. **Design implementation**: Building on the reference HTML template and design mockups
3. **Site structure**: Implementing the defined navigation and page hierarchy

## Languages
- **Content**: Romanian
- **Code**: Standard web technologies (HTML, CSS, JavaScript expected)

## Important Files to Reference
- `inputs/readme.md`: Core project requirements and positioning
- `inputs/2025 New site.md`: Complete sitemap and content (use offset/limit when reading due to 2MB size)
- `inputs/eConta – Scalează cabinetul.html`: Reference implementation for styling and layout patterns

## CRITICAL: Content Accuracy Principles

**⚠️ NEVER fabricate content. These rules are MANDATORY:**

### 1. Content Source of Truth
- **ALL content MUST come from `inputs/2025 New site.md`**
- Read the original specification BEFORE implementing any page
- If content is not in the spec, DO NOT invent it

### 2. Forbidden Fabrications
**NEVER add these without explicit specification:**
- ❌ Mobile apps (eConta does not have mobile apps)
- ❌ Desktop app content not specified in original
- ❌ Fabricated metrics: percentages, improvements, data points, numbers
- ❌ Fake proof points: "200+ cabinets", "15k+ clients", "85% retention"
- ❌ Made-up testimonials or case studies
- ❌ Features that don't exist

### 3. What IS Allowed from Spec
These metrics ARE in the original spec and can be used:
- ✅ "până la 25% reducere" a timpului (automatizare-operationala, line 457)
- ✅ "zero declarații ratate" (automatizare-operationala, line 458)
- ✅ "0,99 € / firmă / lună" pricing model
- ✅ Any content explicitly written in `2025 New site.md`

### 4. Implementation Checklist
Before completing ANY page implementation:
1. ✅ Read the full section from `2025 New site.md`
2. ✅ Verify all sections from spec are included
3. ✅ Check no metrics/percentages are fabricated
4. ✅ Confirm no features mentioned that don't exist
5. ✅ Validate against spec one final time

### 5. Design Guidelines
- **Icons**: Use monochrome SVG icons in theme colors (no emoji, no colored icons)
- **Theme colors**: #0F1220 (bg), #FF4FBF (pink), #5A86FF (blue), #4BE6B1 (green), #FF6B8A (red), #FFBF4F (yellow)
- **Style**: Dark theme B2B SaaS, professional, clean
- **No emojis** in production code unless explicitly requested

### 6. Site Structure (from spec)
Main pages:
1. **Home** (index.html)
2. **Scalează cabinetul** (scaleaza-cabinetul.html)
3. **Automatizare operațională** (automatizare-operationala.html)
4. **Servicii contabile premium** (servicii-premium.html)
5. **Documente & ANAF** (documente-anaf.html)
6. **Venituri & facturare** (venituri-facturare.html)
7. **Prețuri** (preturi.html)

**Note**: Platformă & ecosistem page will be redesigned separately.

### 7. Key Integrations & Features (from spec)
- **ANAF**: eFactura, SPV integration (native)
- **Billing**: Included as module for entrepreneurs (not separate app)
- **Arhivare**: Cloud + local automatic archiving
- **AI**: Document processing, interpretation, clarifications
- **Communication**: Multi-channel (email, WhatsApp, platform)

### 8. What eConta Does NOT Have
- ❌ Mobile apps
- ❌ Features not in specification
- ❌ Any content not explicitly mentioned in `2025 New site.md`

## Working Methodology

When implementing ANY page:
1. Read the relevant section from `inputs/2025 New site.md` completely
2. Take notes on ALL sections and subsections
3. Identify any metrics or data points mentioned
4. Implement ONLY what's in the spec
5. Double-check before marking as complete

**Remember**: It's better to ask for clarification than to fabricate content.