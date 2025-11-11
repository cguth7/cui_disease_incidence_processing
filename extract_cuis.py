#!/usr/bin/env python3
"""Extract first 500 CUIs from disease_codes_Charlie.csv"""

import csv
import json

# Read the CSV and extract CUIs
cuis_data = []
with open('/home/user/cui_disease_incidence_processing/data/disease_codes_Charlie.csv', 'r') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, 1):
        if i > 500:
            break
        cuis_data.append({
            'index': i,
            'cui': row['diseaseid'],
            'name': row['diseasename']
        })

# Save to JSON for reference
with open('/home/user/cui_disease_incidence_processing/output/current_run/cuis_to_process.json', 'w') as f:
    json.dump(cuis_data, f, indent=2)

print(f"Extracted {len(cuis_data)} CUIs")

# Organize into 10 batches of 50 each
batches = []
for batch_num in range(10):
    start_idx = batch_num * 50
    end_idx = start_idx + 50
    batch_cuis = cuis_data[start_idx:end_idx]
    batches.append({
        'batch_number': batch_num + 1,
        'start_index': start_idx + 1,
        'end_index': end_idx,
        'cuis': [cui['cui'] for cui in batch_cuis],
        'cui_details': batch_cuis
    })

# Save batches
with open('/home/user/cui_disease_incidence_processing/output/current_run/batches.json', 'w') as f:
    json.dump(batches, f, indent=2)

print(f"Organized into {len(batches)} batches of 50 CUIs each")

# Print first batch for verification
print(f"\nBatch 1 CUIs (first 10): {batches[0]['cuis'][:10]}")
