# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Claude Persona
You act as an experienced copywritter and webiste designed, experienced in creating sites for fast growth B2B startups that scalled up fast.
You create content that is convicing, high convertion, highlight aligned to the target segment and specifics for the marketing (Romania) while borrowing practices that were proven in the US but are plausble for RO.

## Project Overview

This is the eConta website project focused on creating a new site variant targeting accountants who want to purchase the eConta platform for internal work organization. The project repositions eConta from B2B accounting services to B2B accounting software for independent accountants.

## Deployment Domain

**IMPORTANT**: This site is deployed on **`platforma.econta.ro`**, NOT on the root `econta.ro` domain.

- **Platform site** (this project): `https://platforma.econta.ro/` - B2B software for accountants
- **Services site**: `https://www.econta.ro/` - B2B accounting services for entrepreneurs

All meta tags (canonical, og:url, twitter:url), sitemap.xml, robots.txt, and schema.org URLs must use `https://platforma.econta.ro/`.

The segment banner in the header links to `https://www.econta.ro` to direct entrepreneurs to the services site.

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

### Site Layout Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│ SEGMENT BANNER (top, dismissable)                                       │
│ "Ești antreprenor? Cauți servicii de contabilitate?" → [Vezi oferta]    │
├─────────────────────────────────────────────────────────────────────────┤
│ HEADER                                                                  │
│ ┌─────────┐                                          ┌───────────────┐  │
│ │  LOGO   │         MAIN NAV (6 items)               │  UTILITY NAV  │  │
│ └─────────┘  Scalează | Automatizare | Clienții tăi  │ Despre|Contact│  │
│              Platformă | Prețuri | Comparații        │[Demo button]  │  │
└─────────────────────────────────────────────────────────────────────────┘
```

**Segment Banner**: Link către site-ul pentru antreprenori (al doilea segment de clienți). Nu e în meniu, e un div/banner separat.

### Content Architecture

**Container menu** = jumbo menu cu headline, nu e clickabil direct, dar afișează paginile din el pentru click.

**SITEMAP FINAL (19 pagini)**:

```
MAIN NAV:
├── 📁 SCALEAZĂ CABINETUL (container)
│   ├── Scalează cabinetul
│   └── Studii de caz
├── 📁 AUTOMATIZARE (container)
│   ├── Automatizare operațională
│   ├── Documente & ANAF
│   └── Venituri & facturare
├── 📄 CLIENȚII TĂI (pagină directă - beneficii pentru clienții contabilului)
├── 📁 PLATFORMĂ (container)
│   ├── Cum funcționează eConta
│   ├── Aplicație desktop & integrări
│   ├── Securitate & GDPR
│   └── Clienți noi prin eConta
├── 📁 PREȚURI (container)
│   ├── Prețuri platformă
│   └── Calculator
└── 📁 COMPARAȚII (container - ultimul în meniu)
    ├── vs TaxDome
    ├── vs Keez
    ├── vs Huddle
    └── vs eContaAI

UTILITY NAV (dreapta header):
├── 📄 Despre noi
├── 📄 Contact (cu Calendly)
└── 🔘 [Programează demo] - button CTA

