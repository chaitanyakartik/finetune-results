# Aadhaar OCR Benchmark Results
_Generated: 2026-04-07 17:53_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| qwen35_batch4 | 84 | 0 | 51 | 33 |
| qwen35_compiled | 84 | 0 | 0 | 84 |
| qwen35_torchao_fp8w | 84 | 0 | 0 | 84 |
| qwen35_torchao_int4 | 84 | 0 | 0 | 84 |

## Responded (non-empty)

### Exact Match %

| Field | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|
| name | 90.0% | 95.9% | 95.9% | 94.5% |
| dateOfBirth | 100.0% | 100.0% | 100.0% | 91.8% |
| gender | 100.0% | 100.0% | 100.0% | 100.0% |
| aadharNumber | 96.9% | 100.0% | 100.0% | 100.0% |
| address | 59.3% | 62.1% | 63.6% | 57.6% |
| pincode | 100.0% | 100.0% | 100.0% | 100.0% |
| mobileNumber | 93.8% | 97.0% | 93.9% | 75.8% |

### Char Similarity

| Field | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|
| name | 0.994 | 0.998 | 0.998 | 0.997 |
| dateOfBirth | 1.000 | 1.000 | 1.000 | 0.949 |
| gender | 1.000 | 1.000 | 1.000 | 1.000 |
| aadharNumber | 0.976 | 1.000 | 1.000 | 1.000 |
| address | 0.983 | 0.985 | 0.986 | 0.970 |
| pincode | 1.000 | 1.000 | 1.000 | 1.000 |
| mobileNumber | 0.938 | 0.970 | 0.964 | 0.758 |

### WER  _(name, address only)_

| Field | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|
| address | 0.073 | 0.054 | 0.051 | 0.071 |
| name | 0.050 | 0.021 | 0.016 | 0.036 |

### Normalised CER

| Field | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|
| name | 0.007 | 0.003 | 0.002 | 0.004 |
| dateOfBirth | 0.000 | 0.000 | 0.000 | 0.110 |
| gender | 0.000 | 0.000 | 0.000 | 0.000 |
| aadharNumber | 0.029 | 0.000 | 0.000 | 0.000 |
| address | 0.029 | 0.026 | 0.025 | 0.044 |
| pincode | 0.000 | 0.000 | 0.000 | 0.000 |
| mobileNumber | 0.062 | 0.030 | 0.036 | 0.242 |

### Char Mismatch Rate

| Field | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|
| name | 0.031 | 0.013 | 0.012 | 0.016 |
| dateOfBirth | 0.000 | 0.000 | 0.000 | 0.069 |
| gender | 0.000 | 0.000 | 0.000 | 0.000 |
| aadharNumber | 0.016 | 0.000 | 0.000 | 0.000 |
| address | 0.237 | 0.159 | 0.145 | 0.145 |
| pincode | 0.000 | 0.000 | 0.000 | 0.000 |
| mobileNumber | 0.000 | 0.000 | 0.006 | 0.000 |

## Timing

| Model | workers | n | mean (s) | p50 (s) | p95 (s) | p99 (s) | throughput (req/s) |
|-------|--------:|--:|---------:|--------:|--------:|--------:|------------------:|
| qwen35_batch4 | 4 | 84 | 5.8 | 5.1 | 10.3 | 16.3 | 0.695 |
| qwen35_compiled | 8 | 84 | 11.4 | 9.9 | 24.4 | 34.7 | 0.703 |
| qwen35_torchao_fp8w | 8 | 84 | 35.2 | 35.2 | 56.4 | 66.2 | 0.227 |
| qwen35_torchao_int4 | 8 | 84 | 22.5 | 20.1 | 44.0 | 75.5 | 0.355 |
