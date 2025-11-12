# CUI Incidence Mapper Processing Results

## Overview
This directory contains epidemiological data for 5 UMLS disease codes processed using the **cui-incidence-mapper_2** skill on 2025-11-12.

## Processed Diseases

### 1. C0232600 - Self-induced vomiting
- **Confidence Score:** 0.65 (Moderate)
- **Incidence:** 3.2 per 100,000 person-years
- **Category:** Subtype of Bulimia Nervosa
- **Data Year:** 2005
- **Quality:** Moderate
- **Summary:** Self-induced vomiting is a primary symptom of bulimia nervosa affecting 56-90% of patients. The reported incidence is based on Dutch primary care epidemiological studies.

### 2. C1377940 - Odontogenic myxofibroma
- **Confidence Score:** 0.35 (Low)
- **Incidence:** Extremely rare (0.007 per 100,000)
- **Category:** Rare benign odontogenic tumor
- **Quality:** Weak
- **Summary:** This is one of the rarest odontogenic tumors with reported annual incidence of only 0.07 per million. Limited systematic epidemiological data available; primarily documented through case reports in dental literature.

### 3. C1335661 - Radiation-Related Angiosarcoma
- **Confidence Score:** 0.62 (Moderate-High)
- **Incidence:** 0.05 per 100,000 person-years
- **Category:** Secondary malignancy post-radiotherapy
- **Quality:** Moderate
- **Summary:** RIAS is a rare vascular malignancy following radiotherapy, most commonly after breast cancer treatment. Occurs in 0.05-0.3% of breast cancer patients receiving breast-conserving surgery with adjuvant radiotherapy. Median latency period is 6 years (range 3-12 years).

### 4. C0220647 - Carcinoma of unknown primary (CUP)
- **Confidence Score:** 0.78 (High)
- **Incidence:** 4.1 per 100,000 person-years
- **Category:** Distinct cancer entity
- **Data Year:** 2005
- **Quality:** Strong
- **Summary:** CUP is one of the 10 most frequent cancers worldwide, representing 3-5% of all human malignancies. Population-based incidence of 4.1 per 100,000 based on cancer registry data. Incidence has been declining since the early 1980s due to improved diagnostic techniques.

### 5. C0342765 - D-Glyceric aciduria
- **Confidence Score:** 0.25 (Very Low)
- **Incidence:** Extremely rare
- **Category:** Autosomal recessive metabolic disorder
- **Quality:** None (Insufficient data)
- **Summary:** D-Glyceric aciduria is an extremely rare genetic metabolic disorder caused by D-glycerate kinase deficiency. Prevalence is unknown according to Orphanet and NIH databases. Only scattered case reports exist in medical literature. Presents with highly variable phenotype from severe encephalopathy to normal development.

## File Structure

Each disease has its own JSON file following this naming convention:
- `{CUI}.json` - Individual disease epidemiological data

Example structure:
```json
{
  "cui": "C0220647",
  "cui_name": "Carcinoma of unknown primary",
  "incidence_per_100k": 4.1,
  "confidence": 0.78,
  "data_quality": "strong",
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "...",
  "source": "...",
  "source_url": "...",
  "source_type": "literature"
}
```

## Quality Metrics

### Confidence Distribution
- **High (0.7-1.0):** 1 disease (20%) - Carcinoma of unknown primary
- **Moderate (0.3-0.7):** 3 diseases (60%) - Self-induced vomiting, Radiation-related angiosarcoma
- **Low (0.0-0.3):** 1 disease (20%) - D-Glyceric aciduria

### Data Quality
- **Strong:** 1 disease - Carcinoma of unknown primary
- **Moderate:** 2 diseases - Self-induced vomiting, Radiation angiosarcoma
- **Weak:** 1 disease - Odontogenic myxofibroma
- **None:** 1 disease - D-Glyceric aciduria

## Methodology

### Skill Application
This data was processed using the cui-incidence-mapper_2 skill following these guidelines:

1. **Source Verification:** All data sourced from peer-reviewed literature, cancer registries, and epidemiological databases
2. **Metric Selection:** Applied appropriate incidence vs. prevalence metrics based on disease characteristics
3. **Confidence Scoring:** Evaluated based on:
   - Source quality and verifiability (40% weight)
   - Metric appropriateness (30% weight)
   - Concept coherence (20% weight)
   - Data quality and availability (10% weight)
4. **Hierarchy Detection:** Identified parent-child disease relationships where applicable
5. **Geographic Variation:** Documented regional variation in incidence rates

### Data Year Prioritization
- Prioritized 2005-specific data where available (per skill guidelines for pharmaceutical patent analysis)
- Used best available estimates from proximal years when 2005 data unavailable

## Key Findings

1. **Best Data Quality:** Carcinoma of unknown primary has the strongest epidemiological foundation with cancer registry data (confidence 0.78)

2. **Rare Diseases:** Odontogenic myxofibroma (0.007/100k) and D-Glyceric aciduria present significant epidemiological challenges due to extreme rarity

3. **Disease Specificity:** Self-induced vomiting and Radiation angiosarcoma are subtypes of broader disease categories, requiring parent disease context

4. **Data Availability:** Two extreme rare conditions (C1377940, C0342765) have insufficient population-based data, reflected in lower confidence scores

## Usage Notes

- All incidence rates reported as per 100,000 person-years unless otherwise specified
- Confidence scores reflect overall reliability including source quality, metric appropriateness, and data availability
- Null values used consistently (no "N/A" or "Not provided" strings)
- Source URLs are exact, verifiable links where available
- Geographic variation documented for conditions with significant regional differences

## Related Files

- `PROCESSING_SUMMARY_5DISEASES.txt` - Summary statistics and processing notes
- `RESULTS_SUMMARY_JSON.json` - Aggregate JSON summary of all results

## References

Full source citations included in individual JSON files under "source" field with verification URLs where available.
