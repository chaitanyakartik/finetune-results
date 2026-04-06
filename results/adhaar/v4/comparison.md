# Aadhaar OCR Benchmark Results
_Generated: 2026-03-26 13:41_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| qwen35_9b | 84 | 0 | 1 | 83 |
| qwen35_9b_lora | 84 | 0 | 0 | 84 |
| qwen35_9b_lora_augmented | 84 | 0 | 0 | 84 |
| qwen35_9b_lora_augmented_chkpt129_fixed | 84 | 0 | 0 | 84 |
| qwen35_9b_lora_augmented_chkpt258 | 84 | 0 | 0 | 84 |
| qwen35_9b_lora_augmented_chkpt258_fixed | 84 | 0 | 0 | 84 |
| qwen35_9b_lora_fixed | 84 | 0 | 1 | 83 |
| qwen35_9b_sanity | 84 | 0 | 1 | 83 |
| qwen35_9b_targeted_exp1 | 84 | 0 | 0 | 84 |
| qwen35_9b_targeted_exp2 | 84 | 0 | 0 | 84 |
| qwen35_bestt | 84 | 0 | 0 | 84 |

## Responded (non-empty)

### Exact Match %

| Field | qwen35_9b | qwen35_9b_lora | qwen35_9b_lora_augmented | qwen35_9b_lora_augmented_chkpt129_fixed | qwen35_9b_lora_augmented_chkpt258 | qwen35_9b_lora_augmented_chkpt258_fixed | qwen35_9b_lora_fixed | qwen35_9b_sanity | qwen35_9b_targeted_exp1 | qwen35_9b_targeted_exp2 | qwen35_bestt |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 95.9% | 64.4% | 64.4% | 95.9% | 61.6% | 94.5% | 95.9% | 95.9% | 95.9% | 94.5% | 90.4% |
| dateOfBirth | 94.5% | 76.7% | 80.8% | 98.6% | 82.2% | 95.9% | 94.5% | 94.5% | 100.0% | 100.0% | 98.6% |
| gender | 100.0% | 94.5% | 94.5% | 100.0% | 93.2% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| aadharNumber | 97.5% | 98.8% | 98.8% | 98.8% | 100.0% | 100.0% | 97.5% | 97.5% | 100.0% | 100.0% | 98.8% |
| address | 46.1% | 19.7% | 21.2% | 51.5% | 25.8% | 65.2% | 46.1% | 46.1% | 63.6% | 60.6% | 48.5% |
| pincode | 100.0% | 81.5% | 83.1% | 100.0% | 78.5% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98.5% |
| mobileNumber | 72.7% | 18.2% | 21.2% | 93.9% | 27.3% | 93.9% | 72.7% | 72.7% | 93.9% | 97.0% | 87.9% |

### Char Similarity

| Field | qwen35_9b | qwen35_9b_lora | qwen35_9b_lora_augmented | qwen35_9b_lora_augmented_chkpt129_fixed | qwen35_9b_lora_augmented_chkpt258 | qwen35_9b_lora_augmented_chkpt258_fixed | qwen35_9b_lora_fixed | qwen35_9b_sanity | qwen35_9b_targeted_exp1 | qwen35_9b_targeted_exp2 | qwen35_bestt |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.998 | 0.886 | 0.901 | 0.998 | 0.904 | 0.997 | 0.998 | 0.998 | 0.998 | 0.997 | 0.995 |
| dateOfBirth | 0.950 | 0.898 | 0.962 | 0.991 | 0.949 | 0.959 | 0.950 | 0.950 | 1.000 | 1.000 | 0.986 |
| gender | 1.000 | 0.981 | 0.989 | 1.000 | 0.975 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| aadharNumber | 0.985 | 0.988 | 0.992 | 0.992 | 1.000 | 1.000 | 0.985 | 0.985 | 1.000 | 1.000 | 0.994 |
| address | 0.951 | 0.832 | 0.827 | 0.959 | 0.876 | 0.987 | 0.951 | 0.951 | 0.987 | 0.985 | 0.967 |
| pincode | 1.000 | 0.913 | 0.920 | 1.000 | 0.918 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.997 |
| mobileNumber | 0.727 | 0.468 | 0.586 | 0.939 | 0.627 | 0.939 | 0.727 | 0.727 | 0.939 | 0.970 | 0.893 |

