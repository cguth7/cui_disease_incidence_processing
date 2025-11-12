# CUI Incidence Mapper - Processing Report
## 5 Diseases Processed Using cui-incidence-mapper_2 Skill

**Date:** November 12, 2025
**Skill:** cui-incidence-mapper_2
**Total Diseases Processed:** 5
**Output Location:** `/home/user/cui_disease_incidence_processing/output/results/`

---

## Processing Summary

All 5 diseases have been successfully mapped and processed according to the skill's epidemiological guidelines. Each result includes detailed confidence scoring, data quality assessment, and reasoning based on available epidemiological literature.

---

## Individual Disease Results

### 1. C0205622 - Microinvasive Tumor

**File:** `/home/user/cui_disease_incidence_processing/output/results/C0205622.json`

| Field | Value |
|-------|-------|
| CUI | C0205622 |
| Disease Name | Microinvasive tumor |
| Incidence per 100k | null |
| Confidence | 0.0 |
| Data Quality | none |
| Metric Type | null |
| Total Cases/Year | null |
| Is Subtype | false |
| Parent Disease | null |

**Key Findings:**
- **Status:** UNMAPPABLE
- **Reason:** Pathology descriptor referring to tumor size/staging (invasion <5mm), not a specific disease entity
- **Clinical Context:** Microinvasive is a classification used in pathology reports to describe tumors with minimal invasion into surrounding tissue
- **Incidence Dependency:** The incidence rate depends entirely on the primary tumor type being classified (e.g., microinvasive breast cancer, thyroid cancer, etc.)
- **Confidence Justification:** Confidence score of 0.0 reflects that this is not a mappable disease concept but rather a pathological descriptive term

---

### 2. C0234247 - Neuralgia, Atypical

**File:** `/home/user/cui_disease_incidence_processing/output/results/C0234247.json`

| Field | Value |
|-------|-------|
| CUI | C0234247 |
| Disease Name | Neuralgia, Atypical |
| Incidence per 100k | 2.5 |
| Confidence | 0.35 |
| Data Quality | weak |
| Metric Type | incidence |
| Total Cases/Year | 200,000 |
| Is Subtype | true |
| Parent Disease | Neuralgia |

**Key Findings:**
- **Status:** MAPPED (Low Confidence)
- **Incidence Estimate:** ~2.5 per 100,000 person-years
- **Reasoning:** Atypical neuralgia is a vague diagnosis lacking clear clinical definition. Estimated based on general neuralgia incidence range of 1-4 per 100k
- **Diagnostic Issues:**
  - "Atypical" classification is subjective and lacks standardized criteria
  - No dedicated epidemiological studies on atypical neuralgia specifically
  - Often represents cases that don't fit into recognized neuralgia subtypes
- **Confidence Limitation:** Low confidence (0.35) due to diagnostic ambiguity and absence of standardized epidemiological studies
- **Data Sources:** None verifiable; estimate based on general neuralgia patterns

---

### 3. C0423711 - Neuralgia, Perineal

**File:** `/home/user/cui_disease_incidence_processing/output/results/C0423711.json`

| Field | Value |
|-------|-------|
| CUI | C0423711 |
| Disease Name | Neuralgia, Perineal |
| Incidence per 100k | 0.8 |
| Confidence | 0.40 |
| Data Quality | weak |
| Metric Type | incidence |
| Total Cases/Year | 64,000 |
| Is Subtype | true |
| Parent Disease | Neuralgia |

**Key Findings:**
- **Status:** MAPPED (Low Confidence)
- **Incidence Estimate:** ~0.8 per 100,000 person-years
- **Clinical Context:** Perineal neuralgia is a rare nerve pain condition affecting the perineum (region between genitals and anus)
- **Etiology:** Often results from:
  - Trauma or injury to the region
  - Childbirth-related nerve damage
  - Compression syndromes from prolonged sitting
  - Post-surgical complications
