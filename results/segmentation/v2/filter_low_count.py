import json
import sys

results_path = sys.argv[1] if len(sys.argv) > 1 else "benchmark_results.json"
min_count = int(sys.argv[2]) if len(sys.argv) > 2 else 20

with open(results_path) as f:
    data = json.load(f)

label_metrics = data["label_metrics"]
filtered = {k: v for k, v in label_metrics.items() if v["total"] >= min_count}
removed = {k: v["total"] for k, v in label_metrics.items() if v["total"] < min_count}

print(f"Kept:    {len(filtered)} labels (total >= {min_count})")
print(f"Removed: {len(removed)} labels\n")
print("Removed labels and their counts:")
for label, count in sorted(removed.items(), key=lambda x: x[1], reverse=True):
    print(f"  {label}: {count}")

data["label_metrics"] = filtered
out_path = results_path.replace(".json", f"_filtered{min_count}.json")
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)
print(f"\nSaved filtered results to: {out_path}")