### WER  _(name, address only)_

| Field | qwen35_9b | qwen35_9b_lora | qwen35_9b_lora_augmented | qwen35_9b_lora_augmented_chkpt129_fixed | qwen35_9b_lora_augmented_chkpt258 | qwen35_9b_lora_augmented_chkpt258_fixed | qwen35_9b_lora_fixed | qwen35_9b_sanity | qwen35_9b_targeted_exp1 | qwen35_9b_targeted_exp2 | qwen35_bestt |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| address | 0.144 | 0.353 | 0.344 | 0.118 | 0.262 | 0.049 | 0.142 | 0.144 | 0.050 | 0.055 | 0.088 |
| name | 0.021 | 0.242 | 0.237 | 0.021 | 0.241 | 0.034 | 0.021 | 0.021 | 0.021 | 0.034 | 0.036 |

### Normalised CER

| Field | qwen35_9b | qwen35_9b_lora | qwen35_9b_lora_augmented | qwen35_9b_lora_augmented_chkpt129_fixed | qwen35_9b_lora_augmented_chkpt258 | qwen35_9b_lora_augmented_chkpt258_fixed | qwen35_9b_lora_fixed | qwen35_9b_sanity | qwen35_9b_targeted_exp1 | qwen35_9b_targeted_exp2 | qwen35_bestt |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.003 | 0.130 | 0.118 | 0.003 | 0.117 | 0.004 | 0.003 | 0.003 | 0.003 | 0.004 | 0.007 |
| dateOfBirth | 0.062 | 0.115 | 0.037 | 0.021 | 0.052 | 0.041 | 0.062 | 0.062 | 0.000 | 0.000 | 0.014 |
| gender | 0.000 | 0.027 | 0.021 | 0.000 | 0.034 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| aadharNumber | 0.017 | 0.012 | 0.012 | 0.012 | 0.000 | 0.000 | 0.017 | 0.017 | 0.000 | 0.000 | 0.009 |
| address | 0.102 | 0.236 | 0.234 | 0.083 | 0.168 | 0.023 | 0.102 | 0.102 | 0.023 | 0.026 | 0.062 |
| pincode | 0.000 | 0.100 | 0.092 | 0.000 | 0.085 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.003 |
| mobileNumber | 0.273 | 0.600 | 0.515 | 0.061 | 0.394 | 0.061 | 0.273 | 0.273 | 0.061 | 0.030 | 0.115 |

### Char Mismatch Rate

| Field | qwen35_9b | qwen35_9b_lora | qwen35_9b_lora_augmented | qwen35_9b_lora_augmented_chkpt129_fixed | qwen35_9b_lora_augmented_chkpt258 | qwen35_9b_lora_augmented_chkpt258_fixed | qwen35_9b_lora_fixed | qwen35_9b_sanity | qwen35_9b_targeted_exp1 | qwen35_9b_targeted_exp2 | qwen35_bestt |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.013 | 0.135 | 0.147 | 0.013 | 0.146 | 0.024 | 0.013 | 0.013 | 0.013 | 0.024 | 0.039 |
| dateOfBirth | 0.038 | 0.059 | 0.037 | 0.010 | 0.038 | 0.000 | 0.038 | 0.038 | 0.000 | 0.000 | 0.000 |
| gender | 0.000 | 0.041 | 0.041 | 0.000 | 0.041 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| aadharNumber | 0.000 | 0.000 | 0.012 | 0.012 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.005 |
| address | 0.266 | 0.463 | 0.475 | 0.238 | 0.387 | 0.140 | 0.264 | 0.266 | 0.147 | 0.172 | 0.238 |
| pincode | 0.000 | 0.082 | 0.067 | 0.000 | 0.069 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.003 |
| mobileNumber | 0.000 | 0.218 | 0.261 | 0.000 | 0.130 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.027 |
