# CUI Disease Incidence Processing

Maps UMLS CUI disease codes to global incidence rates using Claude Code agents with parallel processing.

## Overview

This system processes disease codes from pharmaceutical patents and maps them to global disease incidence rates (per 100k person-years) with confidence scoring, hierarchy detection, and year-specific data tracking (prioritizing 2005 data).

**Key Features:**
- ✅ Agent-based processing: Claude orchestrator → parallel Task agents → JSON files
- ✅ 2005-specific incidence data prioritization (with fallback to general estimates)
- ✅ Parallel batch processing (20-100 diseases at a time)
- ✅ Automatic git commit/push workflow
- ✅ Progress tracking with markdown logs
- ✅ Confidence scoring and hierarchy detection
- ✅ Aggregate estimates for umbrella terms

## Quick Start

### Slash Command (Recommended)

Open the project in Claude Code and run:

```
/process-diseases --model haiku --end-row 100
```

**What happens:**
1. Command expands to instructions for Claude orchestrator (Sonnet)
2. Claude reads the CSV and creates a timestamped output directory
3. Claude launches parallel Task agents (using haiku model for cost efficiency)
4. Each agent researches a disease and writes a JSON file
5. Claude commits and pushes results to git automatically

### Manual Processing (Alternative)

If you prefer manual control, run the Python helper script:

```bash
python scripts/batch_processor.py --end-row 100
```

The script prints Task prompts for you to copy/paste manually into Claude.

## Project Structure

```
cui_disease_incidence_processing/
├── .claude/
│   ├── commands/
│   │   └── process-diseases.md       # Slash command for automated workflow
│   └── skills/
│       └── cui-incidence-mapper_2/   # Skill (prompt instructions for agents)
│           └── SKILL.md              # Instructions for mapping CUIs to incidence
├── scripts/
│   └── batch_processor.py            # Optional: Manual helper script
├── data/
│   └── disease_codes_Charlie.csv     # Input: 15k CUI codes & disease names
├── output/
│   └── runs/                         # Output from each run
│       └── run_2025-11-10_18-31-40/  # Example timestamped run
│           ├── results/              # 100 JSON files (one per disease)
│           ├── progress.md           # Batch-by-batch progress tracking
│           └── summary.json          # Final statistics
├── progress.md                       # Root-level progress across all runs
└── README.md
```

## How It Actually Works

### Architecture

```
You → /process-diseases
  ↓
Claude Sonnet (orchestrator)
  ↓
Reads CSV, creates output directory
  ↓
Launches 20-100 Task agents in parallel (haiku model)
  ↓
Each agent:
  1. Receives CUI + disease name
  2. Reads skill instructions from .claude/skills/cui-incidence-mapper_2/
  3. Researches disease (reasoning, web search if needed)
  4. Writes JSON file to output/runs/run_TIMESTAMP/results/{CUI}.json
  ↓
Claude orchestrator waits for all 20 agents to complete
  ↓
Claude commits batch results to git
  ↓
Repeat for next batch (5 batches total for 100 diseases)
  ↓
Claude generates summary.json and pushes to GitHub
```

**Key Points:**
- **No Python execution** in the slash command workflow (Python script is optional)
- **Skills are just prompt instructions** - not code that executes
- **Agents write JSON files directly** - data doesn't "return" to orchestrator
- **Git workflow** - results committed and pushed automatically

### Slash Command Options

```bash
# Process first 100 diseases (5 batches of 20)
/process-diseases --model haiku --end-row 100

# Process first 500 diseases
/process-diseases --model haiku --end-row 500

# Process diseases 100-200
/process-diseases --model haiku --start-row 100 --end-row 200
```

### Manual Python Script (Alternative)

```bash
# For manual control - prints prompts for you to copy/paste
python scripts/batch_processor.py --end-row 100

# Check status of runs
python scripts/batch_processor.py --status
```

## What Are "Skills"?

Skills in Claude Code are **prompt instructions** stored in `.claude/skills/`. They're not executable code.

When an agent is told to "use the cui-incidence-mapper_2 skill", it:
1. Reads the SKILL.md file (markdown with instructions)
2. Follows those instructions to complete the task
3. Returns results based on the instructions

The `cui-incidence-mapper_2` skill tells agents:
- How to research disease incidence rates
- What data sources to prioritize (GLOBOCAN 2005, WHO reports, etc.)
- How to score confidence (0.0-1.0)
- How to detect disease hierarchies (subtypes vs umbrella terms)
- What JSON format to output

## Input Format

The CSV file `data/disease_codes_Charlie.csv` has 15,163 rows with columns:
- `disease_id`: Sequential ID (1-15163)
- `diseaseid`: UMLS CUI code (e.g., C0018099)
- `diseasename`: Disease name (e.g., "Gout")

