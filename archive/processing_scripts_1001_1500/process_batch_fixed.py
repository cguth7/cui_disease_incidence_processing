#!/usr/bin/env python3
"""
Batch processing script for CUI disease incidence mapping
Processes diseases from the CSV by row number (not disease_id)
"""

import csv
import json
from pathlib import Path

def load_diseases_by_row(start_row, end_row):
    """Load diseases from CSV file by row number (1-indexed, skip header)"""
    diseases = []
    csv_path = Path("/home/user/cui_disease_incidence_processing/data/disease_codes_Charlie.csv")

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):  # Start counting from 1
            if start_row <= idx <= end_row:
                diseases.append({
                    'row_number': idx,
                    'disease_id': row['disease_id'],
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
    # Process rows 1001-1500 (500 diseases)
    start_row = 1001
    end_row = 1500

    print(f"Loading diseases from rows {start_row}-{end_row}...")
    diseases = load_diseases_by_row(start_row, end_row)
    print(f"Loaded {len(diseases)} diseases")

    print("\nCreating batches of 5...")
    batches = create_batches(diseases, batch_size=5)
    print(f"Created {len(batches)} batches")

    # Save batch info for reference
    output_dir = Path("/home/user/cui_disease_incidence_processing/output")
    batch_file = output_dir / "batch_1001_1500_info.json"

    with open(batch_file, 'w') as f:
        json.dump({
            'start_row': start_row,
            'end_row': end_row,
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
            print(f"  Row {disease['row_number']}: {disease['cui']} - {disease['name']}")

if __name__ == "__main__":
    main()
