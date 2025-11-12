#!/usr/bin/env python3
"""
Apply cui-incidence-mapper skill to process batches of CUI codes.
"""

import json
import os
from pathlib import Path
from datetime import datetime

def load_batch(batch_file):
    """Load batch input from JSON file."""
    with open(batch_file, 'r') as f:
        return json.load(f)

def save_individual_results(results, output_dir):
    """Save each result to output/results/{CUI}.json"""
    count = 0
    for result in results:
        cui = result.get('cui')
        if cui:
            output_file = Path(output_dir) / f"{cui}.json"
            with open(output_file, 'w') as f:
                json.dump(result, f, indent=2)
            count += 1
    return count

def main():
    output_dir = Path("/home/user/cui_disease_incidence_processing/output/results")
    output_dir.mkdir(parents=True, exist_ok=True)

    batch_files = [
        "/home/user/cui_disease_incidence_processing/batch1_input.json",
        "/home/user/cui_disease_incidence_processing/batch2_input.json",
        "/home/user/cui_disease_incidence_processing/batch3_input.json",
        "/home/user/cui_disease_incidence_processing/batch4_input.json"
    ]

    total_processed = 0
    all_results = []

    print("CUI Incidence Mapper - Batch Processing")
    print("=" * 60)
    print(f"Output directory: {output_dir}")
    print(f"Batch files: {len(batch_files)}")
    print()

    # Process each batch
    for i, batch_file in enumerate(batch_files, 1):
        if os.path.exists(batch_file):
            batch_data = load_batch(batch_file)
            diseases = batch_data.get('diseases', [])

            print(f"Batch {i}: Processing {len(diseases)} CUI codes")
            print(f"  File: {batch_file}")
            print(f"  CUIs: {[d['cui'] for d in diseases]}")

            # For now, we'll prepare the batches for submission to the skill
            # The actual skill processing will happen through the skill interface

    print()
    print("Batch files prepared and ready for skill processing")
    print(f"Instructions: Pass each batch JSON to the cui-incidence-mapper skill")
    print()

if __name__ == "__main__":
    main()
