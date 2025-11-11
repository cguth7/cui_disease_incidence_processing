#!/usr/bin/env python3
"""
Process diseases 1006-1500 (batches 2-100) for CUI disease incidence mapping.
"""

import json
import os
from pathlib import Path

# Read the batch file
with open('/home/user/cui_disease_incidence_processing/output/batch_1001_1500_info.json', 'r') as f:
    batch_data = json.load(f)

# Get batches 2-100 (index 1-99, since batch 1 is index 0)
batches_to_process = batch_data['batches'][1:100]

print(f"Total batches to process: {len(batches_to_process)}")
print(f"Total diseases to process: {len(batches_to_process) * 5}")

# Create output directory if it doesn't exist
output_dir = Path('/home/user/cui_disease_incidence_processing/output/results')
output_dir.mkdir(parents=True, exist_ok=True)

# Flatten all diseases
all_diseases = []
for batch in batches_to_process:
    all_diseases.extend(batch)

print(f"\nProcessing {len(all_diseases)} diseases from rows {all_diseases[0]['row_number']} to {all_diseases[-1]['row_number']}")

# Write the diseases list for reference
with open('/home/user/cui_disease_incidence_processing/diseases_to_process_1006_1500.json', 'w') as f:
    json.dump(all_diseases, f, indent=2)

print(f"Disease list saved to diseases_to_process_1006_1500.json")
print(f"\nFirst disease: {all_diseases[0]}")
print(f"Last disease: {all_diseases[-1]}")
