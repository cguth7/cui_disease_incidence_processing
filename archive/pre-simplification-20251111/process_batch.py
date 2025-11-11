#!/usr/bin/env python3
"""Process a batch of CUIs using the cui-incidence-mapper_2 skill"""

import json
import sys

def load_batch(batch_number):
    """Load batch data from batches.json"""
    with open('/home/user/cui_disease_incidence_processing/output/current_run/batches.json', 'r') as f:
        batches = json.load(f)

    # Find the requested batch (1-indexed)
    for batch in batches:
        if batch['batch_number'] == batch_number:
            return batch

    return None

def split_into_groups(batch_data, group_size=5):
    """Split batch CUIs into groups for parallel processing"""
    cuis = batch_data['cui_details']
    groups = []

    for i in range(0, len(cuis), group_size):
        group = cuis[i:i+group_size]
        groups.append({
            'group_number': (i // group_size) + 1,
            'diseases': [{'cui': d['cui'], 'name': d['name']} for d in group]
        })

    return groups

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process_batch.py <batch_number>")
        sys.exit(1)

    batch_number = int(sys.argv[1])

    # Load batch data
    batch = load_batch(batch_number)
    if not batch:
        print(f"Error: Batch {batch_number} not found")
        sys.exit(1)

    print(f"Processing Batch {batch_number}: Diseases {batch['start_index']}-{batch['end_index']}")

    # Split into groups of 5
    groups = split_into_groups(batch)
    print(f"Split into {len(groups)} groups of 5 CUIs each")

    # Save groups for Task agents to process
    output_dir = f'/home/user/cui_disease_incidence_processing/output/current_run/batch_{batch_number}_groups.json'
    with open(output_dir, 'w') as f:
        json.dump(groups, f, indent=2)

    print(f"Groups saved to: {output_dir}")
    print(f"\nFirst group CUIs: {[d['cui'] for d in groups[0]['diseases']]}")

if __name__ == '__main__':
    main()
