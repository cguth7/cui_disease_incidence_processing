# CUI Disease Incidence Processing

**Orchestrator-driven system for mapping UMLS CUI disease codes to global incidence rates with source tracking and confidence scoring.**

## Overview

This system processes disease codes from pharmaceutical patents and maps them to global disease incidence rates (per 100k person-years). It uses Claude Code's orchestrator pattern with batch processing agents for efficient, verifiable epidemiological data collection.

**Key Features:**
- ✅ **Orchestrator-driven**: You communicate with Claude, who manages everything
- ✅ **Batch processing**: 5 diseases per agent (5x more efficient)
- ✅ **Source tracking**: Every estimate includes citations and URLs
- ✅ **Deterministic output**: Always `output/current_run/` - zero ambiguity
- ✅ **Incremental git commits**: Progress saved every 50 diseases
- ✅ **Confidence scoring**: Data quality assessment (0.0-1.0 scale)
- ✅ **Hierarchy detection**: Identifies disease subtypes and parent conditions

---

## Quick Start

### Process Diseases (Orchestrator-Driven)

Simply tell Claude what you want to process:

```
Process diseases 4001-5000
```

**Claude will:**
1. Archive any previous run to `output/archive/`
2. Create fresh `output/current_run/` directory
3. Create git branch: `claude/process-diseases-4001-5000`
4. Process in batches of 50 diseases (10 agents × 5 diseases each)
5. Report back after each batch
6. Commit + push every 50 diseases
7. Generate final summary when complete

**You can:**
- Monitor progress in real-time
- Ask questions between batches
- Pause/resume as needed
- Review the PR before merging to main

---

## Project Structure

```
cui_disease_incidence_processing/
├── README.md                    # This file
├── PROGRESS.md                  # Master progress tracking (always updated)
├── data/
│   └── disease_codes_Charlie.csv    # 15,163 UMLS CUI codes
├── output/
│   ├── archive/                     # Previous runs (timestamped)
│   │   ├── run_2025-11-10_15-19-09/
│   │   └── run_2025-11-10_18-31-40/
│   └── current_run/                 # Active run (deterministic path!)
│       ├── progress.md              # Detailed batch-by-batch log
│       ├── results/                 # Individual disease JSON files
│       │   ├── C0011849.json
│       │   ├── C0018099.json
│       │   └── ... (one per CUI)
│       └── summary.json             # Generated at completion
├── .claude/
│   ├── settings.local.json          # Git permissions
│   └── skills/
│       └── cui-incidence-mapper_2/  # Batch processing skill
│           └── SKILL.md             # Agent instructions
└── .gitignore
```

**Key Insight:** `output/current_run/` is ALWAYS the active directory. No timestamps, no ambiguity.

---

## How It Works

### Architecture

```
┌─────────────────────────────────┐
│   YOU (User)                    │
│   "Process diseases 4001-5000"  │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│   CLAUDE (Orchestrator)         │
│   - Creates current_run/        │
│   - Launches processing agents  │
│   - Aggregates results          │
│   - Reports back to you         │
│   - Commits to git              │
└────────────┬────────────────────┘
             │
             │ (10 agents × 5 diseases each)
             ↓
┌─────────────────────────────────┐
│   PROCESSING AGENTS (Haiku)     │
│   - Use cui-incidence-mapper_2  │
│   - Process 5 CUIs in batch     │
│   - Include source citations    │
│   - Write JSON files            │
└─────────────────────────────────┘
```

### Workflow Example

**You say:**
> "Process diseases 4001-5000"

**Claude responds:**
> "Starting new run for diseases 4001-5000 (1000 total)
> - Archived previous run to output/archive/run_2025-11-10_15-19-09/
> - Created fresh output/current_run/
> - Branch: claude/process-diseases-4001-5000
> - Processing in 20 batches of 50 diseases each
>
> Launching batch 1 (diseases 4001-4050) via 10 agents..."

[Agents process in parallel]

**Claude reports:**
> "Batch 1 complete: 50/1000 (5%)
> - Mappable: 42 diseases
> - Unmappable: 8 diseases
> - High confidence: 28 results
> - Needs review: 3 diseases (showing questionable estimates)
> - Committed and pushed to branch
> - PROGRESS.md updated
>
> Continuing with batch 2..."

[Repeats for all 20 batches]

**Final report:**
> "Run complete! 1000/1000 diseases processed (100%)
> - Results: output/current_run/results/ (1000 JSON files)
> - Summary: output/current_run/summary.json
> - All batches committed to branch: claude/process-diseases-4001-5000
> - Ready to merge PR to main"

---

## Output Format

### Individual Disease JSON

Each disease gets a JSON file in `output/current_run/results/{CUI}.json`:

```json
{
  "cui": "C0011849",
  "cui_name": "Diabetes Mellitus",
  "incidence_per_100k": 16.5,
  "total_cases_per_year": 1320000,
  "confidence": 0.8,
  "is_subtype": false,
  "parent_disease": null,
  "reasoning": "Global diabetes incidence from IDF 2005 reports...",
  "data_quality": "strong",
  "geographic_variation": "moderate",
  "source": "IDF Diabetes Atlas 2005",
  "source_url": "https://diabetesatlas.org/...",
  "source_type": "registry",
  "year_specific": true,
  "data_year": 2005
}
```

