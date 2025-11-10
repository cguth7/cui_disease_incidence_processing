# Using Haiku for Cost Savings

Save ~95% on costs by using Haiku instead of Sonnet for Task sub-agents.

## How It Works

**You (Charlie)** run the slash command with `--model haiku`
→ **Claude** (the main agent) launches Task sub-agents with Haiku
→ **Task sub-agents** process diseases using Haiku model

## Simple Usage

Just add `--model haiku` to your slash command:

```
/process-diseases --model haiku
```

That's it! Claude will automatically launch all Task agents with Haiku.

## Testing Haiku First (Recommended)

Test with a small batch first:

```
/process-diseases --model haiku --end-row 65
```

This processes first 65 diseases with Haiku. Compare quality to determine if suitable for full run.

## Comparing Haiku vs Sonnet Results

After processing with Haiku, compare to your existing 15 Sonnet results:

### Quality Checks:

1. **Incidence estimates reasonable?**
   - Check a few diseases you know (melanoma, diabetes, etc.)
   - Compare to Sonnet results

2. **Confidence scores well-calibrated?**
   - Are high-confidence estimates actually well-documented diseases?
   - Are low-confidence estimates for rare/uncertain diseases?

3. **Umbrella terms correctly identified?**
   - Check broad categories like "Arthritis" or "Cancer"
   - Should have low confidence (0.2-0.3) and aggregate reasoning

4. **Reasoning quality sufficient?**
   - Does the reasoning explain the estimate?
   - Are data sources mentioned?

### Comparison Script:

```bash
# Check Haiku results
ls output/runs/haiku_test/results/*.json | wc -l

# Sample a few results
cat output/runs/haiku_test/results/C0025202.json  # melanoma
cat output/runs/haiku_test/results/C0036341.json  # schizophrenia

# Compare to Sonnet results
cat output/runs/run_2025-11-10_17-38-14/results/C0018099.json  # Gout (Sonnet)
```

## Cost Comparison

### Full Dataset (15,162 diseases):

| Model | Cost per disease | Total Cost | Quality |
|-------|------------------|------------|---------|
| **Sonnet** | ~$0.12 | **$1,800-2,200** | Best reasoning, highest confidence |
| **Haiku** | ~$0.007 | **$100-150** | Good estimates, faster |

**Savings with Haiku: ~$1,700** (95% reduction)

### When to Use Each Model:

**Use Haiku if:**
- ✅ Budget is limited
- ✅ Test quality is acceptable
- ✅ Speed is important (Haiku is faster)
- ✅ Rough estimates are sufficient

**Use Sonnet if:**
- ✅ Need highest accuracy
- ✅ Complex umbrella term detection critical
- ✅ Detailed reasoning required
- ✅ Budget allows

## Full Production Run with Haiku

If Haiku quality is acceptable, process all 15k diseases:

```
/process-diseases --model haiku
```

Or for parallel processing, run 10 sessions with:

```
/process-diseases --model haiku --start-row 0 --end-row 1516 --output-dir haiku_batch_01
/process-diseases --model haiku --start-row 1516 --end-row 3032 --output-dir haiku_batch_02
... (etc for 10 parallel sessions)
```

### Cost Estimate with Haiku:

- 15,162 diseases × $0.007 = **~$106**
- Processing time: ~1.5 hours (10 parallel sessions)
- **Total savings: ~$1,700 vs Sonnet**

## Hybrid Approach (Best of Both)

Process most with Haiku, use Sonnet for uncertain cases:

1. **Run all with Haiku first** (~$100)
2. **Identify low-confidence results** (confidence < 0.4)
3. **Re-process low-confidence with Sonnet** (~$50-100 for ~500-1000 diseases)
4. **Total cost: ~$150-200** (still 90% savings!)

### Script to find low-confidence results:

```bash
# Find all low-confidence results
find output/runs/haiku_batch_*/results -name "*.json" -exec \
  python3 -c "import json, sys; \
    data = json.load(open(sys.argv[1])); \
    print(sys.argv[1]) if data.get('confidence', 1) < 0.4 else None" {} \;
```

## Behind the Scenes

When you run `/process-diseases --model haiku`:

1. The slash command tells Claude to use Haiku for Task agents
2. batch_processor.py runs and outputs prompts with MODEL: HAIKU label
3. Claude sees this and automatically launches Task agents with `model="haiku"`
4. Results are saved with Haiku-generated estimates
5. You save ~95% on costs!

## Monitoring Haiku Performance

Track quality metrics as you process:

```bash
# Average confidence score
find output/runs/haiku_batch_*/results -name "*.json" -exec \
  python3 -c "import json, sys; print(json.load(open(sys.argv[1])).get('confidence', 0))" {} \; | \
  awk '{sum+=$1; n++} END {print "Average confidence:", sum/n}'

# Distribution by data quality
find output/runs/haiku_batch_*/results -name "*.json" -exec \
  python3 -c "import json, sys; print(json.load(open(sys.argv[1])).get('data_quality', 'unknown'))" {} \; | \
  sort | uniq -c

# Count umbrella terms (should be flagged with low confidence)
grep -r "umbrella" output/runs/haiku_batch_*/results/*.json | wc -l
```

## Recommendation

**Best strategy:**

1. ✅ Test Haiku on 50 diseases first (rows 15-65)
2. ✅ Review quality carefully
3. ✅ If acceptable → use Haiku for all 15k and save $1,700
4. ✅ If marginal → use hybrid approach (Haiku + Sonnet for uncertain)
5. ✅ If poor quality → use Sonnet for accuracy

Start with the test run to make an informed decision! 🚀
