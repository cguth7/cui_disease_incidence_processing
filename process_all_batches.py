#!/usr/bin/env python3
"""
Process all remaining disease batches 2-100 (diseases 1006-1500)
This script will need to be executed with the CUI incidence mapping logic
"""

import json
from pathlib import Path

def main():
    # Load batch info
    batch_file = Path("/home/user/cui_disease_incidence_processing/output/batch_1001_1500_info.json")
    with open(batch_file, 'r') as f:
        batch_data = json.load(f)

    batches = batch_data['batches']
    output_dir = Path("/home/user/cui_disease_incidence_processing/output/results")

    # Track progress
    total_batches = len(batches)
    processed_count = 0

    # Check which diseases are already processed
    existing_files = set(f.stem for f in output_dir.glob("*.json"))

    print(f"Total batches: {total_batches}")
    print(f"Already processed files: {len(existing_files)}")

    # Print batches that need processing
    for i, batch in enumerate(batches[1:], start=2):  # Skip batch 1 (already done)
        diseases_in_batch = [d['cui'] for d in batch]
        already_done = all(cui in existing_files for cui in diseases_in_batch)

        if not already_done:
            print(f"\nBatch {i} needs processing:")
            for disease in batch:
                status = "✓" if disease['cui'] in existing_files else "○"
                print(f"  {status} {disease['cui']}: {disease['name']}")

if __name__ == "__main__":
    main()
