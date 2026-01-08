---
title: "Calculator prețuri - eConta"
description: "Calculează costul exact pentru portofoliul tău. Introdu numărul de firme și volumul lunar."
container: "preturi"
---

# Calculează costul exact pentru portofoliul tău

## Hero

**Subheadline:**
Introdu numărul de firme și volumul lunar. Vezi instant costul total, costul per firmă și impactul real în raport cu onorariile tale.

**Descriere:**
Modelul eConta este **pay-per-use**: plătești un cost fix mic per cod fiscal și costuri variabile doar pentru activitatea efectiv procesată (declarații, documente AI, stocare).

Calculatorul de mai jos îți arată **valoarea reală**, fără estimări aproximative.

---

## Calculator interactiv

<!-- CALCULATOR HTML - DE IMPLEMENTAT -->

**Inputuri:**
- Număr de firme (coduri fiscale)
- Declarații principale (D112, D300, D101, D100) pe lună - total
- Alte declarații pe lună - total
- Documente eFactura pe lună - total
- Alte documente pe lună - total
- Stocare suplimentară (GB) - opțional

**Outputuri:**
- Cost fix lunar (nr firme × 0,99 €)
- Cost declarații principale (nr × 0,50 €)
- Cost alte declarații (nr × 0,20 €)
- Cost documente (nr × 0,05 €) - eFactura = 0
- Cost stocare (GB × 0,19 €)
- **Total lunar**
- **Cost per firmă**

**Notă pentru implementare:** Prima coloană cu prețurile unitare este readonly.

---

## Structura de cost

| Element | Preț unitar |
|---------|-------------|
| Cost fix per cod fiscal | 0,99 € / lună |
| Declarații principale (D112, D300, D101, D100) | 0,50 € / declarație |
| Alte declarații | 0,20 € / declarație |
| eFactura | 0 € |
| Alte documente | 0,05 € / document |
| Stocare suplimentară | 0,19 € / GB / lună |

---

## Întrebări frecvente

### Plătesc dacă nu folosesc într-o lună?

Doar costul fix per firmă (0,99 €). Variabilele apar doar dacă procesezi.

### eFactura este chiar gratuită?

Da, indiferent de volum.

### Pot calcula pe scenarii (ex. +30 firme)?

Calculatorul este gândit pentru o simulare punctuală. Dar dacă știi numărul total de declarații și documente, poți calcula costul total foarte simplu.

### Dacă am arhive mari, se calculează separat?

Da, stocarea suplimentară este opțională și se aplică doar peste pragurile interne.

---

## CTA Final

**CTA Primar:** Vezi structura completă de prețuri
**CTA Secundar:** Programează demo
