#!/usr/bin/env python3
"""
Generate prompts for all remaining batches
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

    # Check which CUIs are already processed
    existing_files = set(f.stem for f in output_dir.glob("*.json"))

    print(f"Total batches: {len(batches)}")
    print(f"Already processed CUIs: {len(existing_files)}")

    # Generate remaining batch information
    remaining_batches = []
    for i, batch in enumerate(batches, start=1):
        cuis_in_batch = [d['cui'] for d in batch]
        already_done = all(cui in existing_files for cui in cuis_in_batch)

        if not already_done:
            remaining_batches.append({
                'batch_num': i,
                'diseases': batch
            })

    print(f"\nRemaining batches to process: {len(remaining_batches)}")

    # Output batch information for next 10 batches
    for batch_info in remaining_batches[:10]:
        print(f"\n=== Batch {batch_info['batch_num']} ===")
        for disease in batch_info['diseases']:
            print(f"{disease['cui']} - {disease['name']}")

if __name__ == "__main__":
    main()