FOOTER:
└── Toate paginile + legal + social
```

### Content Files Structure

Fișierele markdown pentru conținut sunt în `content/` cu naming convention `container--pagina.md`:

```
content/
├── home.md
├── scaleaza-cabinetul--scaleaza-cabinetul.md
├── scaleaza-cabinetul--studii-de-caz.md
├── automatizare--automatizare-operationala.md
├── automatizare--documente-anaf.md
├── automatizare--venituri-facturare.md
├── clientii-tai.md
├── platforma--cum-functioneaza.md
├── platforma--aplicatie-desktop-integrari.md
├── platforma--securitate-gdpr.md
├── platforma--clienti-noi.md
├── preturi--preturi-platforma.md
├── preturi--calculator.md
├── comparatii--vs-taxdome.md
├── comparatii--vs-keez.md
├── comparatii--vs-huddle.md
├── comparatii--vs-econtaai.md
├── despre-noi.md
└── contact.md
```

### CTA Standards
- **CTA Primar**: "Programează demo" (acțiune directă, high commitment)
- **CTA Secundar**: "Vezi cum funcționează" (low commitment, explorare)

### Design Reference
- Base HTML template: `site/index.html` (dark theme with blue/pink accents)
- UI inspiration: `inputs/color theme.png`
- Brand assets: `inputs/logo econta.png`

## Languages
- **Content**: Romanian
- **Code**: Standard web technologies (HTML, CSS, JavaScript expected)

## Important Files to Reference
- `inputs/readme.md`: Core project requirements and positioning
- `inputs/2025 New site.md`: Complete sitemap and content (use offset/limit when reading due to 2MB size)
- `site/index.html`: Reference implementation for styling and layout patterns

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

### 6. Key Integrations & Features (from spec)
- **ANAF**: eFactura, SPV integration (native)
- **Billing**: Included as module for entrepreneurs (not separate app)
- **Arhivare**: Cloud + local automatic archiving
- **AI**: Document processing, interpretation, clarifications
- **Communication**: Multi-channel (email, WhatsApp, platform)

## Company Information (for Despre noi & Contact)

- **Fondatori**: Claudiu (CEO), Petrișor (Expert fiscal-contabil), Dragoș (Tech lead)
- **Entitate legală**: AI DIGITALTRANSFORMATION S.R.L.
- **CUI**: 48990514
- **J**: J40/19937/2023
- **Email**: office@econta.ro
- **Telefon**: +40 784242424
- **Adresă**: Nu se afișează public pe site

**Experiență echipă**: 25+ ani în dezvoltare software de gestiune și contabilitate (Centro de Soft background).

## Copywriting Rules

### DO (Ce să faci):
- Curăță H1 duplicate din conținutul original
- Scurtează secțiuni repetitive
- Îmbunătățește titluri să fie mai "punchier" și orientate pe beneficii
- Standardizează CTA-uri conform standardelor de mai sus
- Structurează clar: Hero → Secțiuni → CTA final
- Elimină emoji-uri excesive (👉) din text - păstrează doar pentru bullet points dacă e necesar
- Păstrează tabelele comparative "Fără/Cu eConta" dar nu le multiplica excesiv

### DON'T (Ce să NU faci):
- NU inventa metrici/procente noi
- NU adăuga features inexistente
- NU fabrica testimoniale sau case studies
- NU adăuga integrări nementionate (doar SAGA, WinMentor sunt confirmate)
- NU schimba prețurile (0.99€/firmă/lună etc.)
- NU adăuga mobile apps (nu există)

## Working Methodology

Citește `content/*.md` complet înainte de implementare. Nu fabrica - întreabă dacă nu e clar.

## Design & UX Learnings

### Navigation
- **Mega menu**: Full-width (100vw), position fixed, cu grid layout pe orizontală
- **NU** dropdowns înguste sau verticale — arată basic/neprofesionist
- Include icons în fiecare menu item pentru scanabilitate

### Page Layout

**Homepage vs Pagini specifice — roluri diferite:**
- **Homepage** = overview, punct de intrare → centered hero, broad messaging
- **Pagini interne** = deep dive pe un topic → problem-focused, pain points vizuale
- ❌ NU copia structura de pe o pagină pe alta fără a gândi rolul

**Hero homepage:**
- Trebuie să comunice CE vindem, nu beneficii vagi
- ❌ "Rămâi relevant într-o contabilitate care se schimbă" — nu spune ce e produsul
- ✅ "Scalează cabinetul fără să scalezi echipa" — direct pe valoare
- Valoarea principală eConta: **scalare fără angajări** (automatizare + standardizare)

**Hero pagini interne** (problem-focused):
  - Eyebrow tag cu problema ("Problema reală a creșterii")
  - Headline care articulează dilema clientului
  - Pain points visual panel (nu doar text)
  - Social proof metrics sub CTA
- **Comparison sections**: Cards side-by-side cu gradiente
  - Roșu/coral pentru "Fără eConta" (rgba(255,107,138,.08))
  - Verde pentru "Cu eConta" (rgba(75,230,177,.08))
  - Icons X și ✓ în pătrate colorate
  - NU tabele simple — arată basic

## Copywriting & Tone of Voice Learnings

### Forma de adresare
- **"Tu"** este corect pentru B2B SaaS modern în România
- Creează apropriere și încredere, nu distanță formală
- Contabilii care caută să scaleze cu tehnologie sunt deschiși la comunicare directă

### Limbaj profesional - CE SĂ EVIȚI
| ❌ Evită | ✅ Folosește |
|----------|-------------|
| "stres" | "presiune operațională" |
| "haos" | "informații disparate" |
| "ținute în cap" | "gestionate informal" |
| "fără surprize" | "predictibil și planificat" |
| "-Stres" (ca metrică) | "Predictibil" sau "Controlat" |

### Limbaj profesional - CE FUNCȚIONEAZĂ
- Terminologie din domeniu: "portofoliu", "operațional", "echipă", "capacitate"
- Headline-uri care articulează problema exact cum o gândește clientul
- Exemple concrete relevante pentru audiență (PFA, Uber, prag TVA/micro)
- Hook-uri directe dar profesionale ("Nu mai pierzi timp întrebând «unde suntem?»")

### Content completeness
Când implementezi o pagină, include TOATE elementele din markdown:
1. ✅ Intro paragraphs (context și empatie)
2. ✅ Exemple concrete (specifice pentru contabili)
3. ✅ Hooks și callouts
4. ✅ Insight boxes cu mesaje cheie
5. ✅ Dashboard/UI previews unde e relevant
6. ✅ Beneficii summary boxes

### Conversion principles
- Above the fold = problema + soluție + CTA + social proof
- Pain points vizuale, nu doar enumerate în text
- Metrici concrete (dar doar cele din spec!)
- CTA-uri clare: "Programează demo" (primary), "Vezi cum funcționează" (secondary)

### Data-Heavy Pages (Case Studies, Comparisons)

**Layout:**
- ❌ NU carduri side-by-side când ai mult conținut (devine înghesuit, criptic)
- ✅ Layout vertical, full-width, cu spațiu generos între secțiuni
- ✅ Grid 2 coloane pentru fiecare caz: summary (stânga) + comparison table (dreapta)

**Tabele comparative (Before/After):**
- ✅ Folosește `<table>` semantic HTML pentru date tabulare, NU div-uri cu grid
- ✅ `<thead>`, `<tbody>`, `<tfoot>` pentru structură clară
- ✅ Stilizare: borders subtile, rows alternante, totals highlighted
- ✅ Footer row cu totale și diferența procentuală

**Principii generale:**
- Conținutul data-heavy trebuie să "respire" — spațiu generos
- Design execution contează la fel de mult ca structura
- Testează vizual înainte de a considera complet

## Comparison Pages (vs X)

### Ierarhia Informației (sus = relevant, jos = explicativ)

1. **Hero: Punchline** - diferența cheie într-o propoziție (statement, NU întrebare)
2. **Quick proof** - 3 diferențe critice cu ❌/✅ vizual, above the fold
3. **Decision matrix** - "Când alegi fiecare" pentru scanners rapizi
4. **Comparison table** - tabelul complet din spec cu ❌/✅
5. **Fairness section** - unde funcționează bine competitorul (recunoaștere onestă)
6. **Solution summary** - ce face eConta diferit (scurt)
7. **Final CTA** - simplu, cu risk reversal

### Principiu
Informația valoroasă sus (decizia în 5 secunde), detaliile și explicațiile jos (pentru cei care vor să citească mai mult).