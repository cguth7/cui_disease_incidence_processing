---
description: Process CUI disease codes in batches with incidence mapping
---

**IMPORTANT: Before starting, read the README.md file to understand the project structure, workflow, and how the system works.**

Run the batch processor to map diseases from disease_codes_Charlie.csv to global incidence rates.

**Usage Options:**

```bash
# Start new run (creates timestamped output directory)
python scripts/batch_processor.py

# Start new run with custom output directory name
python scripts/batch_processor.py --output-dir my_test_run

# Resume from checkpoint in latest run
python scripts/batch_processor.py --resume

# Process specific range of rows
python scripts/batch_processor.py --start-row 1000 --end-row 2000

# Process with custom batch size
python scripts/batch_processor.py --batch-size 50

# Check status of latest run
python scripts/batch_processor.py --status
```

**How it works:**

1. Reads diseases from `data/disease_codes_Charlie.csv`
2. Processes in batches of 100 (configurable)
3. For each batch, prints Task prompts that you should run
4. Each Task agent uses the `cui-incidence-mapper_2` skill to estimate incidence
5. Results saved to `output/runs/run_YYYY-MM-DD_HH-MM-SS/results/`
6. Progress checkpointed after each batch
7. Can resume if interrupted

**Output Structure:**

```
output/runs/run_2025-11-10_12-34-56/
├── results/
│   ├── C0001.json
│   ├── C0002.json
│   └── ...
├── checkpoint.json    # Progress tracking
├── progress.log       # Detailed log
└── summary.json       # Final summary stats
```

**Examples:**

Process all diseases in batches of 100:
```bash
python scripts/batch_processor.py
```

Test with first 500 rows:
```bash
python scripts/batch_processor.py --end-row 500
```

Resume interrupted run:
```bash
python scripts/batch_processor.py --resume
```
