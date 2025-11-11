# CUI Disease Incidence Processing

Simple orchestration system for mapping UMLS CUI disease codes to global incidence and prevalence rates.

## How This Works

This is designed to be **extremely simple**:

1. **You (Human)**: Assign Claude a batch of diseases to process (e.g., "Process diseases 1-500")
2. **Claude (Orchestrator)**: Breaks the batch into chunks of 5 and launches sub-agents in parallel
3. **Sub-agents**: Process each group of 5 diseases using the cui-incidence-mapper_2 skill, writing results to JSON files
4. **Claude**: After ALL diseases are processed, consolidates to CSV and deletes individual JSONs
5. **Claude**: Commits and pushes ONCE to the branch

## Quick Start

Just tell Claude what to process:

```
Process diseases 1-100
```

or

```
Process diseases 1-500
```

Claude will:
- Create output directory structure
- Launch sub-agents to process diseases in batches of 5
- Monitor rate limits to avoid hitting API limits
- Write individual JSON files for each disease (temporary)
- Consolidate all results into CSV and summary stats
- Delete individual JSON files to keep directory clean
- Push ALL results to git branch when complete (ONE commit, not incremental)

## Project Structure

```
cui_disease_incidence_processing/
├── README.md                          # This file
├── data/
│   └── disease_codes_Charlie.csv      # 15,163 UMLS CUI codes with disease names
├── output/
│   ├── disease_incidence_data.csv     # Consolidated results (all diseases)
│   └── summary_stats.json             # Dataset statistics and metadata
├── .claude/
│   └── skills/
│       └── cui-incidence-mapper_2/    # Sub-agent skill for processing
│           └── SKILL.md               # Complete rubric and instructions
└── archive/                           # Previous iterations of this project
```

## Input Data

`data/disease_codes_Charlie.csv` contains 15,163 diseases:

| disease_id | diseaseid | diseasename |
|------------|-----------|-------------|
| 1 | C0018099 | Gout |
| 2 | C0011849 | Diabetes Mellitus |
| ... | ... | ... |

## Output Format

All results are consolidated into two files:

### 1. `disease_incidence_data.csv`
Consolidated CSV with all processed diseases (one row per disease):

| cui | cui_name | incidence_per_100k | prevalence_per_100k | metric_type | confidence | data_quality | source | ... |
|-----|----------|-------------------|---------------------|-------------|------------|--------------|---------|-----|
| C0011849 | Diabetes Mellitus | 16.5 | 8500 | both | 0.8 | strong | IDF Diabetes Atlas 2005 | ... |
| C0018099 | Gout | 150 | null | incidence | 0.78 | strong | Arromdee E et al. (2002) | ... |

**Key Fields:**
- `incidence_per_100k`: New cases per 100,000 person-years
- `prevalence_per_100k`: Existing cases per 100,000 population
- `metric_type`: "incidence" | "prevalence" | "both" | null
- `confidence`: 0.0-1.0 (data quality/reliability)
- `is_subtype`: Boolean indicating if disease is a subtype
- `parent_disease`: Parent disease name if is_subtype=true
- `reasoning`: Detailed explanation for the estimate
- `source`: Citation for the estimate
- `source_url`: Link to verify the data
- `source_type`: registry | literature | estimate

### 2. `summary_stats.json`
Dataset-level statistics including:
- Total diseases processed
- Confidence score distribution
- Data quality breakdown
- Source type distribution
- Metric type counts
- Top data sources used

## Orchestration Instructions for Claude

### When User Says: "Process diseases X-Y"

**CRITICAL: X-Y refers to CSV ROW NUMBERS, NOT disease_id values!**

Example:
- "Process diseases 1-100" = Extract rows 1-100 from CSV (which will have random disease_id values)
- "Process diseases 2001-3000" = Extract rows 2001-3000 from CSV (NOT disease_id 2001-3000!)

1. **Setup**
   - Read `data/disease_codes_Charlie.csv` to get the disease list
   - **Extract diseases from CSV rows X to Y** (use `sed -n 'X,Yp'` or similar)
   - **DO NOT filter by disease_id column** - that's wrong!
   - Create `output/results/` directory if it doesn't exist

2. **Batch Processing**
   - Break the total list into groups of 5 diseases
   - For a batch of 100: create 20 groups of 5
   - For a batch of 500: create 100 groups of 5

3. **Launch Sub-agents**
   - Launch sub-agents using the Task tool with `cui-incidence-mapper_2` skill
   - Process multiple groups in parallel (watch for rate limits!)
   - Each sub-agent receives 5 CUIs and returns 5 results
   - **Rate Limit Strategy**: Start with 5-10 parallel agents, monitor for errors, adjust as needed

4. **Write Results**
   - Each result from sub-agents should be written to `output/results/{CUI}.json`
   - One file per disease (temporary individual JSON files)

5. **Consolidate Results**
   - **CRITICAL**: After ALL diseases are processed, consolidate:
     - Create `output/disease_incidence_data.csv` with all results (one row per disease)
     - Create `output/summary_stats.json` with dataset statistics
     - Delete the `output/results/` directory and all individual JSON files
   - This keeps the repo clean with just 2 files instead of 500+

6. **Final Commit**
   - **ONLY AFTER consolidation is complete**
   - Commit the consolidated CSV and summary JSON
   - Push to branch ONCE (not incremental!)
   - Branch name: `claude/process-diseases-{X}-{Y}`

### Rate Limiting

- **Conservative approach**: Launch 5-10 agents at a time
- Monitor for rate limit errors
- If rate limited, wait and reduce parallelism
- Goal: Fast but sustainable processing

### Error Handling

- If a sub-agent fails, retry that specific group of 5
- Track which CUIs failed and report to user
- Don't let one failure block the entire batch

## The Skill (Processing Rubric)

All processing rules, confidence scoring, source quality standards, and output formats are defined in:

`.claude/skills/cui-incidence-mapper_2/SKILL.md`

This includes:
- Incidence vs prevalence guidelines
- Confidence scoring rubric (0.0-1.0)
- Source quality tiers
- Hierarchy detection rules
- When to use aggregate estimates vs mark as unmappable

## Example Session

**User:**
> Process diseases 1-100

**Claude:**
> Starting batch processing for diseases 1-100 (100 total diseases)
>
> Creating 20 groups of 5 diseases each...
> Launching 10 agents in parallel to process first 50 diseases...
>
> [Processing happens...]
>
> Batch 1-50 complete. Launching next batch...
>
> [More processing...]
>
> ✓ All 100 diseases processed!
> - Mappable: 87 diseases
> - Unmappable: 13 diseases
> - High confidence (≥0.7): 62 results
>
> Consolidating results...
> ✓ Created disease_incidence_data.csv (100 rows)
> ✓ Created summary_stats.json
> ✓ Deleted 100 individual JSON files
>
> Committing and pushing to branch claude/process-diseases-1-100...
> Done!

## Key Principles

1. **Simple**: No complex batch tracking, no incremental commits, no complicated state management
2. **Parallel**: Use sub-agents to process multiple diseases simultaneously
3. **One push**: Commit everything at the end, not incrementally
4. **Rate-aware**: Don't slam the API, be smart about parallelism
5. **Resilient**: Handle failures gracefully, retry when needed

## Archive

Previous, more complex versions of this project are in `archive/`. We simplified because the original approach was too complicated for what we needed.
