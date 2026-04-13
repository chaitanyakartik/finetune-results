"""
retry_oom_errors.py — Retry OOM-failed pages in place with lower parallelism (3 instances per GPU).

Loads preds.json, finds all pages with parse_failure status or CUDA OOM errors,
re-runs inference on just those pages with 3 instances/GPU, updates preds.json.

Usage:
  python retry_oom_errors.py
  python retry_oom_errors.py --preds-file /path/to/preds.json --model-dir /path/to/model
"""

import json
import os
import sys
import argparse
import tempfile
from pathlib import Path

# Add segg_sliding_enhanced_upsampled to path for imports
segg_dir = "/mnt/data/chaitanya/ocr-finetuning/doc_classification/segg_sliding_enhanced_upsampled"
sys.path.insert(0, segg_dir)

from benchmark import worker_sliding_window
from collections import defaultdict

def load_manifest(path):
    docs = defaultdict(list)
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            e = json.loads(line)
            fp = e.get("file_path", "")
            if not fp:
                continue
            docs[e["fileHash"]].append((fp, e))
    for fh in docs:
        docs[fh].sort(key=lambda x: x[1].get("page_num", 0))
    return dict(docs)


def parse_args():
    p = argparse.ArgumentParser(description="Retry OOM-failed pages in preds.json.")
    p.add_argument("--preds-file",    default="preds.json")
    p.add_argument("--model-dir",     default="/mnt/data/chaitanya/ocr-finetuning/models/qwen35_9b-segmentation-lora-classHint-upsampled-merged")
    p.add_argument("--val-manifest",  default="/mnt/data/chaitanya/data/financial_data/manifests/segmentation_val.jsonl")
    p.add_argument("--num-gpus",      type=int, default=2)
    p.add_argument("--instances-per-gpu", type=int, default=3)
    return p.parse_args()


def main():
    args = parse_args()

    # Load current preds
    with open(args.preds_file) as f:
        preds = json.load(f)
    print(f"Loaded {len(preds)} predictions from {args.preds_file}")

    # Find failed pages
    failed_fps = [fp for fp, entry in preds.items()
                  if entry.get("status") == "parse_failure"
                  or "CUDA" in entry.get("raw_response", "")]
    print(f"Found {len(failed_fps)} failed pages (parse_failure or CUDA error)")
    if not failed_fps:
        print("No failures to retry.")
        return

    # Load manifest and build document → pages mapping
    docs = load_manifest(args.val_manifest)
    print(f"Loaded {len(docs)} documents")

    # Map file_path → document
    fp_to_doc = {}
    for doc_pages in docs.values():
        for fp, entry in doc_pages:
            fp_to_doc[fp] = doc_pages

    # Collect unique documents that contain failed pages
    failed_docs = {}
    for fp in failed_fps:
        if fp in fp_to_doc:
            doc_pages = fp_to_doc[fp]
            doc_hash = doc_pages[0][1]["fileHash"]
            if doc_hash not in failed_docs:
                failed_docs[doc_hash] = doc_pages

    print(f"Reprocessing {len(failed_docs)} documents with failed pages")
    print(f"Using {args.num_gpus} GPU(s) × {args.instances_per_gpu} instances = {args.num_gpus * args.instances_per_gpu} workers")

    # Re-run inference on failed docs
    new_results = worker_sliding_window(
        model_dir=args.model_dir,
        val_docs=list(failed_docs.values()),
        num_gpus=args.num_gpus,
        instances_per_gpu=args.instances_per_gpu,
        save_every=5,
    )

    # Merge back into preds
    updated = 0
    for fp, result in new_results.items():
        if result.get("status") == "success" and result.get("pred_is_start") is not None:
            preds[fp] = result
            updated += 1
            print(f"  ✓ {fp}")
        elif fp in preds:
            print(f"  ⚠ {fp} still failed: {result.get('status', '?')}")

    # Save updated preds
    with open(args.preds_file, "w") as f:
        json.dump(preds, f, indent=2, ensure_ascii=False)
    print(f"\nUpdated {updated} predictions in {args.preds_file}")


if __name__ == "__main__":
    main()
