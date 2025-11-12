#!/usr/bin/env python3
"""
Organize diseases into groups of 5 for parallel processing.
"""
import csv
import json

# Read all diseases
diseases = []
with open('diseases_to_process.csv', 'r') as f:
    reader = csv.DictReader(f, fieldnames=['disease_id', 'diseaseid', 'diseasename'])
    for row in reader:
        diseases.append(row)

print(f"Total diseases to process: {len(diseases)}")

# Group into batches of 5
batch_size = 5
batches = []
for i in range(0, len(diseases), batch_size):
    batch = diseases[i:i+batch_size]
    batches.append(batch)

print(f"Total batches: {len(batches)}")

# Save batches to a file for reference
with open('batch_groups.json', 'w') as f:
    json.dump(batches, f, indent=2)

print(f"Batches saved to batch_groups.json")
print(f"\nFirst batch example:")
print(json.dumps(batches[0], indent=2))
