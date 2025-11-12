#!/usr/bin/env python3
"""
Generate prompts for launching batches efficiently
"""
import json
import sys

with open('batch_groups.json', 'r') as f:
    batches = json.load(f)

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else len(batches)

for i in range(start, end):
    batch = batches[i]
    print(f"=== Batch {i} ===")
    for j, disease in enumerate(batch, 1):
        print(f"{j}. {disease['diseaseid']} - {disease['diseasename']}")
    print()
