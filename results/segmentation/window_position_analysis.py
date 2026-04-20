import json
import re
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load preds
with open('/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/v1/qwen35_9b-segmentation-lora-w10-checkpoint-138-merged/preds.json', 'r') as f:
    preds = json.load(f)

# Load ground truth
gt_data = {}
with open('/mnt/data/chaitanya/data/financial_data/manifests/segmentation_val.jsonl', 'r') as f:
    for line in f:
        entry = json.loads(line)
        gt_data[entry['file_path']] = entry

# Group pages by batch_idx
batches = defaultdict(list)
for file_path, pred in preds.items():
    batch_idx = pred['batch_idx']
    # Extract page number from filename (e.g., "_p1.png" -> 1)
    match = re.search(r'_p(\d+)\.png$', file_path)
    if match:
        page_num = int(match.group(1))
        batches[batch_idx].append((page_num, file_path, pred))

# Process each batch
window_position_errors = defaultdict(lambda: {'total': 0, 'fp': 0, 'fn': 0})

for batch_idx, pages in batches.items():
    # Sort by page number
    pages.sort(key=lambda x: x[0])

    # Determine position within window (1-indexed)
    for position, (page_num, file_path, pred) in enumerate(pages, 1):
        pred_is_start = pred['pred_is_start']
        gt_is_start = pred['gt_is_start']

        # Classify
        if pred_is_start and not gt_is_start:
            error_type = 'fp'
        elif not pred_is_start and gt_is_start:
            error_type = 'fn'
        else:
            error_type = None

        # Record stats
        window_position_errors[position]['total'] += 1
        if error_type == 'fp':
            window_position_errors[position]['fp'] += 1
        elif error_type == 'fn':
            window_position_errors[position]['fn'] += 1

# Create output table
rows = []
for pos in range(1, 11):  # Positions 1-10
    stats = window_position_errors[pos]
    total = stats['total']
    fp = stats['fp']
    fn = stats['fn']
    fp_rate = fp / total if total > 0 else 0
    fn_rate = fn / total if total > 0 else 0

    rows.append({
        'window_position': pos,
        'total_pages': total,
        'fp_count': fp,
        'fn_count': fn,
        'fp_rate': fp_rate,
        'fn_rate': fn_rate
    })

df = pd.DataFrame(rows)

# Save CSV
csv_path = '/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/window_position_stats.csv'
df.to_csv(csv_path, index=False)
print(f"CSV saved to {csv_path}")
print(df)

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))
x = df['window_position']
ax.plot(x, df['fp_rate'], marker='o', label='FP Rate', linewidth=2, markersize=8)
ax.plot(x, df['fn_rate'], marker='s', label='FN Rate', linewidth=2, markersize=8)
ax.set_xlabel('Window Position', fontsize=12)
ax.set_ylabel('Error Rate', fontsize=12)
ax.set_title('Error Rates by Window Position', fontsize=14)
ax.set_xticks(range(1, 11))
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_ylim([0, max(df['fp_rate'].max(), df['fn_rate'].max()) * 1.1])

# Save plot
plot_path = '/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/window_position_error_rate.png'
plt.savefig(plot_path, dpi=300, bbox_inches='tight')
print(f"Plot saved to {plot_path}")
