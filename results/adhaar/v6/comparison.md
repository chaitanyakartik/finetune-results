# Aadhaar OCR Benchmark Results
_Generated: 2026-04-02 11:05_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| qwen35 | 84 | 0 | 0 | 84 |
| qwen35_batch4 | 84 | 0 | 51 | 33 |
| qwen35_compiled | 84 | 0 | 0 | 84 |
| qwen35_torchao_fp8 | 84 | 0 | 0 | 84 |
| qwen35_torchao_fp8w | 84 | 0 | 0 | 84 |
| qwen35_torchao_int4 | 84 | 0 | 0 | 84 |

## Responded (non-empty)

### Exact Match %

| Field | qwen35 | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8 | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|------:|------:|
| name | 95.9% | 90.0% | 95.9% | 95.9% | 95.9% | 94.5% |
| dateOfBirth | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 91.8% |
| gender | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| aadharNumber | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| address | 62.1% | 59.3% | 62.1% | 63.6% | 63.6% | 57.6% |
| pincode | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| mobileNumber | 93.9% | 93.8% | 97.0% | 97.0% | 93.9% | 75.8% |

### Char Similarity

| Field | qwen35 | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8 | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.998 | 0.994 | 0.998 | 0.998 | 0.998 | 0.997 |
| dateOfBirth | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.949 |
| gender | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| aadharNumber | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| address | 0.985 | 0.983 | 0.985 | 0.987 | 0.986 | 0.970 |
| pincode | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| mobileNumber | 0.939 | 0.938 | 0.970 | 0.994 | 0.964 | 0.758 |

### WER  _(name, address only)_

| Field | qwen35 | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8 | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|------:|------:|
| address | 0.054 | 0.073 | 0.055 | 0.051 | 0.051 | 0.071 |
| name | 0.021 | 0.050 | 0.021 | 0.021 | 0.021 | 0.036 |

### Normalised CER

| Field | qwen35 | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8 | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.003 | 0.007 | 0.003 | 0.003 | 0.003 | 0.004 |
| dateOfBirth | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.110 |
| gender | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| aadharNumber | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| address | 0.026 | 0.029 | 0.026 | 0.024 | 0.025 | 0.044 |
| pincode | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| mobileNumber | 0.061 | 0.062 | 0.030 | 0.006 | 0.036 | 0.242 |

### Char Mismatch Rate

| Field | qwen35 | qwen35_batch4 | qwen35_compiled | qwen35_torchao_fp8 | qwen35_torchao_fp8w | qwen35_torchao_int4 |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.013 | 0.031 | 0.013 | 0.013 | 0.013 | 0.016 |
| dateOfBirth | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.069 |
| gender | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| aadharNumber | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| address | 0.159 | 0.237 | 0.163 | 0.143 | 0.145 | 0.145 |
| pincode | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| mobileNumber | 0.000 | 0.000 | 0.000 | 0.006 | 0.006 | 0.000 |

## Timing

| Model | workers | n | mean (s) | p50 (s) | p95 (s) | p99 (s) | throughput (req/s) |
|-------|--------:|--:|---------:|--------:|--------:|--------:|------------------:|
| qwen35 | 8 | 84 | 16.4 | 9.7 | 63.9 | 66.1 | 0.487 |
| qwen35_batch4 | 4 | 84 | 5.7 | 4.5 | 9.9 | 20.6 | 0.701 |
| qwen35_compiled | 8 | 84 | 11.4 | 9.6 | 24.0 | 34.5 | 0.700 |
| qwen35_torchao_fp8 | 8 | 84 | 30.7 | 25.7 | 77.3 | 83.4 | 0.261 |
| qwen35_torchao_fp8w | 8 | 84 | 40.5 | 36.4 | 87.5 | 97.8 | 0.197 |
| qwen35_torchao_int4 | 8 | 84 | 27.9 | 21.3 | 75.8 | 78.2 | 0.287 |
