#!/usr/bin/env python3
"""
Page-level regression analysis across 5 segmentation experiments.

Produces a detailed markdown report showing:
  1. Aggregate metrics comparison
  2. Pairwise regressions/improvements (which pages broke/fixed between experiments)
  3. Cross-model alignment (GT suspects, volatile pages)
  4. Per-class trajectory (F1 across all 5 experiments)
"""

import json
import os
from collections import defaultdict

# ─────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────
BASE = "/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation"

EXPERIMENTS = [
    {
        "name": "Exp1: Baseline",
        "short": "baseline",
        "path": f"{BASE}/v1/qwen35_9b_segmentation_sliding_parsing_fix/preds.json",
    },
    {
        "name": "Exp2: LoRA w10",
        "short": "lora_w10",
        "path": f"{BASE}/v1/qwen35_9b-segmentation-lora-w10-checkpoint-138-merged/preds.json",
    },
    {
        "name": "Exp3: LoRA+hint",
        "short": "lora_hint",
        "path": f"{BASE}/v1/qwen35_9b-segmentation-lora-upsampled-epoch5/preds.json",
    },
    {
        "name": "Exp4: Prompt v1",
        "short": "prompt_v1",
        "path": f"{BASE}/v2/segg_sliding_enhanced_upsampled/preds.json",
    },
    {
        "name": "Exp5: Prompt v1+w5",
        "short": "prompt_w5",
        "path": f"{BASE}/v2/segg_w5_no_headers/preds.json",
    },
]

OUTPUT_REPORT = f"{BASE}/regression_analysis.md"


# ─────────────────────────────────────────────
# Loading
# ─────────────────────────────────────────────
def load_all():
    data = []
    for exp in EXPERIMENTS:
        print(f"Loading {exp['name']}...")
        with open(exp["path"]) as f:
            data.append(json.load(f))
    return data


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────
def get_pred(rec):
    """Return predicted is_start as bool, or None for parse failures."""
    if rec.get("status") != "success":
        return None
    p = rec.get("pred_is_start")
    if p is None:
        return None
    return bool(p)


def get_gt(rec):
    return bool(rec["gt_is_start"])


def get_label(rec):
    return rec.get("gt_label", "unknown")


def error_type(rec):
    """Classify page outcome: correct, FP, FN, or parse_fail."""
    pred = get_pred(rec)
    gt = get_gt(rec)
    if pred is None:
        return "parse_fail"
    if pred == gt:
        return "correct"
    if pred and not gt:
        return "FP"
    return "FN"


def is_correct(rec):
    return error_type(rec) == "correct"


def f1_from(tp, fp, fn):
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f = 2 * p * r / (p + r) if (p + r) else 0.0
    return p, r, f


def short_path(key):
    """Shorten image path for readability."""
    # .../images/label/hash_pN.png -> label/hash_pN.png
    parts = key.split("/")
    if len(parts) >= 2:
        return "/".join(parts[-2:])
    return key


# ─────────────────────────────────────────────
# Aggregate metrics per experiment
# ─────────────────────────────────────────────
def compute_aggregate(data, keys):
    tp = fp = tn = fn = parse_fails = 0
    for k in keys:
        rec = data[k]
        et = error_type(rec)
        gt = get_gt(rec)
        if et == "parse_fail":
            parse_fails += 1
        elif et == "correct":
            if gt:
                tp += 1
            else:
                tn += 1
        elif et == "FP":
            fp += 1
        elif et == "FN":
            fn += 1
    prec, rec, f1 = f1_from(tp, fp, fn)
    acc = (tp + tn) / len(keys) if keys else 0
    return {
        "tp": tp, "fp": fp, "tn": tn, "fn": fn,
        "parse_fails": parse_fails,
        "precision": prec, "recall": rec, "f1": f1,
        "accuracy": acc,
    }


