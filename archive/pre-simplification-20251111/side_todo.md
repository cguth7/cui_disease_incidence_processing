# Side TODO - Remaining Work

## Skill Modifications Still Needed

### 1. Update Workflow Section
- **File**: `.claude/skills/cui-incidence-mapper_2/SKILL.md`
- **Section**: "Processing Workflow"
- **Change**: Update to reflect batch processing of 5 diseases instead of single disease processing
- **Current**: Shows single disease workflow
- **Needed**: Batch workflow for array of 5 CUIs

### 2. Update All Example Outputs
- **File**: `.claude/skills/cui-incidence-mapper_2/SKILL.md`
- **Sections**: All example JSON outputs throughout the file
- **Change**: Add source tracking fields to all examples:
  - `"source": "IDF Diabetes Atlas 2005"`
  - `"source_url": "https://diabetesatlas.org/"`
  - `"source_type": "registry"`
- **Current**: Examples missing these 3 fields
- **Needed**: Consistent examples showing source tracking

### 3. Source Type Guidelines
- **File**: `.claude/skills/cui-incidence-mapper_2/SKILL.md`
- **Section**: New section needed after "Data Quality Assessment"
- **Content**: Add guidance on when to use each source_type:
  - **registry**: GLOBOCAN, IDF, WHO surveillance, CDC registries
  - **literature**: Peer-reviewed studies, published cohorts
  - **estimate**: BOTEC calculations for umbrella terms
  - **null**: For unmappable conditions

### 4. Batch Processing Quality Checks
- **File**: `.claude/skills/cui-incidence-mapper_2/SKILL.md`
- **Section**: "Quality Checks"
- **Change**: Add validation for batch mode:
  - Array must have exactly 5 elements
  - Each element must have all required fields
  - Source fields required when confidence > 0.3

## Testing Needed

### 5. Test Batch Mode
- Run a test with 5 diseases to verify:
  - Skill accepts JSON array input
  - Returns array of 5 results
  - Source tracking works
  - File output is valid JSON

### 6. Test Orchestrator Workflow
- Process a small batch (50 diseases) to verify:
  - Branch creation works
  - Git commits every 50 diseases
  - PROGRESS.md updates correctly
  - output/current_run/ structure is correct

## Documentation

### 7. Update .claude/settings.local.json
- Verify git permissions are set
- Remove any slash command references

---

**Priority**: Items 1-3 are cosmetic cleanup. The skill will work as-is but examples won't match the new format.

**Next Steps**: Commit current restructure, then optionally come back to clean up skill examples.
