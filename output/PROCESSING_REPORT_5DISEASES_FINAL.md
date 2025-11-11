# Disease Incidence Mapping Report - 5 Diseases

**Processing Date:** 2025-11-11  
**Skill Used:** cui-incidence-mapper_2  
**Output Directory:** `/home/user/cui_disease_incidence_processing/output/`

---

## Processing Summary

| Metric | Count |
|--------|-------|
| **Total Diseases Processed** | 5 |
| **Successfully Processed** | 5 |
| **High Confidence (≥0.7)** | 1 |
| **Medium Confidence (0.3-0.7)** | 3 |
| **Low Confidence (<0.3)** | 1 |
| **Unmappable (confidence=0.0)** | 1 |

---

## Individual Disease Results

### 1. Disease ID 2733: Congenital Heart Block
- **CUI:** C0149530
- **Incidence:** 0.5 per 100k person-years
- **Confidence:** 0.55 (Medium)
- **Data Quality:** Moderate
- **Metric Type:** Incidence
- **Est. Annual Cases:** 40,000
- **Key Finding:** Rare arrhythmia occurring in ~1 per 20,000 births, often associated with maternal anti-Ro/SSA and anti-La/SSB antibodies
- **Output File:** `/home/user/cui_disease_incidence_processing/output/disease_2733.json`

### 2. Disease ID 2158: Myocardial Diseases
- **CUI:** C0036529
- **Incidence:** null (Unmappable)
- **Confidence:** 0.0 (Unmappable)
- **Data Quality:** None
- **Metric Type:** null
- **Key Finding:** UMBRELLA TERM - Too heterogeneous covering multiple cardiac pathologies (cardiomyopathies, myocarditis, heart failure) with vastly different incidence rates. Requires specification of disease type.
- **Status:** Flagged for refinement - user should specify disease type
- **Output File:** `/home/user/cui_disease_incidence_processing/output/disease_2158.json`

### 3. Disease ID 2383: Tuberculosis
- **CUI:** C0041296
- **Incidence:** 160.0 per 100k person-years
- **Confidence:** 0.9 (High)
- **Data Quality:** Strong
- **Metric Type:** Incidence
- **Data Year:** 2005 (Tier 1 - WHO Registry)
- **Est. Annual Cases:** 12,800,000
- **Geographic Variation:** High (from <5 in developed countries to >200 in high-burden countries)
- **Source:** World Health Organization TB/HIV Fact Sheet 2005
- **Key Finding:** Well-established global incidence based on WHO surveillance data
- **Output File:** `/home/user/cui_disease_incidence_processing/output/disease_2383.json`

### 4. Disease ID 2898: Craniorachischisis
- **CUI:** C0152426
- **Incidence:** "extremely rare" (<0.1 per 100k births)
- **Confidence:** 0.35 (Low)
- **Data Quality:** Weak
- **Metric Type:** Incidence
- **Est. Annual Cases:** Extremely rare
- **Key Finding:** Severe neural tube defect combining cranial and spinal involvement. Very limited epidemiological data available.
- **Source Type:** Case reports (not literature sources)
- **Output File:** `/home/user/cui_disease_incidence_processing/output/disease_2898.json`

### 5. Disease ID 2558: Tethered Cord Syndrome
- **CUI:** C0080218
- **Incidence:** 1.0 per 100k person-years
- **Prevalence:** 10.0 per 100k
- **Confidence:** 0.58 (Medium)
- **Data Quality:** Moderate
- **Metric Type:** Both incidence and prevalence
- **Est. Annual Cases:** 80,000
- **Geographic Variation:** Low
- **Key Finding:** Can present congenitally or acquired later. Epidemiological data limited, estimate based on clinical studies.
- **Output File:** `/home/user/cui_disease_incidence_processing/output/disease_2558.json`

---

## Output Files Generated

1. **Individual Disease Files** (JSON format):
   - `/home/user/cui_disease_incidence_processing/output/disease_2733.json`
   - `/home/user/cui_disease_incidence_processing/output/disease_2158.json`
   - `/home/user/cui_disease_incidence_processing/output/disease_2383.json`
   - `/home/user/cui_disease_incidence_processing/output/disease_2898.json`
   - `/home/user/cui_disease_incidence_processing/output/disease_2558.json`

2. **Batch Results**:
   - `/home/user/cui_disease_incidence_processing/output/batch_results_5diseases.json` (All 5 results in array format)

3. **Processing Summary**:
   - `/home/user/cui_disease_incidence_processing/output/processing_summary_5diseases.json`

---

## Confidence Score Breakdown

**High Confidence (≥0.7):** 1 disease
- Tuberculosis (0.9) - Strong data from WHO registry

**Medium Confidence (0.3-0.7):** 3 diseases
- Congenital Heart Block (0.55) - Moderate data, limited sources
- Tethered Cord Syndrome (0.58) - Moderate epidemiological data
- Craniorachischisis (0.35) - Limited epidemiological data available

**Unmappable (0.0):** 1 disease
- Myocardial Diseases (0.0) - Umbrella term too heterogeneous

---

## Key Observations

1. **Best Mapped:** Tuberculosis - Strong WHO epidemiological data with high confidence
2. **Umbrella Term Alert:** Myocardial Diseases flagged as unmappable - needs specification
3. **Rare Diseases:** Craniorachischisis and Congenital Heart Block have limited epidemiological data
4. **Mixed Metrics:** Tethered Cord Syndrome reported with both incidence and prevalence
5. **Geographic Variation:** Tuberculosis shows high geographic variation (5-fold to 40-fold differences)

---

## Data Quality Summary

| Quality Level | Count | Diseases |
|---------------|-------|----------|
| Strong | 1 | Tuberculosis |
| Moderate | 2 | Congenital Heart Block, Tethered Cord Syndrome |
| Weak | 1 | Craniorachischisis |
| None | 1 | Myocardial Diseases |

---

## Recommendations

1. **For Myocardial Diseases (C0036529):** Specify which type (e.g., dilated cardiomyopathy, acute myocarditis) for proper mapping
2. **For Craniorachischisis:** Limited epidemiological data; consider aggregating with other neural tube defects
3. **For Tuberculosis:** Excellent data quality; use 0.9 confidence score for pharmaceutical market sizing
4. **For Congenital Heart Block:** Consider linking to maternal autoimmune conditions for epidemiological context
5. **For Tethered Cord Syndrome:** Distinguish congenital vs. acquired presentations in future analyses

---

**All output files are in JSON format matching the cui-incidence-mapper_2 skill specification.**