**Key Fields:**
- `incidence_per_100k`: New cases per 100,000 person-years
- `confidence`: 0.0-1.0 (data quality/reliability)
- `source`: Citation for the estimate
- `source_url`: Link to verify the data
- `source_type`: registry | literature | estimate

### Summary Statistics

`output/current_run/summary.json`:

```json
{
  "total_diseases": 1000,
  "completed": 920,
  "unmappable": 80,
  "success_rate": 0.92,
  "confidence_distribution": {
    "high (0.7-1.0)": 590,
    "medium (0.3-0.7)": 250,
    "low (0.1-0.3)": 80,
    "unmappable (0.0)": 80
  },
  "subtypes_identified": 450,
  "data_sources": {
    "registry": 520,
    "literature": 350,
    "estimate": 50,
    "unmappable": 80
  }
}
```

---

## Progress Tracking

### Two Progress Files

**1. `PROGRESS.md` (Root - Master Summary)**

Always updated, shows:
- Current run status
- Overall statistics
- Historical runs in archive

**2. `output/current_run/progress.md` (Detailed Log)**

Batch-by-batch details:
- Batch 1: Diseases 4001-4050 ✓ (50 diseases)
- Batch 2: Diseases 4051-4100 ✓ (50 diseases)
- Complete CUI lists
- Timestamps
- Mappable vs unmappable counts

---

## Git Workflow

### Branch Strategy

One feature branch per run:
```
claude/process-diseases-{start}-{end}

Example: claude/process-diseases-4001-5000
```

### Commit Pattern

**Every 50 diseases:**
```bash
git add PROGRESS.md output/current_run/
git commit -m "Batch X: Process diseases {start}-{end} ({completed}/{total})"
git push origin claude/process-diseases-4001-5000
```

**Files committed:**
- `PROGRESS.md` (master progress)
- `output/current_run/progress.md` (detailed log)
- `output/current_run/results/*.json` (new disease files)

**End of run:**
- Final commit includes `output/current_run/summary.json`
- PR is ready to merge to main
- You review and merge when satisfied

---

## Data Quality

### Confidence Scoring

| Score | Meaning | Example |
|-------|---------|---------|
| **0.8-1.0** | Strong | Cancer registry data (GLOBOCAN) |
| **0.6-0.8** | Moderate-High | Published cohort studies |
| **0.3-0.6** | Moderate | Case reports, limited registries |
| **0.1-0.3** | Low | Rare diseases, sparse data |
| **0.0** | Unmappable | Umbrella terms, non-diseases |

### Source Types

- **registry**: Cancer registries, WHO databases, CDC surveillance
- **literature**: Published peer-reviewed studies
- **estimate**: Back-of-envelope calculations (BOTEC) for umbrella terms

### Unmappable Categories

Some CUIs cannot be mapped to meaningful incidence:
- **Umbrella terms**: "Neoplasms" (too broad)
- **Pathology descriptors**: "Invasive Carcinoma" (no organ specified)
- **Biological processes**: "Carcinogenesis" (not a disease)
- **Functional terms**: "Cerebellar function" (not pathology)
- **Research models**: "Ehrlich Tumor" (mouse model, not human disease)

---

## Input Data

### CSV Format

`data/disease_codes_Charlie.csv` (15,163 rows):

| disease_id | diseaseid | diseasename |
|------------|-----------|-------------|
| 1 | C0018099 | Gout |
| 2 | C0011849 | Diabetes Mellitus |
| ... | ... | ... |

**Column Descriptions:**
- `disease_id`: Sequential ID (1-15,163)
- `diseaseid`: UMLS CUI code (Concept Unique Identifier)
- `diseasename`: Disease name

---

## Advanced Usage

### Resume Processing

If interrupted, Claude can resume:

```
Resume processing from disease 4500
```

Claude will check PROGRESS.md and continue from where it left off.

### Custom Ranges

Process specific subsets:

```
Process diseases 1-1000
Process diseases 10000-11000
```

### Review Questionable Results

After each batch, Claude flags low-confidence results:

```
Review these 3 questionable mappings:
1. C0123456 (confidence: 0.25) - Limited data
2. C0234567 (confidence: 0.15) - Rare syndrome
3. C0345678 (confidence: 0.0) - Unmappable umbrella term
```

---

## Skill Details

### cui-incidence-mapper_2

**Location:** `.claude/skills/cui-incidence-mapper_2/SKILL.md`

**Input:** Array of 5 CUIs
```json
["C0011849", "C0018099", "C0012345", "C0023456", "C0034567"]
```

**Output:** Array of 5 results with source tracking

**Processing Logic:**
1. Research each disease in medical literature
2. Find incidence data (prioritize 2005 if available)
3. Assess confidence based on data quality
4. Identify if disease is a subtype of another condition
5. Include source citation and URL
6. Return structured JSON

---

## Troubleshooting

### "No diseases found in range"

The CSV only has 15,163 diseases. Ensure your range is valid:
```
Valid: Process diseases 1-1000 ✅
Invalid: Process diseases 20000-21000 ❌
```

### "Git push failed"

Check that `.claude/settings.local.json` allows git operations.

### "Branch already exists"

Archive the current run and Claude will create a fresh branch.

---

## Contributing

When adding new features:
1. Keep output in `output/current_run/` (deterministic!)
2. Update `PROGRESS.md` on every commit
3. Include source tracking in any new data fields
4. Document in this README

---

## License

Proprietary - For pharmaceutical patent analysis use only.
