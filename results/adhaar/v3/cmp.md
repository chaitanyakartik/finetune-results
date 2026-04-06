# Aadhaar OCR Benchmark — Detailed Comparison
_Generated: 2026-03-16 19:58_

> Exact Match % and Char Similarity are from the official `compute_metrics` (GT-null samples excluded from denominator).
> Normalized CER, Char Mismatch Rate, and Extra Char Diff use the same denominator but strip all spaces + special chars before computing.


## Exact Match %

| Field | hybrid | hybrid_LoRA_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1_newgt | hybrid_lora_img | qwen35 | qwen35_lora_img |
|-------|------:|------:|------:|------:|------:|------:|------:|
| name | 91.8% | 93.2% | 93.2% | 93.2% | 80.8% | 91.8% | 52.0% |
| dateOfBirth | 100.0% | 100.0% | 100.0% | 100.0% | 76.7% | 93.2% | 74.0% |
| gender | 100.0% | 100.0% | 100.0% | 100.0% | 97.3% | 98.6% | 95.9% |
| aadharNumber | 80.2% | 96.3% | 96.3% | 96.3% | 100.0% | 74.1% | 100.0% |
| address | 54.5% | 57.6% | 51.5% | 51.5% | 40.9% | 47.0% | 18.2% |
| pincode | 98.5% | 100.0% | 100.0% | 100.0% | 92.3% | 93.8% | 73.8% |
| mobileNumber | 90.6% | 93.9% | 81.8% | 81.8% | 81.8% | 65.6% | 24.2% |

## Char Similarity

| Field | hybrid | hybrid_LoRA_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1_newgt | hybrid_lora_img | qwen35 | qwen35_lora_img |
|-------|------:|------:|------:|------:|------:|------:|------:|
| name | 0.9833 | 0.9948 | 0.9956 | 0.9956 | 0.9362 | 0.9847 | 0.8907 |
| dateOfBirth | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9075 | 0.9315 | 0.9473 |
| gender | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9945 | 0.9863 | 0.9808 |
| aadharNumber | 0.8555 | 0.9735 | 0.9716 | 0.9716 | 1.0000 | 0.8027 | 1.0000 |
| address | 0.9698 | 0.9737 | 0.9700 | 0.9700 | 0.9186 | 0.9205 | 0.8672 |
| pincode | 0.9923 | 1.0000 | 1.0000 | 1.0000 | 0.9564 | 0.9590 | 0.9051 |
| mobileNumber | 0.9324 | 0.9647 | 0.8320 | 0.8320 | 0.9061 | 0.6824 | 0.7910 |

## Normalized CER (lower=better)

| Field | hybrid | hybrid_LoRA_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1_newgt | hybrid_lora_img | qwen35 | qwen35_lora_img |
|-------|------:|------:|------:|------:|------:|------:|------:|
| name | 0.0183 | 0.0071 | 0.0062 | 0.0062 | 0.0804 | 0.0180 | 0.1439 |
| dateOfBirth | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.1027 | 0.0685 | 0.0634 |
| gender | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0091 | 0.0137 | 0.0228 |
| aadharNumber | 1.3704 | 0.2284 | 0.0556 | 0.0556 | 0.0000 | 1.4877 | 0.0000 |
| address | 0.0534 | 0.0463 | 0.0535 | 0.0535 | 0.1079 | 0.1263 | 0.1901 |
| pincode | 0.0103 | 0.0000 | 0.0000 | 0.0000 | 0.0487 | 0.0436 | 0.1154 |
| mobileNumber | 0.0781 | 0.0455 | 0.1758 | 0.1758 | 0.0970 | 0.3281 | 0.2333 |

## Char Mismatch Rate (substitutions only)

| Field | hybrid | hybrid_LoRA_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1_newgt | hybrid_lora_img | qwen35 | qwen35_lora_img |
|-------|------:|------:|------:|------:|------:|------:|------:|
| name | 0.0372 | 0.0268 | 0.0259 | 0.0259 | 0.0941 | 0.0369 | 0.2011 |
| dateOfBirth | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0651 | 0.0000 | 0.0497 |
| gender | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0183 | 0.0000 | 0.0183 |
| aadharNumber | 0.5833 | 0.0864 | 0.0000 | 0.0000 | 0.0000 | 0.6327 | 0.0000 |
| address | 0.2181 | 0.1949 | 0.2384 | 0.2384 | 0.2776 | 0.2218 | 0.4585 |
| pincode | 0.0103 | 0.0000 | 0.0000 | 0.0000 | 0.0205 | 0.0128 | 0.1051 |
| mobileNumber | 0.0531 | 0.0515 | 0.0273 | 0.0273 | 0.0364 | 0.0531 | 0.2242 |

## Extra Char Diff (length errors only)

| Field | hybrid | hybrid_LoRA_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1 | hybrid_LoRA_ocr_aux_chkpt_1_newgt | hybrid_lora_img | qwen35 | qwen35_lora_img |
|-------|------:|------:|------:|------:|------:|------:|------:|
| name | 0.0039 | 0.0015 | 0.0015 | 0.0015 | 0.0388 | 0.0049 | 0.0428 |
| dateOfBirth | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0411 | 0.0685 | 0.0137 |
| gender | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0091 | 0.0137 | 0.0228 |
| aadharNumber | 1.3302 | 0.2222 | 0.0556 | 0.0556 | 0.0000 | 1.4290 | 0.0000 |
| address | 0.0446 | 0.0366 | 0.0413 | 0.0413 | 0.0796 | 0.1039 | 0.0853 |
| pincode | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0308 | 0.0308 | 0.0154 |
| mobileNumber | 0.0406 | 0.0091 | 0.1576 | 0.1576 | 0.0606 | 0.2906 | 0.0667 |
