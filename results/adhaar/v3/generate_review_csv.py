import json
import csv
import os
from difflib import SequenceMatcher

def char_sim(a, b):
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, str(a), str(b)).ratio()

EXACT_MATCH_FIELDS = {"name", "dateOfBirth", "gender", "aadharNumber", "pincode", "mobileNumber"}
ADDRESS_FIELD = "address"
ADDRESS_CHAR_SIM_THRESHOLD = 0.70

def collect_errors(benchmark_path):
    with open(benchmark_path) as f:
        data = json.load(f)

    errors = []  # list of (image_basename, field, gt, pred)

    for img_path, sample in data["per_sample_logs"].items():
        if not sample.get("has_response"):
            continue
        basename = img_path
        fields = sample.get("fields", {})

        for field in ["name", "dateOfBirth", "gender", "aadharNumber", "pincode", "mobileNumber"]:
            if field not in fields:
                continue
            info = fields[field]
            gt = info.get("gt")
            pred = info.get("pred")
            exact = info.get("exact")

            # Skip if both null (field not present in card)
            if gt is None and pred is None:
                continue

            # Show if not exact match
            if exact != 1:
                errors.append((basename, field, gt if gt is not None else "", pred if pred is not None else ""))

        if ADDRESS_FIELD in fields:
            info = fields[ADDRESS_FIELD]
            gt = info.get("gt")
            pred = info.get("pred")
            sim = info.get("char_sim")

            if gt is None and pred is None:
                continue

            # Compute char_sim if not in data
            if sim is None:
                sim = char_sim(gt, pred)

            if sim < ADDRESS_CHAR_SIM_THRESHOLD:
                errors.append((basename, ADDRESS_FIELD, gt if gt is not None else "", pred if pred is not None else ""))

    return errors


def write_review_csv(errors, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["PRED Correct?", "Field", "GT", "Pred", "Image"])
        for (basename, field, gt, pred) in errors:
            writer.writerow(["", field, gt, pred, basename])

    print(f"Written {len(errors)} errors to {out_path}")


base = "/mnt/data/chaitanya/ocr-finetuning/benchmark/results_v3"

# Val set
val_errors = collect_errors(f"{base}/hybrid_deepseek_qwen35/benchmark_results.json")
write_review_csv(val_errors, f"{base}/hybrid_deepseek_qwen35/review_errors_val.csv")

# Train set
train_errors = collect_errors(f"{base}/hybrid_deepseek_qwen35_train/benchmark_results.json")
write_review_csv(train_errors, f"{base}/hybrid_deepseek_qwen35_train/review_errors_train.csv")
