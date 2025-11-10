#!/usr/bin/env python3
"""
Automated disease processing script for Claude Code
Processes diseases from CSV in batches using Task agents
"""

import csv
import json
from pathlib import Path
from datetime import datetime

# Configuration
START_ROW = 100
END_ROW = 1000
BATCH_SIZE = 100
CSV_PATH = "data/disease_codes_Charlie.csv"

def create_output_directory():
    """Create timestamped output directory"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = Path(f"output/runs/run_{timestamp}")
    results_dir = output_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    # Save run configuration
    config = {
        "timestamp": timestamp,
        "start_row": START_ROW,
        "end_row": END_ROW,
        "batch_size": BATCH_SIZE,
        "csv_path": CSV_PATH
    }

    with open(output_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)

    return output_dir, results_dir

def load_diseases():
    """Load diseases from CSV"""
    diseases = []
    with open(CSV_PATH, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if START_ROW <= i < END_ROW:
                diseases.append({
                    'index': i,
                    'disease_id': row['disease_id'],
                    'cui': row['diseaseid'],
                    'name': row['diseasename']
                })
    return diseases

def create_batches(diseases, batch_size):
    """Split diseases into batches"""
    batches = []
    for i in range(0, len(diseases), batch_size):
        batches.append(diseases[i:i + batch_size])
    return batches

if __name__ == "__main__":
    # Create output directory
    output_dir, results_dir = create_output_directory()
    print(f"Created output directory: {output_dir}")

    # Load diseases
    diseases = load_diseases()
    print(f"Loaded {len(diseases)} diseases (rows {START_ROW}-{END_ROW})")

    # Create batches
    batches = create_batches(diseases, BATCH_SIZE)
    print(f"Split into {len(batches)} batches of size {BATCH_SIZE}")

    # Save disease list
    with open(output_dir / "diseases.json", "w") as f:
        json.dump(diseases, f, indent=2)

    print(f"\nReady to process {len(diseases)} diseases in {len(batches)} batches")
    print(f"Results will be saved to: {results_dir}")
