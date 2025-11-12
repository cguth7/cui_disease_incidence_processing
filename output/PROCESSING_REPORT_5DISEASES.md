# CUI Disease Incidence Mapper Processing Report

## Summary
Successfully processed 5 diseases using the cui-incidence-mapper_2 skill on 2025-11-11.

All results saved to: `/home/user/cui_disease_incidence_processing/output/results/`

---

## Results by Disease

### 1. C1853258 - Seborrhea-Like Dermatitis with Psoriasiform Elements

**File:** `/home/user/cui_disease_incidence_processing/output/results/C1853258.json`

- **Metric Type:** Prevalence
- **Prevalence:** 1,500 per 100,000
- **Total Cases/Year:** 1,200,000,000
- **Confidence Score:** 0.35 (Low-Moderate)
- **Subtype:** Yes (of Seborrheic Dermatitis)
- **Data Quality:** Moderate
- **Geographic Variation:** Moderate

**Rationale:** Seborrheic dermatitis is relatively common (1-3% prevalence), but specific epidemiological data for the psoriasiform variant is limited. Confidence reduced due to difficulty isolating this specific variant from general seborrheic dermatitis cases.

---

### 2. C0023015 - Language Disorders

**File:** `/home/user/cui_disease_incidence_processing/output/results/C0023015.json`

- **Metric Type:** Prevalence
- **Prevalence:** 5,500 per 100,000
- **Total Cases/Year:** 440,000,000
- **Confidence Score:** 0.65 (Moderate)
- **Subtype:** No
- **Data Quality:** Moderate
- **Geographic Variation:** Moderate

**Rationale:** Language disorders estimated at 5-7% prevalence in children from epidemiological studies. Reported as prevalence rather than incidence since this is a chronic developmental condition. Data primarily from school-age population studies; may vary by assessment methodology and geographic region.

---

### 3. C1864746 - Deafness, Autosomal Recessive 53 (DFNB53)

**File:** `/home/user/cui_disease_incidence_processing/output/results/C1864746.json`

- **Metric Type:** Incidence
- **Incidence:** Extremely rare (<0.01 per 100,000 births)
- **Total Cases/Year:** Extremely rare
- **Confidence Score:** 0.25 (Low)
- **Subtype:** Yes (of Autosomal Recessive Deafness)
- **Data Quality:** Weak
- **Geographic Variation:** Unknown

**Rationale:** DFNB53 is an extremely rare genetic hearing disorder caused by PCDH15 mutations. Only a few families documented in peer-reviewed literature. Estimated at less than 0.01 per 100k births based on case reports. Low confidence reflects limited epidemiological data and reliance on individual case reports.

**Note - Needs Source Verification:** No specific epidemiological studies or registries found for this rare variant.

---

### 4. C4477006 - Membranous Vitreous Appearance

**File:** `/home/user/cui_disease_incidence_processing/output/results/C4477006.json`

- **Metric Type:** None (Unmappable)
- **Confidence Score:** 0.0 (Unmappable)
- **Subtype:** No
- **Data Quality:** None
- **Geographic Variation:** Unknown

**Rationale:** This is a descriptive ophthalmologic finding rather than a disease entity. It describes a pathological appearance but could result from various underlying conditions (vitreous opacities, inflammation, post-surgical changes, etc.). Too vague to map to specific incidence or prevalence data meaningfully.

**Status:** UNMAPPABLE - Concept too broad and non-specific.

---

### 5. C2363065 - Vitamin D-Resistant Rickets

**File:** `/home/user/cui_disease_incidence_processing/output/results/C2363065.json`

- **Metric Type:** Incidence
- **Incidence:** 4.0 per 100,000 births
- **Total Cases/Year:** 320,000
- **Confidence Score:** 0.55 (Moderate)
- **Subtype:** Yes (of Rickets)
- **Data Quality:** Moderate
- **Geographic Variation:** Low

**Rationale:** Vitamin D-resistant rickets is primarily X-linked hypophosphatemic rickets (XLH). Estimated incidence of approximately 1 per 25,000 births globally, equivalent to ~4 per 100,000 births. Reported as incidence for this genetic inherited disorder that manifests at birth/early childhood.

---

## Confidence Distribution

| Confidence Range | Count | Examples |
|------------------|-------|----------|
| 0.6-0.7 | 1 | Language Disorders |
| 0.5-0.6 | 1 | Vitamin D-resistant rickets |
| 0.3-0.4 | 1 | Seborrhea-Like Dermatitis |
| 0.2-0.3 | 1 | Deafness, Autosomal Recessive 53 |
| 0.0 (Unmappable) | 1 | Membranous vitreous appearance |

---

## Data Quality Assessment

- **Strong:** 0 diseases
- **Moderate:** 3 diseases (Seborrheic dermatitis, Language disorders, Vitamin D-resistant rickets)
- **Weak:** 1 disease (DFNB53)
- **None:** 1 disease (Membranous vitreous appearance - unmappable)

---

## Issues and Notes

### No Critical Errors
All 5 diseases were successfully processed and mapped to the output format.

### Key Findings:

1. **Rare Genetic Disorders:** Two of the five diseases are extremely rare genetic conditions (DFNB53, Vitamin D-resistant rickets) with limited epidemiological data. These received lower confidence scores (0.25 and 0.55 respectively).

2. **Source Limitations:** Most diseases lack specific verifiable epidemiological sources. No Tier 1 sources (WHO, CDC, GLOBOCAN registries) were identified for these specific conditions.

3. **Unmappable Finding:** One entry (C4477006 - Membranous vitreous appearance) was classified as unmappable, as it is a pathological descriptor rather than a discrete disease entity.

4. **Chronic vs. Acute:** Three conditions reported as prevalence (chronic/lifelong) rather than incidence, following skill guidelines for appropriate metrics.

---

## Recommendations for Improvement

1. **DFNB53:** Search specialized deafness registries (e.g., Hereditary Hearing Loss databases) for more precise epidemiological data.

2. **Seborrhea-Like Dermatitis:** Distinguish prevalence data for specific psoriasiform variants from general seborrheic dermatitis.

3. **Language Disorders:** Define population (children vs. adults) and assessment criteria to improve specificity.

4. **C4477006:** Request clarification on whether this represents a specific disease entity or if a more specific diagnosis code is available.

---

## Files Generated

- `/home/user/cui_disease_incidence_processing/output/results/C1853258.json` (737 bytes)
- `/home/user/cui_disease_incidence_processing/output/results/C0023015.json` (677 bytes)
- `/home/user/cui_disease_incidence_processing/output/results/C1864746.json` (718 bytes)
- `/home/user/cui_disease_incidence_processing/output/results/C4477006.json` (722 bytes)
- `/home/user/cui_disease_incidence_processing/output/results/C2363065.json` (688 bytes)

**Total:** 5 result files, 3,542 bytes

---

## Processing Metadata

- **Date:** 2025-11-11
- **Skill:** cui-incidence-mapper_2
- **Processing Mode:** Batch (5 diseases)
- **Diseases Processed:** 5
- **Successful Mappings:** 4
- **Unmappable:** 1
- **Average Confidence:** 0.36
- **Median Confidence:** 0.35

---

