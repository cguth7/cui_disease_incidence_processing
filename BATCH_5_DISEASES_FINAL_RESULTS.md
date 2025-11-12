# CUI Incidence Mapper - Batch Processing Results
## 5 Diseases Processed

**Processing Date:** November 12, 2025  
**Skill Used:** cui-incidence-mapper_2  
**Batch Input:** 5 diseases with UMLS CUI codes

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Diseases Processed | 5 |
| Success Rate | 100% (5/5) |
| High Confidence (0.7-1.0) | 0 |
| Medium Confidence (0.3-0.7) | 1 |
| Low Confidence (0.1-0.3) | 4 |
| Strong Data Quality | 0 |
| Moderate Data Quality | 1 |
| Weak Data Quality | 4 |

---

## Disease Processing Details

### 1. C3151077 - Aortic Aneurysm, Familial Thoracic 7

**Classification:** Specific genetic subtype  
**Parent Disease:** Familial Thoracic Aortic Aneurysm  
**Incidence:** Extremely rare (<0.01 per 100k)  
**Confidence:** 0.2 (Low)  
**Data Quality:** Weak  

**Key Findings:**
- TAA7 is caused by TGFBR2 mutations
- Represents a rare genetic form of familial thoracic aortic aneurysm
- No systematic epidemiological data available
- Based on scattered case reports
- Confidence limited by weak data quality and absence of epidemiological studies

**Output File:** `/home/user/cui_disease_incidence_processing/output/results/C3151077.json`

---

### 2. C4551899 - Cholestasis, Benign Recurrent Intrahepatic 1

**Classification:** Specific genetic subtype (BRIC1)  
**Parent Disease:** Benign Recurrent Intrahepatic Cholestasis  
**Incidence:** Extremely rare (<0.01 per 100k)  
**Confidence:** 0.2 (Low)  
**Data Quality:** Weak  

**Key Findings:**
- BRIC1 caused by ATP8B1 mutations
- Extremely rare genetic liver disorder
- Characterized by episodes of cholestasis and pruritus
- Limited to scattered case reports and small family studies
- No systematic epidemiological surveillance data

**Output File:** `/home/user/cui_disease_incidence_processing/output/results/C4551899.json`

---

### 3. C0375536 - Congenital Osteodystrophy

**Classification:** Heterogeneous group of bone dysplasias  
**Incidence:** Extremely rare (<1 per 100k aggregate)  
**Confidence:** 0.25 (Low)  
**Data Quality:** Weak  

**Key Findings:**
- Encompasses multiple skeletal dysplasias
- Includes Albright hereditary osteodystrophy (AHO) and related disorders
- Heterogeneous group with varying clinical presentations
- Limited individual epidemiological data for each subtype
- Aggregate estimate reflects multiple rare skeletal dysplasia types

**Output File:** `/home/user/cui_disease_incidence_processing/output/results/C0375536.json`

---

### 4. C1838577 - Cerebral Autosomal Recessive Arteriopathy with Subcortical Infarcts and Leukoencephalopathy

**Classification:** Specific rare genetic disorder (CARASIL)  
**Incidence:** Extremely rare (<0.001 per 100k)  
**Confidence:** 0.2 (Low)  
**Data Quality:** Weak  

**Key Findings:**
- Rare genetic cerebrovascular disorder
- Caused by HTRA1 gene mutations
- <100 confirmed cases documented worldwide in medical literature
- Characterized by progressive cerebral small vessel disease
- Incidence and prevalence data from case reports only

**Output File:** `/home/user/cui_disease_incidence_processing/output/results/C1838577.json`

---

### 5. C2242816 - Chronic Secretory Otitis Media

**Classification:** Specific subtype of Otitis media (serous otitis media/OME)  
**Parent Disease:** Otitis media  
**Prevalence:** 5,000 per 100k (5% of population)  
**Total Cases/Year:** ~400 million globally  
**Confidence:** 0.55 (Moderate)  
**Data Quality:** Moderate  
**Metric Type:** Prevalence  

**Key Findings:**
- Also known as serous otitis media or otitis media with effusion (OME)
- Most common in children (20-90% experience OME at some point)
- Chronic form affects 5-10% persistently
- Prevalence varies significantly by age group
- Based on pediatric epidemiological studies and WHO guidelines
- Most common cause of hearing loss in children

**Output File:** `/home/user/cui_disease_incidence_processing/output/results/C2242816.json`

---

## Output Files Generated

### Individual Results (JSON Format)
All results follow the cui-incidence-mapper_2 specification with required fields:

- `/home/user/cui_disease_incidence_processing/output/results/C3151077.json`
- `/home/user/cui_disease_incidence_processing/output/results/C4551899.json`
- `/home/user/cui_disease_incidence_processing/output/results/C0375536.json`
- `/home/user/cui_disease_incidence_processing/output/results/C1838577.json`
- `/home/user/cui_disease_incidence_processing/output/results/C2242816.json`

### Batch Results Array
- `/home/user/cui_disease_incidence_processing/output/results/BATCH_5_DISEASES_RESULTS.json`  
  Contains all 5 results in valid JSON array format per skill specifications

### Summary Reports
- `/home/user/cui_disease_incidence_processing/output/results/5_DISEASES_PROCESSING_SUMMARY.txt`  
  Detailed processing summary with statistics and notes

---

## Field Documentation

Each result contains these key fields:

| Field | Description |
|-------|-------------|
| `cui` | UMLS Concept Unique Identifier |
| `cui_name` | Full disease name from UMLS |
| `incidence_per_100k` | New cases per 100,000 person-years (or "extremely rare") |
| `prevalence_per_100k` | Existing cases per 100,000 population |
| `metric_type` | "incidence", "prevalence", "both", or null |
| `total_cases_per_year` | Global estimated cases per year |
| `confidence` | 0.0-1.0 confidence score reflecting data quality |
| `is_subtype` | Boolean: is this a specific subtype? |
| `parent_disease` | Name of broader disease category |
| `reasoning` | Explanation of data source and methodology |
| `data_quality` | "strong", "moderate", "weak", or "none" |
| `geographic_variation` | "low", "moderate", "high", or "unknown" |
| `year_specific` | Boolean: is data from a specific year? |
| `data_year` | Year of data (or null) |
| `source` | Full citation of data source |
| `source_url` | URL to verify data (null if not available) |
| `source_type` | "registry", "literature", "estimate", or null |

---

## Quality Assessment

### Confidence Scoring Rationale

**C3151077 (0.2):** Extremely rare genetic variant with only case reports  
**C4551899 (0.2):** Rare genetic disorder, minimal systematic data  
**C0375536 (0.25):** Heterogeneous umbrella category, weak epidemiological data  
**C1838577 (0.2):** <100 cases worldwide, case report-based evidence  
**C2242816 (0.55):** Moderate - pediatric epidemiological data available

### Data Limitations

1. **Four rare genetic disorders** have limited epidemiological data
   - Confidence capped at 0.2-0.25 due to weak data quality
   - No verifiable Tier 1 sources (registries, WHO data)
   - Relies on case reports and small studies

2. **Chronic secretory otitis media** has moderate data
   - Confidence 0.55 reflects available pediatric studies
   - Geographic and age-dependent variation noted
   - Source citations provided but URLs not verified

---

## Processing Notes

- All JSON files are valid and follow skill specifications
- No unmappable diseases encountered
- Confidence scores are conservative and appropriate
- Geographic variation documented where applicable
- No sources were fabricated; null used where data unavailable
- Metric types chosen appropriately (prevalence for chronic conditions)
- All extremely rare diseases marked as such rather than false precision

---

## Batch Processing Workflow

1. ✓ Created batch input JSON with 5 diseases
2. ✓ Applied cui-incidence-mapper_2 guidelines
3. ✓ Generated individual JSON output files for each CUI
4. ✓ Created batch results array (BATCH_5_DISEASES_RESULTS.json)
5. ✓ Validated all JSON files for syntax correctness
6. ✓ Generated comprehensive processing summary
7. ✓ Documented quality assessment and rationale

---

## Files Locations

```
/home/user/cui_disease_incidence_processing/
├── batch_input_5_diseases.json
├── output/results/
│   ├── C3151077.json
│   ├── C4551899.json
│   ├── C0375536.json
│   ├── C1838577.json
│   ├── C2242816.json
│   ├── BATCH_5_DISEASES_RESULTS.json
│   └── 5_DISEASES_PROCESSING_SUMMARY.txt
└── BATCH_5_DISEASES_FINAL_RESULTS.md (this file)
```

---

## Conclusion

All 5 diseases have been successfully processed using the cui-incidence-mapper_2 skill. Four diseases are extremely rare genetic disorders with limited epidemiological data (confidence 0.2-0.25), while one disease (chronic secretory otitis media) is more common with moderate epidemiological data (confidence 0.55). All results follow the skill's specification for JSON output format and field requirements.

