"""
Generate an interactive HTML review page for benchmark results.
Shows GT vs predictions side-by-side with images, highlighting errors.
"""
import json
import os
import re
import difflib
from pathlib import Path
from html import escape

RESULTS_DIR = Path(__file__).parent
FIELDS = ["name", "dateOfBirth", "gender", "aadharNumber", "address", "pincode", "mobileNumber"]
# Fields that count toward "error" badges and sorting (address excluded — too noisy)
ERROR_FIELDS = ["name", "dateOfBirth", "gender", "aadharNumber", "pincode", "mobileNumber"]

# ── Which models to include (order matters for display) ──────────────────
MODEL_DIRS = [
    ("hybrid_deepseek_qwen35",                "Hybrid Base"),
    ("hybrid_deepseek_qwen35_LoRA_chkpt_1",   "Hybrid LoRA ep1"),
    ("hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1", "Hybrid LoRA+OCR ep1"),
]

def _is_indic(c):
    cp = ord(c)
    return 0x0900 <= cp <= 0x0DFF

def strip_indic(text):
    if not text: return text
    cleaned = "".join(c for c in text if not _is_indic(c))
    return re.sub(r"  +", " ", cleaned).strip()

def norm(val, field):
    """Match benchmark.py normalise() exactly."""
    if val is None: return ""
    text = str(val).strip()
    text = strip_indic(text)
    text = text.lower()
    if field == "dateOfBirth":
        text = text.replace("-", "/")
        text = re.sub(r"[^\w/]", " ", text)
    elif field == "aadharNumber":
        text = re.sub(r"[^\w]", "", text)
        if re.fullmatch(r'\d{4}', text):
            text = 'x' * 8 + text
    elif field == "name":
        pass
    else:
        text = re.sub(r"[^a-z0-9\s]", "", text)
    return re.sub(r"\s+", " ", text).strip()

def char_sim(a, b):
    if not a and not b: return 1.0
    if not a or not b: return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()

def diff_html(gt_str, pred_str):
    """Produce character-level diff HTML highlighting mismatches."""
    if gt_str == pred_str:
        return escape(pred_str) if pred_str else '<span class="null">null</span>'
    if not pred_str:
        return '<span class="null">null</span>'
    if not gt_str:
        return f'<span class="added">{escape(pred_str)}</span>'

    sm = difflib.SequenceMatcher(None, gt_str, pred_str)
    parts = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            parts.append(escape(pred_str[j1:j2]))
        elif op == "replace":
            parts.append(f'<span class="changed">{escape(pred_str[j1:j2])}</span>')
        elif op == "insert":
            parts.append(f'<span class="added">{escape(pred_str[j1:j2])}</span>')
        elif op == "delete":
            pass  # missing from pred
    return "".join(parts)

def load_preds(dirname):
    path = RESULTS_DIR / dirname / "preds.json"
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)

def build_html():
    # Load all model predictions
    models = []
    all_preds = {}
    for dirname, label in MODEL_DIRS:
        preds = load_preds(dirname)
        if preds:
            models.append((dirname, label))
            all_preds[dirname] = preds

    if not models:
        print("No preds.json found!")
        return

    # Collect all image keys from the first model
    first_preds = all_preds[models[0][0]]
    all_keys = sorted(first_preds.keys())

    # Compute per-sample, per-model, per-field results
    samples = []
    for img_path in all_keys:
        gt_data = None
        sample_results = {}
        has_any_error = False
        error_fields = set()

        for dirname, label in models:
            preds = all_preds.get(dirname, {})
            entry = preds.get(img_path)
            if not entry:
                continue
            if gt_data is None:
                gt_data = entry.get("gt_data") or {}

            pred_fields = entry.get("pred_fields") or {}
            field_results = {}
            for f in FIELDS:
                gv = norm(gt_data.get(f), f)
                pv = norm(pred_fields.get(f), f)
                exact = (gv == pv) if gv else True  # skip if GT is empty
                sim = char_sim(gv, pv) if gv else 1.0
                gt_raw = str(gt_data.get(f)) if gt_data.get(f) is not None else None
                pred_raw = str(pred_fields.get(f)) if pred_fields.get(f) is not None else None
                field_results[f] = {
                    "gt": gt_raw,
                    "pred": pred_raw,
                    "exact": exact,
                    "sim": sim,
                }
                if not exact and f in ERROR_FIELDS:
                    has_any_error = True
                    error_fields.add(f)
            sample_results[dirname] = {
                "field_results": field_results,
                "raw_response": entry.get("raw_response", ""),
                "ocr_text": entry.get("ocr_text", ""),
            }

        samples.append({
            "img_path": img_path,
            "gt_data": gt_data or {},
            "results": sample_results,
            "has_error": has_any_error,
            "error_fields": error_fields,
        })

    # Sort: errors first, then by number of error fields desc
    samples.sort(key=lambda s: (-len(s["error_fields"]), not s["has_error"], s["img_path"]))

    # Count stats
    n_total = len(samples)
    n_errors = sum(1 for s in samples if s["has_error"])
    n_perfect = n_total - n_errors

    # ── Build HTML ───────────────────────────────────────────────────────
    model_labels = [label for _, label in models]
    model_dirs = [d for d, _ in models]

    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aadhaar OCR Benchmark Review</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0d1117; color: #c9d1d9; padding: 20px; }}
