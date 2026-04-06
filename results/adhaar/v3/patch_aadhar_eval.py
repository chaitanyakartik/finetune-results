"""
Patches benchmark_results.json in-place with corrected aadharNumber evaluation.
Normalization: strip all whitespace, uppercase, if 4 chars prepend 8 X's.
"""
import json
import re
import copy
from difflib import SequenceMatcher

def normalize_aadhar(s):
    if s is None:
        return None
    s = re.sub(r'\s+', '', str(s)).upper()
    if len(s) == 4:
        s = 'X' * 8 + s
    return s

def char_sim(a, b):
    if a is None and b is None:
        return 1.0
    if a is None or b is None:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()

def recompute_field_metrics(data):
    changed = 0
    for img_path, sample in data["per_sample_logs"].items():
        fields = sample.get("fields", {})
        if "aadharNumber" not in fields:
            continue
        info = fields["aadharNumber"]
        gt_raw  = info.get("gt")
        pred_raw = info.get("pred")

        gt_norm   = normalize_aadhar(gt_raw)
        pred_norm = normalize_aadhar(pred_raw)

        old_exact = info.get("exact")
        old_sim   = info.get("char_sim")

        if gt_norm is None and pred_norm is None:
            new_exact = None
            new_sim   = 1.0
        elif gt_norm is None or pred_norm is None:
            new_exact = 0
            new_sim   = 0.0
        else:
            new_exact = 1 if gt_norm == pred_norm else 0
            new_sim   = round(char_sim(gt_norm, pred_norm), 6)

        if new_exact != old_exact or abs((new_sim or 0) - (old_sim or 0)) > 1e-6:
            info["exact"]    = new_exact
            info["char_sim"] = new_sim
            # store normalized values so the HTML can show them
            info["gt_norm"]   = gt_norm
            info["pred_norm"] = pred_norm
            changed += 1

    return changed

def recompute_overall_metrics(data):
    """Recompute overall + responded metrics for aadharNumber from per_sample_logs."""
    for metrics_key in ("overall_metrics", "responded_metrics"):
        if metrics_key not in data:
            continue
        metrics = data[metrics_key]
        if "aadharNumber" not in metrics.get("fields", {}):
            continue

        total_exact = 0
        total_sim   = 0.0
        support     = 0

        for img_path, sample in data["per_sample_logs"].items():
            if metrics_key == "responded_metrics" and not sample.get("has_response"):
                continue
            info = sample.get("fields", {}).get("aadharNumber")
            if info is None:
                continue
            if info.get("exact") is None:
                continue
            support     += 1
            total_exact += info["exact"]
            total_sim   += info.get("char_sim", 0.0)

        if support > 0:
            metrics["fields"]["aadharNumber"]["exact_match_pct"] = round(total_exact / support * 100, 2)
            metrics["fields"]["aadharNumber"]["char_sim"]        = round(total_sim / support, 4)
            metrics["fields"]["aadharNumber"]["support"]         = support


def patch(path):
    with open(path) as f:
        data = json.load(f)

    changed = recompute_field_metrics(data)
    recompute_overall_metrics(data)

    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"{path}")
    print(f"  aadharNumber entries updated: {changed}")
    am = data["overall_metrics"]["fields"].get("aadharNumber", {})
    print(f"  new exact_match_pct: {am.get('exact_match_pct')}  char_sim: {am.get('char_sim')}\n")


base = "/mnt/data/chaitanya/ocr-finetuning/benchmark/results_v3"
patch(f"{base}/hybrid_deepseek_qwen35/benchmark_results.json")
patch(f"{base}/hybrid_deepseek_qwen35_train/benchmark_results.json")
