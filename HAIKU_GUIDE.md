# Using Haiku for Cost Savings

Save ~95% on costs by using Haiku instead of Sonnet for Task agents.

## How It Works

The **main agent** (this Claude Code session) runs on Sonnet/Opus, but you can specify **Haiku for Task sub-agents**.

## Step 1: Test Haiku Quality First

Process 50 test diseases with Haiku to verify quality:

```bash
# Generate test batch with Haiku flag
python scripts/batch_processor.py \
  --start-row 15 \
  --end-row 65 \
  --output-dir haiku_test \
  --model haiku \
  --non-interactive
```

This will output Task prompts with a reminder to use Haiku.

## Step 2: Launch Task Agents with Haiku

When the script outputs Task prompts, launch them like this:

**Using the Task tool (programmatically):**

```python
Task(
    subagent_type="general-purpose",
    description="Map C0025202 - melanoma",
    model="haiku",  # ← This specifies Haiku!
    prompt="""Use the cui-incidence-mapper_2 skill to map this disease...

CUI: C0025202
Disease Name: melanoma
...
"""
)
```

**In this Claude Code session, you would invoke:**

```
I need you to launch Task agents with model="haiku" for the following diseases:
[paste prompts from batch_processor output]
```

## Step 3: Compare Haiku vs Sonnet Results

After processing 50 diseases with Haiku, compare to your existing 15 Sonnet results:

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

If Haiku quality passes your tests, use it for all 15k diseases:

### Parallel Processing with Haiku:

```bash
# Generate parallel commands for Haiku
python scripts/generate_parallel_commands.py \
  --num-parallel 10 \
  --model haiku

# This outputs 10 commands like:
python scripts/batch_processor.py \
  --start-row 0 \
  --end-row 1516 \
  --output-dir haiku_batch_01 \
  --model haiku \
  --non-interactive
```

Then launch Task agents with `model="haiku"` in each session.

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

## Example: Launching Task with Haiku

Here's exactly what you do in this Claude Code session:

```
Please launch 10 Task agents in parallel with model="haiku" for these diseases:

1. C0025202 - melanoma
   [paste full prompt]

2. C0036341 - Schizophrenia
   [paste full prompt]

3. [etc...]
```

I will then invoke:
```python
Task(subagent_type="general-purpose", model="haiku", description="Map C0025202 - melanoma", prompt="...")
Task(subagent_type="general-purpose", model="haiku", description="Map C0036341 - Schizophrenia", prompt="...")
...
```

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
