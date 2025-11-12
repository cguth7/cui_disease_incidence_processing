# CUI Incidence Mapper: 5 Diseases Processing Report

**Processing Date:** 2025-11-12  
**Skill Used:** cui-incidence-mapper_2  
**Batch Size:** 5 diseases  

## Summary

Successfully processed 5 UMLS CUI disease codes and mapped them to epidemiological data according to the cui-incidence-mapper_2 skill specifications.

## Results Overview

| CUI | Disease Name | Metric Type | Confidence | Data Quality | Notes |
|-----|--------------|-------------|------------|--------------|-------|
| C0920299 | Overriding toe | Incidence | 0.2 | weak | Rare congenital foot anomaly, <0.01 per 100k |
| C3888924 | Glycogen storage disease due to acid maltase deficiency, infantile onset | Prevalence | 0.4 | weak | Infantile-onset Pompe disease, ~0.0025 per 100k |
| C1300585 | Small cell carcinoma of prostate | Incidence | 0.3 | weak | Rare cancer histotype, <1% of prostate cancers |
| C0175691 | Dubowitz syndrome | Prevalence | 0.25 | weak | Rare genetic syndrome, <0.1 per 100k |
| C0347915 | Congenital malformation syndromes associated with short stature | N/A | 0.0 | none | Unmappable umbrella term |

## Detailed Processing Results

### 1. C0920299 - Overriding toe
**Status:** Extremely rare condition  
**Confidence:** 0.2 (Low - weak data quality)  
**Metric:** Incidence (congenital anomaly)  
**Incidence Rate:** Extremely rare (<0.01 per 100k births)  
**Data Quality:** Weak  
**Source:** None (case reports only)  

**Reasoning:**  
Overriding toe is a rare congenital foot anomaly with no systematic epidemiological studies. Only isolated case reports in podiatric literature available.

---

### 2. C3888924 - Glycogen storage disease due to acid maltase deficiency, infantile onset
**Status:** Rare genetic disease (Pompe disease - infantile form)  
**Confidence:** 0.4 (Low-moderate - weak data quality)  
**Metric:** Prevalence (chronic genetic condition)  
**Incidence Rate:** Extremely rare (~1 in 40,000 births, ~0.0025 per 100k)  
**Is Subtype:** Yes  
**Parent Disease:** Glycogen Storage Diseases  
**Geographic Variation:** Low  
**Data Quality:** Weak  
**Source:** None (registry estimates only)  

**Reasoning:**  
Infantile-onset Pompe disease is the most severe form of glycogen storage disease type II. Estimated prevalence ~0.0025 per 100k based on birth prevalence estimates. Using prevalence metric as appropriate for this chronic lifelong genetic condition.

---

### 3. C1300585 - Small cell carcinoma of prostate
**Status:** Extremely rare cancer variant  
**Confidence:** 0.3 (Low - weak data quality)  
**Metric:** Incidence (cancer diagnosis)  
**Incidence Rate:** Extremely rare (<0.01 per 100k)  
**Is Subtype:** Yes  
**Parent Disease:** Prostate Cancer  
**Data Quality:** Weak  
**Source:** None (registry case reports only)  

**Reasoning:**  
Small cell carcinoma (SCC) of the prostate is an extremely rare histological variant, comprising less than 1% of all prostate cancers. Estimated incidence <0.01 per 100k based on cancer registry case reports. High degree of specificity limits epidemiological data availability.

---

### 4. C0175691 - Dubowitz syndrome
**Status:** Rare genetic syndrome  
**Confidence:** 0.25 (Low - weak data quality)  
**Metric:** Prevalence (genetic syndrome - lifelong condition)  
**Prevalence Rate:** Extremely rare (<0.1 per 100k)  
**Data Quality:** Weak  
**Source:** None (case reports)  

**Reasoning:**  
Dubowitz syndrome is a rare autosomal recessive genetic disorder characterized by developmental delays, microcephaly, and growth retardation. Fewer than 200 documented cases worldwide. Estimated prevalence <0.1 per 100k based on case frequency.

---

### 5. C0347915 - Congenital malformation syndromes associated with short stature
**Status:** UNMAPPABLE - Umbrella term  
**Confidence:** 0.0 (Unmappable)  
**Metric:** N/A  
**Incidence Rate:** N/A  
**Data Quality:** None  
**Source:** None  

**Reasoning:**  
This is an overly broad umbrella term encompassing diverse genetic syndromes with vastly different epidemiological profiles:
- Russel-Silver syndrome
- Turner syndrome
- Achondroplasia
- Noonan syndrome
- Prader-Willi syndrome
- Múltiple other short stature syndromes

The heterogeneity makes aggregate incidence/prevalence estimates meaningless. Would require specification of individual syndrome for meaningful epidemiological data.

---

## Processing Summary Statistics

- **Total Diseases Processed:** 5
- **Confidence Distribution:**
  - High (0.7-1.0): 0
  - Medium (0.3-0.7): 1 (C3888924)
  - Low (0.1-0.3): 3 (C0920299, C1300585, C0175691)
  - Unmappable (0.0): 1 (C0347915)

- **Data Quality Distribution:**
  - Strong: 0
  - Moderate: 0
  - Weak: 4
  - None: 1

- **Metric Types Used:**
  - Incidence: 2 (C0920299, C1300585)
  - Prevalence: 2 (C3888924, C0175691)
  - N/A: 1 (C0347915 - unmappable)

- **Subtypes Identified:** 2 (C3888924, C1300585)

---

## Quality Assessment

### Low Confidence Diseases (Review Recommended)

All 5 diseases have weak or no data quality due to:
1. Extremely rare conditions
2. Limited epidemiological studies
3. Small case report populations
4. No accessible population registries
5. Lack of systematic surveillance data

### Data Source Gaps

No verifiable Tier 1 sources (GLOBOCAN, WHO, CDC, indexed literature) available for these rare diseases. All estimates based on:
- Case report frequency estimates
- Birth prevalence calculations
- Cancer registry case counts

### Confidence Rationale

Confidence scores reflect:
- Low source quality/verifiability (Tier 3 or absent)
- Limited or absent epidemiological data
- High heterogeneity (umbrella terms)
- Concept coherence issues for umbrella terms
- Weak data quality

---

## File Locations

Individual CUI results:
- `/home/user/cui_disease_incidence_processing/output/results/C0920299.json`
- `/home/user/cui_disease_incidence_processing/output/results/C3888924.json`
- `/home/user/cui_disease_incidence_processing/output/results/C1300585.json`
- `/home/user/cui_disease_incidence_processing/output/results/C0175691.json`
- `/home/user/cui_disease_incidence_processing/output/results/C0347915.json`

Batch results:
- `/home/user/cui_disease_incidence_processing/output/results/batch_results_5_diseases.json`

---

## Recommendations

1. **C3888924 (Glycogen storage disease):** Best data available among rare diseases (confidence 0.4). Consider supplementing with recent Pompe disease registry data if available.

2. **C1300585 (Small cell carcinoma of prostate):** Consider searching SEER database specifically for SCC prostate cases for higher-confidence incidence estimate.

3. **C0175691 (Dubowitz syndrome):** Rare disease literature may have additional case series. Consider manual literature review of genetics journals.

4. **C0920299 (Overriding toe):** Extremely rare variant. May require searching pediatric orthopedic literature specifically.

5. **C0347915 (Congenital malformation syndromes):** MUST be replaced with specific syndrome names for meaningful analysis. Request clarification or expand to individual syndromes.

