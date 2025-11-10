# Parallel Processing Guide

Process all 15,162 diseases **10x faster** by running parallel sessions!

## Why Parallel?

- ✅ **No file conflicts**: Each CUI gets unique filename (e.g., `C0018099.json`)
- ✅ **Non-overlapping ranges**: Different sessions process different rows
- ✅ **Separate output dirs**: Each session writes to its own directory
- ✅ **No shared state**: Completely independent processing

## Strategy: 10 Parallel Sessions

Split 15,162 diseases into 10 parallel batches of ~1,516 diseases each:

```bash
# Session 1: rows 0-1516
python scripts/batch_processor.py --start-row 0 --end-row 1516 \
  --output-dir parallel_batch_01 --non-interactive

# Session 2: rows 1516-3032
python scripts/batch_processor.py --start-row 1516 --end-row 3032 \
  --output-dir parallel_batch_02 --non-interactive

# Session 3: rows 3032-4548
python scripts/batch_processor.py --start-row 3032 --end-row 4548 \
  --output-dir parallel_batch_03 --non-interactive

# Session 4: rows 4548-6064
python scripts/batch_processor.py --start-row 4548 --end-row 6064 \
  --output-dir parallel_batch_04 --non-interactive

# Session 5: rows 6064-7580
python scripts/batch_processor.py --start-row 6064 --end-row 7580 \
  --output-dir parallel_batch_05 --non-interactive

# Session 6: rows 7580-9096
python scripts/batch_processor.py --start-row 7580 --end-row 9096 \
  --output-dir parallel_batch_06 --non-interactive

# Session 7: rows 9096-10612
python scripts/batch_processor.py --start-row 9096 --end-row 10612 \
  --output-dir parallel_batch_07 --non-interactive

# Session 8: rows 10612-12128
python scripts/batch_processor.py --start-row 10612 --end-row 12128 \
  --output-dir parallel_batch_08 --non-interactive

# Session 9: rows 12128-13644
python scripts/batch_processor.py --start-row 12128 --end-row 13644 \
  --output-dir parallel_batch_09 --non-interactive

# Session 10: rows 13644-15162
python scripts/batch_processor.py --start-row 13644 --end-row 15162 \
  --output-dir parallel_batch_10 --non-interactive
```

## How to Run

### Option 1: Multiple Terminal Windows/Tabs

1. Open 10 terminal windows
2. Copy one command into each terminal
3. Run all simultaneously
4. Each generates Task prompts - process them in parallel

### Option 2: Multiple Claude Code Sessions

1. Open 10 Claude Code web sessions (or terminals)
2. Navigate to project directory in each
3. Run one batch_processor command per session
4. When script outputs Task prompts, launch Task agents in that session
5. Process continues independently

### Option 3: Background Jobs (Linux/Mac)

```bash
# Launch all 10 in background
python scripts/batch_processor.py --start-row 0 --end-row 1516 \
  --output-dir parallel_batch_01 --non-interactive &

python scripts/batch_processor.py --start-row 1516 --end-row 3032 \
  --output-dir parallel_batch_02 --non-interactive &

# ... repeat for all 10
# Monitor with: jobs
```

## Merging Results

After all parallel sessions complete, merge results into single directory:

```bash
# Create final results directory
mkdir -p output/final_results

# Copy all JSON results
cp output/runs/parallel_batch_*/results/*.json output/final_results/

# Verify count
ls output/final_results/*.json | wc -l
# Should output: 15162

# Check for duplicates (should be 0)
ls output/final_results/*.json | xargs basename -a | sort | uniq -d | wc -l
```

## Commit Strategy for Parallel Processing

Since you're processing in parallel, commit each batch as it completes:

```bash
# After batch 1 completes
git add output/runs/parallel_batch_01/results/*.json
git commit -m "Add parallel batch 1: rows 0-1516 (1516 diseases)"
git push

# After batch 2 completes
git add output/runs/parallel_batch_02/results/*.json
git commit -m "Add parallel batch 2: rows 1516-3032 (1516 diseases)"
git push

# ... etc
```

This ensures incremental progress is saved to GitHub.

## Cost Estimation

### With Sonnet:
- ~$0.10-0.15 per disease
- 15,162 diseases × $0.12 = **~$1,800-2,200**
- Parallel processing doesn't change cost, just time

### With Haiku:
- ~$0.005-0.01 per disease
- 15,162 diseases × $0.007 = **~$100-150**
- **~95% cost savings vs Sonnet**

## Testing Haiku Cost Savings

Before processing all 15k diseases with Haiku, test quality on a small batch:

```bash
# Test batch with Haiku
python scripts/batch_processor.py --start-row 15 --end-row 65 \
  --output-dir haiku_test --non-interactive
```

Then launch Task agents with `--model haiku`:
- Compare incidence estimates to your existing 15 Sonnet results
- Check confidence score calibration
- Verify umbrella term detection
- Review reasoning quality

If Haiku quality is acceptable → use it for all 15k diseases and save ~$1,500-2,000!

## Monitoring Progress

Track progress across parallel sessions:

```bash
# Count total processed
find output/runs/parallel_batch_*/results -name "*.json" | wc -l

# Check each batch
for i in {01..10}; do
  count=$(ls output/runs/parallel_batch_$i/results/*.json 2>/dev/null | wc -l)
  echo "Batch $i: $count diseases"
done

# Summary
echo "Total processed: $(find output/runs/parallel_batch_*/results -name "*.json" | wc -l) / 15162"
```

## Estimated Timeline

### Serial Processing (1 session):
- ~10-20 diseases per batch (parallel Task agents within batch)
- ~152 batches × 5 min/batch = **12-15 hours total**

### Parallel Processing (10 sessions):
- Same per-session rate
- **~1.2-1.5 hours total** (10x speedup!)

## Troubleshooting

**Q: Can sessions interfere with each other?**
A: No! Each uses separate `--output-dir`, so files never conflict.

**Q: What if one session fails?**
A: Just rerun that specific session. Others are unaffected.

**Q: How do I know which ranges to use?**
A: Use the commands above - they're pre-calculated to split 15,162 evenly.

**Q: Can I run more than 10 parallel sessions?**
A: Yes! Just split ranges further. Could do 20 sessions of ~750 diseases each.

## Next Steps

1. **Test Haiku first** (rows 15-65) to decide on model
2. **Choose parallel strategy** (10 sessions recommended)
3. **Launch all sessions** simultaneously
4. **Commit incrementally** as batches complete
5. **Merge results** when all done
6. **Verify count** matches 15,162

Good luck! 🚀
