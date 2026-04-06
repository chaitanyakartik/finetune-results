# Aadhaar OCR Benchmark Results
_Generated: 2026-04-02 12:14_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| qwen35 | 84 | 0 | 1 | 83 |

## Responded (non-empty)

### Exact Match %

| Field | qwen35 |
|-------|------:|
| name | 93.2% |
| dateOfBirth | 93.2% |
| gender | 100.0% |
| aadharNumber | 80.2% |
| address | 46.1% |
| pincode | 96.9% |
| mobileNumber | 66.7% |

### Char Similarity

| Field | qwen35 |
|-------|------:|
| name | 0.998 |
| dateOfBirth | 0.931 |
| gender | 1.000 |
| aadharNumber | 0.902 |
| address | 0.927 |
| pincode | 0.982 |
| mobileNumber | 0.704 |

### WER  _(name, address only)_

| Field | qwen35 |
|-------|------:|
| name | 0.027 |
| address | 0.160 |

### Normalised CER

| Field | qwen35 |
|-------|------:|
| name | 0.004 |
| dateOfBirth | 0.069 |
| gender | 0.000 |
| aadharNumber | 0.129 |
| address | 0.127 |
| pincode | 0.018 |
| mobileNumber | 0.321 |

### Char Mismatch Rate

| Field | qwen35 |
|-------|------:|
| name | 0.024 |
| dateOfBirth | 0.000 |
| gender | 0.000 |
| aadharNumber | 0.061 |
| address | 0.251 |
| pincode | 0.003 |
| mobileNumber | 0.076 |

## Timing

| Model | workers | n | mean (s) | p50 (s) | p95 (s) | p99 (s) | throughput (req/s) |
|-------|--------:|--:|---------:|--------:|--------:|--------:|------------------:|
| qwen35 | 8 | 84 | 18.8 | 9.0 | 91.2 | 95.3 | 0.425 |