# ─────────────────────────────────────────────
# Pairwise regression analysis
# ─────────────────────────────────────────────
def compute_pairwise(data_a, data_b, keys):
    improvements = []  # was wrong in A, correct in B
    regressions = []   # was correct in A, wrong in B
    both_correct = []
    both_wrong = []

    for k in keys:
        rec_a, rec_b = data_a[k], data_b[k]
        c_a = is_correct(rec_a)
        c_b = is_correct(rec_b)
        label = get_label(rec_a)
        et_a = error_type(rec_a)
        et_b = error_type(rec_b)

        entry = {"key": k, "label": label, "et_a": et_a, "et_b": et_b}

        if c_a and c_b:
            both_correct.append(entry)
        elif not c_a and not c_b:
            both_wrong.append(entry)
        elif not c_a and c_b:
            improvements.append(entry)
        else:
            regressions.append(entry)

    # Group by class
    def group_by_class(items):
        by_class = defaultdict(list)
        for item in items:
            by_class[item["label"]].append(item)
        return dict(sorted(by_class.items(), key=lambda x: -len(x[1])))

    return {
        "improvements": improvements,
        "regressions": regressions,
        "both_correct": both_correct,
        "both_wrong": both_wrong,
        "improvements_by_class": group_by_class(improvements),
        "regressions_by_class": group_by_class(regressions),
    }


# ─────────────────────────────────────────────
# Cross-model alignment (all 5)
# ─────────────────────────────────────────────
def compute_alignment(all_data, keys):
    all_correct = []
    all_wrong = []
    volatile = []
    patterns = {}

    for k in keys:
        correct_vec = tuple(is_correct(d[k]) for d in all_data)
        patterns[k] = correct_vec
        label = get_label(all_data[0][k])
        gt = get_gt(all_data[0][k])

        if all(correct_vec):
            all_correct.append(k)
        elif not any(correct_vec):
            # All wrong — GT suspect
            preds = tuple(get_pred(d[k]) for d in all_data)
            all_wrong.append({
                "key": k, "label": label, "gt": gt,
                "preds": preds,
                "all_same_pred": len(set(p for p in preds if p is not None)) <= 1,
            })
        else:
            # Count flips
            flips = sum(1 for i in range(1, len(correct_vec)) if correct_vec[i] != correct_vec[i - 1])
            if flips >= 2:
                volatile.append({
                    "key": k, "label": label, "gt": gt,
                    "pattern": correct_vec, "flips": flips,
                })

    volatile.sort(key=lambda x: -x["flips"])
    return {
        "all_correct": all_correct,
        "all_wrong": all_wrong,
        "volatile": volatile,
        "patterns": patterns,
    }


# ─────────────────────────────────────────────
# Per-class trajectory
# ─────────────────────────────────────────────
def compute_class_trajectories(all_data, keys):
    # For each experiment, compute per-class TP/FP/FN
    n_exp = len(all_data)
    class_metrics = defaultdict(lambda: [{"tp": 0, "fp": 0, "fn": 0, "tn": 0} for _ in range(n_exp)])
    class_total = defaultdict(int)
    class_support = defaultdict(int)  # GT=START count

    for k in keys:
        label = get_label(all_data[0][k])
        gt = get_gt(all_data[0][k])
        class_total[label] += 1
        if gt:
            class_support[label] += 1

        for i, d in enumerate(all_data):
            et = error_type(d[k])
            m = class_metrics[label][i]
            if et == "correct":
                if gt:
                    m["tp"] += 1
                else:
                    m["tn"] += 1
            elif et == "FP":
                m["fp"] += 1
            elif et == "FN":
                m["fn"] += 1
            elif et == "parse_fail":
                # Count parse fails as the appropriate error type
                if gt:
                    m["fn"] += 1  # missed a start
                else:
                    m["fp"] += 1  # unclear, but doesn't count as TN

    # Compute F1 per class per experiment
    trajectories = {}
    for label in sorted(class_metrics.keys()):
        support = class_support[label]
        total = class_total[label]
        exp_data = []
        for i in range(n_exp):
            m = class_metrics[label][i]
            p, r, f1 = f1_from(m["tp"], m["fp"], m["fn"])
            exp_data.append({
                "tp": m["tp"], "fp": m["fp"], "fn": m["fn"],
                "precision": p, "recall": r, "f1": f1,
            })
        trajectories[label] = {
            "support": support,
            "total": total,
            "experiments": exp_data,
        }

    return trajectories


