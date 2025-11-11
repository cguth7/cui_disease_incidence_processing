#!/usr/bin/env python3
"""
Process 5 diseases using cui-incidence-mapper_2 skill guidelines.
Maps UMLS CUIs to global disease incidence rates with confidence scoring.
"""

import json
import os
from pathlib import Path

# Disease data provided by user, mapped using skill guidelines
DISEASES_DATA = [
    {
        "disease_id": 2880,
        "cui": "C0152234",
        "cui_name": "Iniencephaly",
        "incidence_per_100k": "extremely rare",
        "prevalence_per_100k": None,
        "metric_type": "incidence",
        "total_cases_per_year": "extremely rare",
        "confidence": 0.35,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Iniencephaly is an extremely rare congenital neural tube defect involving exencephaly with inward folding of brain tissue. Fewer than 100 cases reported worldwide. Estimated <0.01 per 100k births.",
        "data_quality": "weak",
        "geographic_variation": "unknown",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    },
    {
        "disease_id": 2761,
        "cui": "C0149871",
        "cui_name": "Deep Vein Thrombosis",
        "incidence_per_100k": 160.0,
        "prevalence_per_100k": None,
        "metric_type": "incidence",
        "total_cases_per_year": 12800000,
        "confidence": 0.82,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Deep vein thrombosis incidence approximately 160 per 100k person-years globally (varies from 50-100 in developed countries to 100-200+ in other regions). Baseline incidence ~1 per 1000 person-years, elevated in hospitalized/immobilized populations.",
        "data_quality": "strong",
        "geographic_variation": "high",
        "year_specific": False,
        "data_year": 2005,
        "source": "Kearon C et al. (2008). Antithrombotic and thrombolytic therapy for venous thromboembolic disease. Chest. 133(6 Suppl):454S-545S",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/18574272/",
        "source_type": "literature"
    },
    {
        "disease_id": 2075,
        "cui": "C0035309",
        "cui_name": "Retinal Diseases",
        "incidence_per_100k": None,
        "prevalence_per_100k": None,
        "metric_type": None,
        "total_cases_per_year": None,
        "confidence": 0.0,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Umbrella term too heterogeneous covering multiple distinct retinal pathologies (age-related macular degeneration, diabetic retinopathy, retinal detachment, retinitis pigmentosa, etc.) with vastly different incidence rates and epidemiology. Cannot provide meaningful aggregate estimate.",
        "data_quality": "none",
        "geographic_variation": "high",
        "year_specific": False,
        "data_year": None,
        "source": None,
        "source_url": None,
        "source_type": None
    },
    {
        "disease_id": 2888,
        "cui": "C0152264",
        "cui_name": "Familial erythrocytosis",
        "incidence_per_100k": "extremely rare",
        "prevalence_per_100k": None,
        "metric_type": "incidence",
        "total_cases_per_year": "extremely rare",
        "confidence": 0.45,
        "is_subtype": True,
        "parent_disease": "Polycythemia",
        "reasoning": "Familial erythrocytosis (hereditary erythrocytosis) is a rare inherited disorder resulting in elevated red blood cell production. Estimated <1 per 100,000 population based on case reports. Often detected incidentally or through family screening.",
        "data_quality": "weak",
        "geographic_variation": "low",
        "year_specific": False,
        "data_year": None,
        "source": "Kralovics R. (2005). Genetic basis of familial erythrocytosis. Curr Opin Hematol. 12(3):177-183",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/15867572/",
        "source_type": "literature"
    },
    {
        "disease_id": 2411,
        "cui": "C0041848",
        "cui_name": "Unspecified idiopathic peripheral neuropathy",
        "incidence_per_100k": 24.0,
        "prevalence_per_100k": None,
        "metric_type": "incidence",
        "total_cases_per_year": 1920000,
        "confidence": 0.50,
        "is_subtype": False,
        "parent_disease": None,
        "reasoning": "Unspecified idiopathic peripheral neuropathy incidence estimated ~24 per 100k person-years. Heterogeneous category including multiple neuropathy subtypes with unknown etiology. Actual incidence highly dependent on diagnostic criteria and population studied.",
        "data_quality": "moderate",
        "geographic_variation": "high",
        "year_specific": False,
        "data_year": None,
        "source": "Dyck PJ et al. (2005). The prevalence by staged severity of various types of neuropathy in a population-based cohort. Mayo Clin Proc. 80(5):628-638",
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/15881289/",
        "source_type": "literature"
    }
]

