# How to Specify Models for Task Agents

Quick reference for using different models (Haiku, Sonnet, Opus) with Task sub-agents.

## TL;DR

**Main agent (this session)**: Always Sonnet/Opus (you're talking to it now)
**Task sub-agents**: You choose Haiku/Sonnet/Opus when launching them

## The Two-Step Process

### Step 1: Run batch_processor with --model flag

```bash
# For Haiku (cheap, fast)
python scripts/batch_processor.py --model haiku --end-row 100

# For Sonnet (best quality, default)
python scripts/batch_processor.py --model sonnet --end-row 100

# For Opus (highest reasoning, expensive)
python scripts/batch_processor.py --model opus --end-row 100
```

This tells the script to **remind you** which model to use for Task agents.

### Step 2: Launch Task agents with that model

When the batch_processor outputs Task prompts, you tell me (Claude) to launch them **with the specified model**.

## Example Workflow

### Using Haiku (Recommended for Testing):

```bash
# Step 1: Generate batch with Haiku flag
python scripts/batch_processor.py \
  --model haiku \
  --start-row 15 \
  --end-row 65 \
  --output-dir haiku_test \
  --non-interactive
```

**Output will show:**
```
BATCH 1: Ready to process 50 diseases
MODEL: HAIKU
================================================================================
TO PROCESS THIS BATCH:
Launch Task agents with model='haiku' for each disease below.

# Task: Map C0025202 - melanoma (model=haiku)
--------------------------------------------------------------------------------
Use the cui-incidence-mapper_2 skill to map this disease...
...
```

**Step 2: Tell me to launch Task agents:**

> Hey Claude, please launch Task agents with model="haiku" for these 10 diseases in parallel:
>
> [paste the prompts from above]

**I will then invoke:**

```python
Task(subagent_type="general-purpose", model="haiku", description="Map C0025202 - melanoma", prompt="...")
Task(subagent_type="general-purpose", model="haiku", description="Map C0036341 - Schizophrenia", prompt="...")
# ... etc for all 10 diseases
```

## Model Selection Guide

| Model | Use When | Cost/Disease | Speed | Quality |
|-------|----------|--------------|-------|---------|
| **Haiku** | Budget-conscious, good estimates sufficient | ~$0.007 | Fastest | Good |
| **Sonnet** | Balance of cost and quality (default) | ~$0.12 | Medium | Excellent |
| **Opus** | Highest reasoning needed, complex cases | ~$0.50 | Slowest | Best |

## Cost Comparison for Full Dataset

### 15,162 diseases:

- **Haiku**: ~$100-150 total
- **Sonnet**: ~$1,800-2,200 total
- **Opus**: ~$7,500-8,000 total

**Haiku saves ~$1,700 (95%) vs Sonnet!**

## When You Tell Me to Launch Tasks

### ✅ Correct way to request with Haiku:

> "Launch 10 Task agents in parallel with model='haiku' for these diseases: [prompts]"

or

> "Process these diseases using Haiku model: [prompts]"

### ✅ Correct way to request with Sonnet:

> "Launch 10 Task agents in parallel with model='sonnet' for these diseases: [prompts]"

or just

> "Process these diseases: [prompts]"
> (Sonnet is default if not specified)

### ❌ What NOT to do:

Don't just paste the prompts without specifying the model, or I'll use Sonnet by default and you won't get the cost savings!

## Batch Processor Model Flag

The `--model` flag in batch_processor doesn't actually change which model is used - it just:

1. ✅ Prints reminder in output
2. ✅ Labels tasks with the intended model
3. ✅ Helps you remember which model to request when launching Task agents

**You still need to tell me (Claude) to use that model when launching the Task agents!**

## Parallel Processing with Models

### Example: 10 parallel sessions with Haiku

```bash
# Generate commands
python scripts/generate_parallel_commands.py --num-parallel 10 --model haiku

# This outputs commands like:
python scripts/batch_processor.py \
  --start-row 0 --end-row 1516 \
  --model haiku \
  --output-dir haiku_batch_01 \
  --non-interactive
```

Then in each session, when you ask me to launch Task agents, specify `model="haiku"`.

## Testing Before Committing

**Strongly recommended:** Test Haiku on 50 diseases first:

```bash
python scripts/batch_processor.py \
  --model haiku \
  --start-row 15 \
  --end-row 65 \
  --output-dir haiku_test \
  --non-interactive
```

Then ask me to:
> "Launch Task agents with model='haiku' for the diseases in this batch"

Compare results to your existing 15 Sonnet results and decide if quality is acceptable.

## Summary

1. **batch_processor --model flag**: Just a reminder/label
2. **Actual model specification**: When you ask me to launch Task agents
3. **Always specify the model**: When requesting Task agent launches
4. **Test Haiku first**: Before committing to 15k diseases
5. **Parallel + Haiku**: 10x speed + 95% cost savings = 🚀

Questions? See HAIKU_GUIDE.md for detailed testing instructions!
