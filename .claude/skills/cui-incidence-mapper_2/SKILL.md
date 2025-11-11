---
name: cui-incidence-mapper
description: Maps UMLS CUI disease codes to global incidence rates with confidence scores and hierarchy detection. For pharmaceutical patent analysis requiring epidemiological data. Flags unmappable umbrella terms and identifies disease subtypes.
---

# CUI Incidence Mapper

Maps UMLS CUIs to global disease incidence rates (per 100k person-years) with confidence scoring and hierarchy detection.

## When to Use

- Converting UMLS CUIs from pharmaceutical patents to incidence rates
- Identifying disease hierarchies (specific subtypes vs umbrella terms)
- Quality-checking disease incidence estimates

## Input Format

**BATCH MODE (5 diseases):**
```json
{
  "diseases": [
    {"cui": "C0030354", "name": "Papilloma"},
    {"cui": "C0334533", "name": "Intraductal papilloma of breast"},
    {"cui": "C0011849", "name": "Diabetes Mellitus"},
    {"cui": "C0018099", "name": "Gout"},
    {"cui": "C0006142", "name": "Malignant neoplasm of breast"}
  ]
}
```

Process all 5 diseases and return an array of 5 results.

## Output Format

**CRITICAL: Return ONLY valid JSON array. No additional text, no markdown formatting, no explanations outside the JSON structure.**

For batch input of 5 diseases, return an array of 5 results:

```json
[
  {
    "cui": "C0030354",
    "cui_name": "Papilloma",
    "incidence_per_100k": null,
    "prevalence_per_100k": null,
    "metric_type": null,
    "total_cases_per_year": null,
    "confidence": 0.0,
    "is_subtype": false,
    "parent_disease": null,
    "reasoning": "Umbrella term covering 25+ distinct papilloma types with vastly different incidence rates.",
    "data_quality": "none",
    "geographic_variation": "high",
    "year_specific": false,
    "data_year": null,
    "source": null,
    "source_url": null,
    "source_type": null
  },
  {
    "cui": "C0011849",
    "cui_name": "Diabetes Mellitus",
    "incidence_per_100k": 16.5,
    "prevalence_per_100k": null,
    "metric_type": "incidence",
    "total_cases_per_year": 1320000,
    "confidence": 0.8,
    "is_subtype": false,
    "parent_disease": null,
    "reasoning": "Reporting incidence (new diagnoses). Global diabetes incidence from IDF 2005: ~16.5 per 100k person-years.",
    "data_quality": "strong",
    "geographic_variation": "moderate",
    "year_specific": true,
    "data_year": 2005,
    "source": "IDF Diabetes Atlas 2005",
    "source_url": "https://diabetesatlas.org/atlas/2005/",
    "source_type": "registry"
  }
]
```

**Never include:**
- Markdown code blocks (no ```json or ```)
- Explanatory text before or after the JSON array
- Additional fields not specified above
- Phrases like "Not provided" or "N/A" - use null instead

### Fields

- **incidence_per_100k**: Number, "extremely rare", or null - NEW CASES per 100k person-years (single point estimate only - no ranges). Use null if incidence data doesn't exist for this condition.
- **prevalence_per_100k**: Number or null - EXISTING CASES per 100k population at a point in time. Use this for chronic conditions like obesity, diabetes prevalence, etc. where incidence isn't the primary metric.
- **metric_type**: "incidence" | "prevalence" | "both" | null - Which metric(s) are reported. Use "prevalence" for chronic conditions where incidence isn't well-defined.
- **total_cases_per_year**: Estimated global cases per year (for incidence: incidence_per_100k × 80000; for prevalence: prevalence_per_100k × 80000), or null
- **confidence**: 0.0 (unmappable) to 1.0 (certain) - **CRITICAL: This reflects OVERALL quality including: (1) source quality and verifiability, (2) appropriateness of metric for this condition, (3) concept coherence (is this a well-defined disease?), (4) data availability**
- **is_subtype**: Boolean - is this a specific subtype?
- **parent_disease**: Name of broader category (if applicable)
- **reasoning**: 1-2 sentence explanation including which metric was used and why
- **data_quality**: strong/moderate/weak/none
- **geographic_variation**: low/moderate/high/unknown
- **year_specific**: Boolean - true if data is specifically from 2005, false if general/other year
- **data_year**: Number or null - the specific year data is from (2005 preferred, or actual year found)
- **source**: String or null - **EXACT citation with full details**. For literature: "Author et al. (Year). Title. Journal. Volume:Pages". For registries: "Database Name, Organization (Year)". **USE NULL if no verifiable source found - DO NOT FABRICATE**
- **source_url**: String or null - **EXACT, DIRECT URL to the data**. Must be verifiable. **USE NULL if you cannot provide an exact link - DO NOT GUESS OR FABRICATE URLS**
- **source_type**: "registry" | "literature" | "estimate" | null - Type of source (registry=cancer/disease registries, literature=peer-reviewed studies, estimate=BOTEC calculations)

