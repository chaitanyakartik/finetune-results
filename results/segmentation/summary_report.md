# Segmentation Finetuning — Summary Report

## Task
Detect document boundaries (START/CONTINUE) in multi-page financial document bundles using Qwen3.5-9B with sliding-window inference. Evaluated on 1981 pages (166 boundaries).

## Experiments

| # | What we tried | F1 | Precision | Recall | Key result |
|---|---|---|---|---|---|
| 1 | **Baseline** — zero-shot, window=10 | 0.587 | 0.544 | 0.639 | High false positive rate (89 FPs) — model is trigger-happy |
| 2 | **LoRA finetune** (checkpoint 138, w10) | 0.667 | 0.628 | 0.710 | Finetuning helps across the board (+30 net pages fixed) |
| 3 | **LoRA + upsampled STARTs + class hint** (epoch 5) | **0.782** | 0.775 | 0.789 | Best model. Upsampling minority class was the biggest single win (+46 net pages) |
| 4 | **Enhanced prompt only** (no finetune, w10) | 0.774 | 0.784 | 0.765 | Gemini-informed prompt nearly matches finetuned model without any training |
| 5 | **Enhanced prompt + LoRA + w5 window** | 0.767 | 0.770 | 0.765 | Smaller window reintroduced GSTR false positives. Net negative vs Exp3 |

## What worked
- **Upsampling underrepresented boundary types** was the single biggest improvement (Exp2->Exp3: +46 net pages)
- **LoRA finetuning** gave a solid baseline lift (Exp1->Exp2: +30 net pages)
- **Prompt engineering** (using Gemini to analyze errors and generate better rules) achieved near-finetuned accuracy with zero training cost
- **25 document classes** now at F1=1.0 (up from 8 in baseline)

## What didn't work
- **Shrinking the window from 10 to 5** (Exp5) caused 43 regressions vs 39 improvements — net negative. GSTR forms need the wider context to avoid hallucinating page breaks
- **Exp4 and Exp5 are lateral moves** from Exp3, not improvements — they trade errors rather than fixing them

## Remaining hard cases
- **GSTR forms**: 13 false positives in latest — model marks continuation pages as new documents. Worst offender across all experiments
- **schedules_and_annexures**: F1 stuck at ~0.44 — both false positives and false negatives. Boundaries are genuinely ambiguous
- **municipal_mutation_record**: F1=0.00 in ALL experiments — model never detects these boundaries. Likely needs targeted training data
- **26 pages** all 5 models get wrong with the same prediction — likely ground truth annotation errors worth auditing

## Recommendation
- **Ship Exp3** (LoRA+hint epoch5) as current best — highest F1 at 0.782
- **Audit the 26 GT suspect pages** before next training run — fixing bad labels is free accuracy
- **Add targeted training data** for municipal_mutation_record and schedules_and_annexures
- **Keep window=10** — the w5 experiment showed it's too narrow for long repetitive documents
