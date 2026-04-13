#!/usr/bin/env python3
"""Generate HTML for manual review of the 23 shared FN failures (both epoch4 and ckpt240 wrong)."""

import json, re, base64, os
from collections import defaultdict
from pathlib import Path

PREDS_E4   = "/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/v1/qwen35_9b-segmentation-lora-upsampled-epoch4/preds.json"
PREDS_C240 = "/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/v1/seg_continued_ckpt240/preds.json"
OUT_HTML   = "/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/v1/shared_fn_review.html"

print("Loading preds...")
with open(PREDS_E4)   as f: e4   = json.load(f)
with open(PREDS_C240) as f: c240 = json.load(f)

# Build page lookup: packet -> page_num -> full key
page_lookup = defaultdict(dict)
for k in e4:
    m = re.search(r'/([^/]+)/([^/]+)_p(\d+)\.png$', k)
    if m:
        page_lookup[m.group(2)][int(m.group(3))] = k

# Collect 23 shared FNs
cases = []
for k, r in c240.items():
    if r['status'] != 'success': continue
    m = re.search(r'/([^/]+)/([^/]+)_p(\d+)\.png$', k)
    if not m: continue
    label, packet, page_num = m.group(1), m.group(2), int(m.group(3))
    anchor = r.get('anchor_page_num', 0)
    if page_num == 1 and anchor == 1: continue  # skip trivial p1

    pred_c = bool(r['pred_is_start'])
    gt     = bool(r['gt_is_start'])
    if not (not pred_c and gt): continue  # only FNs

    anchor_class = r.get('anchor_class', '?')
    gt_label     = r.get('gt_label', '?')
    if anchor_class == gt_label: continue  # skip same-class FNs

    e4_rec = e4.get(k)
    if not e4_rec: continue
    pred_e4    = bool(e4_rec.get('pred_is_start'))
    e4_correct = (pred_e4 == gt)
    if e4_correct: continue  # skip unique-to-ckpt240 regressions

    # Find previous page
    prev_key   = page_lookup[packet].get(page_num - 1)
    prev_r     = e4.get(prev_key) if prev_key else None
    prev_label = prev_r.get('gt_label', '?') if prev_r else '?'
    prev_gt    = bool(prev_r.get('gt_is_start')) if prev_r else None

    cases.append({
        'key':          k,
        'prev_key':     prev_key,
        'packet':       packet,
        'page_num':     page_num,
        'gt_label':     gt_label,
        'anchor_class': anchor_class,
        'prev_label':   prev_label,
        'prev_gt':      prev_gt,
        'pred_e4':      pred_e4,
        'pred_c240':    pred_c,
        'gt':           gt,
    })

# Sort by packet then page
cases.sort(key=lambda x: (x['packet'], x['page_num']))
print(f"Found {len(cases)} shared FN cases")

def img_tag(path, caption):
    if not path or not os.path.exists(path):
        return f'<div class="img-missing">Image not found<br><small>{path}</small></div>'
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    ext = Path(path).suffix.lstrip('.')
    return f'''
        <figure>
            <img src="data:image/{ext};base64,{b64}" />
            <figcaption>{caption}</figcaption>
        </figure>'''

# Build HTML
FINANCIAL_SIBLINGS = {
    'pnl_statement', 'balance_sheet', 'notes_to_accounts',
    'schedules_and_annexures', 'other_financial_doc', 'combined_pnl_bs'
}
PROPERTY_SIBLINGS = {
    'municipal_mutation_record', 'village_form_7_12',
    'property_revenue_docs', 'property_ownership_docs'
}

def cluster_tag(lbl):
    if lbl in FINANCIAL_SIBLINGS: return '<span class="tag fin">financial sibling</span>'
    if lbl in PROPERTY_SIBLINGS:  return '<span class="tag prop">property sibling</span>'
    return ''