## Source Quality Standards

**CRITICAL RULES:**
1. **NO FABRICATION**: If you cannot find a verifiable source with an exact URL, use `source: null` and `source_url: null`. This is REQUIRED and ACCEPTABLE.
2. **EXACT URLS ONLY**: source_url must be a direct, clickable link to the actual data/paper. Generic homepage URLs are NOT acceptable.
3. **NO GUESSING**: If you're not certain where data came from, use null. Lower confidence accordingly.
4. **Confidence reflects EVERYTHING**: Source quality + metric appropriateness + concept coherence + data availability

**Source quality directly impacts confidence scoring. Low-quality OR missing sources MUST result in lower confidence scores.**

### Tier 1 Sources (Required for confidence ≥ 0.7)

**Cancer Registries:**
- GLOBOCAN (IARC) - https://gco.iarc.fr/
- SEER (Surveillance, Epidemiology, and End Results Program) - https://seer.cancer.gov/
- IARC (International Agency for Research on Cancer) - https://www.iarc.who.int/
- National cancer registries with published methodology

**Government Health Agencies:**
- WHO (World Health Organization) reports and databases
- CDC (Centers for Disease Control and Prevention)
- National health ministries with surveillance data
- Government epidemiological bulletins

**Peer-Reviewed Literature:**
- MUST provide exact citation: "Author et al. (Year). Title. Journal. Volume:Pages"
- MUST be from indexed medical journals (PubMed, Scopus, Web of Science)
- Examples:
  - "Smith J et al. (2005). Global incidence of hepatocellular carcinoma. Lancet Oncol. 6(8):621-630"
  - "Jones A et al. (2004). Epidemiology of systemic lupus erythematosus. Arthritis Rheum. 50(2):345-353"

### Tier 2 Sources (Max confidence = 0.6)

**Regional/Hospital Registries:**
- Hospital-based registries with defined catchment populations
- Regional disease surveillance systems
- State or provincial health department data

**Medical Textbooks/Reviews:**
- MUST cite primary data sources
- Example: "Harrison's Principles of Internal Medicine (2005), citing WHO 2003 data"

**Professional Society Guidelines:**
- MUST reference primary epidemiological studies
- Example: "American Diabetes Association Clinical Guidelines (2005), based on IDF 2004 study"

### Tier 3 Sources (Max confidence = 0.4)

**Advocacy Organizations (if citing primary sources):**
- ONLY acceptable if they cite peer-reviewed studies or government data
- MUST verify the primary source and cite it directly
- Example: If an advocacy site cites "WHO 2005", go verify the WHO source and cite that instead

**Secondary Literature:**
- Review articles without primary data collection
- Older epidemiological studies (pre-2000 for 2005 target data)

### Unacceptable Sources (Must significantly reduce confidence to ≤ 0.3)

❌ **Commercial/Product-Selling Sites:**
- Health product vendors (supplement sellers, device manufacturers, diagnostic companies)
- Sites with "buy now" or "shop" buttons related to the disease
- Patient marketplaces or commercial health portals
- Example: Sites selling "iron detectors" for hemochromatosis, vitamin supplements, etc.

❌ **General Health Information Sites Without Methodology:**
- WebMD, Healthline, MayoClinic patient information pages (unless citing specific studies)
- Wikipedia (use the cited sources instead)
- Health blogs or news aggregators

❌ **Uncited or Vague Sources:**
- "Medical literature" without specific citation
- "Studies show" without naming the studies
- Organizational websites without methodology

