---
description: Process CUI disease codes in batches with incidence mapping
---

# Automated Disease Processing Workflow

Process disease CUI codes in batches using parallel Task agents with automatic git tracking.

---

## Processing Steps

### 1. Setup Output Directory

Create timestamped run directory:
```
output/runs/run_YYYY-MM-DD_HH-MM-SS/
├── results/         # Individual JSON files for each disease
├── progress.md      # Batch-by-batch progress tracking
└── summary.json     # Final statistics (created at end)
```

### 2. Read Input CSV

- **File**: `data/disease_codes_Charlie.csv`
- **Columns**: `disease_id`, `diseaseid` (CUI code), `diseasename`
- Use Python csv module to read rows

### 3. Process in Batches

**Batch size**: 20-100 diseases per batch

For each batch:

1. **Launch Task agents in parallel** (single message, multiple tool calls):
   - `subagent_type="general-purpose"`
   - `model="haiku"` (for cost efficiency)
   - Prompt: "Use the cui-incidence-mapper_2 skill to map this disease to global incidence rates. CUI: {cui}, Disease Name: {name}. Save JSON result to: output/runs/run_{timestamp}/results/{cui}.json"

2. **Wait for all agents** in the batch to complete

3. **Update progress file** (`output/runs/run_{timestamp}/progress.md`):
   - Add batch completion entry with count of diseases processed
   - List CUIs processed in this batch
   - Track mappable vs unmappable

4. **CRITICAL: Commit and push to git after EVERY batch:**
   ```bash
   git add -A
   git commit -m "Complete batch {batch_num}: diseases {start}-{end}"
   git push -u origin claude/process-diseases-{start}_{end}-{session_id}
   ```

   **Branch naming**: `claude/process-diseases-{start}_{end}-{session_id}`
   - `{start}`: First disease index in the full run (e.g., 1, 101, 201)
   - `{end}`: Last disease index in the full run (e.g., 100, 200, 300)
   - `{session_id}`: Unique session identifier
   - Example: `claude/process-diseases-1_100-011CUzgiK4Jp35y4oXKyCUf7`

5. **Continue to next batch** until all diseases processed

### 4. Finalize Run

After all batches complete:

1. **Generate summary.json** in `output/runs/run_{timestamp}/summary.json`:
   ```json
   {
     "total_diseases": 100,
     "completed": 92,
     "unmappable": 8,
     "success_rate": 0.92,
     "confidence_distribution": {
       "high (0.7-1.0)": 59,
       "medium (0.3-0.7)": 25,
       "low (0.1-0.3)": 8,
       "unmappable (0.0)": 8
     },
     "subtypes_identified": 45
   }
   ```

2. **Update root progress.md** at repository root:
   - Total diseases processed across all runs
   - Overall success rate
   - High confidence results count

3. **Final commit and push**:
   ```bash
   git add -A
   git commit -m "Finalize run: {total} diseases processed"
   git push
   ```

---

## File Locations

### Input
- `data/disease_codes_Charlie.csv` - 15,163 disease CUI codes

### Output (per run)
- `output/runs/run_{timestamp}/results/{CUI}.json` - Individual disease results
- `output/runs/run_{timestamp}/progress.md` - Batch-by-batch progress
- `output/runs/run_{timestamp}/summary.json` - Final run statistics

### Root Progress
- `progress.md` - Overall progress across all runs

---

## Git Workflow

**IMPORTANT**: Push to git after EVERY batch (not just at the end)!

- **Branch format**: `claude/process-diseases-{start}_{end}-{session_id}`
  - The `{start}_{end}` part indicates the disease index range for this run
  - Must start with `claude/` and end with session ID for push authentication

- **After each batch**: Commit batch results and push
- **After all batches**: Final commit with summary.json and updated progress.md

This ensures incremental progress is saved and visible on GitHub throughout the run.

---

## Command Line Options

When invoked, parse these options:
- `--start-row N`: Start at disease index N (default: 1)
- `--end-row N`: End at disease index N (required)
- `--model MODEL`: Model for Task agents (default: haiku)

Example: `/process-diseases --model haiku --start-row 1 --end-row 100`
