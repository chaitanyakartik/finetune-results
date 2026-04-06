# Aadhaar OCR Benchmark Results
_Generated: 2026-03-11 19:46_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| hybrid_deepseek_qwen35_gemini_gt | 85 | 0 | 0 | 85 |
| hybrid_deepseek_qwen35_partial_gemini_gt | 85 | 0 | 0 | 85 |
| hybrid_deepseek_qwen_gemini_gt | 85 | 0 | 0 | 85 |
| qwen35_gemini_gt | 85 | 0 | 2 | 83 |
| qwen35_partial_gemini_gt | 85 | 0 | 0 | 85 |
| qwen3vl_gemini_gt | 85 | 0 | 4 | 81 |

## Overall

### Exact Match %

| Field | hybrid_deepseek_qwen35_gemini_gt | hybrid_deepseek_qwen35_partial_gemini_gt | hybrid_deepseek_qwen_gemini_gt | qwen35_gemini_gt | qwen35_partial_gemini_gt | qwen3vl_gemini_gt |
|-------|------:|------:|------:|------:|------:|------:|
| name | 88.0% | 81.3% | 81.3% | 92.0% | 72.0% | 74.7% |
| dateOfBirth | 98.5% | 88.1% | 94.0% | 97.0% | 89.5% | 97.0% |
| gender | 100.0% | 100.0% | 97.3% | 100.0% | 100.0% | 100.0% |
| aadharNumber | 13.2% | 5.3% | 14.5% | 1.3% | 96.0% | 27.6% |
| address | 49.2% | 47.8% | 46.3% | 44.8% | 40.3% | 34.3% |
| pincode | 96.9% | 95.4% | 93.8% | 93.8% | 96.9% | 83.1% |
| mobileNumber | 87.9% | 87.9% | 90.9% | 69.7% | 63.6% | 78.8% |

### Char Similarity

| Field | hybrid_deepseek_qwen35_gemini_gt | hybrid_deepseek_qwen35_partial_gemini_gt | hybrid_deepseek_qwen_gemini_gt | qwen35_gemini_gt | qwen35_partial_gemini_gt | qwen3vl_gemini_gt |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.980 | 0.935 | 0.909 | 0.985 | 0.924 | 0.875 |
| dateOfBirth | 0.999 | 0.966 | 0.952 | 0.996 | 0.976 | 0.982 |
| gender | 1.000 | 1.000 | 0.984 | 1.000 | 1.000 | 1.000 |
| aadharNumber | 0.592 | 0.871 | 0.733 | 0.712 | 0.980 | 0.755 |
| address | 0.965 | 0.965 | 0.933 | 0.908 | 0.957 | 0.801 |
| pincode | 0.995 | 0.992 | 0.964 | 0.951 | 0.992 | 0.856 |
| mobileNumber | 0.927 | 0.958 | 0.921 | 0.750 | 0.921 | 0.809 |

### WER  _(name, address only)_

| Field | hybrid_deepseek_qwen35_gemini_gt | hybrid_deepseek_qwen35_partial_gemini_gt | hybrid_deepseek_qwen_gemini_gt | qwen35_gemini_gt | qwen35_partial_gemini_gt | qwen3vl_gemini_gt |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.059 | 0.129 | 0.148 | 0.037 | 0.168 | 0.206 |
| address | 0.102 | 0.108 | 0.152 | 0.169 | 0.117 | 0.314 |

## Responded (non-empty)

### Exact Match %

| Field | hybrid_deepseek_qwen35_gemini_gt | hybrid_deepseek_qwen35_partial_gemini_gt | hybrid_deepseek_qwen_gemini_gt | qwen35_gemini_gt | qwen35_partial_gemini_gt | qwen3vl_gemini_gt |
|-------|------:|------:|------:|------:|------:|------:|
| name | 88.0% | 81.3% | 81.3% | 92.0% | 72.0% | 74.7% |
| dateOfBirth | 98.5% | 88.1% | 94.0% | 97.0% | 89.5% | 97.0% |
| gender | 100.0% | 100.0% | 97.3% | 100.0% | 100.0% | 100.0% |
| aadharNumber | 13.2% | 5.3% | 14.5% | 1.3% | 96.0% | 27.6% |
| address | 49.2% | 47.8% | 46.3% | 46.1% | 40.3% | 36.5% |
| pincode | 96.9% | 95.4% | 93.8% | 96.8% | 96.9% | 88.5% |
| mobileNumber | 87.9% | 87.9% | 90.9% | 69.7% | 63.6% | 78.8% |

### Char Similarity

| Field | hybrid_deepseek_qwen35_gemini_gt | hybrid_deepseek_qwen35_partial_gemini_gt | hybrid_deepseek_qwen_gemini_gt | qwen35_gemini_gt | qwen35_partial_gemini_gt | qwen3vl_gemini_gt |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.980 | 0.935 | 0.909 | 0.985 | 0.924 | 0.875 |
| dateOfBirth | 0.999 | 0.966 | 0.952 | 0.996 | 0.976 | 0.982 |
| gender | 1.000 | 1.000 | 0.984 | 1.000 | 1.000 | 1.000 |
| aadharNumber | 0.592 | 0.871 | 0.733 | 0.722 | 0.980 | 0.755 |
| address | 0.965 | 0.965 | 0.933 | 0.936 | 0.957 | 0.852 |
| pincode | 0.995 | 0.992 | 0.964 | 0.982 | 0.992 | 0.913 |
| mobileNumber | 0.927 | 0.958 | 0.921 | 0.750 | 0.921 | 0.809 |

### WER  _(name, address only)_

| Field | hybrid_deepseek_qwen35_gemini_gt | hybrid_deepseek_qwen35_partial_gemini_gt | hybrid_deepseek_qwen_gemini_gt | qwen35_gemini_gt | qwen35_partial_gemini_gt | qwen3vl_gemini_gt |
|-------|------:|------:|------:|------:|------:|------:|
| name | 0.059 | 0.129 | 0.148 | 0.037 | 0.168 | 0.206 |
| address | 0.102 | 0.108 | 0.152 | 0.143 | 0.117 | 0.271 |
