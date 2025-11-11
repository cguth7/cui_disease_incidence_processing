# Archived Run: 2025-11-11

## Reason for Archival
This run was archived due to **source quality issues** identified during processing.

## Issues Found
- **Low-quality sources**: Commercial/advocacy websites used as primary sources
- **Vague citations**: Sources like "American Hemochromatosis Society" without primary literature
- **Inflated confidence scores**: Diseases with weak sources receiving confidence ≥ 0.6
- **Example**: Hemochromatosis Type 1 cited an iron detector vendor site with 0.68 confidence

## Action Taken
1. Updated skill definition (`cui-incidence-mapper_2`) with strict source quality standards:
   - Tier 1 (≥0.7 confidence): Registry data or exact peer-reviewed citations required
   - Tier 2 (max 0.6): Regional registries, textbooks citing primary sources
   - Tier 3 (max 0.4): Advocacy orgs, secondary literature
   - Unacceptable (≤0.3): Commercial sites, uncited sources

2. Archived all work from this run
3. Starting fresh with updated standards

## Files Archived
- `run_2025-11-11_00-00-00/` - 50 disease results with quality issues
- `batch_input.json` - Input batch configurations
- `batch_results.json` - Raw batch results

## Next Steps
Reprocess diseases 300-399 with strict source quality requirements.
