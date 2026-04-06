# Aadhaar OCR Benchmark Results
_Generated: 2026-03-25 12:02_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| hybrid_chandra_qwen35_LoRA_augmented_aux_v2_chkpt1 | 84 | 0 | 0 | 84 |
| hybrid_chandra_qwen35_best | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35 | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35_LoRA_augmented_aux_v2 | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35_LoRA_augmented_no_aux | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35_LoRA_augmented_no_aux_chkpt1 | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35_LoRA_augmented_no_aux_v2_chkpt1 | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35_LoRA_chkpt_1 | 85 | 1 | 0 | 84 |
| hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1 | 85 | 1 | 0 | 84 |
| hybrid_deepseek_qwen35_best | 84 | 0 | 0 | 84 |
| hybrid_deepseek_qwen35_bestt | 84 | 0 | 0 | 84 |
| qwen35 | 84 | 0 | 0 | 84 |
| qwen35_LoRA_augmented_no_aux | 84 | 0 | 0 | 84 |
| qwen35_LoRA_augmented_no_aux_chkpt1 | 84 | 0 | 0 | 84 |
| xchandra_LoRA_augmented_aux_v2_chkpt1 | 84 | 0 | 0 | 84 |

## Responded (non-empty)

### Exact Match %

| Field | hybrid_chandra_qwen35_LoRA_augmented_aux_v2_chkpt1 | hybrid_chandra_qwen35_best | hybrid_deepseek_qwen35 | hybrid_deepseek_qwen35_LoRA_augmented_aux_v2 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_chkpt1 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_v2_chkpt1 | hybrid_deepseek_qwen35_LoRA_chkpt_1 | hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1 | hybrid_deepseek_qwen35_best | hybrid_deepseek_qwen35_bestt | qwen35 | qwen35_LoRA_augmented_no_aux | qwen35_LoRA_augmented_no_aux_chkpt1 | xchandra_LoRA_augmented_aux_v2_chkpt1 |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 87.7% | 89.0% | 91.8% | 77.0% | 78.4% | 90.5% | 90.5% | 93.2% | 93.2% | 90.5% | 89.0% | 91.8% | 53.4% | 91.8% | 54.8% |
| dateOfBirth | 97.3% | 97.3% | 100.0% | 71.2% | 74.2% | 98.5% | 98.5% | 100.0% | 100.0% | 98.5% | 97.3% | 93.2% | 72.6% | 94.5% | 95.9% |
| gender | 100.0% | 100.0% | 100.0% | 97.3% | 97.3% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 98.6% | 95.9% | 100.0% | 94.5% |
| aadharNumber | 81.5% | 96.3% | 80.2% | 96.0% | 96.0% | 97.3% | 92.0% | 96.3% | 96.3% | 96.0% | 96.3% | 75.0% | 100.0% | 100.0% | 71.6% |
| address | 48.5% | 51.5% | 54.5% | 40.9% | 42.4% | 51.5% | 51.5% | 57.6% | 51.5% | 56.1% | 51.5% | 47.7% | 24.2% | 48.5% | 22.7% |
| pincode | 98.5% | 98.5% | 98.5% | 89.2% | 87.7% | 96.9% | 96.9% | 100.0% | 100.0% | 96.9% | 98.5% | 95.3% | 75.4% | 96.9% | 83.1% |
| mobileNumber | 87.9% | 90.9% | 90.6% | 81.8% | 81.8% | 90.9% | 87.9% | 93.9% | 81.8% | 90.9% | 90.9% | 65.6% | 24.2% | 90.9% | 84.8% |

### Char Similarity

