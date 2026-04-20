# Segmentation Experiments — Model Registry

## Experiment Summary

| # | Name | Dir | Finetuned? | Window | Prompt | Hint? | Acc | F1 | TP | FP | FN | Key Change |
|---|------|-----|-----------|--------|--------|-------|-----|-----|---|---|---|------------|
| 1 | Baseline | v1/qwen35_9b_segmentation_sliding_parsing_fix | No | 10 | v0 | No | 92.48% | 0.587 | 106 | 89 | 60 | Zero-shot base model |
| 2 | LoRA w10 | v1/qwen35_9b-segmentation-lora-w10-checkpoint-138-merged | Yes (ckpt 138) | 10 | v0 | No | 94.18% | 0.667 | 115 | 68 | 47 | First LoRA finetune |
| 3 | LoRA+hint epoch5 | v1/qwen35_9b-segmentation-lora-upsampled-epoch5 | Yes (epoch 5) | 10 | v0 | Yes | 96.31% | 0.782 | 131 | 38 | 35 | Upsampled START class + classification hint |
| 4 | Enhanced prompt w10 | v2/segg_sliding_enhanced_upsampled | No | 10 | v1 | Yes | 96.26% | 0.774 | 127 | 35 | 39 | Gemini-informed prompt, no finetuning |
| 5 | Enhanced+agg w5 | v2/segg_w5_no_headers | Yes | 5 | v1 | Yes | 96.11% | 0.767 | 127 | 38 | 39 | Smaller window, aggressive upsampling, no headers |

**Base model**: Qwen3.5-9B (`models--Qwen--Qwen3.5-9B/snapshots/c202236235762e1c871ad0ccb60c8ee5ba337b9a`)
**Eval set**: 1981 pages (166 START, 1815 CONTINUE) from `segmentation_val.jsonl`

---

## Prompt Versions

### v0 — Basic prompt
**Location**: `doc_classification/qwen35_9b_segmentation_sliding_enhanced/prompts.py`

Basic sliding-window segmentation prompt with:
- Generic continuity signals (same header/footer style, sequential page numbers, mid-sentence content)
- Generic forced segmentation rules (different title/entity/form header = new start)
- ITR one-page rule
- Basic financial statement sibling rules (4 types)
- Software tax report rules

### v1 — Enhanced prompt (Gemini-informed)
**Location**: `doc_classification/segg_sliding_enhanced_upsampled/prompts.py`

Built using a Gemini-assisted error analysis pipeline:
1. `analyze_errors_gemini.py` sent error cases (with surrounding page images) to Gemini 2.0 Flash for visual analysis
2. `generate_better_prompt.py` used Gemini 3-Pro to synthesize findings into improved rules
3. Results saved to `prompt_improvements.json`, then integrated into prompts.py

**Key additions over v0:**
- **Text continuation markers**: "Carried Over" / "continued..." patterns
- **Audit document chains**: FORM 3CD/3CA continuations explicitly handled
- **Property doc attachments**: Index-II, CHALLAN MTR Form Number-6, Receipt of Document Handling Charges = CONTINUATION
- **Specific form headers that force START**: "INDIAN INCOME TAX RETURN ACKNOWLEDGEMENT", "FORM NO. 16" (with logo), "FORM 3CA"
- **Legal/corporate starts**: "INDIA NON JUDICIAL" stamp, "RENT AGREEMENT" title, "Certificate of Incorporation"
- **Web reports**: Breadcrumbs like "Home > MCA Services" + government portal logos
- **GSTR-3B section**: Multi-page GSTR-3B should NOT be over-segmented; only START if GSTIN/Year/Period changes
- **Expanded financial siblings**: Added combined_pnl_bs, other_financial_doc, "Independent Auditor's Report", "Statement of Changes in Equity"
- **Regional scripts**: Gujarati numerals (7/12), Hindi/Marathi survey number text
- **Balance sheet rule**: Merged from standalone section into broader financial sibling rules

---

## Detailed Experiment Descriptions