# ─────────────────────────────────────────────
# Report generation
# ─────────────────────────────────────────────
def generate_report(all_data, keys):
    lines = []

    def h(n, text):
        lines.append(f"\n{'#' * n} {text}\n")

    def table_row(*cells):
        lines.append("| " + " | ".join(str(c) for c in cells) + " |")

    def table_sep(n):
        lines.append("|" + "|".join("---" for _ in range(n)) + "|")

    lines.append("# Segmentation Regression Analysis — 5-Experiment Comparison\n")
    lines.append(f"*{len(keys)} pages evaluated across all experiments*\n")

    # ── 1. Aggregate Overview ────────────────────────────────────────────────
    h(2, "1. Aggregate Metrics Overview")

    table_row("Experiment", "Accuracy", "F1", "Precision", "Recall", "TP", "FP", "FN", "TN", "Parse Fail")
    table_sep(10)
    for i, exp in enumerate(EXPERIMENTS):
        agg = compute_aggregate(all_data[i], keys)
        table_row(
            exp["name"],
            f"{agg['accuracy']:.4f}",
            f"{agg['f1']:.4f}",
            f"{agg['precision']:.4f}",
            f"{agg['recall']:.4f}",
            agg["tp"], agg["fp"], agg["fn"], agg["tn"], agg["parse_fails"],
        )

    # ── 2. Pairwise Regressions ──────────────────────────────────────────────
    h(2, "2. Pairwise Regression Analysis")

    for i in range(len(all_data) - 1):
        pair = compute_pairwise(all_data[i], all_data[i + 1], keys)
        name_a = EXPERIMENTS[i]["name"]
        name_b = EXPERIMENTS[i + 1]["name"]

        h(3, f"2.{i + 1} {name_a} -> {name_b}")

        n_imp = len(pair["improvements"])
        n_reg = len(pair["regressions"])
        n_same = len(pair["both_correct"]) + len(pair["both_wrong"])
        lines.append(f"**Net: {'+' if n_imp >= n_reg else ''}{n_imp - n_reg}** "
                      f"({n_imp} improvements, {n_reg} regressions, {n_same} unchanged)\n")

        # Regressions detail
        if pair["regressions"]:
            h(4, f"REGRESSIONS ({n_reg} pages worse)")

            # By error transition type
            by_transition = defaultdict(list)
            for item in pair["regressions"]:
                transition = f"{item['et_a']}->{item['et_b']}"
                by_transition[transition].append(item)

            for trans, items in sorted(by_transition.items(), key=lambda x: -len(x[1])):
                lines.append(f"\n**{trans}** ({len(items)} pages):\n")

                # Group by class
                by_class = defaultdict(list)
                for item in items:
                    by_class[item["label"]].append(item)

                for cls, cls_items in sorted(by_class.items(), key=lambda x: -len(x[1])):
                    desc = _describe_error(cls, cls_items, trans)
                    lines.append(f"- **{cls}**: {len(cls_items)} -- {desc}")
                    # Show first 3 specific pages
                    for item in cls_items[:3]:
                        lines.append(f"  - `{short_path(item['key'])}`")
                    if len(cls_items) > 3:
                        lines.append(f"  - *...and {len(cls_items) - 3} more*")

        # Improvements detail
        if pair["improvements"]:
            h(4, f"IMPROVEMENTS ({n_imp} pages fixed)")

            by_transition = defaultdict(list)
            for item in pair["improvements"]:
                transition = f"{item['et_a']}->{item['et_b']}"
                by_transition[transition].append(item)

            for trans, items in sorted(by_transition.items(), key=lambda x: -len(x[1])):
                lines.append(f"\n**{trans}** ({len(items)} pages):\n")

                by_class = defaultdict(list)
                for item in items:
                    by_class[item["label"]].append(item)

                for cls, cls_items in sorted(by_class.items(), key=lambda x: -len(x[1])):
                    desc = _describe_improvement(cls, cls_items, trans)
                    lines.append(f"- **{cls}**: {len(cls_items)} -- {desc}")
                    for item in cls_items[:3]:
                        lines.append(f"  - `{short_path(item['key'])}`")
                    if len(cls_items) > 3:
                        lines.append(f"  - *...and {len(cls_items) - 3} more*")

    # ── 3. Cross-Model Alignment ─────────────────────────────────────────────
    h(2, "3. Cross-Model Alignment (All 5 Experiments)")

    alignment = compute_alignment(all_data, keys)

    h(3, "3.1 Universal Successes")
    lines.append(f"**{len(alignment['all_correct'])} pages** all 5 experiments get correct.\n")

    h(3, "3.2 Universal Failures (GT Suspects)")
    all_wrong = alignment["all_wrong"]
    lines.append(f"**{len(all_wrong)} pages** all 5 experiments get wrong.\n")

    if all_wrong:
        # Split into strong suspects (all predict same) vs mixed
        strong = [x for x in all_wrong if x["all_same_pred"]]
        mixed = [x for x in all_wrong if not x["all_same_pred"]]

        if strong:
            lines.append(f"\n**Strong GT suspects** ({len(strong)} pages — all 5 models agree on prediction, disagree with GT):\n")
            by_label = defaultdict(list)
            for item in strong:
                by_label[item["label"]].append(item)

            table_row("Label", "Count", "GT", "All predict", "Example pages")
            table_sep(5)
            for lbl, items in sorted(by_label.items(), key=lambda x: -len(x[1])):
                gt_val = "START" if items[0]["gt"] else "CONTINUE"
                pred_val = "START" if items[0]["preds"][0] else "CONTINUE"
                examples = ", ".join(f"`{short_path(x['key'])}`" for x in items[:3])
                table_row(lbl, len(items), gt_val, pred_val, examples)

        if mixed:
            lines.append(f"\n**Mixed failures** ({len(mixed)} pages — all wrong but predictions differ):\n")
            by_label = defaultdict(list)
            for item in mixed:
                by_label[item["label"]].append(item)
            for lbl, items in sorted(by_label.items(), key=lambda x: -len(x[1])):
                lines.append(f"- **{lbl}**: {len(items)} pages")

    h(3, "3.3 Most Volatile Pages (flip >= 2 times)")
    volatile = alignment["volatile"]
    lines.append(f"**{len(volatile)} pages** flip between correct/incorrect 2+ times across experiments.\n")

    if volatile:
        def pattern_str(p):
            return "".join("Y" if c else "N" for c in p)

        table_row("Page", "Label", "GT", "Pattern (1-2-3-4-5)", "Flips")
        table_sep(5)
        for item in volatile[:40]:
            gt_val = "START" if item["gt"] else "CONT"
            table_row(
                f"`{short_path(item['key'])}`",
                item["label"], gt_val,
                pattern_str(item["pattern"]),
                item["flips"],
            )
        if len(volatile) > 40:
            lines.append(f"\n*...and {len(volatile) - 40} more volatile pages*\n")

    # ── 4. Per-Class Trajectory ──────────────────────────────────────────────
    h(2, "4. Per-Class Trajectory")

    trajectories = compute_class_trajectories(all_data, keys)

    h(3, "4.1 Full Trajectory Table (classes with support >= 2)")

    # Header
    exp_short = [e["short"] for e in EXPERIMENTS]
    header = ["Class", "Support", "Total"]
    for s in exp_short:
        header.extend([f"F1_{s}", f"FP_{s}", f"FN_{s}"])
    table_row(*header)
    table_sep(len(header))

    # Filter and sort by max F1 swing
    rows = []
    for label, traj in trajectories.items():
        if traj["support"] < 2:
            continue
        f1s = [e["f1"] for e in traj["experiments"]]
        swing = max(f1s) - min(f1s) if f1s else 0
        rows.append((label, traj, swing))

    rows.sort(key=lambda x: -x[2])  # most volatile classes first

    for label, traj, swing in rows:
        row = [label, traj["support"], traj["total"]]
        for e in traj["experiments"]:
            row.extend([f"{e['f1']:.3f}", e["fp"], e["fn"]])
        table_row(*row)

    # ── 4.2 Biggest winners/losers ───────────────────────────────────────────
    h(3, "4.2 Biggest Winners (F1 improved baseline -> latest)")
    winners = []
    losers = []
    stubborn = []
    for label, traj, swing in rows:
        f1_first = traj["experiments"][0]["f1"]
        f1_last = traj["experiments"][-1]["f1"]
        delta = f1_last - f1_first
        if delta > 0.05:
            winners.append((label, traj, f1_first, f1_last, delta))
        elif delta < -0.05:
            losers.append((label, traj, f1_first, f1_last, delta))
        elif f1_last < 0.5 and traj["support"] >= 2:
            stubborn.append((label, traj, f1_first, f1_last))

    winners.sort(key=lambda x: -x[4])
    for label, traj, f1_first, f1_last, delta in winners:
        fp_delta = traj["experiments"][-1]["fp"] - traj["experiments"][0]["fp"]
        fn_delta = traj["experiments"][-1]["fn"] - traj["experiments"][0]["fn"]
        lines.append(f"- **{label}**: F1 {f1_first:.3f} -> {f1_last:.3f} (+{delta:.3f}), FP {'+' if fp_delta >= 0 else ''}{fp_delta}, FN {'+' if fn_delta >= 0 else ''}{fn_delta}")

    h(3, "4.3 Biggest Losers (F1 regressed baseline -> latest)")
    losers.sort(key=lambda x: x[4])
    for label, traj, f1_first, f1_last, delta in losers:
        fp_delta = traj["experiments"][-1]["fp"] - traj["experiments"][0]["fp"]
        fn_delta = traj["experiments"][-1]["fn"] - traj["experiments"][0]["fn"]
        lines.append(f"- **{label}**: F1 {f1_first:.3f} -> {f1_last:.3f} ({delta:.3f}), FP {'+' if fp_delta >= 0 else ''}{fp_delta}, FN {'+' if fn_delta >= 0 else ''}{fn_delta}")

    h(3, "4.4 Stubbornly Wrong (F1 < 0.5 in latest, support >= 2)")
    for label, traj, f1_first, f1_last in stubborn:
        total_errors = traj["experiments"][-1]["fp"] + traj["experiments"][-1]["fn"]
        lines.append(f"- **{label}**: F1={f1_last:.3f} (support={traj['support']}, total pages={traj['total']}, errors in latest={total_errors})")

    # ── 5. Cumulative regression tracker ─────────────────────────────────────
    h(2, "5. Cumulative Regression Tracker")
    lines.append("Tracks pages that were correct in baseline but broke at some point and never recovered.\n")

    baseline_correct = set(k for k in keys if is_correct(all_data[0][k]))
    latest_correct = set(k for k in keys if is_correct(all_data[-1][k]))

    lost = baseline_correct - latest_correct  # correct in baseline, wrong in latest
    gained = latest_correct - baseline_correct  # wrong in baseline, correct in latest

    lines.append(f"- **Baseline correct, Latest wrong (net regressions)**: {len(lost)} pages")
    lines.append(f"- **Baseline wrong, Latest correct (net improvements)**: {len(gained)} pages")
    lines.append(f"- **Net change**: {'+' if len(gained) >= len(lost) else ''}{len(gained) - len(lost)} pages\n")

    if lost:
        h(3, "5.1 Regressions from Baseline (correct in Exp1, wrong in Exp5)")

        by_label = defaultdict(list)
        for k in lost:
            label = get_label(all_data[0][k])
            pattern = tuple(is_correct(d[k]) for d in all_data)
            et_latest = error_type(all_data[-1][k])
            by_label[label].append({"key": k, "pattern": pattern, "et_latest": et_latest})

        for lbl, items in sorted(by_label.items(), key=lambda x: -len(x[1])):
            fp_count = sum(1 for x in items if x["et_latest"] == "FP")
            fn_count = sum(1 for x in items if x["et_latest"] == "FN")
            pf_count = sum(1 for x in items if x["et_latest"] == "parse_fail")
            parts = []
            if fp_count:
                parts.append(f"{fp_count} now FP")
            if fn_count:
                parts.append(f"{fn_count} now FN")
            if pf_count:
                parts.append(f"{pf_count} parse fail")
            lines.append(f"\n**{lbl}** ({len(items)} regressions: {', '.join(parts)}):")
            for item in items:
                pat = "".join("Y" if c else "N" for c in item["pattern"])
                lines.append(f"- `{short_path(item['key'])}` [{pat}] -> {item['et_latest']}")

    if gained:
        h(3, "5.2 Net Improvements (wrong in Exp1, correct in Exp5)")

        by_label = defaultdict(list)
        for k in gained:
            label = get_label(all_data[0][k])
            et_baseline = error_type(all_data[0][k])
            by_label[label].append({"key": k, "et_baseline": et_baseline})

        for lbl, items in sorted(by_label.items(), key=lambda x: -len(x[1])):
            fp_fixed = sum(1 for x in items if x["et_baseline"] == "FP")
            fn_fixed = sum(1 for x in items if x["et_baseline"] == "FN")
            pf_fixed = sum(1 for x in items if x["et_baseline"] == "parse_fail")
            parts = []
            if fp_fixed:
                parts.append(f"{fp_fixed} were FP")
            if fn_fixed:
                parts.append(f"{fn_fixed} were FN")
            if pf_fixed:
                parts.append(f"{pf_fixed} were parse fail")
            lines.append(f"- **{lbl}**: {len(items)} fixed ({', '.join(parts)})")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# Error description helpers
