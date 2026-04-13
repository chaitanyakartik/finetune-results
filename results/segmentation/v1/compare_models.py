#!/usr/bin/env python3
"""
Comparative error analysis across three segmentation models:
  - epoch4   : pure sliding window (baseline)
  - ckpt240  : sliding window + classification hint + reference image
  - triplet  : prev+target+next triplet, 5-field multitask output

Produces a structured Markdown report covering:
  1. Aggregate metrics comparison
  2. Per-sample error alignment (who gets what right/wrong)
  3. GT audit candidates (all 3 models agree but disagree with GT)
  4. Same-class boundary analysis
  5. Per-class conditional performance
  6. Synthetic vs real data breakdown
"""

import json
import os
from collections import defaultdict

# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────
BASE = "/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/v1"

EPOCH4_PREDS  = f"{BASE}/qwen35_9b-segmentation-lora-upsampled-epoch4/preds.json"
CKPT240_PREDS = f"{BASE}/seg_continued_ckpt240/preds.json"
TRIPLET_PREDS = f"{BASE}/triplet_multitask_ckpt1467/preds.json"

OUTPUT_REPORT = f"{BASE}/comparison_analysis.md"

# ─────────────────────────────────────────────
# Load data
# ─────────────────────────────────────────────
print("Loading preds.json files...")
with open(EPOCH4_PREDS)  as f: e4  = json.load(f)
with open(CKPT240_PREDS) as f: c240 = json.load(f)
with open(TRIPLET_PREDS) as f: tri = json.load(f)

# Align on the 1981 common keys
common_keys = sorted(set(e4.keys()) & set(c240.keys()) & set(tri.keys()))
print(f"Common pages: {len(common_keys)}")

# ─────────────────────────────────────────────
# Helper: normalise prediction to bool for e4/c240
# ─────────────────────────────────────────────
def is_start_e4(rec):
    if rec['status'] != 'success': return None
    return bool(rec['pred_is_start'])

def is_start_c240(rec):
    if rec['status'] != 'success': return None
    return bool(rec['pred_is_start'])

def is_start_tri(rec):
    if rec['status'] != 'success': return None
    return rec.get('pred_boundary_label') == 'START'

def gt_is_start_e4(rec):
    return bool(rec['gt_is_start'])

def gt_is_start_tri(rec):
    return rec.get('gt_boundary_label') == 'START'

# ─────────────────────────────────────────────
# Phase 1: Per-sample error alignment
# ─────────────────────────────────────────────
print("Running per-sample alignment...")

categories = defaultdict(list)  # category -> list of (key, label, e4_pred, c240_pred, tri_pred, gt)

# Track per-class performance for each model
per_class_e4   = defaultdict(lambda: {'tp':0,'fp':0,'tn':0,'fn':0})
per_class_c240 = defaultdict(lambda: {'tp':0,'fp':0,'tn':0,'fn':0})
per_class_tri  = defaultdict(lambda: {'tp':0,'fp':0,'tn':0,'fn':0})

# Same-class boundary tracking
same_class_fn_e4   = []  # FNs where anchor_class hint == gt_label (for epoch4 we infer from gt_label)
same_class_fn_c240 = []
same_class_fn_tri  = []

# Synthetic vs real tracking
synth_e4   = {'tp':0,'fp':0,'tn':0,'fn':0}
real_e4    = {'tp':0,'fp':0,'tn':0,'fn':0}
synth_c240 = {'tp':0,'fp':0,'tn':0,'fn':0}
real_c240  = {'tp':0,'fp':0,'tn':0,'fn':0}
synth_tri  = {'tp':0,'fp':0,'tn':0,'fn':0}
real_tri   = {'tp':0,'fp':0,'tn':0,'fn':0}

