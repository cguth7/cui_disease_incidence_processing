#!/usr/bin/env python3
"""Generate all batch groups for processing"""

import json

# Load the batches file
with open('/home/user/cui_disease_incidence_processing/output/current_run/batches.json', 'r') as f:
    all_batches = json.load(f)

# Generate groups for batches 2-10
for batch_num in range(2, 11):
    batch = all_batches[batch_num - 1]  # 0-indexed

    print(f"\n{'='*60}")
    print(f"BATCH {batch_num}: Diseases {batch['start_index']}-{batch['end_index']}")
    print(f"{'='*60}")

    # Split into groups of 5
    cui_details = batch['cui_details']
    for group_idx in range(10):
        start = group_idx * 5
        end = start + 5
        group_diseases = cui_details[start:end]

        group_num = group_idx + 1
        print(f"\n## Group {group_num} (Batch {batch_num}):")
        for d in group_diseases:
            print(f"  {d['cui']} - {d['name']}")
