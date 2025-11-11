#!/usr/bin/env python3
"""
Consolidate individual JSON results into CSV and summary statistics
"""

import json
import csv
from pathlib import Path
from collections import Counter

def main():
    results_dir = Path("/home/user/cui_disease_incidence_processing/output/results")
    output_dir = Path("/home/user/cui_disease_incidence_processing/output")

    # Read all JSON files
    all_results = []
    json_files = list(results_dir.glob("*.json"))

    print(f"Found {len(json_files)} JSON files to consolidate")

    for json_file in json_files:
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                all_results.append(data)
        except Exception as e:
            print(f"Error reading {json_file}: {e}")

    print(f"Successfully loaded {len(all_results)} disease records")

    # Sort by CUI
    all_results.sort(key=lambda x: x.get('cui', ''))

    # Write consolidated CSV
    csv_path = output_dir / "disease_incidence_data.csv"
    fieldnames = [
        'cui', 'cui_name', 'incidence_per_100k', 'prevalence_per_100k',
        'metric_type', 'total_cases_per_year', 'confidence', 'is_subtype',
        'parent_disease', 'reasoning', 'data_quality', 'geographic_variation',
        'year_specific', 'data_year', 'source', 'source_url', 'source_type'
    ]

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for result in all_results:
            # Ensure all fields are present
            row = {field: result.get(field) for field in fieldnames}
            writer.writerow(row)

    print(f"Wrote consolidated CSV to {csv_path}")

    # Generate summary statistics
    confidence_bins = {
        'high (0.7-1.0)': 0,
        'medium (0.3-0.7)': 0,
        'low (0.1-0.3)': 0,
        'unmappable (0.0)': 0
    }

    data_quality_counts = Counter()
    metric_type_counts = Counter()
    source_type_counts = Counter()
    subtype_count = 0

    for result in all_results:
        # Confidence distribution
        conf = result.get('confidence', 0.0)
        if conf >= 0.7:
            confidence_bins['high (0.7-1.0)'] += 1
        elif conf >= 0.3:
            confidence_bins['medium (0.3-0.7)'] += 1
        elif conf >= 0.1:
            confidence_bins['low (0.1-0.3)'] += 1
        else:
            confidence_bins['unmappable (0.0)'] += 1

        # Data quality
        data_quality_counts[result.get('data_quality', 'unknown')] += 1

        # Metric type
        metric_type_counts[result.get('metric_type', 'null')] += 1

        # Source type
        source_type_counts[result.get('source_type', 'null')] += 1

        # Subtype count
        if result.get('is_subtype'):
            subtype_count += 1

    # Summary statistics
    summary = {
        'total_processed': len(all_results),
        'batch_range': '1001-1500',
        'confidence_distribution': confidence_bins,
        'data_quality_breakdown': dict(data_quality_counts),
        'metric_type_counts': dict(metric_type_counts),
        'source_type_distribution': dict(source_type_counts),
        'subtypes_identified': subtype_count,
        'review_needed': confidence_bins['low (0.1-0.3)'] + confidence_bins['unmappable (0.0)']
    }

    summary_path = output_dir / "summary_stats.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"Wrote summary statistics to {summary_path}")

    # Print summary
    print("\n=== SUMMARY ===")
    print(f"Total diseases processed: {summary['total_processed']}")
    print(f"\nConfidence Distribution:")
    for level, count in confidence_bins.items():
        print(f"  {level}: {count}")
    print(f"\nData Quality:")
    for quality, count in data_quality_counts.items():
        print(f"  {quality}: {count}")
    print(f"\nSubtypes identified: {subtype_count}")
    print(f"Records needing review: {summary['review_needed']}")

if __name__ == "__main__":
    main()