### Source Quality Rules

1. **Always prefer primary sources over secondary sources**
   - If an advocacy site cites "Lancet 2005", find and cite the Lancet article directly
   - Never cite a website that's merely summarizing other work

2. **For Tier 1 confidence (≥0.7), you MUST have:**
   - Exact citation (journal article with author/year/volume/pages, OR)
   - Official registry data (GLOBOCAN, WHO, CDC) with specific report/year

3. **For literature sources, include:**
   - Full citation in `source` field
   - DOI or PubMed URL in `source_url` field (if available)
   - `source_type: "literature"`

4. **If best available source is Tier 2/3:**
   - Lower confidence accordingly (see max confidence limits above)
   - Explain in reasoning: "Limited to [source type], confidence capped at [score]"

5. **Commercial/advocacy sites:**
   - If it's selling products related to the disease: confidence ≤ 0.3
   - If methodology is unclear: confidence ≤ 0.4
   - Always try to find the original source they're citing

### Examples of Proper Source Citations

**Good - Tier 1 Registry:**
```json
{
  "source": "GLOBOCAN 2005 (IARC)",
  "source_url": "https://gco.iarc.fr/",
  "source_type": "registry",
  "confidence": 0.88
}
```

**Good - Tier 1 Peer-Reviewed:**
```json
{
  "source": "Parkin DM et al. (2005). Global cancer statistics, 2002. CA Cancer J Clin. 55(2):74-108",
  "source_url": "https://pubmed.ncbi.nlm.nih.gov/15761078/",
  "source_type": "literature",
  "confidence": 0.85
}
```

**Acceptable - Tier 2:**
```json
{
  "source": "Regional hospital registry data (2000-2005) from Johns Hopkins",
  "source_url": null,
  "source_type": "registry",
  "confidence": 0.55,
  "reasoning": "Limited to regional hospital data, not population-based; confidence capped at 0.55"
}
```

**Poor - Must Lower Confidence:**
```json
{
  "source": "American Hemochromatosis Society",
  "source_url": "https://www.americanhemochromatosis.org/",
  "source_type": "literature",
  "confidence": 0.68
}
```
❌ WRONG - This is an advocacy/commercial site. Should be ≤0.3 confidence unless it cites primary sources that you verify.

**Corrected Version:**
```json
{
  "source": "Adams PC et al. (2005). Hemochromatosis and iron-overload screening in a racially diverse population. N Engl J Med. 352:1769-78",
  "source_url": "https://pubmed.ncbi.nlm.nih.gov/15858186/",
  "source_type": "literature",
  "confidence": 0.72,
  "reasoning": "Population-based screening study from peer-reviewed literature; moderate confidence due to limited geographic scope"
}
```

## Confidence Scoring

**Confidence reflects the OVERALL reliability of the entire data point, considering ALL of these factors:**

1. **Source Quality & Verifiability** (40% weight)
   - Is there an exact, verifiable source with URL?
   - Is it from a Tier 1 source (registry, peer-reviewed literature)?
   - Can the data be independently verified?

2. **Metric Appropriateness** (30% weight)
   - Is the reported metric (incidence vs prevalence) appropriate for this condition?
   - For acute/incident diseases: use incidence
   - For chronic conditions: prefer prevalence
   - Deduct confidence if forcing wrong metric

3. **Concept Coherence** (20% weight)
   - Is this a well-defined, specific disease entity?
   - Or is it an umbrella term, process descriptor, or vague category?

4. **Data Quality & Availability** (10% weight)
   - How robust is the underlying epidemiological data?
   - Geographic coverage, sample size, methodology

| Score | Criteria | Example |
|-------|----------|---------|
| 0.9-1.0 | Tier 1 source + exact URL + appropriate metric + well-defined disease | Breast cancer incidence from GLOBOCAN with exact link |
| 0.7-0.8 | Tier 1 source + appropriate metric BUT generic URL or minor issues | Diabetes incidence from IDF but only homepage URL |
| 0.5-0.6 | Tier 2 source OR appropriate metric but weak source | Regional registry data, or prevalence for rare condition |
| 0.3-0.4 | No verifiable source OR inappropriate metric OR vague concept | Estimate from case reports, or "incidence" for chronic condition |
| 0.2-0.3 | **Aggregate umbrella estimate** - BOTEC sum of subcategories | "Respiration Disorders" (sum of major respiratory conditions) |
| 0.1-0.2 | Multiple major issues: no source + vague concept + wrong metric | Wild guess for poorly-defined umbrella term |
| 0.0 | **Unmappable** - too broad/generic to estimate meaningfully | "Disease", "Disorder", overly generic terms |