Example:
```csv
disease_id,diseaseid,diseasename
1,C0018099,Gout
2,C0020557,Hypertriglyceridemia
3,C0003864,Arthritis
```

## Output Format

Each disease gets a JSON file in `output/runs/run_TIMESTAMP/results/{CUI}.json`:

```json
{
  "cui": "C0018099",
  "cui_name": "Gout",
  "incidence_per_100k": 120,
  "total_cases_per_year": 9600000,
  "confidence": 0.85,
  "year_specific": true,
  "data_year": 2005,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Based on GLOBOCAN 2005 data showing 120 per 100k incidence...",
  "data_quality": "good",
  "geographic_variation": "moderate"
}
```

**New Fields (added for 2005 data tracking):**
- `year_specific`: Boolean - true if 2005-specific data was found
- `data_year`: Number or null - actual year of the data source (2005 if found, other year or null if not)

**For unmappable diseases:**
```json
{
  "cui": "C0001418",
  "cui_name": "Adenocarcinoma",
  "incidence_per_100k": null,
  "confidence": 0.0,
  "year_specific": false,
  "data_year": null,
  "reasoning": "Too generic - adenocarcinoma can occur in many organs with vastly different incidence rates..."
}
```

### Confidence Scoring

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | Strong registry data (WHO, cancer registries) |
| 0.7-0.8 | Good medical literature estimates |
| 0.5-0.6 | Educated guess from disease category |
| 0.3-0.4 | Very uncertain, limited data |
| 0.2-0.3 | **Aggregate umbrella estimate** (BOTEC sum) |
| 0.1-0.2 | Wild guess based on disease class |
| 0.0 | Unmappable - too broad to estimate |

### Umbrella Terms

For broad categories like "Neoplasms", the system provides aggregate BOTEC estimates:

```json
{
  "cui": "C0027651",
  "cui_name": "Neoplasms",
  "incidence_per_100k": 45000,
  "total_cases_per_year": 3600000000,
  "confidence": 0.2,
  "year_specific": false,
  "data_year": null,
  "reasoning": "Aggregate BOTEC summing major cancer types: lung (47), breast (40), colorectal (32)..."
}
```

## Progress Tracking

After processing, check the progress files:

### Root Progress (`progress.md`)
Shows overall progress across all runs:
- Total diseases processed (100 of 15,163 = 0.67%)
- Success rate (92%)
- High confidence results (59)

### Run Progress (`output/runs/run_TIMESTAMP/progress.md`)
Shows batch-by-batch details:
- Which batches are complete
- Mappable vs unmappable per batch
- List of all CUIs processed

### Summary (`output/runs/run_TIMESTAMP/summary.json`)
Final statistics:
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

## Scaling Up

### Current Status
- ✅ Processed: 100 diseases (0.67% of 15k dataset)
- ✅ Success rate: 92%
- ⏳ Remaining: 15,063 diseases

### Processing Larger Batches

You can process 100 diseases at a time instead of 20:

```
/process-diseases --model haiku --start-row 100 --end-row 600
```

This will process diseases 100-600 in 5 batches of 100 agents each (faster than 25 batches of 20).

### Estimated Costs (using haiku model)
- Per disease: ~$0.01-0.02
- 100 diseases: ~$1-2
- 1000 diseases: ~$10-20
- Full 15k dataset: ~$150-300

## 2005 Data Priority

The skill prioritizes finding 2005-specific incidence data:
- **Sources**: GLOBOCAN 2005, WHO 2005 reports, cancer registries circa 2005
- **Fallback**: If 2005 data unavailable, uses best available estimate from any year
- **Tracking**: `year_specific` and `data_year` fields show whether 2005 data was found

**Note**: Currently only batch 5 (diseases 81-100) has the 2005 tracking fields. Batches 1-4 can be reprocessed if needed for consistency.

## Common Unmappable Terms

Based on first 100 diseases, these types are typically unmappable (confidence 0.0):
- Generic pathology terms: "Adenocarcinoma" (without organ specification)
- Biological processes: "Carcinogenesis"
- Overly broad umbrella terms: "Neoplasms" (though we provide BOTEC estimates)
- Umbrella disease categories: "Primary malignant neoplasm"

Success rate: **92%** are successfully mapped to incidence estimates.

## Questions?

- Check the skill documentation: `.claude/skills/cui-incidence-mapper_2/SKILL.md`
- View progress tracking: `progress.md` and `output/runs/*/progress.md`
- Review results: `output/runs/*/results/*.json`
- Check slash command: `.claude/commands/process-diseases.md`
