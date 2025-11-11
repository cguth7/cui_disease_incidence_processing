#!/usr/bin/env python3
"""
Generate task groups for processing diseases 2001-3000.
Outputs groups of 5 diseases that will be processed by sub-agents.
"""
import csv

# Read diseases
diseases = []
with open('diseases_to_process_2001_3000.json', 'r') as f:
    for line in f:
        parts = line.strip().split(',', 2)
        if len(parts) == 3:
            disease_id, cui, disease_name = parts
            diseases.append({
                'disease_id': disease_id,
                'cui': cui,
                'disease_name': disease_name
            })

print(f"Total diseases to process: {len(diseases)}")

# Group into batches of 5
batch_size = 5
batches = []
for i in range(0, len(diseases), batch_size):
    batch = diseases[i:i+batch_size]
    batches.append(batch)

print(f"Total batches (5 diseases each): {len(batches)}")

# Write batches to a file for reference
with open('task_batches.txt', 'w') as f:
    for i, batch in enumerate(batches, 1):
        f.write(f"Batch {i}:\n")
        for disease in batch:
            f.write(f"  {disease['disease_id']}: {disease['cui']} - {disease['disease_name']}\n")
        f.write("\n")

print(f"Batch information written to task_batches.txt")
print(f"\nFirst batch example:")
for disease in batches[0]:
    print(f"  {disease['disease_id']}: {disease['cui']} - {disease['disease_name']}")
