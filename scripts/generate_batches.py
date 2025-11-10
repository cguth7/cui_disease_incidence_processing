#!/usr/bin/env python3
"""
Generate batch information for CUI disease processing.
Outputs batch details in JSON format for automated processing.
"""

import csv
import json
import sys
from pathlib import Path


def generate_batches(csv_path, batch_size=100, start_row=0, end_row=None):
    """Generate batches of diseases from CSV."""
    diseases = []

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i < start_row:
                continue
            if end_row and i >= end_row:
                break
            diseases.append({
                "row_num": i,
                "cui": row.get("diseaseid", "").strip(),
                "name": row.get("diseasename", "").strip(),
                "incidence_number": row.get("disease_id", "").strip()
            })

    # Split into batches
    batches = []
    for i in range(0, len(diseases), batch_size):
        batch = diseases[i:i + batch_size]
        batches.append({
            "batch_num": i // batch_size,
            "start_row": start_row + i,
            "end_row": start_row + i + len(batch),
            "count": len(batch),
            "diseases": batch
        })

    return {
        "total_diseases": len(diseases),
        "batch_size": batch_size,
        "total_batches": len(batches),
        "batches": batches
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate batch information for disease processing")
    parser.add_argument("--csv", default="data/disease_codes_Charlie.csv", help="Path to CSV file")
    parser.add_argument("--batch-size", type=int, default=100, help="Batch size")
    parser.add_argument("--start-row", type=int, default=0, help="Start from specific row")
    parser.add_argument("--end-row", type=int, help="End at specific row")
    parser.add_argument("--batch-num", type=int, help="Get specific batch number")
    parser.add_argument("--summary", action="store_true", help="Show only summary")

    args = parser.parse_args()

    result = generate_batches(
        args.csv,
        batch_size=args.batch_size,
        start_row=args.start_row,
        end_row=args.end_row
    )

    if args.summary:
        print(f"Total diseases: {result['total_diseases']}")
        print(f"Batch size: {result['batch_size']}")
        print(f"Total batches: {result['total_batches']}")
    elif args.batch_num is not None:
        if 0 <= args.batch_num < len(result['batches']):
            print(json.dumps(result['batches'][args.batch_num], indent=2))
        else:
            print(f"Error: Batch {args.batch_num} not found", file=sys.stderr)
            sys.exit(1)
    else:
        print(json.dumps(result, indent=2))
