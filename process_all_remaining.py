#!/usr/bin/env python3
"""
Generate task launch data for all remaining batches (2-10)
This will output the data needed for 90 parallel Task agents
"""

import json

# Load batches
with open('/home/user/cui_disease_incidence_processing/output/current_run/batches.json', 'r') as f:
    all_batches = json.load(f)

task_data = []

for batch_num in range(2, 11):  # Batches 2-10
    batch = all_batches[batch_num - 1]
    cui_details = batch['cui_details']

    # Split into 10 groups of 5
    for group_idx in range(10):
        start = group_idx * 5
        end = start + 5
        group_diseases = cui_details[start:end]

        task_data.append({
            'batch': batch_num,
            'group': group_idx + 1,
            'diseases': group_diseases
        })

# Save to file for reference
with open('/home/user/cui_disease_incidence_processing/output/current_run/remaining_tasks.json', 'w') as f:
    json.dump(task_data, f, indent=2)

print(f"Total tasks to launch: {len(task_data)}")
print(f"That's {len(task_data) * 5} diseases across batches 2-10")