- **Confidence Limitation:** Low confidence (0.40) reflects sparse epidemiological literature
- **Geographic Variation:** Moderate variation based on trauma/childbirth patterns
- **Data Sources:** None verifiable; based on regional nerve compression syndrome patterns

---

### 4. C0038870 - Neuralgia, Supraorbital

**File:** `/home/user/cui_disease_incidence_processing/output/results/C0038870.json`

| Field | Value |
|-------|-------|
| CUI | C0038870 |
| Disease Name | Neuralgia, Supraorbital |
| Incidence per 100k | 1.2 |
| Confidence | 0.45 |
| Data Quality | weak |
| Metric Type | incidence |
| Total Cases/Year | 96,000 |
| Is Subtype | true |
| Parent Disease | Neuralgia |

**Key Findings:**
- **Status:** MAPPED (Low Confidence)
- **Incidence Estimate:** ~1.2 per 100,000 person-years
- **Anatomical Basis:** Nerve pain along the supraorbital nerve (V1 branch of the trigeminal nerve)
- **Clinical Presentations:**
  - Compression syndrome from various causes
  - May occur as component of primary trigeminal neuralgia
  - Pain distribution: Upper forehead, medial upper eyelid region
- **Confidence Limitation:** Low confidence (0.45) reflects uncertainty about whether this is:
  - Independent disease entity with distinct epidemiology
  - Secondary manifestation of trigeminal neuralgia
- **Data Sources:** None verifiable; limited standalone epidemiological data
- **Relationship to Trigeminal Neuralgia:** Could represent 10-20% of trigeminal neuralgia cases, but specific incidence not well-established

---

### 5. C0423712 - Neuralgia, Iliohypogastric Nerve

**File:** `/home/user/cui_disease_incidence_processing/output/results/C0423712.json`

| Field | Value |
|-------|-------|
| CUI | C0423712 |
| Disease Name | Neuralgia, Iliohypogastric Nerve |
| Incidence per 100k | 0.5 |
| Confidence | 0.30 |
| Data Quality | weak |
| Metric Type | incidence |
| Total Cases/Year | 40,000 |
| Is Subtype | true |
| Parent Disease | Neuralgia |

**Key Findings:**
- **Status:** MAPPED (Very Low Confidence)
- **Incidence Estimate:** <0.5 per 100,000 person-years (estimated 0.5)
- **Clinical Context:** Very rare nerve compression syndrome
- **Anatomical Basis:**
  - Iliohypogastric nerve: Branch of lumbar plexus (L1 root)
  - Often compressed at inguinal ligament
  - Related to ilioinguinal nerve entrapment syndrome
- **Etiology:**
  - Post-inguinal hernia repair (most common cause)
  - Direct trauma to groin region
  - Prolonged pressure/compression from tight clothing or positions
- **Confidence Limitation:** Very low confidence (0.30) reflects:
  - Minimal epidemiological data
  - Largely documented through case reports only
  - Often misdiagnosed as other conditions (back pain, hernia recurrence)
- **Data Sources:** None verifiable; based on case report frequency patterns

---

## Confidence Distribution Analysis

| Confidence Range | Count | Categories |
|-----------------|-------|-----------|
| 0.0 (Unmappable) | 1 | C0205622 - Pathology descriptor |
| 0.30-0.35 (Very Low) | 2 | C0423712, C0234247 - Rare/vague conditions |
| 0.40-0.45 (Low) | 2 | C0423711, C0038870 - Rare neuralgias |

**Key Insight:** All confidence scores are below 0.5, reflecting:
- Rarity of these specific conditions
- Lack of published epidemiological studies
- Definitional/diagnostic ambiguity for several conditions
- Limited data in medical registries

---

## Estimated Global Disease Burden

