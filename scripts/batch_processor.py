#!/usr/bin/env python3
"""
Batch processor for CUI disease incidence mapping.
Processes diseases in batches of 100 using parallel Task agents.
"""

import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class BatchProcessor:
    def __init__(
        self,
        csv_path: str,
        batch_size: int = 100,
        output_dir: Optional[str] = None,
        start_row: Optional[int] = None,
        end_row: Optional[int] = None,
    ):
        self.csv_path = Path(csv_path)
        self.batch_size = batch_size
        self.start_row = start_row or 0
        self.end_row = end_row

        # Setup output directory
        if output_dir:
            self.run_dir = Path("output/runs") / output_dir
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.run_dir = Path("output/runs") / f"run_{timestamp}"

        self.results_dir = self.run_dir / "results"
        self.checkpoint_file = self.run_dir / "checkpoint.json"
        self.log_file = self.run_dir / "progress.log"
        self.summary_file = self.run_dir / "summary.json"

        # Create directories
        self.results_dir.mkdir(parents=True, exist_ok=True)

        # Load checkpoint if exists
        self.checkpoint = self._load_checkpoint()

    def _load_checkpoint(self) -> Dict:
        """Load checkpoint if it exists."""
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file, 'r') as f:
                return json.load(f)
        return {
            "last_completed_batch": -1,
            "last_completed_row": -1,
            "total_rows": 0,
            "completed_cuis": [],
            "failed_cuis": [],
            "timestamp": None,
            "batch_size": self.batch_size
        }

    def _save_checkpoint(self, batch_num: int, row_num: int, completed: List[str], failed: List[str]):
        """Save progress checkpoint."""
        self.checkpoint.update({
            "last_completed_batch": batch_num,
            "last_completed_row": row_num,
            "completed_cuis": completed,
            "failed_cuis": failed,
            "timestamp": datetime.now().isoformat(),
            "batch_size": self.batch_size
        })
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.checkpoint, f, indent=2)

    def _log(self, message: str):
        """Log message to file and stdout."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        with open(self.log_file, 'a') as f:
            f.write(log_msg + "\n")

    def read_diseases(self) -> List[Dict]:
        """Read diseases from CSV file."""
        diseases = []
        with open(self.csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if self.start_row and i < self.start_row:
                    continue
                if self.end_row and i >= self.end_row:
                    break
                # Support both column naming conventions
                cui = row.get("CUI") or row.get("diseaseid", "")
                name = row.get("STR") or row.get("diseasename", "")
                incidence_num = row.get("val") or row.get("disease_id", "")

                diseases.append({
                    "row_num": i,
                    "cui": cui.strip() if cui else "",
                    "name": name.strip() if name else "",
                    "incidence_number": incidence_num.strip() if incidence_num else ""
                })
        return diseases

    def generate_task_prompt(self, cui: str, name: str, incidence_number: str) -> str:
        """Generate prompt for Task agent."""
        output_file = self.results_dir / f"{cui}.json"

        return f"""Use the cui-incidence-mapper_2 skill to map this disease to global incidence rates.

CUI: {cui}
Disease Name: {name}
Provided Incidence Number: {incidence_number}

Follow the skill instructions to:
1. Assess if this is mappable or an umbrella term (if umbrella, provide aggregate BOTEC estimate)
2. Estimate global incidence per 100k person-years
3. Provide confidence score and reasoning
4. Output valid JSON only (no markdown, no extra text)

Save the JSON result to: {output_file}

