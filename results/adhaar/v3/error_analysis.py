"""
Error analysis for a benchmark_results.json using two metrics:
  1. Character Mismatch Rate — positional substitution errors after normalization
  2. Extra Character Diff   — length difference after normalization

Usage:
  python error_analysis.py <results_dir>
  python error_analysis.py  # defaults to hybrid_deepseek_qwen35_LoRA_chkpt_1
"""
import json, re, sys, os
from collections import defaultdict

FIELDS = ["name", "dateOfBirth", "gender", "aadharNumber", "address", "pincode", "mobileNumber"]

def normalize(text):
    if text is None:
        return ""
    return re.sub(r'[^a-zA-Z0-9]', '', str(text)).lower()

def char_mismatch_rate(gt, pred):
    gt_n, pred_n = normalize(gt), normalize(pred)
    if not gt_n and not pred_n:
        return None
    if not gt_n:
        return 1.0
    min_len = min(len(gt_n), len(pred_n))
    mismatches = sum(gt_n[i] != pred_n[i] for i in range(min_len))
    return mismatches / len(gt_n)

def extra_char_diff(gt, pred):
    gt_n, pred_n = normalize(gt), normalize(pred)
    if not gt_n and not pred_n:
        return None
    if not gt_n:
        return 1.0
    return abs(len(pred_n) - len(gt_n)) / len(gt_n)

# ── Load data ─────────────────────────────────────────────────────────────────

results_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(__file__), "hybrid_deepseek_qwen35_LoRA_chkpt_1"
)

with open(os.path.join(results_dir, "benchmark_results.json")) as f:
    data = json.load(f)

print(f"Results: {os.path.basename(results_dir)}")
print(f"Samples: {data['summary']['total']}\n")

# ── Per-field aggregates ──────────────────────────────────────────────────────

field_mismatch = defaultdict(list)
field_extra    = defaultdict(list)
field_exact    = defaultdict(list)

worst_mismatch = defaultdict(list)
worst_extra    = defaultdict(list)

for img_path, sample in data["per_sample_logs"].items():
    for field in FIELDS:
        f = sample["fields"].get(field, {})
        gt, pred = f.get("gt"), f.get("pred")
        if gt is None and pred is None:
            continue

        exact = 1 if f.get("exact") == 1 else 0
        field_exact[field].append(exact)

        mr = char_mismatch_rate(gt, pred)
        ed = extra_char_diff(gt, pred)

        if mr is not None:
            field_mismatch[field].append(mr)
            if mr > 0:
                worst_mismatch[field].append((mr, os.path.basename(img_path), gt, pred))
        if ed is not None:
            field_extra[field].append(ed)
            if ed > 0:
                worst_extra[field].append((ed, os.path.basename(img_path), gt, pred))

# ── Summary table ─────────────────────────────────────────────────────────────

print(f"{'Field':<15} {'N':>4} {'Exact%':>8} {'AvgMismatch':>12} {'AvgExtraDiff':>13}")
print("─" * 56)

for field in FIELDS:
    n = len(field_exact[field])
    if n == 0:
        print(f"{field:<15} {'0':>4}")
        continue
    exact_pct = 100 * sum(field_exact[field]) / n
    avg_mm = sum(field_mismatch[field]) / len(field_mismatch[field]) if field_mismatch[field] else 0
    avg_ed = sum(field_extra[field]) / len(field_extra[field]) if field_extra[field] else 0
    print(f"{field:<15} {n:>4} {exact_pct:>7.2f}% {avg_mm:>11.4f} {avg_ed:>12.4f}")

# ── Top-5 worst per field ────────────────────────────────────────────────────

for metric_name, worst_dict in [("MISMATCH", worst_mismatch), ("EXTRA DIFF", worst_extra)]:
    print(f"\n{'='*70}")
    print(f"Top-5 worst {metric_name} errors per field")
    print(f"{'='*70}")
    for field in FIELDS:
        items = sorted(worst_dict[field], key=lambda x: -x[0])[:5]
        if not items:
            continue
        print(f"\n  {field}:")
        for rate, img, gt, pred in items:
            print(f"    {rate:.4f}  GT={repr(gt):<30}  Pred={repr(pred):<30}  [{img}]")

# ── Error type breakdown ──────────────────────────────────────────────────────

print(f"\n{'='*70}")
print("Error type breakdown (non-exact-match samples)")
print(f"{'='*70}")
print(f"{'Field':<15} {'Errors':>6} {'Pure Subst':>11} {'Pure Len':>9} {'Both':>6} {'GT/Pred null':>13}")
print("─" * 62)

for field in FIELDS:
    errors = []
    for img_path, sample in data["per_sample_logs"].items():
        f = sample["fields"].get(field, {})
        gt, pred = f.get("gt"), f.get("pred")
        if gt is None and pred is None:
            continue
        if f.get("exact") == 1:
            continue
        if f.get("exact") is None:
            continue
        mr = char_mismatch_rate(gt, pred)
        ed = extra_char_diff(gt, pred)
        errors.append((mr or 0, ed or 0, gt, pred))

    if not errors:
        continue

    pure_subst = sum(1 for mr, ed, g, p in errors if mr > 0 and ed == 0)
    pure_len   = sum(1 for mr, ed, g, p in errors if mr == 0 and ed > 0)
    both       = sum(1 for mr, ed, g, p in errors if mr > 0 and ed > 0)
    null_issue = sum(1 for mr, ed, g, p in errors if (g is None) != (p is None))

    print(f"{field:<15} {len(errors):>6} {pure_subst:>11} {pure_len:>9} {both:>6} {null_issue:>13}")
