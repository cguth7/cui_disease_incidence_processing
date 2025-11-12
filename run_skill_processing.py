#!/usr/bin/env python3
"""
Process CUI codes through the cui-incidence-mapper_2 skill
and save individual results to output/results/{CUI}.json
"""

import json
import sys
from pathlib import Path

# Read batch 1 input
batch1_input = {
    "diseases": [
        {"cui": "C2751318"},
        {"cui": "C2825306"},
        {"cui": "C2826320"},
        {"cui": "C2861580"},
        {"cui": "C2910340"}
    ]
}

# Read batch 2 input
batch2_input = {
    "diseases": [
        {"cui": "C2930971"},
        {"cui": "C2931071"},
        {"cui": "C2931187"},
        {"cui": "C2931254"},
        {"cui": "C2931286"}
    ]
}

output_dir = Path("/home/user/cui_disease_incidence_processing/output/results")
output_dir.mkdir(parents=True, exist_ok=True)

print("="*70)
print("CUI INCIDENCE MAPPER - BATCH PROCESSING")
print("="*70)

print("\nBATCH 1 INPUT:")
print(json.dumps(batch1_input, indent=2))

print("\nExpected: Array of 5 results with disease incidence data")
print("\nWaiting for Batch 1 results from skill...")
print("Please provide the JSON array with 5 results...")

# Instructions for user
print("\n" + "="*70)
print("INSTRUCTIONS FOR SKILL PROCESSING")
print("="*70)
print("\n1. The skill is ready to process Batch 1:")
print(json.dumps(batch1_input, indent=2))
print("\n2. Skill should return a JSON array with 5 result objects")
print("\n3. Each result will be saved to output/results/{CUI}.json")
print("\n4. Then Batch 2 will be processed similarly")
print("\nReady to receive results...")