**Key principles:**
- **Be conservative**: If uncertain, lower confidence and explain why
- **No source is OK**: Use null and reduce confidence rather than fabricating
- **Wrong metric = lower confidence**: Don't report incidence when only prevalence exists

## Incidence vs Prevalence: Which Metric to Use

**CRITICAL: Use the appropriate metric for each condition. Using the wrong metric reduces confidence.**

### Use INCIDENCE (new cases per 100k person-years) for:
- **Acute diseases**: Infections, acute injuries, acute events
- **Cancers**: Most cancers are reported as incidence
- **Incident conditions with clear onset**: Heart attacks, strokes, new diabetes diagnoses
- **Conditions with a diagnosis date**: When there's a clear "became a case" moment

Examples: Breast cancer, myocardial infarction, influenza, acute leukemia

### Use PREVALENCE (existing cases per 100k population) for:
- **Chronic conditions**: Obesity, hypertension, chronic diseases
- **Lifelong conditions**: Most genetic disorders, developmental disabilities
- **Conditions where incidence is poorly defined**: Mental health conditions, chronic pain
- **When only prevalence data exists in literature**: Even if incidence might theoretically exist

Examples: Obesity, autism spectrum disorder, chronic kidney disease, schizophrenia prevalence

### Use BOTH when:
- The condition has both well-documented incidence AND prevalence data
- Example: Diabetes (incidence of new diagnoses + prevalence of all diabetics)