h1 {{ color: #58a6ff; margin-bottom: 8px; }}
.stats {{ color: #8b949e; margin-bottom: 20px; font-size: 14px; }}
.stats span {{ margin-right: 20px; }}
.stats .err {{ color: #f85149; }}
.stats .ok {{ color: #3fb950; }}

.controls {{ position: sticky; top: 0; background: #0d1117; padding: 12px 0; z-index: 100; border-bottom: 1px solid #30363d; margin-bottom: 20px; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.controls label {{ color: #8b949e; font-size: 13px; cursor: pointer; }}
.controls select, .controls input {{ background: #161b22; color: #c9d1d9; border: 1px solid #30363d; border-radius: 6px; padding: 6px 10px; font-size: 13px; }}
.controls button {{ background: #21262d; color: #c9d1d9; border: 1px solid #30363d; border-radius: 6px; padding: 6px 14px; cursor: pointer; font-size: 13px; }}
.controls button:hover {{ background: #30363d; }}
.controls button.active {{ background: #1f6feb; border-color: #1f6feb; color: #fff; }}

.sample {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; margin-bottom: 16px; overflow: hidden; }}
.sample.perfect {{ border-color: #238636; }}
.sample.has-error {{ border-color: #f85149; }}
.sample-header {{ padding: 12px 16px; background: #21262d; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }}
.sample-header:hover {{ background: #30363d; }}
.sample-header .filename {{ font-family: monospace; font-size: 13px; color: #58a6ff; }}
.sample-header .badges {{ display: flex; gap: 6px; }}
.badge {{ padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }}
.badge.error {{ background: #f8514922; color: #f85149; }}
.badge.ok {{ background: #23863622; color: #3fb950; }}

.sample-body {{ display: none; padding: 16px; }}
.sample-body.open {{ display: block; }}

.sample-content {{ display: grid; grid-template-columns: 300px 1fr; gap: 16px; }}
.image-panel img {{ width: 100%; border-radius: 6px; border: 1px solid #30363d; }}

.fields-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
.fields-table th {{ text-align: left; padding: 6px 10px; background: #21262d; color: #8b949e; font-weight: 600; border-bottom: 1px solid #30363d; position: sticky; top: 0; }}
.fields-table td {{ padding: 6px 10px; border-bottom: 1px solid #21262d; vertical-align: top; max-width: 300px; word-wrap: break-word; }}
.fields-table tr.error td {{ background: #f851490d; }}
.fields-table td.field-name {{ font-weight: 600; color: #d2a8ff; white-space: nowrap; }}
.fields-table td.gt {{ color: #3fb950; font-family: monospace; font-size: 12px; }}
.fields-table td.pred {{ font-family: monospace; font-size: 12px; }}
.fields-table td.pred .changed {{ background: #f8514944; color: #ffa198; border-radius: 2px; padding: 0 1px; }}
.fields-table td.pred .added {{ background: #f8514944; color: #ffa198; border-radius: 2px; padding: 0 1px; }}
.fields-table td.pred .null {{ color: #484f58; font-style: italic; }}
.fields-table td.sim {{ color: #8b949e; text-align: right; font-family: monospace; }}
.fields-table td.sim.low {{ color: #f85149; }}
.fields-table td.sim.mid {{ color: #d29922; }}
.fields-table td.sim.high {{ color: #3fb950; }}

.model-label {{ font-size: 11px; color: #8b949e; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
.expand-all {{ margin-left: auto; }}
</style>
</head>
<body>
<h1>Aadhaar OCR Benchmark Review</h1>
<div class="stats">
    <span>Total: {n_total}</span>
    <span class="err">Errors: {n_errors}</span>
    <span class="ok">Perfect: {n_perfect}</span>
    <span>Models: {', '.join(model_labels)}</span>
</div>

<div class="controls">
    <label>Filter:
        <select id="filter">
            <option value="all">All samples</option>
            <option value="errors" selected>Errors only</option>
            <option value="perfect">Perfect only</option>
        </select>
    </label>
    <label>Field:
        <select id="fieldFilter">
            <option value="all">All fields</option>
            {"".join(f'<option value="{f}">{f}</option>' for f in FIELDS)}
        </select>
    </label>
    <label>Search:
        <input type="text" id="search" placeholder="filename or GT value...">
    </label>
    <button class="expand-all" onclick="toggleAll()">Expand/Collapse All</button>
</div>

<div id="samples">
"""]

    for idx, sample in enumerate(samples):
        img_path = sample["img_path"]
        filename = os.path.basename(img_path)
        gt = sample["gt_data"]
        has_error = sample["has_error"]
        err_fields = sample["error_fields"]

        err_class = "has-error" if has_error else "perfect"
        err_badges = "".join(f'<span class="badge error">{f}</span>' for f in sorted(err_fields))
        if not has_error:
            err_badges = '<span class="badge ok">all correct</span>'

        data_fields = " ".join(sorted(err_fields)) if err_fields else ""

        html_parts.append(f"""
<div class="sample {err_class}" data-has-error="{str(has_error).lower()}" data-error-fields="{escape(data_fields)}" data-filename="{escape(filename.lower())}">
  <div class="sample-header" onclick="toggle(this)">
    <span class="filename">{escape(filename)}</span>
    <div class="badges">{err_badges}</div>
  </div>
  <div class="sample-body" id="body-{idx}">
    <div class="sample-content">
      <div class="image-panel">
        <img src="/image?path={escape(img_path)}" loading="lazy" alt="{escape(filename)}">
      </div>
      <div>
        <table class="fields-table">
          <thead><tr>
            <th>Field</th>
            <th>Ground Truth</th>
""")
        for dirname, label in models:
            html_parts.append(f'            <th>{escape(label)}</th>\n')
        html_parts.append('            <th>Sim</th>\n          </tr></thead>\n          <tbody>\n')

        for f in FIELDS:
            gt_val = str(gt.get(f)) if gt.get(f) is not None else None
            gt_display = escape(gt_val) if gt_val else '<span class="null">null</span>'

            # Check if any model got this wrong
            any_wrong = f in err_fields
            row_class = ' class="error"' if any_wrong else ''

            html_parts.append(f'          <tr{row_class}>\n')
            html_parts.append(f'            <td class="field-name">{f}</td>\n')
            html_parts.append(f'            <td class="gt">{gt_display}</td>\n')

            for dirname, label in models:
                res = sample["results"].get(dirname, {}).get("field_results", {}).get(f, {})
                pred_val = res.get("pred")
                sim = res.get("sim", 1.0)
                exact = res.get("exact", True)

                if gt_val and not exact:
                    pred_html = diff_html(gt_val, pred_val)
                elif pred_val is None:
                    pred_html = '<span class="null">null</span>'
                else:
                    pred_html = escape(pred_val)

                html_parts.append(f'            <td class="pred">{pred_html}</td>\n')

            # Show worst sim across models
            sims = []
            for dirname, _ in models:
                res = sample["results"].get(dirname, {}).get("field_results", {}).get(f, {})
                if gt_val:  # only show sim if GT exists
                    sims.append(res.get("sim", 1.0))
            if sims:
                worst_sim = min(sims)
                sim_class = "high" if worst_sim >= 0.95 else ("mid" if worst_sim >= 0.8 else "low")
                html_parts.append(f'            <td class="sim {sim_class}">{worst_sim:.3f}</td>\n')
            else:
                html_parts.append(f'            <td class="sim">-</td>\n')

            html_parts.append('          </tr>\n')

        html_parts.append('          </tbody>\n        </table>\n      </div>\n    </div>\n  </div>\n</div>\n')

    html_parts.append("""
</div>

<script>
function toggle(header) {
    const body = header.nextElementSibling;
    body.classList.toggle('open');
}
function toggleAll() {
    const bodies = document.querySelectorAll('.sample-body');
    const anyOpen = Array.from(bodies).some(b => b.classList.contains('open'));
    bodies.forEach(b => { if (anyOpen) b.classList.remove('open'); else b.classList.add('open'); });
}
function applyFilters() {
    const filter = document.getElementById('filter').value;
    const fieldFilter = document.getElementById('fieldFilter').value;
    const search = document.getElementById('search').value.toLowerCase();
    document.querySelectorAll('.sample').forEach(s => {
        let show = true;
        if (filter === 'errors' && s.dataset.hasError !== 'true') show = false;
        if (filter === 'perfect' && s.dataset.hasError !== 'false') show = false;
        if (fieldFilter !== 'all' && !s.dataset.errorFields.includes(fieldFilter)) show = false;
        if (search && !s.dataset.filename.includes(search) && !s.textContent.toLowerCase().includes(search)) show = false;
        s.style.display = show ? '' : 'none';
    });
}
document.getElementById('filter').addEventListener('change', applyFilters);
document.getElementById('fieldFilter').addEventListener('change', applyFilters);
document.getElementById('search').addEventListener('input', applyFilters);
applyFilters();
</script>
</body>
</html>""")

    out_path = RESULTS_DIR / "review.html"
    with open(out_path, "w") as f:
        f.write("".join(html_parts))
    print(f"Written to {out_path}")
    print(f"Samples: {n_total}, Errors: {n_errors}, Perfect: {n_perfect}")

if __name__ == "__main__":
    build_html()
