"""
1. Merges train correction CSVs into one
2. Applies corrections (pred-correct / both-wrong) to best_manifests
3. Re-runs eval for all results_v3 folders using updated manifests
"""
import os, sys, json, csv, shutil
from collections import defaultdict

sys.path.insert(0, "/mnt/data/chaitanya/ocr-finetuning/benchmark")
from benchmark import compute_metrics, FIELDS

VERIFIED_DIR  = "/mnt/data/chaitanya/data/processed/aws/chaitanya_verified"
MANIFESTS_DIR = "/mnt/data/chaitanya/data/processed/aws/best_manifests"
RESULTS_V3    = "/mnt/data/chaitanya/ocr-finetuning/benchmark/results_v3"

TRAIN_CSV_FILES = [
    "corrections_train-2.csv",   # rows 0-59  (most complete for that range)
    "corrections_train-3.csv",   # rows 60-231
    "corrections_train-4.csv",   # rows 233-417
    "corrections_train.csv",     # fallback for anything still blank
]
VAL_CSV = "corrections_val.csv"

# ── 1. Merge train corrections ────────────────────────────────────────────────

def load_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def merge_train_corrections():
    all_rows = [load_csv(os.path.join(VERIFIED_DIR, f)) for f in TRAIN_CSV_FILES]
    n = len(all_rows[0])
    merged = []
    blank = 0
    for i in range(n):
        chosen = None
        for rows in all_rows:
            if rows[i]["verdict"]:
                chosen = rows[i]
                break
        if chosen is None:
            chosen = all_rows[0][i]
            blank += 1
        merged.append(chosen)
    print(f"Train corrections: {n} rows, {n-blank} reviewed, {blank} blank (skipped)")
    return merged

# ── 2. Build correction lookup: basename -> {field: new_gt_value} ─────────────

def build_correction_map(rows):
    """
    For each row:
      pred-correct  → new GT = pred value
      both-wrong    → new GT = corrected_value
      gt-correct    → no change (skip)
      blank         → no change (skip)
    Returns: {basename: {field: new_value}}
    """
    corrections = defaultdict(dict)
    pred_correct = both_wrong = skipped = 0
    for r in rows:
        verdict = r["verdict"]
        if verdict == "pred-correct":
            basename = os.path.basename(r["image"])
            corrections[basename][r["field"]] = r["pred"]
            pred_correct += 1
        elif verdict == "both-wrong":
            val = r["corrected_value"].strip()
            if val:
                basename = os.path.basename(r["image"])
                corrections[basename][r["field"]] = val
                both_wrong += 1
            else:
                skipped += 1  # both-wrong but no correction typed
        # gt-correct / blank → no change
    print(f"  pred-correct: {pred_correct}, both-wrong applied: {both_wrong}, both-wrong skipped (no value): {skipped}")
    return corrections

# ── 3. Patch a manifest file ──────────────────────────────────────────────────

def patch_manifest(src_path, dst_path, corrections):
    updated = 0
    lines_out = []
    with open(src_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            basename = os.path.basename(entry["file_path"])
            if basename in corrections:
                for field, new_val in corrections[basename].items():
                    old_val = entry["data"].get(field)
                    entry["data"][field] = new_val if new_val != "" else None
                    print(f"  [{basename}] {field}: {repr(old_val)} → {repr(entry['data'][field])}")
                updated += 1
            lines_out.append(json.dumps(entry, ensure_ascii=False))
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines_out) + "\n")
    print(f"  Patched {updated} entries → {dst_path}")

# ── 4. Re-run eval for a results folder ──────────────────────────────────────