| Field | hybrid_chandra_qwen35_LoRA_augmented_aux_v2_chkpt1 | hybrid_chandra_qwen35_best | hybrid_deepseek_qwen35 | hybrid_deepseek_qwen35_LoRA_augmented_aux_v2 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_chkpt1 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_v2_chkpt1 | hybrid_deepseek_qwen35_LoRA_chkpt_1 | hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1 | hybrid_deepseek_qwen35_best | hybrid_deepseek_qwen35_bestt | qwen35 | qwen35_LoRA_augmented_no_aux | qwen35_LoRA_augmented_no_aux_chkpt1 | xchandra_LoRA_augmented_aux_v2_chkpt1 |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.989 | 0.990 | 0.983 | 0.916 | 0.932 | 0.981 | 0.982 | 0.995 | 0.996 | 0.981 | 0.990 | 0.985 | 0.910 | 0.996 | 0.690 |
| dateOfBirth | 0.997 | 0.997 | 1.000 | 0.924 | 0.911 | 0.999 | 0.999 | 1.000 | 1.000 | 0.999 | 0.997 | 0.931 | 0.938 | 0.945 | 0.982 |
| gender | 1.000 | 1.000 | 1.000 | 0.995 | 0.995 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.986 | 0.992 | 1.000 | 0.984 |
| aadharNumber | 0.891 | 0.974 | 0.856 | 0.974 | 0.974 | 0.989 | 0.945 | 0.974 | 0.972 | 0.978 | 0.974 | 0.813 | 1.000 | 1.000 | 0.821 |
| address | 0.969 | 0.969 | 0.970 | 0.907 | 0.924 | 0.977 | 0.966 | 0.974 | 0.970 | 0.973 | 0.969 | 0.935 | 0.876 | 0.973 | 0.756 |
| pincode | 0.997 | 0.997 | 0.992 | 0.947 | 0.939 | 0.995 | 0.995 | 1.000 | 1.000 | 0.995 | 0.997 | 0.974 | 0.913 | 0.995 | 0.844 |
| mobileNumber | 0.931 | 0.962 | 0.932 | 0.835 | 0.906 | 0.953 | 0.934 | 0.965 | 0.832 | 0.964 | 0.962 | 0.682 | 0.813 | 0.909 | 0.923 |

### WER  _(name, address only)_

| Field | hybrid_chandra_qwen35_LoRA_augmented_aux_v2_chkpt1 | hybrid_chandra_qwen35_best | hybrid_deepseek_qwen35 | hybrid_deepseek_qwen35_LoRA_augmented_aux_v2 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_chkpt1 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_v2_chkpt1 | hybrid_deepseek_qwen35_LoRA_chkpt_1 | hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1 | hybrid_deepseek_qwen35_best | hybrid_deepseek_qwen35_bestt | qwen35 | qwen35_LoRA_augmented_no_aux | qwen35_LoRA_augmented_no_aux_chkpt1 | xchandra_LoRA_augmented_aux_v2_chkpt1 |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.082 | 0.055 | 0.043 | 0.173 | 0.158 | 0.050 | 0.050 | 0.030 | 0.030 | 0.050 | 0.055 | 0.039 | 0.260 | 0.032 | 0.372 |
| address | 0.090 | 0.089 | 0.086 | 0.183 | 0.167 | 0.078 | 0.099 | 0.074 | 0.089 | 0.079 | 0.089 | 0.142 | 0.278 | 0.072 | 0.375 |

### Normalised CER

