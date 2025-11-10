#!/usr/bin/env python3
"""
Generate parallel processing commands for batch execution.
Splits the dataset into N parallel batches with non-overlapping row ranges.
"""

import argparse


def generate_parallel_commands(
    total_rows: int,
    num_parallel: int = 10,
    start_row: int = 0,
    batch_size: int = 100,
    model: str = "sonnet"
):
    """Generate parallel batch processing commands."""

    remaining_rows = total_rows - start_row
    rows_per_session = remaining_rows // num_parallel

    print(f"# Parallel Processing Commands")
    print(f"# Total rows: {total_rows}")
    print(f"# Starting from: {start_row}")
    print(f"# Remaining rows: {remaining_rows}")
    print(f"# Parallel sessions: {num_parallel}")
    print(f"# Rows per session: ~{rows_per_session}")
    print(f"# Model: {model}")
    print(f"# Batch size: {batch_size}")
    print()
    print("# Copy these commands into separate terminal windows/sessions:")
    print()

    for i in range(num_parallel):
        session_start = start_row + (i * rows_per_session)

        # Last session gets any remainder
        if i == num_parallel - 1:
            session_end = total_rows
        else:
            session_end = session_start + rows_per_session

        session_num = i + 1
        diseases_count = session_end - session_start

        print(f"# Session {session_num}: {diseases_count} diseases (rows {session_start}-{session_end})")
        print(f"python scripts/batch_processor.py \\")
        print(f"  --start-row {session_start} \\")
        print(f"  --end-row {session_end} \\")
        print(f"  --batch-size {batch_size} \\")
        print(f"  --output-dir parallel_batch_{session_num:02d} \\")
        print(f"  --non-interactive")

        if model == "haiku":
            print(f"  # Then launch Task agents with: --model haiku")

        print()

    print(f"# Total diseases to process: {remaining_rows}")
    print()
    print("# After all complete, merge results:")
    print("mkdir -p output/final_results")
    print("cp output/runs/parallel_batch_*/results/*.json output/final_results/")
    print("ls output/final_results/*.json | wc -l  # Should be", remaining_rows)


def main():
    parser = argparse.ArgumentParser(
        description="Generate parallel processing commands",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate 10 parallel sessions for all 15,162 diseases
  python scripts/generate_parallel_commands.py

  # Generate 20 parallel sessions (faster, more sessions to manage)
  python scripts/generate_parallel_commands.py --num-parallel 20

  # Start from row 1000 (skip already processed)
  python scripts/generate_parallel_commands.py --start-row 1000

  # Generate commands for Haiku model testing
  python scripts/generate_parallel_commands.py --model haiku --num-parallel 5
        """
    )

    parser.add_argument(
        "--total-rows",
        type=int,
        default=15162,
        help="Total rows in CSV (default: 15162)"
    )
    parser.add_argument(
        "--num-parallel",
        type=int,
        default=10,
        help="Number of parallel sessions (default: 10)"
    )
    parser.add_argument(
        "--start-row",
        type=int,
        default=0,
        help="Starting row (default: 0)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Batch size within each session (default: 100)"
    )
    parser.add_argument(
        "--model",
        choices=["sonnet", "haiku"],
        default="sonnet",
        help="Model to use (default: sonnet)"
    )

    args = parser.parse_args()

    generate_parallel_commands(
        total_rows=args.total_rows,
        num_parallel=args.num_parallel,
        start_row=args.start_row,
        batch_size=args.batch_size,
        model=args.model
    )


if __name__ == "__main__":
    main()
