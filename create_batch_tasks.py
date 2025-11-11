#!/usr/bin/env python3
"""Generate Task invocation data for a specific batch"""

import json
import sys

if len(sys.argv) < 2:
    print("Usage: python3 create_batch_tasks.py <batch_number>")
    sys.exit(1)

batch_num = int(sys.argv[1])

# Load remaining tasks
with open('/home/user/cui_disease_incidence_processing/output/current_run/remaining_tasks.json', 'r') as f:
    all_tasks = json.load(f)

# Filter for the requested batch
batch_tasks = [t for t in all_tasks if t['batch'] == batch_num]

print(f"Batch {batch_num} has {len(batch_tasks)} groups:")
for task in batch_tasks:
    diseases = task['diseases']
    print(f"\nGroup {task['group']}:")
    for d in diseases:
        print(f"  {d['cui']} - {d['name']}")