### When In Doubt:
1. Check what the epidemiological literature primarily reports for this condition
2. If literature uses prevalence, report prevalence (don't fabricate incidence)
3. Explain in reasoning which metric you used and why
4. Reduce confidence if you had to use a suboptimal metric

## Hierarchy Detection

### Subtype Indicators (is_subtype = true)

- **Anatomical specificity**: "Intraductal papilloma of breast" vs "Papilloma"
- **Histological**: "Ductal carcinoma in situ" vs "Carcinoma in situ"
- **Genetic**: "Spastic paraplegia 4" vs "Spastic paraplegia"
- **Age**: "Juvenile psoriatic arthritis" vs "Psoriatic arthritis"
- **Severity**: "Severe aplastic anemia" vs "Aplastic anemia"

### Umbrella Terms

#### Aggregate Umbrella Terms (confidence = 0.2-0.3)

For umbrella terms where you CAN estimate the aggregate incidence by summing major subcategories:

**When to provide aggregate estimates:**
- The umbrella term has a finite, identifiable set of major subcategories
- You can reasonably estimate or find data for the main subcategories
- The estimate is useful for pharmaceutical market sizing

**Examples:**
- "Respiration Disorders" → Sum of asthma, COPD, pneumonia, bronchitis, URI
- "Intestinal infectious disease" → Sum of viral, bacterial, and parasitic GI infections
- "Cardiovascular Disease" → Sum of MI, stroke, heart failure, arrhythmias

**How to handle:**
1. Identify the 5-10 major subcategories that comprise the umbrella term
2. Estimate incidence for each major subcategory
3. Sum the subcategories to get aggregate estimate
4. Set confidence to 0.2-0.3 (low but not zero)
5. In reasoning, explain: "Aggregate BOTEC estimate summing: [list major categories]"
6. Set data_quality to "weak" (since it's a composite)

#### Unmappable Umbrella Terms (confidence = 0.0)

For umbrella terms that are TOO broad to estimate:

- Generic pathology: "Neoplasm", "Carcinoma", "Sarcoma" (without organ specification)
- Overly broad: "Disease", "Disorder", "Syndrome"
- Vague compound terms: "and/or" diseases without clear boundaries

## Estimation Guidelines

**CRITICAL: Always provide a single point estimate - never use ranges like "range: X-Y".**

**TARGET YEAR: 2005**
- **PRIORITIZE finding 2005-specific incidence data** from registries, WHO reports, or epidemiological studies
- If 2005 data is available, set `year_specific: true` and `data_year: 2005`
- If 2005 data is NOT available, use the best available estimate from any year
  - Set `year_specific: false`
  - Set `data_year` to the actual year of the data (if known) or null
  - Note in reasoning if using data from a different year
- Common sources for 2005 data: GLOBOCAN 2005, WHO 2005 reports, cancer registry data circa 2005

For diseases with geographic variation, provide a global average or median and note the variation in the `geographic_variation` field and `reasoning`.

### When You Have Strong Data (2005-specific)
```json
{
  "incidence_per_100k": 15.2,
  "total_cases_per_year": 1216000,
  "confidence": 0.9,
  "data_quality": "strong",
  "reasoning": "Type 2 diabetes incidence from IDF 2005 report: ~15 per 100k globally.",
  "year_specific": true,
  "data_year": 2005
}
```

### When 2005 Data Not Available
```json
{
  "incidence_per_100k": 18.5,
  "total_cases_per_year": 1480000,
  "confidence": 0.85,
  "data_quality": "strong",
  "reasoning": "No 2005-specific data available. Using 2010 WHO estimate of ~18.5 per 100k.",
  "year_specific": false,
  "data_year": 2010
}
```

### Geographic Variation

When incidence varies significantly by region, provide a global average and note the variation:

```json
{
  "incidence_per_100k": 12.0,
  "total_cases_per_year": 960000,
  "confidence": 0.8,
  "geographic_variation": "high",
  "reasoning": "HCC global average ~12 per 100k from GLOBOCAN 2005, varies from <2 in North America to >25 in East Asia due to HBV/HCV.",
  "year_specific": true,
  "data_year": 2005
}
```

### Extremely Rare
```json
{
  "incidence_per_100k": "extremely rare",
  "total_cases_per_year": "extremely rare",
  "confidence": 0.3,
  "reasoning": "Tetraphocomelia: <0.01 per 100k births based on case reports.",
  "year_specific": false,
  "data_year": null
}
```

### Aggregate Umbrella Term (BOTEC Estimate)
```json
{
  "incidence_per_100k": 15000,
  "total_cases_per_year": 1200000000,
  "confidence": 0.25,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Aggregate BOTEC estimate summing major respiratory conditions: asthma (1500), COPD (400), pneumonia (5000), acute bronchitis (3000), URI (5000+) = ~15,000 per 100k. Low confidence due to heterogeneity and overlap between categories.",
  "data_quality": "weak",
  "geographic_variation": "high",
  "year_specific": false,
  "data_year": null
}
```

### Unmappable (Too Broad)
```json
{
  "incidence_per_100k": null,
  "total_cases_per_year": null,
  "confidence": 0.0,
  "reasoning": "Umbrella term too broad and generic to estimate meaningfully. Would require specification of organ system or disease type.",
  "data_quality": "none",
  "geographic_variation": "unknown",
  "year_specific": false,
  "data_year": null
}
```

## Data Quality Assessment

- **strong**: Cancer registries, WHO/CDC surveillance, large cohort studies
- **moderate**: Published cohorts, hospital registries, regional databases
- **weak**: Case reports, single-center studies, expert estimates
- **none**: No data, umbrella terms, theoretical conditions

## Processing Workflow

### Single Disease
1. Assess specificity - mappable or umbrella term?
2. Search knowledge for epidemiological data
3. Estimate incidence with appropriate unit
4. Assign confidence based on data quality
5. Check hierarchy - subtype? parent?
6. Format as JSON
7. Validate medical plausibility

### Batch Processing

For CSV files:
1. Process each CUI individually
2. Work in chunks (100-500)
3. Save checkpoints every 100
4. Track progress
5. Flag confidence < 0.3 for review
6. Output results CSV + summary statistics

## Quality Checks

**JSON formatting:**
- Must be valid JSON (no markdown, no extra text)
- All required fields present
- Use null for missing values, never "Not provided" or "N/A"

**Sanity checks:**
- Incidence < 100,000 per 100k (except extremely common conditions like URI)
- Rare diseases: low confidence unless strong data
- Common diseases: high confidence
- Aggregate umbrella terms: confidence = 0.2-0.3
- Unmappable umbrella terms: confidence = 0.0

**Logical consistency:**
- If is_subtype = true, parent_disease ≠ null
- If confidence = 0.0, incidence_per_100k = null
- If confidence = 0.2-0.3 (aggregate), data_quality should be "weak"
- If data_quality = "none", confidence must be 0.0

**Medical plausibility:**
- Congenital anomalies: < 10 per 100k
- Common cancers: 10-50 per 100k
- Diabetes: 10-20 per 100k

## Example Outputs

### Acute Disease with Incidence
```json
{
  "cui": "C0011849",
  "cui_name": "Diabetes Mellitus Type 2",
  "incidence_per_100k": 15.2,
  "prevalence_per_100k": null,
  "metric_type": "incidence",
  "total_cases_per_year": 1216000,
  "confidence": 0.88,
  "is_subtype": true,
  "parent_disease": "Diabetes Mellitus",
  "reasoning": "Reporting incidence (new diagnoses) at ~15 per 100k person-years based on IDF 2005 data.",
  "data_quality": "strong",
  "geographic_variation": "moderate",
  "year_specific": true,
  "data_year": 2005,
  "source": "IDF Diabetes Atlas 2005",
  "source_url": "https://diabetesatlas.org/atlas/2005/",
  "source_type": "registry"
}
```

### Chronic Condition with Prevalence
```json
{
  "cui": "C0028754",
  "cui_name": "Obesity",
  "incidence_per_100k": null,
  "prevalence_per_100k": 9800,
  "metric_type": "prevalence",
  "total_cases_per_year": 784000000,
  "confidence": 0.82,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Obesity measured as prevalence, not incidence. WHO 2005 data shows 9.8% of global adults obese (9,800 per 100k).",
  "data_quality": "strong",
  "geographic_variation": "high",
  "year_specific": true,
  "data_year": 2005,
  "source": "Kelly T et al. (2008). Global burden of obesity in 2005 and projections to 2030. Int J Obes. 32:1431-1437",
  "source_url": "https://pubmed.ncbi.nlm.nih.gov/18607383/",
  "source_type": "literature"
}
```

### No Verifiable Source Found
```json
{
  "cui": "C0012345",
  "cui_name": "Rare Syndrome XYZ",
  "incidence_per_100k": 0.5,
  "prevalence_per_100k": null,
  "metric_type": "incidence",
  "total_cases_per_year": 40000,
  "confidence": 0.35,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Estimated ~0.5 per 100k based on case report frequency, but no systematic epidemiological studies found.",
  "data_quality": "weak",
  "geographic_variation": "unknown",
  "year_specific": false,
  "data_year": null,
  "source": null,
  "source_url": null,
  "source_type": null
}
```

### Rare Syndrome
```json
{
  "cui": "C1865872",
  "cui_name": "Acromesomelic Dysplasia, Maroteaux Type",
  "incidence_per_100k": "extremely rare",
  "total_cases_per_year": "extremely rare",
  "confidence": 0.3,
  "is_subtype": true,
  "parent_disease": "Skeletal Dysplasia",
  "reasoning": "Extremely rare skeletal dysplasia, <100 cases worldwide, <0.01 per 100k births.",
  "data_quality": "weak",
  "geographic_variation": "unknown"
}
```

### Aggregate Umbrella Term
```json
{
  "cui": "C0035204",
  "cui_name": "Respiration Disorders",
  "incidence_per_100k": 15000,
  "total_cases_per_year": 1200000000,
  "confidence": 0.25,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Aggregate BOTEC summing major respiratory conditions: asthma (~1500), COPD (~400), pneumonia (~5000), acute bronchitis (~3000), URI (~5000+). Total ~15,000 per 100k. Heterogeneous conditions with significant overlap.",
  "data_quality": "weak",
  "geographic_variation": "high"
}
```

### Unmappable Umbrella Term
```json
{
  "cui": "C0023903",
  "cui_name": "Liver and Intrahepatic Bile Duct Neoplasm",
  "incidence_per_100k": null,
  "total_cases_per_year": null,
  "confidence": 0.0,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Umbrella term too heterogeneous: includes benign (hemangiomas) and malignant (HCC, cholangiocarcinoma) tumors with vastly different incidence rates and clinical significance. Aggregate estimate not meaningful.",
  "data_quality": "none",
  "geographic_variation": "high"
}
```

### Geographic Variation
```json
{
  "cui": "C0019151",
  "cui_name": "Hepatocellular Carcinoma",
  "incidence_per_100k": 12.0,
  "total_cases_per_year": 960000,
  "confidence": 0.85,
  "is_subtype": true,
  "parent_disease": "Liver Cancer",
  "reasoning": "HCC global average ~12 per 100k, but varies dramatically from <2 in North America/Europe to >25 in East Asia due to HBV/HCV.",
  "data_quality": "strong",
  "geographic_variation": "high"
}
```

### Multi-System Syndrome
```json
{
  "cui": "C0036391",
  "cui_name": "Schwartz-Jampel Syndrome",
  "incidence_per_100k": "extremely rare",
  "total_cases_per_year": "extremely rare",
  "confidence": 0.3,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Rare genetic disorder with skeletal dysplasia and myotonia, <0.1 per 100k based on case frequency.",
  "data_quality": "weak",
  "geographic_variation": "unknown"
}
```

### Compound Condition
```json
{
  "cui": "C3495801",
  "cui_name": "Juvenile Psoriatic Arthritis",
  "incidence_per_100k": 1.0,
  "total_cases_per_year": 80000,
  "confidence": 0.5,
  "is_subtype": true,
  "parent_disease": "Psoriatic Arthritis",
  "reasoning": "Juvenile-onset psoriatic arthritis, estimated ~1 per 100k children (pediatric rheumatology studies).",
  "data_quality": "moderate",
  "geographic_variation": "low"
}
```

## Common Pitfalls

❌ **Don't:**
- Give high confidence to aggregate umbrella estimates (max 0.3)
- Use aggregate estimates for overly broad terms like "Disease" or "Disorder"
- Give overconfident estimates for rare diseases
- Ignore geographic variation
- Confuse prevalence with incidence (always report NEW cases/year)
- Miss parent-child relationships

✅ **Do:**
- Try aggregate BOTEC estimates for umbrella terms with identifiable subcategories
- Use confidence 0.2-0.3 for aggregate estimates
- Lower confidence when uncertain
- Flag truly unmappable terms with confidence 0.0
- Explain reasoning clearly (list subcategories for aggregates)
- Note data quality limitations

## Batch Output Format

For large datasets, create:

**1. Results CSV**
```csv
cui,cui_name,incidence_per_100k,total_cases_per_year,confidence,is_subtype,parent_disease,reasoning,data_quality,geographic_variation
```

**2. Summary Statistics JSON**
```json
{
  "total_processed": 15000,
  "confidence_distribution": {
    "high (0.7-1.0)": 6500,
    "medium (0.3-0.7)": 5000,
    "low (0.1-0.3)": 2000,
    "unmappable (0.0)": 1500
  },
  "subtypes_identified": 8500,
  "review_needed": 2000
}
```

**3. Review Queue CSV**
All entries with confidence < 0.3

**4. Hierarchy Map JSON**
```json
{
  "Papilloma": ["Intraductal papilloma of breast", "Urothelial papilloma"],
  "Diabetes Mellitus": ["Type 1", "Type 2"]
}
```

## Validation Benchmarks

Check estimates against known values:

| Disease | Expected Incidence | Expected Confidence |
|---------|-------------------|---------------------|
| Type 2 Diabetes | 12-18 per 100k | >0.9 |
| Breast Cancer | 40-50 per 100k (women) | >0.9 |
| Lung Cancer | 15-25 per 100k | >0.8 |
| Multiple Sclerosis | 2-10 per 100k | 0.7-0.9 |
| Huntington's Disease | 0.5-1 per 100k | 0.6-0.8 |

## Notes

- **Incidence vs Prevalence**: Always report incidence (NEW cases per year), not prevalence (total existing cases)
- **Unit**: Per 100,000 person-years is standard
- **Geographic variation**: Document when incidence varies >2-fold by region
- **Umbrella detection**: Critical for data quality - flag aggressively
- **Conservative approach**: Lower confidence is better than false precision