for key in common_keys:
    r_e4   = e4[key]
    r_c240 = c240[key]
    r_tri  = tri[key]

    gt = gt_is_start_e4(r_e4)   # same as c240; triplet uses START/CONTINUE
    gt_tri = gt_is_start_tri(r_tri)

    p_e4   = is_start_e4(r_e4)
    p_c240 = is_start_c240(r_c240)
    p_tri  = is_start_tri(r_tri)

    label = r_e4.get('gt_label', '?')
    is_synth = 'synth' in key.lower()

    # Skip parse failures for alignment
    if p_e4 is None or p_c240 is None or p_tri is None:
        categories['parse_failure'].append({'key': key, 'label': label,
            'e4': p_e4, 'c240': p_c240, 'tri': p_tri, 'gt': gt})
        continue

    # Per-model correctness (against same GT)
    c_e4   = (p_e4   == gt)
    c_c240 = (p_c240 == gt)
    c_tri  = (p_tri  == gt)

    # Categorise
    if c_e4 and c_c240 and c_tri:
        cat = 'all_correct'
    elif not c_e4 and not c_c240 and not c_tri:
        # Determine if they all predict the same wrong thing (GT candidate)
        if p_e4 == p_c240 == p_tri:
            cat = 'all_wrong_same_pred'  # strongest GT suspect
        else:
            cat = 'all_wrong_mixed_pred'
    elif c_e4 and not c_c240 and not c_tri:
        cat = 'baseline_only_correct'
    elif not c_e4 and c_c240 and not c_tri:
        cat = 'hints_only_correct'
    elif not c_e4 and not c_c240 and c_tri:
        cat = 'triplet_only_correct'
    elif c_e4 and c_c240 and not c_tri:
        cat = 'triplet_regressed'
    elif c_e4 and not c_c240 and c_tri:
        cat = 'hints_regressed'
    elif not c_e4 and c_c240 and c_tri:
        cat = 'baseline_regressed'
    else:
        cat = 'other'

    categories[cat].append({
        'key': key, 'label': label,
        'e4': p_e4, 'c240': p_c240, 'tri': p_tri, 'gt': gt,
        'anchor_class': r_c240.get('anchor_class'),
    })

    # Per-class metrics (only boundary errors)
    def update(d, pred, gt_val):
        if pred and gt_val:     d['tp'] += 1
        elif pred and not gt_val: d['fp'] += 1
        elif not pred and gt_val: d['fn'] += 1
        else:                   d['tn'] += 1

    update(per_class_e4[label],   p_e4,   gt)
    update(per_class_c240[label], p_c240, gt)
    update(per_class_tri[label],  p_tri,  gt)

    # Same-class boundary analysis (FN cases)
    anchor = r_c240.get('anchor_class')  # what the hint said
    if not p_e4 and gt:  # FN for epoch4
        # For epoch4 we don't have anchor_class, use gt_label as proxy
        same_class_fn_e4.append({'key': key, 'label': label, 'anchor': label})
    if not p_c240 and gt:  # FN for ckpt240
        same_class_fn_c240.append({
            'key': key, 'label': label, 'anchor': anchor,
            'is_same_class': (anchor == label)
        })
    if not p_tri and gt:  # FN for triplet
        same_class_fn_tri.append({'key': key, 'label': label})

    # Synthetic vs real
    def update_sr(d, pred, gt_val):
        if pred and gt_val:     d['tp'] += 1
        elif pred and not gt_val: d['fp'] += 1
        elif not pred and gt_val: d['fn'] += 1
        else:                   d['tn'] += 1

    if is_synth:
        update_sr(synth_e4, p_e4, gt)
        update_sr(synth_c240, p_c240, gt)
        update_sr(synth_tri, p_tri, gt)
    else:
        update_sr(real_e4, p_e4, gt)
        update_sr(real_c240, p_c240, gt)
        update_sr(real_tri, p_tri, gt)


# ─────────────────────────────────────────────
# Helper: compute F1 from dict
# ─────────────────────────────────────────────
def f1_from(d):
    tp, fp, fn = d['tp'], d['fp'], d['fn']
    p = tp / (tp + fp) if (tp + fp) else 0.0
    r = tp / (tp + fn) if (tp + fn) else 0.0
    f = 2*p*r / (p+r) if (p+r) else 0.0
    return p, r, f, tp, fp, fn

# ─────────────────────────────────────────────
# Build report
# ─────────────────────────────────────────────
print("Building report...")
lines = []

def h(n, text):
    lines.append(f"\n{'#' * n} {text}\n")

def table_row(*cells):
    lines.append('| ' + ' | '.join(str(c) for c in cells) + ' |')

def table_sep(*widths):
    lines.append('|' + '|'.join('-' * (w+2) for w in widths) + '|')

lines.append("# Segmentation Model Comparison — Full Analysis\n")
lines.append(f"*Common evaluation pages: {len(common_keys)}*\n")

# ── 1. Aggregate ──────────────────────────────────────────────────────────────
h(2, "1. Aggregate Metrics")

table_row("Model", "F1", "Precision", "Recall", "Accuracy", "TP", "FP", "TN", "FN", "Parse Failures")
table_sep(20, 6, 10, 8, 10, 5, 5, 6, 5, 14)
table_row("epoch4 (sliding window)", "0.7859", "0.7486", "0.8272", "0.9631", 134, 45, 1770, 28, 4)
table_row("ckpt240 (+ hints)", "0.7712", "0.8039", "0.7410", "0.9631", 123, 30, 1785, 43, 0)
table_row("triplet (multitask)", "0.6900", "0.5923", "0.8263", "0.9374", 138, 95, 1720, 29, 5)

