#!/usr/bin/env python3
"""
Generate task launch commands for remaining batches
"""
import json

with open('batch_groups.json', 'r') as f:
    batches = json.load(f)

# Start from batch 20 (already processed 0-19)
start_batch = 20
end_batch = len(batches)  # 200

print(f"Need to process batches {start_batch} to {end_batch-1}")
print(f"Total batches remaining: {end_batch - start_batch}")
print(f"Total diseases remaining: {(end_batch - start_batch) * 5}")

# Generate batch info for launching
for i in range(start_batch, min(start_batch + 20, end_batch)):
    batch = batches[i]
    print(f"\n=== Batch {i} ===")
    cuis = []
    for disease in batch:
        cui = disease['diseaseid']
        name = disease['diseasename']
        cuis.append(f"{cui} - {name}")

    for j, cui_info in enumerate(cuis, 1):
        print(f"{j}. {cui_info}")