### Exp1: Baseline (Zero-shot sliding window)
- **Directory**: `v1/qwen35_9b_segmentation_sliding_parsing_fix`
- **Model**: Qwen3.5-9B base (no finetuning)
- **Inference**: Sliding window of 10 pages, v0 prompt
- **Training**: None
- **Notes**: This is the "parsing_fix" version. The original `qwen35_9b_segmentation_sliding` had 533 parse failures; this version fixed the output parsing to handle edge cases. Still has high FP count (89) — model is trigger-happy marking continuation pages as starts.

### Exp2: LoRA w10 (First finetune)
- **Directory**: `v1/qwen35_9b-segmentation-lora-w10-checkpoint-138-merged`
- **Model**: Qwen3.5-9B + LoRA, checkpoint 138, merged
- **Inference**: Sliding window of 10, v0 prompt
- **Training**: LoRA finetuning on segmentation training data, window=10
- **Key change from Exp1**: Finetuning reduces both FP (89->68) and FN (60->47). Biggest gains: fewer hallucinated starts in multi-page documents.

### Exp3: LoRA + hint + upsampled (Best F1)
- **Directory**: `v1/qwen35_9b-segmentation-lora-upsampled-epoch5`
- **Model**: Qwen3.5-9B + LoRA, upsampled training data, epoch 5, merged
- **Inference**: Sliding window of 10, v0 prompt, classification hint
- **Training**: LoRA with upsampled START examples (addressing class imbalance), 5 epochs
- **Key change from Exp2**: Upsampling + classification hint dramatically reduces FP (68->38) and FN (47->35). Best F1 at 0.782. Remaining errors concentrated in gstr_form (16 FP), property_ownership_docs (12 FP), pnl_statement (6 FN), schedules_and_annexures (4 FP + 5 FN).

### Exp4: Enhanced prompt w10 (Prompt engineering, no finetune)
- **Directory**: `v2/segg_sliding_enhanced_upsampled`
- **Model**: Qwen3.5-9B base (NO finetuning)
- **Inference**: Sliding window of 10, v1 prompt (enhanced), classification hint
- **Training**: None — pure prompt engineering experiment
- **Key change from Exp3**: Tests whether the enhanced prompt alone (without finetuning) can match finetuned performance. Achieves 96.26% accuracy (comparable to Exp3's 96.31%) with slightly fewer FP (35 vs 38) but more FN (39 vs 35). The prompt improvements help with precision but hurt recall slightly.

### Exp5: Enhanced prompt + aggressive upsampling w5 (Latest)
- **Directory**: `v2/segg_w5_no_headers`
- **Model**: Qwen3.5-9B + LoRA (w5_no_headers variant, merged)
- **Inference**: Sliding window of **5** (reduced from 10), v1 prompt (no headers variant), classification hint
- **Training**: LoRA with aggressive upsampling of underrepresented boundary types
- **Key change from Exp4**: Combines finetuning with enhanced prompt. Window reduced to 5 (faster inference). Despite smaller context, maintains comparable accuracy (96.11%). 1 parse failure. Has error concentration at window position 3 (30 errors vs 12 in w10).

---

## Progression Logic

```
Exp1 (zero-shot) --[add LoRA]--> Exp2 (finetune)
    --[upsample + hint]--> Exp3 (best F1)
    --[new prompt, drop finetune]--> Exp4 (prompt-only test)
    --[add finetune + shrink window]--> Exp5 (latest)
```

Key questions this progression answers:
1. **Does finetuning help?** Yes: Exp1->Exp2 shows +0.08 F1
2. **Does upsampling help?** Yes: Exp2->Exp3 shows +0.115 F1
3. **Can prompt engineering replace finetuning?** Nearly: Exp4 (no finetune) matches Exp3 (finetuned) on accuracy
4. **Does smaller window hurt?** Slightly: Exp5 w5 is -0.15% accuracy vs Exp4 w10, with error concentration at position 3
5. **Remaining hard cases**: gstr_form FPs, schedules_and_annexures (both FP+FN), pnl_statement FNs, property doc FPs
