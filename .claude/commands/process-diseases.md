---
description: Process CUI disease codes in batches with incidence mapping
---

Run the batch processor to map diseases from disease_codes_Charlie.csv to global incidence rates.

**IMPORTANT - Model Selection:**

The user can specify `--model haiku` or `--model sonnet` in the slash command args. Parse this and use it when launching Task agents.

**Examples:**
- `/process-diseases` → Use Sonnet (default)
- `/process-diseases --model haiku` → Use Haiku for all Task agents
- `/process-diseases --model haiku --end-row 100` → Use Haiku, process first 100 rows

**Usage Options:**

```bash
# Start new run (creates timestamped output directory)
python scripts/batch_processor.py

# USE HAIKU for cost savings (95% cheaper)
python scripts/batch_processor.py --model haiku

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

1. Parse user's slash command args (especially `--model` flag)
2. Run: `python scripts/batch_processor.py [args]`
3. Script outputs Task prompts for each disease in batch
4. **YOU (Claude) launch Task agents with the specified model**
   - If user specified `--model haiku`, use `model="haiku"` in Task calls
   - If user specified `--model sonnet` or no model, use `model="sonnet"`
5. Each Task agent uses `cui-incidence-mapper_2` skill to estimate incidence
6. Results saved to `output/runs/run_YYYY-MM-DD_HH-MM-SS/results/`
7. Progress checkpointed after each batch

**CRITICAL: When launching Task agents, check the batch_processor output for MODEL reminder and use that model!**

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