| Field | hybrid_chandra_qwen35_LoRA_augmented_aux_v2_chkpt1 | hybrid_chandra_qwen35_best | hybrid_deepseek_qwen35 | hybrid_deepseek_qwen35_LoRA_augmented_aux_v2 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_chkpt1 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_v2_chkpt1 | hybrid_deepseek_qwen35_LoRA_chkpt_1 | hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1 | hybrid_deepseek_qwen35_best | hybrid_deepseek_qwen35_bestt | qwen35 | qwen35_LoRA_augmented_no_aux | qwen35_LoRA_augmented_no_aux_chkpt1 | xchandra_LoRA_augmented_aux_v2_chkpt1 |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.014 | 0.012 | N/A | 0.098 | 0.087 | 0.020 | 0.020 | N/A | N/A | 0.021 | 0.012 | N/A | 0.116 | 0.005 | 0.320 |
| dateOfBirth | 0.004 | 0.004 | N/A | 0.083 | 0.097 | 0.002 | 0.002 | N/A | N/A | 0.002 | 0.004 | N/A | 0.065 | 0.055 | 0.082 |
| gender | 0.000 | 0.000 | N/A | 0.009 | 0.009 | 0.000 | 0.000 | N/A | N/A | 0.000 | 0.000 | N/A | 0.016 | 0.000 | 0.046 |
| aadharNumber | 0.143 | 0.034 | N/A | 0.041 | 0.041 | 0.014 | 0.069 | N/A | N/A | 0.028 | 0.034 | N/A | 0.000 | 0.000 | 0.281 |
| address | 0.055 | 0.054 | N/A | 0.121 | 0.101 | 0.040 | 0.064 | N/A | N/A | 0.047 | 0.054 | N/A | 0.168 | 0.049 | 0.326 |
| pincode | 0.003 | 0.003 | N/A | 0.064 | 0.069 | 0.005 | 0.005 | N/A | N/A | 0.005 | 0.003 | N/A | 0.105 | 0.005 | 0.177 |
| mobileNumber | 0.079 | 0.049 | N/A | 0.173 | 0.091 | 0.054 | 0.076 | N/A | N/A | 0.045 | 0.049 | N/A | 0.221 | 0.091 | 0.121 |

### Char Mismatch Rate

| Field | hybrid_chandra_qwen35_LoRA_augmented_aux_v2_chkpt1 | hybrid_chandra_qwen35_best | hybrid_deepseek_qwen35 | hybrid_deepseek_qwen35_LoRA_augmented_aux_v2 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_chkpt1 | hybrid_deepseek_qwen35_LoRA_augmented_no_aux_v2_chkpt1 | hybrid_deepseek_qwen35_LoRA_chkpt_1 | hybrid_deepseek_qwen35_LoRA_ocr_aux_chkpt_1 | hybrid_deepseek_qwen35_best | hybrid_deepseek_qwen35_bestt | qwen35 | qwen35_LoRA_augmented_no_aux | qwen35_LoRA_augmented_no_aux_chkpt1 | xchandra_LoRA_augmented_aux_v2_chkpt1 |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.033 | 0.022 | N/A | 0.115 | 0.105 | 0.037 | 0.026 | N/A | N/A | 0.027 | 0.022 | N/A | 0.189 | 0.036 | 0.105 |
| dateOfBirth | 0.004 | 0.004 | N/A | 0.068 | 0.067 | 0.002 | 0.002 | N/A | N/A | 0.002 | 0.004 | N/A | 0.038 | 0.000 | 0.041 |
| gender | 0.000 | 0.000 | N/A | 0.018 | 0.018 | 0.000 | 0.000 | N/A | N/A | 0.000 | 0.000 | N/A | 0.032 | 0.000 | 0.025 |
| aadharNumber | 0.098 | 0.030 | N/A | 0.034 | 0.034 | 0.014 | 0.062 | N/A | N/A | 0.027 | 0.030 | N/A | 0.000 | 0.000 | 0.205 |
| address | 0.294 | 0.294 | N/A | 0.285 | 0.290 | 0.235 | 0.245 | N/A | N/A | 0.221 | 0.294 | N/A | 0.386 | 0.233 | 0.293 |
| pincode | 0.003 | 0.003 | N/A | 0.033 | 0.054 | 0.005 | 0.005 | N/A | N/A | 0.005 | 0.003 | N/A | 0.110 | 0.005 | 0.018 |
| mobileNumber | 0.054 | 0.054 | N/A | 0.024 | 0.030 | 0.027 | 0.051 | N/A | N/A | 0.051 | 0.054 | N/A | 0.233 | 0.000 | 0.058 |