Return the final JSON result in your response."""

    def create_batch_commands(self, batch: List[Dict]) -> str:
        """Create commands to launch Task agents for a batch."""
        commands = []
        for disease in batch:
            prompt = self.generate_task_prompt(
                disease["cui"],
                disease["name"],
                disease["incidence_number"]
            )
            # Escape quotes for command line
            escaped_prompt = prompt.replace('"', '\\"').replace('\n', '\\n')
            commands.append(
                f'claude task general-purpose "{escaped_prompt}" --description "Map {disease["cui"]}"'
            )
        return "\n".join(commands)

    def process_batch(self, batch_num: int, batch: List[Dict]) -> tuple[List[str], List[str]]:
        """Process a batch of diseases."""
        self._log(f"Processing batch {batch_num + 1} ({len(batch)} diseases)...")

        # Generate list of CUIs in this batch
        cuis = [d["cui"] for d in batch]

        # Print instructions for user
        print("\n" + "="*80)
        print(f"BATCH {batch_num + 1}: Ready to process {len(batch)} diseases")
        print("="*80)
        print("\nTO PROCESS THIS BATCH:")
        print("Copy and paste the Task commands below into Claude Code.\n")

        # Print Task commands
        for disease in batch:
            prompt = self.generate_task_prompt(
                disease["cui"],
                disease["name"],
                disease["incidence_number"]
            )
            print(f"\nTask: Map {disease['cui']} - {disease['name']}")
            print("-" * 80)
            print(prompt)
            print("-" * 80)

        print("\n" + "="*80)
        print("After all Task agents complete, press ENTER to continue...")
        print("="*80)
        input()

        # Check which succeeded
        completed = []
        failed = []
        for cui in cuis:
            result_file = self.results_dir / f"{cui}.json"
            if result_file.exists():
                completed.append(cui)
            else:
                failed.append(cui)

        self._log(f"Batch {batch_num + 1} complete: {len(completed)} succeeded, {len(failed)} failed")

        return completed, failed

    def run(self, resume: bool = False):
        """Run the batch processing."""
        self._log(f"Starting batch processor (run directory: {self.run_dir})")

        # Read diseases
        diseases = self.read_diseases()
        total_diseases = len(diseases)
        self._log(f"Loaded {total_diseases} diseases from {self.csv_path}")

        # Determine starting point
        start_idx = 0
        if resume and self.checkpoint["last_completed_row"] >= 0:
            start_idx = self.checkpoint["last_completed_row"] + 1
            self._log(f"Resuming from row {start_idx}")

        # Process in batches
        all_completed = self.checkpoint.get("completed_cuis", [])
        all_failed = self.checkpoint.get("failed_cuis", [])

        for batch_num, i in enumerate(range(start_idx, total_diseases, self.batch_size)):
            batch = diseases[i:i + self.batch_size]

            completed, failed = self.process_batch(batch_num, batch)

            all_completed.extend(completed)
            all_failed.extend(failed)

            # Save checkpoint
            last_row = i + len(batch) - 1
            self._save_checkpoint(batch_num, last_row, all_completed, all_failed)

        # Generate summary
        self._generate_summary(total_diseases, all_completed, all_failed)
        self._log("Processing complete!")

    def _generate_summary(self, total: int, completed: List[str], failed: List[str]):
        """Generate summary statistics."""
        summary = {
            "run_directory": str(self.run_dir),
            "timestamp": datetime.now().isoformat(),
            "total_diseases": total,
            "completed": len(completed),
            "failed": len(failed),
            "success_rate": len(completed) / total if total > 0 else 0,
            "failed_cuis": failed
        }

        with open(self.summary_file, 'w') as f:
            json.dump(summary, f, indent=2)

        self._log(f"\nSUMMARY:")
        self._log(f"  Total: {total}")
        self._log(f"  Completed: {len(completed)}")
        self._log(f"  Failed: {len(failed)}")
        self._log(f"  Success Rate: {summary['success_rate']:.1%}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Batch process CUI disease incidence mapping")
    parser.add_argument("--csv", default="data/disease_codes_Charlie.csv", help="Path to CSV file")
    parser.add_argument("--batch-size", type=int, default=100, help="Batch size")
    parser.add_argument("--output-dir", help="Custom output directory name")
    parser.add_argument("--start-row", type=int, help="Start from specific row")
    parser.add_argument("--end-row", type=int, help="End at specific row")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--status", action="store_true", help="Show status of latest run")

    args = parser.parse_args()

    if args.status:
        # Show status of latest run
        runs_dir = Path("output/runs")
        if not runs_dir.exists():
            print("No runs found")
            return

        latest = max(runs_dir.iterdir(), key=lambda p: p.stat().st_mtime)
        checkpoint_file = latest / "checkpoint.json"

        if checkpoint_file.exists():
            with open(checkpoint_file, 'r') as f:
                checkpoint = json.load(f)
            print(f"\nLatest run: {latest.name}")
            print(f"Last completed batch: {checkpoint['last_completed_batch'] + 1}")
            print(f"Last completed row: {checkpoint['last_completed_row'] + 1}")
            print(f"Completed CUIs: {len(checkpoint['completed_cuis'])}")
            print(f"Failed CUIs: {len(checkpoint['failed_cuis'])}")
        else:
            print(f"No checkpoint found for {latest.name}")
        return

    # Run batch processor
    processor = BatchProcessor(
        csv_path=args.csv,
        batch_size=args.batch_size,
        output_dir=args.output_dir,
        start_row=args.start_row,
        end_row=args.end_row,
    )

    processor.run(resume=args.resume)


if __name__ == "__main__":
    main()