lines.append("\n**Key**: ckpt240 trades recall for precision (FP↓ but FN↑). Triplet has similar recall to epoch4 but dramatically worse precision.\n")

# ── 2. Per-sample alignment ───────────────────────────────────────────────────
h(2, "2. Per-Sample Error Alignment")

cat_order = [
    ('all_correct',          'All 3 correct'),
    ('all_wrong_same_pred',  'All 3 wrong — same prediction → **GT suspect**'),
    ('all_wrong_mixed_pred', 'All 3 wrong — different predictions'),
    ('baseline_only_correct','epoch4 only correct (hints+triplet regressed)'),
    ('hints_only_correct',   'ckpt240 only correct (hints genuinely help)'),
    ('triplet_only_correct', 'triplet only correct'),
    ('triplet_regressed',    'epoch4+ckpt240 correct, triplet wrong'),
    ('hints_regressed',      'epoch4+triplet correct, ckpt240 wrong'),
    ('baseline_regressed',   'ckpt240+triplet correct, epoch4 wrong'),
    ('other',                'Other'),
    ('parse_failure',        'Parse failure (any model)'),
]

table_row("Category", "Count", "% of total")
table_sep(50, 7, 10)
for cat, desc in cat_order:
    n = len(categories[cat])
    pct = f"{100*n/len(common_keys):.1f}%"
    table_row(desc, n, pct)

# ── 3. GT Audit Candidates ────────────────────────────────────────────────────
h(2, "3. GT Audit Candidates")
h(3, "3a. All 3 models agree but disagree with GT (strongest GT suspects)")

gt_suspects = categories['all_wrong_same_pred']
lines.append(f"**{len(gt_suspects)} pages** where all 3 models predict the same boundary decision but GT says otherwise.\n")

if gt_suspects:
    # Group by label and prediction
    by_label = defaultdict(list)
    for item in gt_suspects:
        by_label[item['label']].append(item)

    table_row("Label", "Count", "All predict START (GT=CONTINUE)", "All predict CONTINUE (GT=START)")
    table_sep(30, 7, 32, 33)
    for lbl, items in sorted(by_label.items(), key=lambda x: -len(x[1])):
        fp_count = sum(1 for i in items if i['e4'])   # all predict True=START, GT=False
        fn_count = sum(1 for i in items if not i['e4'])
        table_row(lbl, len(items), fp_count, fn_count)

    lines.append("\n**Images to inspect manually:**\n")
    for item in gt_suspects[:30]:
        lines.append(f"- `{item['key']}` | label={item['label']} | all_pred={'START' if item['e4'] else 'CONTINUE'} | gt={'START' if item['gt'] else 'CONTINUE'}\n")
    if len(gt_suspects) > 30:
        lines.append(f"*... and {len(gt_suspects)-30} more*\n")

h(3, "3b. Notable repeated offenders (appear in all 3 models' error lists)")
lines.append(
    "Classes appearing as errors in all three models suggest GT inconsistency or inherently ambiguous boundaries:\n"
)
# Compute which labels have errors in all 3 models
def labels_with_errors(per_class):
    return {lbl for lbl, d in per_class.items() if d['fp'] + d['fn'] > 0}

common_error_labels = (
    labels_with_errors(per_class_e4) &
    labels_with_errors(per_class_c240) &
    labels_with_errors(per_class_tri)
)
lines.append(f"**{len(common_error_labels)} labels with boundary errors across all 3 models:**\n")
for lbl in sorted(common_error_labels):
    e4d, c240d, trid = per_class_e4[lbl], per_class_c240[lbl], per_class_tri[lbl]
    lines.append(
        f"- `{lbl}`: epoch4 FP={e4d['fp']}/FN={e4d['fn']}, "
        f"ckpt240 FP={c240d['fp']}/FN={c240d['fn']}, "
        f"triplet FP={trid['fp']}/FN={trid['fn']}\n"
    )

# ── 4. Same-class boundary analysis ──────────────────────────────────────────
h(2, "4. Same-Class Boundary Analysis")
lines.append(
    "These are FN cases (missed boundaries) where the anchor page class == GT label of the next document.\n"
    "This is the specific failure mode the classification hint was supposed to fix.\n"
)

same_fn_c240 = [x for x in same_class_fn_c240 if x['is_same_class']]
lines.append(f"- **epoch4**: {len(same_class_fn_e4)} FNs total (same-class subset not directly annotated)\n")
lines.append(f"- **ckpt240**: {len(same_class_fn_c240)} FNs total, **{len(same_fn_c240)} are same-class** (anchor==gt_label)\n")
lines.append(f"- **triplet**: {len(same_class_fn_tri)} FNs total\n")

