#!/usr/bin/env python3
"""
Batch processing script for CUI disease incidence mapping
Processes diseases from the CSV and creates batches for sub-agent processing
"""

import csv
import json
import os
from pathlib import Path

def load_diseases(start_id, end_id):
    """Load diseases from CSV file within the specified range"""
    diseases = []
    csv_path = Path("/home/user/cui_disease_incidence_processing/data/disease_codes_Charlie.csv")

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            disease_id = int(row['disease_id'])
            if start_id <= disease_id <= end_id:
                diseases.append({
                    'disease_id': disease_id,
                    'cui': row['diseaseid'],
                    'name': row['diseasename']
                })

    return diseases

def create_batches(diseases, batch_size=5):
    """Create batches of diseases for processing"""
    batches = []
    for i in range(0, len(diseases), batch_size):
        batch = diseases[i:i+batch_size]
        batches.append(batch)
    return batches

def main():
    # Process diseases 1001-1500
    start_id = 1001
    end_id = 1500

    print(f"Loading diseases {start_id}-{end_id}...")
    diseases = load_diseases(start_id, end_id)
    print(f"Loaded {len(diseases)} diseases")

    print("\nCreating batches of 5...")
    batches = create_batches(diseases, batch_size=5)
    print(f"Created {len(batches)} batches")

    # Save batch info for reference
    output_dir = Path("/home/user/cui_disease_incidence_processing/output")
    batch_file = output_dir / "batch_1001_1500_info.json"

    with open(batch_file, 'w') as f:
        json.dump({
            'start_id': start_id,
            'end_id': end_id,
            'total_diseases': len(diseases),
            'total_batches': len(batches),
            'batch_size': 5,
            'batches': batches
        }, f, indent=2)

    print(f"\nBatch info saved to {batch_file}")

    # Print first few batches as examples
    print("\nFirst 3 batches:")
    for i, batch in enumerate(batches[:3]):
        print(f"\nBatch {i+1}:")
        for disease in batch:
            print(f"  {disease['cui']}: {disease['name']}")

if __name__ == "__main__":
    main()
