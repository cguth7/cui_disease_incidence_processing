---
description: Process CUI disease codes in batches with incidence mapping
---

# STEP 1: READ THE README FIRST

**CRITICAL: Before doing ANYTHING else, use the Read tool to read README.md in its entirety.**

The README explains:
- Project structure and workflow
- How the cui-incidence-mapper_2 skill works
- Input/output formats
- The batch processing system

**DO NOT proceed until you have read and understood the README.**

---

# STEP 2: Understand the Workflow

## IMPORTANT: The batch_processor.py script is for MANUAL/INTERACTIVE use

The `scripts/batch_processor.py` script is designed for **human users** who want to:
1. Run the script
2. Copy/paste Task prompts manually into Claude
3. Press ENTER to continue after each batch

**This does NOT work for automated Claude processing** because:
- The script calls `input()` to wait for human interaction
- It prints prompts expecting manual copy/paste
- Claude cannot interact with `input()` prompts

---

# STEP 3: For Automated Claude Processing

**To process diseases automatically, you should:**

1. **Create a timestamped output directory:**
   ```
   output/runs/run_YYYY-MM-DD_HH-MM-SS/results/
   ```

2. **Read the CSV directly** using Python csv module:
   - File: `data/disease_codes_Charlie.csv`
   - Columns: `disease_id`, `diseaseid` (CUI code), `diseasename`

3. **For each disease, launch a Task agent** with the haiku model:
   - Use `Task` tool with `subagent_type="general-purpose"`
   - Set `model="haiku"` for cost efficiency
   - Pass the prompt telling agent to use `cui-incidence-mapper_2` skill
   - Save results to `output/runs/run_TIMESTAMP/results/{CUI}.json`

4. **Process in batches** (e.g., 50-100 at a time):
   - Launch multiple Task agents in parallel (single message with multiple tool calls)
   - Wait for all agents to complete
   - Save checkpoint after each batch
   - Continue to next batch

5. **Generate summary** when complete:
   - Count successes/failures
   - Create summary.json with statistics

---

# Example Workflow for Claude

```python
# 1. Read CSV
import csv
diseases = []
with open('data/disease_codes_Charlie.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        diseases.append({
            'cui': row['diseaseid'],
            'name': row['diseasename']
        })

# 2. Create output directory
from pathlib import Path
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_dir = Path(f"output/runs/run_{timestamp}/results")
output_dir.mkdir(parents=True, exist_ok=True)

# 3. Process in batches - launch Task agents
# For each disease, launch Task with prompt:
# "Use the cui-incidence-mapper_2 skill to map this disease to global incidence rates.
# CUI: {cui}
# Disease Name: {name}
# Save JSON result to: {output_dir}/{cui}.json"
```

---

# Manual Processing (Human Users)

If you want to process manually using the interactive script:

```bash
# Process first 500 rows
python scripts/batch_processor.py --end-row 500

# Resume from checkpoint
python scripts/batch_processor.py --resume

# Check status
python scripts/batch_processor.py --status
```

The script will print Task prompts that you copy/paste into Claude manually.