# ─────────────────────────────────────────────
def _describe_error(cls, items, transition):
    """Generate human-readable description of regression pattern."""
    if "->FP" in transition:
        return f"hallucinated new document starts on continuation pages"
    elif "->FN" in transition:
        return f"missed actual document boundaries"
    elif "->parse_fail" in transition:
        return f"output became unparseable"
    return f"prediction changed to wrong answer"


def _describe_improvement(cls, items, transition):
    """Generate human-readable description of improvement pattern."""
    if "FP->" in transition:
        return f"stopped hallucinating starts (false positives removed)"
    elif "FN->" in transition:
        return f"now detects previously missed boundaries"
    elif "parse_fail->" in transition:
        return f"parse failures fixed"
    return f"prediction corrected"


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
if __name__ == "__main__":
    all_data = load_all()

    # Get common keys
    key_sets = [set(d.keys()) for d in all_data]
    common_keys = sorted(key_sets[0].intersection(*key_sets[1:]))
    print(f"Common pages: {len(common_keys)}")

    # Sanity check: verify aggregate metrics match known values
    print("\nSanity check — aggregate metrics:")
    for i, exp in enumerate(EXPERIMENTS):
        agg = compute_aggregate(all_data[i], common_keys)
        print(f"  {exp['short']:15s} TP={agg['tp']:3d} FP={agg['fp']:3d} FN={agg['fn']:3d} "
              f"F1={agg['f1']:.4f} Acc={agg['accuracy']:.4f} ParseFail={agg['parse_fails']}")

    # Generate report
    print("\nGenerating report...")
    report = generate_report(all_data, common_keys)

    with open(OUTPUT_REPORT, "w") as f:
        f.write(report)

    print(f"\nReport written to: {OUTPUT_REPORT}")
