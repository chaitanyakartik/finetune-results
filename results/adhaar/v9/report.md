# Aadhaar OCR Benchmark Results — v9 Holdout
_Generated: 2026-04-20 11:54_
_GT: human-verified from Gemini × Qwen diff (25 docs, 22 corrections)_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| gemini_3.1_pro | 25 | 0 | 0 | 25 |
| qwen35_9b_exp2 | 25 | 0 | 0 | 25 |

## Responded (non-empty)

### Exact Match %

| Field | gemini_3.1_pro | qwen35_9b_exp2 |
|-------|------:|------:|
| name | 100.0% | 84.0% |
| dateOfBirth | 100.0% | 92.0% |
| gender | 100.0% | 96.0% |
| aadharNumber | 100.0% | 100.0% |
| address | 76.0% | 80.0% |
| pincode | 100.0% | 96.0% |
| mobileNumber | 100.0% | 92.3% |

### Char Similarity

| Field | gemini_3.1_pro | qwen35_9b_exp2 |
|-------|------:|------:|
| name | 1.000 | 0.933 |
| dateOfBirth | 1.000 | 0.956 |
| gender | 1.000 | 0.960 |
| aadharNumber | 1.000 | 1.000 |
| address | 0.835 | 0.892 |
| pincode | 1.000 | 0.993 |
| mobileNumber | 1.000 | 0.985 |

### WER  _(name, address only)_

| Field | gemini_3.1_pro | qwen35_9b_exp2 |
|-------|------:|------:|
| name | 0.000 | 0.067 |
| address | 0.096 | 0.069 |

### Normalised CER

| Field | gemini_3.1_pro | qwen35_9b_exp2 |
|-------|------:|------:|
| name | 0.000 | 0.044 |
| dateOfBirth | 0.000 | 0.044 |
| gender | 0.000 | 0.040 |
| aadharNumber | 0.000 | 0.000 |
| address | 0.045 | 0.034 |
| pincode | 0.000 | 0.007 |
| mobileNumber | 0.000 | 0.015 |

### Char Mismatch Rate

| Field | gemini_3.1_pro | qwen35_9b_exp2 |
|-------|------:|------:|
| name | 0.000 | 0.068 |
| dateOfBirth | 0.000 | 0.044 |
| gender | 0.000 | 0.040 |
| aadharNumber | 0.000 | 0.000 |
| address | 0.165 | 0.114 |
| pincode | 0.000 | 0.007 |
| mobileNumber | 0.000 | 0.015 |

## Timing

| Model | n | mean (s) | p50 (s) | p95 (s) |
|-------|--:|---------:|--------:|--------:|
| qwen35_9b_exp2 | 25 | 21.5 | 15.1 | 49.5 |
| gemini_3.1_pro | 25 | — | — | — |