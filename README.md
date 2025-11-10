# CUI Disease Incidence Processing

Automated batch processing system for mapping UMLS CUI disease codes to global incidence rates using Claude Code.

## Overview

This system processes thousands of disease codes from pharmaceutical patents and maps them to global disease incidence rates (per 100k person-years) with confidence scoring and hierarchy detection.

**Key Features:**
- ✅ Batch processing in groups of 100 (configurable)
- ✅ Parallel Task agents using `cui-incidence-mapper_2` skill
- ✅ Checkpoint/resume functionality
- ✅ Isolated timestamped runs
- ✅ Aggregate estimates for umbrella terms
- ✅ Progress tracking and logging

## Quick Start

### 1. In Claude Code CLI

```bash
# Navigate to project directory
cd cui_disease_incidence_processing

# Run the processor
python scripts/batch_processor.py
```

### 2. In Claude Code Web

Open the project and type:
```
/process-diseases
```

The script will print Task prompts for each disease in the batch. Copy and run them in Claude Code Web.

## Project Structure

```
cui_disease_incidence_processing/
├── .claude/
│   ├── commands/
│   │   └── process-diseases.md       # Slash command
│   └── skills/
│       └── cui-incidence-mapper_2/   # Incidence mapping skill
├── scripts/
│   └── batch_processor.py            # Main processing script
├── data/
│   └── disease_codes_Charlie.csv     # Input: CUI codes & names
├── output/
│   └── runs/                         # Output runs
│       ├── run_2025-11-10_12-34-56/
│       │   ├── results/              # JSON results per CUI
│       │   ├── checkpoint.json       # Progress tracking
│       │   ├── progress.log          # Detailed log
│       │   └── summary.json          # Final statistics
│       └── ...
└── README.md
```

## Usage

### Basic Commands

```bash
# Start new run
python scripts/batch_processor.py

# Resume from checkpoint
python scripts/batch_processor.py --resume

# Check status
python scripts/batch_processor.py --status

# Process specific range
python scripts/batch_processor.py --start-row 1000 --end-row 2000

# Custom batch size
python scripts/batch_processor.py --batch-size 50

# Custom output directory
python scripts/batch_processor.py --output-dir test_run_v2
```

### Slash Command

In Claude Code Web, type:
```
/process-diseases
```

This will show the documentation and command options.

## How It Works

1. **Read CSV**: Loads disease codes from `data/disease_codes_Charlie.csv`
2. **Batch Processing**: Splits into batches of 100
3. **Generate Prompts**: Creates Task prompts for each disease
4. **User Runs Tasks**: You copy/paste prompts into Claude Code
5. **Agents Process**: Each Task agent loads `cui-incidence-mapper_2` skill
6. **Save Results**: JSON files saved to `output/runs/run_TIMESTAMP/results/`
7. **Checkpoint**: Progress saved after each batch
8. **Resume**: Can continue if interrupted

## Input Format

CSV file with columns:
- `CUI`: UMLS Concept Unique Identifier
- `STR`: Disease name/string
- `val`: Provided incidence number (optional)

Example:
```csv
CUI,STR,val
C0009443,Common Cold,9685009838
C0040425,Acute tonsillitis,6456673226
```

## Output Format

Each disease gets a JSON file in `results/`:

```json
{
  "cui": "C0009443",
  "cui_name": "Common Cold",
  "incidence_per_100k": 350000,
  "total_cases_per_year": 28000000000,
  "confidence": 0.9,
  "is_subtype": true,
  "parent_disease": "Upper Respiratory Tract Infection",
  "reasoning": "Common cold is highly prevalent with adults averaging 2-3 episodes...",
  "data_quality": "strong",
  "geographic_variation": "low"
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

For broad categories like "Respiration Disorders", the system provides aggregate BOTEC estimates:

```json
{
  "cui": null,
  "cui_name": "Respiration Disorders",
  "incidence_per_100k": 8500,
  "total_cases_per_year": 680000000,
  "confidence": 0.25,
  "reasoning": "Aggregate BOTEC summing: URI (5000), bronchitis (1500), pneumonia (1000)..."
}
```

## Checkpoint & Resume

After each batch, a checkpoint is saved:

```json
{
  "last_completed_batch": 4,
  "last_completed_row": 400,
  "total_rows": 15000,
  "completed_cuis": ["C0001", "C0002", ...],
  "failed_cuis": ["C0123"],
  "timestamp": "2025-11-10T12:34:56",
  "batch_size": 100
}
```

To resume:
```bash
python scripts/batch_processor.py --resume
```

## Workflow for Claude Code Web

1. Open project in Claude Code Web
2. Run: `python scripts/batch_processor.py`
3. Script prints batch of Task prompts
4. Copy each Task prompt
5. Paste and run in Claude Code Web
6. Wait for all 100 agents to complete
7. Press ENTER in the script to continue
8. Repeat for next batch

## Examples

### Test with small sample

```bash
# Process first 500 rows only
python scripts/batch_processor.py --end-row 500
```

### Resume interrupted run

```bash
# Pick up where you left off
python scripts/batch_processor.py --resume
```

### Check progress

```bash
python scripts/batch_processor.py --status
```

Output:
```
Latest run: run_2025-11-10_12-34-56
Last completed batch: 5
Last completed row: 500
Completed CUIs: 450
Failed CUIs: 50
```

### Custom batch size for testing

```bash
# Process in smaller batches
python scripts/batch_processor.py --batch-size 10 --end-row 100
```

## Troubleshooting

**Issue**: Task agents don't have the skill

**Solution**: The skill is in `.claude/skills/cui-incidence-mapper_2/`. Each Task prompt explicitly tells agents to use this skill.

---

**Issue**: Can't resume from checkpoint

**Solution**: Make sure you're in the same directory and run with `--resume` flag:
```bash
python scripts/batch_processor.py --resume
```

---

**Issue**: Results missing for some CUIs

**Solution**: Check `checkpoint.json` for `failed_cuis` list. Re-run those manually or adjust batch size.

## Tips

- **Start small**: Test with `--end-row 100` first
- **Monitor progress**: Check `progress.log` for detailed logging
- **Batch size**: Adjust based on your system (50-100 works well)
- **Resume frequently**: The system checkpoints after each batch
- **Review failures**: Check `failed_cuis` in summary.json

## Output Analysis

After completion, check `summary.json`:

```json
{
  "run_directory": "output/runs/run_2025-11-10_12-34-56",
  "timestamp": "2025-11-10T14:22:33",
  "total_diseases": 15000,
  "completed": 14850,
  "failed": 150,
  "success_rate": 0.99,
  "failed_cuis": ["C0123", "C0456", ...]
}
```

## License

MIT

## Questions?

Open an issue or check the skill documentation in `.claude/skills/cui-incidence-mapper_2/SKILL.md`
