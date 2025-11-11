#!/usr/bin/env python3
"""Analyze batch results and generate statistics"""

import json
import os
import sys

def analyze_batch_results(results_dir):
    """Analyze all JSON results in the directory"""
    stats = {
        "total_processed": 0,
        "mappable": 0,
        "unmappable": 0,
        "high_confidence": 0,
        "medium_confidence": 0,
        "low_confidence": 0,
        "confidence_0": 0,
        "subtypes": 0,
        "aggregate_estimates": 0
    }

    low_confidence_list = []

    for filename in os.listdir(results_dir):
        if not filename.endswith('.json'):
            continue

        filepath = os.path.join(results_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)

        stats["total_processed"] += 1
        confidence = data.get("confidence", 0)

        if confidence >= 0.7:
            stats["high_confidence"] += 1
            stats["mappable"] += 1
        elif confidence >= 0.3:
            stats["medium_confidence"] += 1
            stats["mappable"] += 1
        elif confidence > 0:
            stats["low_confidence"] += 1
            stats["mappable"] += 1
            low_confidence_list.append({
                "cui": data.get("cui"),
                "name": data.get("cui_name"),
                "confidence": confidence
            })
        else:
            stats["confidence_0"] += 1
            stats["unmappable"] += 1

        if data.get("is_subtype"):
            stats["subtypes"] += 1

        if 0.2 <= confidence <= 0.3:
            stats["aggregate_estimates"] += 1

    return stats, low_confidence_list

if __name__ == '__main__':
    results_dir = '/home/user/cui_disease_incidence_processing/output/current_run/results'
    stats, low_conf = analyze_batch_results(results_dir)

    print(f"Total Processed: {stats['total_processed']}")
    print(f"Mappable: {stats['mappable']}")
    print(f"Unmappable: {stats['unmappable']}")
    print(f"High Confidence (0.7-1.0): {stats['high_confidence']}")
    print(f"Medium Confidence (0.3-0.7): {stats['medium_confidence']}")
    print(f"Low Confidence (0.1-0.3): {stats['low_confidence']}")
    print(f"Subtypes Identified: {stats['subtypes']}")
    print(f"Aggregate Estimates: {stats['aggregate_estimates']}")

    if low_conf:
        print(f"\nLow Confidence Results ({len(low_conf)}):")
        for item in low_conf:
            print(f"  - {item['cui']} ({item['name']}): {item['confidence']}")

    # Save stats
    with open('/home/user/cui_disease_incidence_processing/output/current_run/batch_stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