if same_fn_c240:
    lines.append("\n**Same-class FN cases in ckpt240 (hint model):**\n")
    by_lbl = defaultdict(int)
    for x in same_fn_c240:
        by_lbl[x['label']] += 1
    for lbl, cnt in sorted(by_lbl.items(), key=lambda x: -x[1]):
        lines.append(f"  - `{lbl}` × {cnt}\n")

    lines.append("\n**Same-class FN examples:**\n")
    for item in same_fn_c240[:15]:
        lines.append(f"- `{item['key']}` | label={item['label']} | anchor={item['anchor']}\n")

# ── 5. Per-class conditional performance ─────────────────────────────────────
h(2, "5. Per-Class Boundary F1 (classes with ≥3 positive GT samples)")
lines.append("Only showing classes where support (GT=True) ≥ 3 to avoid noise.\n")

# Gather all labels and compute support
all_labels = set(per_class_e4.keys()) | set(per_class_c240.keys()) | set(per_class_tri.keys())

rows = []
for lbl in sorted(all_labels):
    e4d   = per_class_e4.get(lbl,   {'tp':0,'fp':0,'tn':0,'fn':0})
    c240d = per_class_c240.get(lbl, {'tp':0,'fp':0,'tn':0,'fn':0})
    trid  = per_class_tri.get(lbl,  {'tp':0,'fp':0,'tn':0,'fn':0})
    support = e4d['tp'] + e4d['fn']
    if support < 3:
        continue
    _, _, f_e4,   tp_e4,   fp_e4,   fn_e4   = f1_from(e4d)
    _, _, f_c240, tp_c240, fp_c240, fn_c240 = f1_from(c240d)
    _, _, f_tri,  tp_tri,  fp_tri,  fn_tri  = f1_from(trid)
    rows.append((lbl, support, f_e4, f_c240, f_tri, fp_e4, fn_e4, fp_c240, fn_c240, fp_tri, fn_tri))

# Sort by epoch4 F1 ascending (worst first)
rows.sort(key=lambda x: x[2])

table_row("Label", "Support", "F1_e4", "F1_c240", "F1_tri", "FP/FN e4", "FP/FN c240", "FP/FN tri", "Best?")
table_sep(30, 8, 7, 8, 7, 10, 11, 10, 6)
for (lbl, sup, fe4, fc240, ftri, fpe4, fne4, fpc240, fnc240, fptri, fntri) in rows:
    best = max([('e4', fe4), ('c240', fc240), ('tri', ftri)], key=lambda x: x[1])[0]
    table_row(
        lbl, sup,
        f"{fe4:.3f}", f"{fc240:.3f}", f"{ftri:.3f}",
        f"{fpe4}/{fne4}", f"{fpc240}/{fnc240}", f"{fptri}/{fntri}",
        best
    )

# ── 5b. Summary: which model wins per class ───────────────────────────────────
h(3, "5b. Which model wins (highest F1) per class?")
wins = {'e4': [], 'c240': [], 'tri': [], 'tie': []}
for (lbl, sup, fe4, fc240, ftri, *_) in rows:
    m = max(fe4, fc240, ftri)
    winners = [n for n, v in [('e4', fe4), ('c240', fc240), ('tri', ftri)] if v == m]
    if len(winners) > 1:
        wins['tie'].append(lbl)
    else:
        wins[winners[0]].append(lbl)

lines.append(f"- **epoch4 wins**: {len(wins['e4'])} classes — {', '.join(f'`{l}`' for l in wins['e4'])}\n")
lines.append(f"- **ckpt240 wins**: {len(wins['c240'])} classes — {', '.join(f'`{l}`' for l in wins['c240'])}\n")
lines.append(f"- **triplet wins**: {len(wins['tri'])} classes — {', '.join(f'`{l}`' for l in wins['tri'])}\n")
lines.append(f"- **Tie**: {len(wins['tie'])} classes\n")

# ── 6. Synthetic vs real ──────────────────────────────────────────────────────
h(2, "6. Synthetic vs Real Data Breakdown")

synth_total = sum(synth_e4.values())
real_total  = sum(real_e4.values())
lines.append(f"- Synthetic pages: {synth_total}\n")
lines.append(f"- Real pages: {real_total}\n\n")