def reeval(results_dir, gt_manifest_path):
    preds_path   = os.path.join(results_dir, "preds.json")
    results_path = os.path.join(results_dir, "benchmark_results.json")

    with open(preds_path) as f:
        preds = json.load(f)

    # Load updated GT keyed by basename
    gt = {}
    with open(gt_manifest_path) as f:
        for line in f:
            line = line.strip()
            if line:
                e = json.loads(line)
                gt[os.path.basename(e["file_path"])] = e.get("data", {})

    # Merge updated GT into preds
    matched = 0
    for fp, entry in preds.items():
        basename = os.path.basename(fp)
        if basename in gt:
            entry["gt_data"] = gt[basename]
            matched += 1
    print(f"  GT matched: {matched} / {len(preds)}")

    # Recompute metrics
    total    = len(preds)
    errors   = sum(1 for v in preds.values() if v.get("status") == "error")
    empty    = sum(1 for v in preds.values()
                   if v.get("status") == "success"
                   and not any(v.get("pred_fields", {}).get(ff) not in (None, "", "null") for ff in FIELDS))
    overall, responded, logs = compute_metrics(preds)

    result = {
        "summary":           {"total": total, "errors": errors, "empty": empty, "valid": total - errors - empty},
        "overall_metrics":   overall,
        "responded_metrics": responded,
        "per_sample_logs":   logs,
    }
    with open(results_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    # Also save updated preds
    with open(preds_path, "w") as f:
        json.dump(preds, f, indent=2, ensure_ascii=False)
    print(f"  Saved → {results_path}")

    # Print summary
    for label, m in [("OVERALL", overall), ("RESPONDED", responded)]:
        print(f"\n  {label} (n={m['sample_count']}):")
        for field, fm in m["fields"].items():
            print(f"    {field:<15} exact={fm['exact_match_pct']:6.2f}%  char_sim={fm['char_sim']:.4f}")

# ── Main ─────────────────────────────────────────────────────────────────────

print("=" * 60)
print("STEP 1: Merge train corrections")
print("=" * 60)
train_rows = merge_train_corrections()
train_corrections = build_correction_map(train_rows)

print()
print("=" * 60)
print("STEP 2: Load val corrections")
print("=" * 60)
val_rows = load_csv(os.path.join(VERIFIED_DIR, VAL_CSV))
print(f"Val corrections: {len(val_rows)} rows, {sum(1 for r in val_rows if r['verdict'])} reviewed")
val_corrections = build_correction_map(val_rows)

print()
print("=" * 60)
print("STEP 3: Patch manifests")
print("=" * 60)

# Backup originals first
for name in ["manifest_train.jsonl", "manifest_val.jsonl", "manifest_full.jsonl"]:
    src = os.path.join(MANIFESTS_DIR, name)
    bak = src + ".bak"
    if not os.path.exists(bak):
        shutil.copy2(src, bak)
        print(f"Backed up {name}")

print("\nPatching manifest_train.jsonl...")
patch_manifest(
    os.path.join(MANIFESTS_DIR, "manifest_train.jsonl"),
    os.path.join(MANIFESTS_DIR, "manifest_train.jsonl"),
    train_corrections,
)

print("\nPatching manifest_val.jsonl...")
patch_manifest(
    os.path.join(MANIFESTS_DIR, "manifest_val.jsonl"),
    os.path.join(MANIFESTS_DIR, "manifest_val.jsonl"),
    val_corrections,
)

print("\nPatching manifest_full.jsonl (train + val)...")
# full = train + val, patch with both correction sets combined
combined = {**train_corrections}
for basename, fields in val_corrections.items():
    combined.setdefault(basename, {}).update(fields)
patch_manifest(
    os.path.join(MANIFESTS_DIR, "manifest_full.jsonl"),
    os.path.join(MANIFESTS_DIR, "manifest_full.jsonl"),
    combined,
)

print()
print("=" * 60)
print("STEP 4: Re-evaluate all results_v3 folders")
print("=" * 60)

val_manifest   = os.path.join(MANIFESTS_DIR, "manifest_val.jsonl")
train_manifest = os.path.join(MANIFESTS_DIR, "manifest_train.jsonl")

runs = [
    ("hybrid_deepseek_qwen35",       val_manifest),
    ("qwen35",                        val_manifest),
    ("hybrid_deepseek_qwen35_train",  train_manifest),
]

for folder, manifest in runs:
    results_dir = os.path.join(RESULTS_V3, folder)
    if not os.path.exists(os.path.join(results_dir, "preds.json")):
        print(f"\nSkipping {folder} — no preds.json")
        continue
    print(f"\n{'─'*60}")
    print(f"Re-evaluating: {folder}")
    print(f"GT manifest:   {manifest}")
    print(f"{'─'*60}")
    reeval(results_dir, manifest)

print("\nDone.")
