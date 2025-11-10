# CUI Incidence Mapper Skill

## Installation

1. Download `cui-incidence-mapper.zip`
2. In Claude Code, go to Settings → Skills
3. Click "Upload Skill"
4. Select the zip file
5. The skill will be installed and ready to use

## What's Inside

```
cui-incidence-mapper/
└── SKILL.md (required skill file)
```

## Usage

In any Claude Code session:

```
Using the cui-incidence-mapper skill, map this disease:
CUI: C0030354
Disease Name: Papilloma
```

## What It Does

Maps UMLS CUI disease codes to:
- Global incidence rates (per 100k person-years)
- Confidence scores (0.0 to 1.0)
- Disease hierarchies (subtypes and parents)
- Data quality assessments
- Geographic variation notes

## Batch Processing

Upload a CSV with `CUI` and `STR` columns:

```
Using the cui-incidence-mapper skill, process my_cuis.csv
and output results to cui_results.csv
```

## Output Format

Returns JSON with:
- `incidence_per_100k` - rate, range, "extremely rare", or null
- `confidence` - 0.0 (unmappable) to 1.0 (certain)
- `is_subtype` - boolean
- `parent_disease` - name of broader category
- `reasoning` - explanation
- `data_quality` - strong/moderate/weak/none
- `geographic_variation` - low/moderate/high/unknown

## Key Features

✅ Flags unmappable umbrella terms (confidence = 0.0)  
✅ Identifies disease subtypes and parent categories  
✅ Conservative confidence scoring  
✅ Handles batch processing  
✅ Quality checks and validation  

## Example Output

```json
{
  "cui": "C0011849",
  "cui_name": "Diabetes Mellitus Type 2",
  "incidence_per_100k": 15.2,
  "confidence": 0.95,
  "is_subtype": true,
  "parent_disease": "Diabetes Mellitus",
  "reasoning": "Well-documented global incidence ~15 per 100k (IDF/WHO).",
  "data_quality": "strong",
  "geographic_variation": "moderate"
}
```

## Skill Format

This skill follows the standard Claude Code skill format:
- YAML frontmatter with `name` and `description`
- Concise markdown instructions (<500 lines)
- No extraneous documentation files
- Ready to upload and use

---

Ready to map your 15k CUIs! 🚀