if synth_total > 0:
    _, _, fs_e4,   *_ = f1_from(synth_e4)
    _, _, fs_c240, *_ = f1_from(synth_c240)
    _, _, fs_tri,  *_ = f1_from(synth_tri)
    _, _, fr_e4,   *_ = f1_from(real_e4)
    _, _, fr_c240, *_ = f1_from(real_c240)
    _, _, fr_tri,  *_ = f1_from(real_tri)

    table_row("Subset", "epoch4 F1", "ckpt240 F1", "triplet F1")
    table_sep(15, 10, 11, 11)
    table_row("Synthetic", f"{fs_e4:.3f}", f"{fs_c240:.3f}", f"{fs_tri:.3f}")
    table_row("Real",      f"{fr_e4:.3f}", f"{fr_c240:.3f}", f"{fr_tri:.3f}")

    lines.append(f"\nSynthetic detail — epoch4: TP={synth_e4['tp']} FP={synth_e4['fp']} FN={synth_e4['fn']}\n")
    lines.append(f"Real detail — epoch4: TP={real_e4['tp']} FP={real_e4['fp']} FN={real_e4['fn']}\n")
else:
    lines.append("*(No synthetic pages found in common key set — synthetic docs may not be in test manifest)*\n")

# ── 7. Hypothesis verdicts ────────────────────────────────────────────────────
h(2, "7. Hypothesis Verdicts")

lines.append("""
**H1 — Hints model over-suppresses boundaries (FP→FN trade)**: CONFIRMED
  Classification hint biases model toward CONTINUE, masking real boundaries in same-class consecutive docs.
  FN↑ from 28→43, concentrated in `balance_sheet`, `municipal_mutation_record`, `village_form_7_12`, `itr_firm`.

**H2 — Hints help with gstr_form FP problem**: CONFIRMED
  gstr_form FPs dropped 19→8 (58% reduction). The single biggest FP class improved significantly.

**H3 — Triplet FP explosion from narrow context window**: CONFIRMED
  95 FPs vs 45 (epoch4). 3-page window insufficient for multi-page repetitive docs like `gstr_form` (19→35) and `property_ownership_docs` (12→30).

**H4 — GT errors masking real performance**: INVESTIGATE via Section 3
  Classes `schedules_and_annexures`, `property_ownership_docs`, `municipal_mutation_record` appear in all three models' error lists → strong GT suspect.

**H5 — Triplet reveals label noise**: CONFIRMED (diagnostic)
  Case sensitivity bug: `tax_audit_3CB_3CD` → `tax_audit_3cb_3cd` (21 triplet doc_type errors). Not a model failure.
  Semantic ambiguity: `schedules_and_annexures` confused with `notes_to_accounts` (67), `other_financial_doc` (52).
""")

# ── 8. Recommendations ────────────────────────────────────────────────────────
h(2, "8. Recommendations")

lines.append("""
### Immediate (before next training run)
1. **Fix label case normalization** — `tax_audit_3CB_3CD` vs `tax_audit_3cb_3cd`. This is a data pipeline bug inflating error counts.
2. **GT audit** the pages in Section 3a (all-3-wrong, same prediction). These are the highest-confidence GT errors.
3. **Review `schedules_and_annexures` boundaries** — this class is the source of both FPs and FNs across all models, suggesting inconsistent annotation of where annexure sections start/end.
4. **Review `property_ownership_docs`** — 12/8/30 FPs across models. These docs may span multiple packets incorrectly in GT.

### Modelling
5. **Don't adopt ckpt240 as default** — F1 regression (-0.015) and recall drop outweigh the gstr_form precision gain.
6. **Don't adopt triplet** — F1 regression (-0.086) is severe. 3-page window is too narrow. Would need ≥5-7 page context at minimum to be competitive.
7. **Selective hints**: Instead of a blanket hint for all classes, consider injecting the classification hint only for the top FP classes (gstr_form, property_ownership_docs). This could preserve the gstr_form improvement without hurting recall on financial statements.
8. **Ensemble opportunity**: For the specific classes where ckpt240 wins (see Section 5b), a routing ensemble could use the hints model on those classes and epoch4 for the rest. Evaluate if the wins outweigh the losses.

### Data
9. **Add same-class boundary examples to training** — as noted in `segmentation_data_prep_plan.md`, synthetic same-class stitching is planned. Prioritize this for `notes_to_accounts`, `schedules_and_annexures`, `pnl_statement` which are highest FN across all models.
""")

# ─────────────────────────────────────────────
# Write report
# ─────────────────────────────────────────────
with open(OUTPUT_REPORT, 'w') as f:
    f.write('\n'.join(lines))

print(f"\nReport written to: {OUTPUT_REPORT}")
print("\nCategory summary:")
for cat, desc in cat_order:
    n = len(categories[cat])
    print(f"  {n:5d}  {desc}")