rows = []
prev_packet = None
for i, c in enumerate(cases):
    if c['packet'] != prev_packet:
        rows.append(f'<tr class="packet-header"><td colspan="5">Packet: <code>{c["packet"]}</code></td></tr>')
        prev_packet = c['packet']

    prev_caption = (
        f'<b>PREV page</b> (p{c["page_num"]-1})<br>'
        f'Label: <code>{c["prev_label"]}</code><br>'
        f'GT is_start: <span class="{"start" if c["prev_gt"] else "cont"}">'
        f'{"START" if c["prev_gt"] else "CONTINUE"}</span>'
    )
    curr_caption = (
        f'<b>THIS page</b> (p{c["page_num"]}) — MISSED BOUNDARY<br>'
        f'GT Label: <code>{c["gt_label"]}</code> {cluster_tag(c["gt_label"])}<br>'
        f'Anchor hint: <code>{c["anchor_class"]}</code> {cluster_tag(c["anchor_class"])}<br>'
        f'GT is_start: <span class="start">START</span> &nbsp;'
        f'epoch4 pred: <span class="cont">CONTINUE</span> &nbsp;'
        f'ckpt240 pred: <span class="cont">CONTINUE</span>'
    )

    rows.append(f'''
    <tr>
        <td class="idx">{i+1}</td>
        <td class="images">
            {img_tag(c["prev_key"], prev_caption)}
        </td>
        <td class="arrow">→</td>
        <td class="images">
            {img_tag(c["key"], curr_caption)}
        </td>
        <td class="meta">
            <b>Cluster:</b><br>
            prev: {cluster_tag(c["prev_label"]) or f'<code>{c["prev_label"]}</code>'}<br>
            curr: {cluster_tag(c["gt_label"]) or f'<code>{c["gt_label"]}</code>'}
            <hr>
            <b>Why both fail:</b><br>
            Visually indistinguishable boundary — same domain documents back-to-back
        </td>
    </tr>''')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Shared FN Review — epoch4 & ckpt240</title>
<style>
  body {{ font-family: system-ui, sans-serif; background: #111; color: #eee; margin: 0; padding: 16px; }}
  h1 {{ color: #fff; }}
  .summary {{ background: #1e1e2e; border-left: 4px solid #f38ba8; padding: 12px 16px; margin-bottom: 24px; border-radius: 4px; }}
  .cluster-key {{ display: flex; gap: 16px; margin-bottom: 16px; }}
  .tag {{ display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; }}
  .tag.fin  {{ background: #45475a; color: #cba6f7; border: 1px solid #cba6f7; }}
  .tag.prop {{ background: #45475a; color: #fab387; border: 1px solid #fab387; }}
  table {{ border-collapse: collapse; width: 100%; }}
  tr.packet-header td {{ background: #313244; color: #89b4fa; font-size: 1em; padding: 8px 12px; font-weight: bold; border-top: 2px solid #89b4fa; }}
  tr {{ border-bottom: 1px solid #313244; }}
  td {{ padding: 12px 8px; vertical-align: top; }}
  td.idx {{ color: #6c7086; font-size: 0.85em; width: 30px; text-align: center; }}
  td.images {{ width: 38%; }}
  td.arrow {{ width: 30px; text-align: center; font-size: 2em; color: #f38ba8; padding-top: 80px; }}
  td.meta {{ width: 200px; font-size: 0.82em; color: #bac2de; }}
  td.meta hr {{ border-color: #313244; margin: 8px 0; }}
  figure {{ margin: 0 0 8px 0; }}
  figure img {{ max-width: 100%; border: 1px solid #45475a; border-radius: 4px; display: block; }}
  figcaption {{ font-size: 0.78em; color: #a6adc8; margin-top: 6px; line-height: 1.4; }}
  .start {{ color: #a6e3a1; font-weight: bold; }}
  .cont  {{ color: #f38ba8; font-weight: bold; }}
  .img-missing {{ background: #313244; color: #6c7086; padding: 20px; border-radius: 4px; font-size: 0.8em; }}
  code {{ background: #313244; padding: 1px 5px; border-radius: 3px; font-size: 0.9em; }}
</style>
</head>
<body>
<h1>Shared FN Review: {len(cases)} cases where both epoch4 & ckpt240 miss the boundary</h1>

<div class="summary">
  <b>Pattern:</b> All 23 failures fall into two visually-similar-class clusters.<br>
  The boundary is between documents that look nearly identical to a sliding window.
  <div class="cluster-key" style="margin-top:10px">
    <span class="tag fin">financial sibling</span> pnl_statement / balance_sheet / notes_to_accounts / schedules_and_annexures / other_financial_doc
    &nbsp;&nbsp;
    <span class="tag prop">property sibling</span> municipal_mutation_record / village_form_7_12 / property_revenue_docs
  </div>
</div>

<table>
  <thead>
    <tr>
      <th>#</th><th>Previous page</th><th></th><th>Missed boundary (GT=START, both predict CONTINUE)</th><th>Notes</th>
    </tr>
  </thead>
  <tbody>
    {''.join(rows)}
  </tbody>
</table>
</body>
</html>'''

with open(OUT_HTML, 'w') as f:
    f.write(html)

print(f"Written: {OUT_HTML}")