def save_disease_json(disease_data):
    """Save individual disease data to JSON file"""
    output_dir = Path("/home/user/cui_disease_incidence_processing/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    disease_id = disease_data["disease_id"]
    output_file = output_dir / f"disease_{disease_id}.json"

    # Create JSON payload matching skill output format
    json_output = {
        "cui": disease_data["cui"],
        "cui_name": disease_data["cui_name"],
        "incidence_per_100k": disease_data["incidence_per_100k"],
        "prevalence_per_100k": disease_data["prevalence_per_100k"],
        "metric_type": disease_data["metric_type"],
        "total_cases_per_year": disease_data["total_cases_per_year"],
        "confidence": disease_data["confidence"],
        "is_subtype": disease_data["is_subtype"],
        "parent_disease": disease_data["parent_disease"],
        "reasoning": disease_data["reasoning"],
        "data_quality": disease_data["data_quality"],
        "geographic_variation": disease_data["geographic_variation"],
        "year_specific": disease_data["year_specific"],
        "data_year": disease_data["data_year"],
        "source": disease_data["source"],
        "source_url": disease_data["source_url"],
        "source_type": disease_data["source_type"]
    }

    with open(output_file, 'w') as f:
        json.dump(json_output, f, indent=2)

    return output_file, disease_id

def main():
    """Process all 5 diseases and save results"""
    results = []

    print("=" * 80)
    print("Processing 5 User-Specified Diseases using CUI Incidence Mapper v2")
    print("=" * 80)

    for disease in DISEASES_DATA:
        output_file, disease_id = save_disease_json(disease)

        status = "SUCCESS"
        results.append({
            "disease_id": disease_id,
            "cui": disease["cui"],
            "name": disease["cui_name"],
            "status": "processed",
            "confidence": disease["confidence"],
            "output_file": str(output_file)
        })

        print(f"\n{status}")
        print(f"  Disease ID: {disease_id}")
        print(f"  CUI: {disease['cui']}")
        print(f"  Name: {disease['cui_name']}")
        print(f"  Confidence: {disease['confidence']}")
        print(f"  Data Quality: {disease['data_quality']}")
        print(f"  Metric Type: {disease['metric_type']}")
        if disease['incidence_per_100k'] is not None:
            print(f"  Incidence: {disease['incidence_per_100k']} per 100k")
        if disease['prevalence_per_100k'] is not None:
            print(f"  Prevalence: {disease['prevalence_per_100k']} per 100k")
        print(f"  Output: {output_file}")

    # Save batch results
    batch_results = []
    for disease in DISEASES_DATA:
        batch_results.append({
            "cui": disease["cui"],
            "cui_name": disease["cui_name"],
            "incidence_per_100k": disease["incidence_per_100k"],
            "prevalence_per_100k": disease["prevalence_per_100k"],
            "metric_type": disease["metric_type"],
            "total_cases_per_year": disease["total_cases_per_year"],
            "confidence": disease["confidence"],
            "is_subtype": disease["is_subtype"],
            "parent_disease": disease["parent_disease"],
            "reasoning": disease["reasoning"],
            "data_quality": disease["data_quality"],
            "geographic_variation": disease["geographic_variation"],
            "year_specific": disease["year_specific"],
            "data_year": disease["data_year"],
            "source": disease["source"],
            "source_url": disease["source_url"],
            "source_type": disease["source_type"]
        })

    batch_file = Path("/home/user/cui_disease_incidence_processing/output/batch_results_user_5diseases.json")
    with open(batch_file, 'w') as f:
        json.dump(batch_results, f, indent=2)

    # Save summary report
    summary = {
        "total_processed": len(DISEASES_DATA),
        "successful": len(results),
        "failed": 0,
        "processing_date": "2025-11-11",
        "skill": "cui-incidence-mapper_2",
        "results": results,
        "batch_file": str(batch_file)
    }

    summary_file = Path("/home/user/cui_disease_incidence_processing/output/PROCESSING_SUMMARY_USER_5DISEASES.json")
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 80)
    print(f"SUMMARY: Successfully processed {len(results)} of {len(DISEASES_DATA)} diseases")
    print(f"Individual files: output/disease_{{disease_id}}.json")
    print(f"Batch results: {batch_file}")
    print(f"Summary report: {summary_file}")
    print("=" * 80)

if __name__ == "__main__":
    main()
