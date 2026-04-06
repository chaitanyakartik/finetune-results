import json
import os
from difflib import SequenceMatcher

def char_sim(a, b):
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, str(a), str(b)).ratio()

ADDRESS_CHAR_SIM_THRESHOLD = 0.70

def collect_errors(benchmark_path):
    """Returns flat list — one entry per (image, field) error."""
    with open(benchmark_path) as f:
        data = json.load(f)

    errors = []

    for img_path, sample in data["per_sample_logs"].items():
        if not sample.get("has_response"):
            continue
        fields = sample.get("fields", {})

        for field in ["name", "dateOfBirth", "gender", "aadharNumber", "pincode", "mobileNumber"]:
            if field not in fields:
                continue
            info = fields[field]
            gt = info.get("gt")
            pred = info.get("pred")
            if gt is None and pred is None:
                continue
            if info.get("exact") != 1:
                errors.append({
                    "image": img_path,
                    "field": field,
                    "gt": gt if gt is not None else "",
                    "pred": pred if pred is not None else "",
                    "char_sim": info.get("char_sim"),
                })

        if "address" in fields:
            info = fields["address"]
            gt = info.get("gt")
            pred = info.get("pred")
            sim = info.get("char_sim")
            if gt is None and pred is None:
                continue
            if sim is None:
                sim = char_sim(gt, pred)
            if sim < ADDRESS_CHAR_SIM_THRESHOLD:
                errors.append({
                    "image": img_path,
                    "field": "address",
                    "gt": gt if gt is not None else "",
                    "pred": pred if pred is not None else "",
                    "char_sim": round(sim, 3),
                })

    return errors


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>OCR Review: {title}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', sans-serif; background: #0f1117; color: #e0e0e0; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}

  #topbar {{
    display: flex; align-items: center; gap: 12px; flex-shrink: 0;
    padding: 8px 16px; background: #1a1d27; border-bottom: 1px solid #2a2d3a;
  }}
  #topbar h2 {{ font-size: 13px; color: #aaa; font-weight: 400; white-space: nowrap; }}
  #progress {{ font-size: 13px; color: #7c8cf8; font-weight: 600; white-space: nowrap; }}
  #progress-bar-wrap {{ width: 120px; height: 5px; background: #2a2d3a; border-radius: 3px; flex-shrink: 0; }}
  #progress-bar {{ height: 5px; background: #7c8cf8; border-radius: 3px; transition: width 0.2s; }}

  #port-wrap {{ margin-left: auto; display: flex; align-items: center; gap: 6px; }}
  #port-wrap label {{ font-size: 11px; color: #555; }}
  #port-input {{
    width: 70px; background: #0f1117; border: 1px solid #2a2d3a; border-radius: 4px;
    color: #7c8cf8; font-size: 12px; padding: 3px 6px; text-align: center;
  }}
  #port-input:focus {{ outline: none; border-color: #7c8cf8; }}

  #main {{ display: flex; flex: 1; overflow: hidden; }}

  #img-panel {{
    flex: 1; display: flex; align-items: center; justify-content: center;
    background: #080a10; padding: 16px; overflow: hidden; position: relative; min-width: 0;
  }}
  #img-panel img {{
    max-width: 100%; max-height: 100%; object-fit: contain;
    border-radius: 6px; box-shadow: 0 4px 24px rgba(0,0,0,0.6);
  }}
  #img-error {{ display: none; color: #555; font-size: 12px; text-align: center; }}
  #img-path {{
    position: absolute; bottom: 6px; left: 0; right: 0;
    text-align: center; font-size: 10px; color: #333; padding: 0 8px; word-break: break-all;
  }}

  #right-panel {{
    width: 400px; flex-shrink: 0; display: flex; flex-direction: column;
    background: #13151f; border-left: 1px solid #2a2d3a;
  }}

  #field-section {{ padding: 16px; flex: 1; overflow-y: auto; }}

  .field-tag {{
    display: inline-block; font-size: 10px; font-weight: 700; color: #7c8cf8;
    text-transform: uppercase; letter-spacing: 1px; background: #1e2240;
    padding: 3px 8px; border-radius: 4px; margin-bottom: 12px;
  }}
  .sim-tag {{ font-size: 10px; color: #555; margin-left: 6px; }}

  .val-block {{ margin-bottom: 10px; }}
  .val-label {{ font-size: 10px; color: #555; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }}
  .val-box {{
    font-size: 14px; padding: 8px 10px; border-radius: 6px; border: 1px solid;
    background: #0f1117; word-break: break-word; line-height: 1.5;
  }}
  .val-box.gt   {{ border-color: #1e3a2a; color: #6fcf97; }}
  .val-box.pred {{ border-color: #3a1e1e; color: #eb5757; }}
  .val-box.pred.pred-correct {{ border-color: #1e3a2a; color: #6fcf97; }}

  #correction-wrap {{ margin-top: 10px; display: none; }}
  #correction-wrap .val-label {{ color: #f2c94c; }}
  #correction-input {{
    width: 100%; background: #0f1117; border: 1px solid #4a4010; border-radius: 6px;
    color: #f2c94c; font-size: 13px; padding: 8px 10px; font-family: inherit;
    resize: none; min-height: 60px;
  }}
  #correction-input:focus {{ outline: none; border-color: #f2c94c; }}

  #verdict-section {{ padding: 14px 16px; border-top: 1px solid #2a2d3a; flex-shrink: 0; }}
  .verdict-row {{ display: flex; gap: 8px; }}
  .vbtn {{
    flex: 1; padding: 10px 6px; border: 2px solid transparent; border-radius: 8px;
    font-size: 12px; font-weight: 600; cursor: pointer; transition: all 0.12s;
    background: #1a1d27; text-align: center; line-height: 1.3;
  }}
  .vbtn.gt-correct   {{ color: #eb5757; border-color: #3a1e1e; }}
  .vbtn.gt-correct:hover, .vbtn.gt-correct.active  {{ background: #2e1515; border-color: #eb5757; }}
  .vbtn.pred-correct {{ color: #6fcf97; border-color: #1e3a2a; }}
  .vbtn.pred-correct:hover, .vbtn.pred-correct.active {{ background: #152e1f; border-color: #6fcf97; }}
  .vbtn.both-wrong   {{ color: #f2c94c; border-color: #3a3010; }}
  .vbtn.both-wrong:hover, .vbtn.both-wrong.active {{ background: #2a2310; border-color: #f2c94c; }}

  #nav-section {{
    padding: 10px 16px; border-top: 1px solid #2a2d3a; display: flex; gap: 8px; flex-shrink: 0;
  }}
  .nav-btn {{
    flex: 1; padding: 9px; border: 1px solid #2a2d3a; border-radius: 8px;
    background: #1a1d27; color: #e0e0e0; font-size: 13px; cursor: pointer;
  }}
  .nav-btn:hover {{ background: #2a2d3a; }}
  .nav-btn:disabled {{ opacity: 0.3; cursor: default; }}
  #btn-export {{
    flex: 1; padding: 9px; border: 1px solid #7c8cf8; border-radius: 8px;
    background: #1a1d27; color: #7c8cf8; font-size: 13px; cursor: pointer; font-weight: 600;
  }}
  #btn-export:hover {{ background: #1e2240; }}
  #kbd-hint {{ font-size: 10px; color: #333; text-align: center; padding: 5px 0 8px; }}
</style>
</head>
<body>

<div id="topbar">
  <h2>OCR Review &mdash; {title}</h2>
  <span id="progress">1 / {total}</span>
  <div id="progress-bar-wrap"><div id="progress-bar" style="width:0%"></div></div>
  <div id="port-wrap">
    <label>Server port</label>
    <input id="port-input" type="number" value="8888" onchange="updatePort()">
  </div>
</div>

<div id="main">
  <div id="img-panel">
    <img id="img" src="" alt="" onerror="showImgError()">
    <div id="img-error">Image failed to load.<br>Check server port above.</div>
    <div id="img-path"></div>
  </div>

  <div id="right-panel">
    <div id="field-section">
      <div id="field-tag-wrap"></div>
      <div class="val-block">
        <div class="val-label">Ground Truth</div>
        <div class="val-box gt" id="val-gt"></div>
      </div>
      <div class="val-block">
        <div class="val-label">Prediction</div>
        <div class="val-box pred" id="val-pred"></div>
      </div>
      <div id="correction-wrap">
        <div class="val-label">Correct Value</div>
        <textarea id="correction-input" placeholder="Type the correct value..."></textarea>
      </div>
    </div>

    <div id="verdict-section">
      <div class="verdict-row">
        <button class="vbtn gt-correct"   onclick="setVerdict('gt-correct')"   title="[Z] GT is correct, pred is wrong">✗ Pred Wrong</button>
        <button class="vbtn pred-correct" onclick="setVerdict('pred-correct')" title="[C] Pred is correct, GT is wrong">✓ GT Wrong</button>
        <button class="vbtn both-wrong"   onclick="setVerdict('both-wrong')"   title="[B] Both wrong, enter correction">~ Both Wrong</button>
      </div>
    </div>

    <div id="nav-section">
      <button class="nav-btn" id="btn-prev" onclick="navigate(-1)">&#8592; Prev</button>
      <button class="nav-btn" id="btn-next" onclick="navigate(1)">Next &#8594;</button>
      <button id="btn-export" onclick="exportCSV()">Export CSV</button>
    </div>
    <div id="kbd-hint">Z = Pred Wrong &nbsp;|&nbsp; C = GT Wrong &nbsp;|&nbsp; B = Both Wrong &nbsp;|&nbsp; ← → Navigate</div>
  </div>
</div>

<script>
const ERRORS = {errors_json};

let current = 0;
const verdicts     = new Array(ERRORS.length).fill(null);  // 'gt-correct' | 'pred-correct' | 'both-wrong'
const corrections  = new Array(ERRORS.length).fill("");

function imgUrl(imgPath) {{
  const port = document.getElementById('port-input').value || '8888';
  return `http://localhost:${{port}}${{imgPath}}`;
}}

function updatePort() {{
  const item = ERRORS[current];
  document.getElementById('img').src = imgUrl(item.image);
}}

function showImgError() {{
  document.getElementById('img').style.display = 'none';
  document.getElementById('img-error').style.display = 'block';
}}

function render() {{
  const item = ERRORS[current];

  // Image
  const imgEl = document.getElementById('img');
  imgEl.style.display = 'block';
  document.getElementById('img-error').style.display = 'none';
  imgEl.src = imgUrl(item.image);
  document.getElementById('img-path').textContent = item.image;

  // Field tag
  document.getElementById('field-tag-wrap').innerHTML =
    `<span class="field-tag">${{item.field}}</span>` +
    (item.char_sim != null ? `<span class="sim-tag">char sim: ${{item.char_sim}}</span>` : '');

  // Values
  document.getElementById('val-gt').textContent   = item.gt   || '(empty)';
  const predEl = document.getElementById('val-pred');
  predEl.textContent = item.pred || '(empty)';
  predEl.className = 'val-box pred' + (verdicts[current] === 'pred-correct' ? ' pred-correct' : '');

  // Correction box
  const corrWrap = document.getElementById('correction-wrap');
  corrWrap.style.display = verdicts[current] === 'both-wrong' ? 'block' : 'none';
  if (verdicts[current] === 'both-wrong') {{
    document.getElementById('correction-input').value = corrections[current] || '';
  }}

  // Verdict buttons
  document.querySelectorAll('.vbtn').forEach(b => b.classList.remove('active'));
  if (verdicts[current]) {{
    document.querySelector(`.vbtn.${{verdicts[current]}}`).classList.add('active');
  }}

  // Progress
  const done = verdicts.filter(v => v !== null).length;
  document.getElementById('progress').textContent = `${{current + 1}} / ${{ERRORS.length}}  (${{done}} reviewed)`;
  document.getElementById('progress-bar').style.width = ((current + 1) / ERRORS.length * 100) + '%';

  // Nav
  document.getElementById('btn-prev').disabled = current === 0;
  document.getElementById('btn-next').disabled = current === ERRORS.length - 1;
}}

function save() {{
  if (verdicts[current] === 'both-wrong') {{
    corrections[current] = document.getElementById('correction-input').value;
  }}
}}

function setVerdict(v) {{
  save();
  verdicts[current] = v;
  // Auto-advance unless it's 'both-wrong' (user needs to type correction) or last item
  if (v !== 'both-wrong' && current < ERRORS.length - 1) {{
    current++;
  }}
  render();
}}

function navigate(dir) {{
  save();
  current = Math.max(0, Math.min(ERRORS.length - 1, current + dir));
  render();
}}

function exportCSV() {{
  save();
  // columns: verdict, field, gt, pred, corrected_value, image
  const rows = [['verdict', 'field', 'gt', 'pred', 'corrected_value', 'image']];
  for (let i = 0; i < ERRORS.length; i++) {{
    const e = ERRORS[i];
    const v = verdicts[i] || '';
    const corr = v === 'both-wrong' ? (corrections[i] || '') : '';
    rows.push([v, e.field, e.gt, e.pred, corr, e.image]);
  }}
  const csv = rows.map(r => r.map(c => `"${{String(c).replace(/"/g,'""')}}"`).join(',')).join('\n');
  const a = document.createElement('a');
  a.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
  a.download = 'corrections_{title}.csv';
  a.click();
}}

document.addEventListener('keydown', e => {{
  const tag = e.target.tagName;
  if (tag === 'TEXTAREA' || tag === 'INPUT') return;
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') navigate(1);
  else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') navigate(-1);
  else if (e.key === 'z' || e.key === 'Z') setVerdict('gt-correct');
  else if (e.key === 'c' || e.key === 'C') setVerdict('pred-correct');
  else if (e.key === 'b' || e.key === 'B') setVerdict('both-wrong');
}});

render();
</script>
</body>
</html>"""


def generate_html(benchmark_path, out_path, title):
    errors = collect_errors(benchmark_path)
    errors_json = json.dumps(errors, ensure_ascii=False)
    html = HTML_TEMPLATE.format(
        title=title,
        total=len(errors),
        errors_json=errors_json,
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {out_path}  ({len(errors)} field errors)")


base = "/mnt/data/chaitanya/ocr-finetuning/benchmark/results_v3"

generate_html(
    f"{base}/hybrid_deepseek_qwen35/benchmark_results.json",
    f"{base}/hybrid_deepseek_qwen35/review_val.html",
    "val"
)

generate_html(
    f"{base}/hybrid_deepseek_qwen35_train/benchmark_results.json",
    f"{base}/hybrid_deepseek_qwen35_train/review_train.html",
    "train"
)