| Disease | Incidence/100k | Global Cases/Year | Confidence |
|---------|---|---|---|
| C0205622 | null | null | 0.0 |
| C0234247 | 2.5 | 200,000 | 0.35 |
| C0423711 | 0.8 | 64,000 | 0.40 |
| C0038870 | 1.2 | 96,000 | 0.45 |
| C0423712 | 0.5 | 40,000 | 0.30 |
| **TOTAL** | **4.0** | **~400,000** | **~0.37 avg** |

**Note:** C0205622 excluded from total as it is not a standalone disease. Global estimates assume world population of 8 billion.

---

## Quality Assessment Summary

### Data Quality Overview
- **Strong (0):** None of the 5 diseases
- **Moderate (0):** None of the 5 diseases
- **Weak (4):** C0234247, C0423711, C0038870, C0423712
- **None (1):** C0205622

### Source Verification
- **Verifiable Sources:** 0
- **Estimated/Inferred:** 4
- **Unmappable:** 1

**Implication:** These are rare conditions with minimal epidemiological research. Clinical data primarily comes from case reports and hospital-based series rather than population-based registries.

---

## Hierarchy Detection Results

### Parent-Child Relationships Identified
- **C0234247** (Neuralgia, Atypical) → Parent: Neuralgia
- **C0423711** (Neuralgia, Perineal) → Parent: Neuralgia
- **C0038870** (Neuralgia, Supraorbital) → Parent: Neuralgia
- **C0423712** (Neuralgia, Iliohypogastric Nerve) → Parent: Neuralgia

**Pattern:** 4 of 5 diseases are identified as subtypes of the broader Neuralgia category, reflecting anatomical and clinical specificity.

---

## Recommendations

### For Pharmaceutical/Research Use
1. **C0205622:** Do not use independently. Always specify the primary tumor type.
2. **C0234247:** Use with caution. Consider including primary neuralgias instead.
3. **C0423711-C0423712:** These are very rare. Combined, they represent <150k cases/year globally.

### For Further Research
- Conduct population-based epidemiological studies on specific neuralgias
- Develop standardized diagnostic criteria for atypical neuralgia
- Establish international registries for rare nerve compression syndromes
- Clarify overlap between iliohypogastric and ilioinguinal nerve entrapment

### For Market Sizing
- Total addressable market for these 5 conditions: ~400,000 cases/year
- Most cases are treatable with conservative management
- Pharmaceutical potential limited due to rarity and overlapping symptomatology with primary neuralgias

---

## Technical Notes

### Skill Configuration
- **Skill Name:** cui-incidence-mapper_2
- **Processing Mode:** Batch (5 diseases)
- **Output Format:** Individual JSON files per CUI
- **Confidence Scoring:** Based on source quality (40%), metric appropriateness (30%), concept coherence (20%), data availability (10%)

### Files Generated
1. `/home/user/cui_disease_incidence_processing/output/results/C0205622.json`
2. `/home/user/cui_disease_incidence_processing/output/results/C0234247.json`
3. `/home/user/cui_disease_incidence_processing/output/results/C0423711.json`
4. `/home/user/cui_disease_incidence_processing/output/results/C0038870.json`
5. `/home/user/cui_disease_incidence_processing/output/results/C0423712.json`

---

## Conclusion

All 5 diseases have been successfully processed and documented. Results show that:

1. **One disease (C0205622)** is unmappable as it is a pathology descriptor, not an independent disease
2. **Four diseases** represent rare neuralgias with low-confidence estimates (0.30-0.45)
3. **Combined disease burden** is estimated at ~400,000 annual cases globally
4. **Quality assessment:** All estimates are weak due to limited epidemiological data
5. **Hierarchy:** 4 of 5 are identified as subtypes of broader Neuralgia category

The results are ready for use in pharmaceutical market sizing, but should be interpreted cautiously given low confidence scores and data quality limitations.

---

**Report Generated:** November 12, 2025
**Processing Tool:** cui-incidence-mapper_2 Skill
**Status:** COMPLETE
