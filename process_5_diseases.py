import json
import os

# Process 5 diseases according to cui-incidence-mapper_2 skill specifications
diseases_data = [
    {
        "cui": "C0920299",
        "cui_name": "Overriding toe",
        "incidence_per_100k": "extremely rare",
        "prevalence_per_100k": None,
        "metric_type": "incidence",
        "total_cases_per_year": "extremely rare",
        "confidence": 0.2,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Overriding toe is a rare congenital foot anomaly. <0.01 per 100k births based on podiatric case reports. No systematic epidemiological studies available.",
        "data_quality": "weak",
        "geographic_variation": "unknown",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    },
    {
        "cui": "C3888924",
        "cui_name": "Glycogen storage disease due to acid maltase deficiency, infantile onset",
        "incidence_per_100k": "extremely rare",
        "prevalence_per_100k": None,
        "metric_type": "prevalence",
        "total_cases_per_year": "extremely rare",
        "confidence": 0.4,
        "is_subtype": True,
        "parent_disease": "Glycogen Storage Diseases",
        "reasoning": "Infantile-onset Pompe disease (glycogen storage disease type II) is extremely rare. Estimated 1 in 40,000 births globally, approximately 0.0025 per 100k. Using prevalence as appropriate for chronic genetic condition.",
        "data_quality": "weak",
        "geographic_variation": "low",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    },
    {
        "cui": "C1300585",
        "cui_name": "Small cell carcinoma of prostate",
        "incidence_per_100k": "extremely rare",
        "prevalence_per_100k": None,
        "metric_type": "incidence",
        "total_cases_per_year": "extremely rare",
        "confidence": 0.3,
        "is_subtype": True,
        "parent_disease": "Prostate Cancer",
        "reasoning": "Small cell carcinoma of prostate is extremely rare histological variant, comprising <1% of all prostate cancers. <0.01 per 100k estimated from cancer registry case reports.",
        "data_quality": "weak",
        "geographic_variation": "unknown",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    },
    {
        "cui": "C0175691",
        "cui_name": "Dubowitz syndrome",
        "incidence_per_100k": "extremely rare",
        "prevalence_per_100k": None,
        "metric_type": "prevalence",
        "total_cases_per_year": "extremely rare",
        "confidence": 0.25,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Dubowitz syndrome is a rare autosomal recessive disorder with developmental delays and microcephaly. Estimated prevalence <0.1 per 100k based on <200 documented cases worldwide.",
        "data_quality": "weak",
        "geographic_variation": "unknown",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    },
    {
        "cui": "C0347915",
        "cui_name": "Congenital malformation syndromes associated with short stature",
        "incidence_per_100k": None,
        "prevalence_per_100k": None,
        "metric_type": None,
        "total_cases_per_year": None,
        "confidence": 0.0,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Umbrella term too heterogeneous to estimate. Includes diverse genetic syndromes (Russel-Silver, Turner, achondroplasia, etc.) with vastly different incidence/prevalence rates. Would require specification of individual syndrome for meaningful epidemiological data.",
        "data_quality": "none",
        "geographic_variation": "unknown",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    }
]

# Save each result to output/results/{CUI}.json
output_dir = "/home/user/cui_disease_incidence_processing/output/results"
for disease in diseases_data:
    cui = disease["cui"]
    filename = f"{output_dir}/{cui}.json"
    with open(filename, 'w') as f:
        json.dump(disease, f, indent=2)
    print(f"Saved: {filename}")

# Also save the complete batch as an array
batch_filename = f"{output_dir}/batch_results_5_diseases.json"
with open(batch_filename, 'w') as f:
    json.dump(diseases_data, f, indent=2)
print(f"\nBatch results saved to: {batch_filename}")

# Print summary
print(f"\nProcessed {len(diseases_data)} diseases:")
for d in diseases_data:
    print(f"  {d['cui']}: {d['cui_name']} (confidence: {d['confidence']})")
