#!/usr/bin/env python3
"""
Extract specific batches from batch_groups.json for processing
"""
import json
import sys

with open('batch_groups.json', 'r') as f:
    batches = json.load(f)

# Get batch range from command line
start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else len(batches)

selected_batches = batches[start:end]

print(f"Extracting batches {start} to {end-1} ({len(selected_batches)} batches)")
print(json.dumps(selected_batches, indent=2))
