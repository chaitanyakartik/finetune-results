# Aadhaar OCR Benchmark Results
_Generated: 2026-03-16 12:45_

## Summary

| Model | Total | Errors | Empty | Valid |
|-------|------:|-------:|------:|------:|
| base-datasetA-hybrid | 85 | 0 | 0 | 85 |
| base-datasetA-standard | 85 | 0 | 1 | 84 |
| base-datasetB-hybrid-letterhead-detect | 85 | 0 | 1 | 84 |
| base-datasetB-hybrid | 85 | 0 | 0 | 85 |
| base-datasetB-standard-letterhead-detect | 85 | 0 | 3 | 82 |
| base-datasetB-standard | 85 | 0 | 1 | 84 |
| v1-datasetA-hybrid | 85 | 0 | 0 | 85 |
| v1-datasetA-standard | 85 | 0 | 0 | 85 |
| v1-datasetB-hybrid-letterhead-detect | 85 | 0 | 0 | 85 |
| v1-datasetB-hybrid-letterhead-explicit | 85 | 0 | 0 | 85 |
| v1-datasetB-hybrid | 85 | 0 | 0 | 85 |
| v1-datasetB-standard-letterhead-detect | 85 | 0 | 0 | 85 |
| v1-datasetB-standard-letterhead-explicit | 85 | 0 | 0 | 85 |
| v1-datasetB-standard | 85 | 0 | 0 | 85 |
| v2-datasetA-hybrid | 85 | 0 | 0 | 85 |
| v2-datasetA-standard | 85 | 0 | 2 | 83 |
| v2-datasetB-hybrid-letterhead-detect | 0 | 0 | 0 | 0 |
| v2-datasetB-hybrid-letterhead-explicit | 0 | 0 | 0 | 0 |
| v2-datasetB-hybrid | 0 | 0 | 0 | 0 |
| v2-datasetB-standard-letterhead-detect | 0 | 0 | 0 | 0 |
| v2-datasetB-standard-letterhead-explicit | 0 | 0 | 0 | 0 |
| v2-datasetB-standard | 0 | 0 | 0 | 0 |
| v3-datasetA-hybrid | 85 | 0 | 0 | 85 |
| v3-datasetA-standard | 85 | 0 | 0 | 85 |

## Overall

### Exact Match %

| Field | base-datasetA-hybrid | base-datasetA-standard | base-datasetB-hybrid-letterhead-detect | base-datasetB-hybrid | base-datasetB-standard-letterhead-detect | base-datasetB-standard | v1-datasetA-hybrid | v1-datasetA-standard | v1-datasetB-hybrid-letterhead-detect | v1-datasetB-hybrid-letterhead-explicit | v1-datasetB-hybrid | v1-datasetB-standard-letterhead-detect | v1-datasetB-standard-letterhead-explicit | v1-datasetB-standard | v2-datasetA-hybrid | v2-datasetA-standard | v2-datasetB-hybrid-letterhead-detect | v2-datasetB-hybrid-letterhead-explicit | v2-datasetB-hybrid | v2-datasetB-standard-letterhead-detect | v2-datasetB-standard-letterhead-explicit | v2-datasetB-standard | v3-datasetA-hybrid | v3-datasetA-standard |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 89.3% | 90.7% | 88.0% | 89.3% | 92.0% | 90.7% | 77.3% | 61.3% | 77.3% | 76.0% | 77.3% | 57.3% | 57.3% | 57.3% | 73.3% | 48.0% | N/A | N/A | N/A | N/A | N/A | N/A | 78.7% | 50.7% |
| dateOfBirth | 97.0% | 97.0% | 97.0% | 97.0% | 95.5% | 97.0% | 77.6% | 76.1% | 76.1% | 76.1% | 76.1% | 74.6% | 74.6% | 71.6% | 59.7% | 61.2% | N/A | N/A | N/A | N/A | N/A | N/A | 67.2% | 74.6% |
| gender | 100.0% | 98.6% | 100.0% | 100.0% | 98.6% | 98.6% | 97.3% | 97.3% | 95.9% | 95.9% | 95.9% | 95.9% | 98.6% | 98.6% | 93.2% | 86.3% | N/A | N/A | N/A | N/A | N/A | N/A | 97.3% | 95.9% |
| aadharNumber | 69.7% | 69.7% | 71.0% | 69.7% | 77.6% | 69.7% | 90.8% | 93.4% | 92.1% | 92.1% | 92.1% | 94.7% | 94.7% | 94.7% | 34.2% | 38.2% | N/A | N/A | N/A | N/A | N/A | N/A | 82.9% | 92.1% |
| address | 53.7% | 46.3% | 50.8% | 53.7% | 40.3% | 46.3% | 43.3% | 32.8% | 40.3% | 38.8% | 40.3% | 23.9% | 23.9% | 28.4% | 35.8% | 17.9% | N/A | N/A | N/A | N/A | N/A | N/A | 40.3% | 20.9% |
| pincode | 96.9% | 95.4% | 95.4% | 96.9% | 87.7% | 95.4% | 90.8% | 80.0% | 90.8% | 81.5% | 90.8% | 83.1% | 73.8% | 83.1% | 89.2% | 67.7% | N/A | N/A | N/A | N/A | N/A | N/A | 90.8% | 80.0% |
| mobileNumber | 87.9% | 63.6% | 84.8% | 87.9% | 54.5% | 63.6% | 81.8% | 30.3% | 78.8% | 63.6% | 81.8% | 33.3% | 33.3% | 33.3% | 78.8% | 12.1% | N/A | N/A | N/A | N/A | N/A | N/A | 81.8% | 24.2% |

### Char Similarity

| Field | base-datasetA-hybrid | base-datasetA-standard | base-datasetB-hybrid-letterhead-detect | base-datasetB-hybrid | base-datasetB-standard-letterhead-detect | base-datasetB-standard | v1-datasetA-hybrid | v1-datasetA-standard | v1-datasetB-hybrid-letterhead-detect | v1-datasetB-hybrid-letterhead-explicit | v1-datasetB-hybrid | v1-datasetB-standard-letterhead-detect | v1-datasetB-standard-letterhead-explicit | v1-datasetB-standard | v2-datasetA-hybrid | v2-datasetA-standard | v2-datasetB-hybrid-letterhead-detect | v2-datasetB-hybrid-letterhead-explicit | v2-datasetB-hybrid | v2-datasetB-standard-letterhead-detect | v2-datasetB-standard-letterhead-explicit | v2-datasetB-standard | v3-datasetA-hybrid | v3-datasetA-standard |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.981 | 0.984 | 0.980 | 0.981 | 0.972 | 0.984 | 0.936 | 0.888 | 0.944 | 0.942 | 0.944 | 0.895 | 0.899 | 0.899 | 0.906 | 0.803 | N/A | N/A | N/A | N/A | N/A | N/A | 0.937 | 0.889 |
| dateOfBirth | 0.996 | 0.996 | 0.996 | 0.996 | 0.981 | 0.996 | 0.963 | 0.963 | 0.954 | 0.954 | 0.954 | 0.951 | 0.951 | 0.948 | 0.713 | 0.792 | N/A | N/A | N/A | N/A | N/A | N/A | 0.826 | 0.940 |
| gender | 1.000 | 0.986 | 1.000 | 1.000 | 0.986 | 0.986 | 0.995 | 0.995 | 0.992 | 0.992 | 0.992 | 0.992 | 0.997 | 0.997 | 0.943 | 0.888 | N/A | N/A | N/A | N/A | N/A | N/A | 0.995 | 0.992 |
| aadharNumber | 0.826 | 0.807 | 0.819 | 0.826 | 0.856 | 0.807 | 0.953 | 0.968 | 0.962 | 0.962 | 0.962 | 0.977 | 0.977 | 0.977 | 0.600 | 0.637 | N/A | N/A | N/A | N/A | N/A | N/A | 0.856 | 0.950 |
| address | 0.970 | 0.921 | 0.957 | 0.970 | 0.863 | 0.921 | 0.944 | 0.898 | 0.946 | 0.833 | 0.951 | 0.908 | 0.825 | 0.907 | 0.907 | 0.750 | N/A | N/A | N/A | N/A | N/A | N/A | 0.929 | 0.866 |
| pincode | 0.995 | 0.967 | 0.980 | 0.995 | 0.890 | 0.967 | 0.964 | 0.949 | 0.974 | 0.862 | 0.977 | 0.946 | 0.854 | 0.941 | 0.944 | 0.828 | N/A | N/A | N/A | N/A | N/A | N/A | 0.956 | 0.926 |
| mobileNumber | 0.934 | 0.689 | 0.889 | 0.934 | 0.611 | 0.689 | 0.933 | 0.861 | 0.918 | 0.764 | 0.921 | 0.818 | 0.721 | 0.839 | 0.835 | 0.409 | N/A | N/A | N/A | N/A | N/A | N/A | 0.914 | 0.823 |

### WER  _(name, address only)_

| Field | base-datasetA-hybrid | base-datasetA-standard | base-datasetB-hybrid-letterhead-detect | base-datasetB-hybrid | base-datasetB-standard-letterhead-detect | base-datasetB-standard | v1-datasetA-hybrid | v1-datasetA-standard | v1-datasetB-hybrid-letterhead-detect | v1-datasetB-hybrid-letterhead-explicit | v1-datasetB-hybrid | v1-datasetB-standard-letterhead-detect | v1-datasetB-standard-letterhead-explicit | v1-datasetB-standard | v2-datasetA-hybrid | v2-datasetA-standard | v2-datasetB-hybrid-letterhead-detect | v2-datasetB-hybrid-letterhead-explicit | v2-datasetB-hybrid | v2-datasetB-standard-letterhead-detect | v2-datasetB-standard-letterhead-explicit | v2-datasetB-standard | v3-datasetA-hybrid | v3-datasetA-standard |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| address | 0.086 | 0.155 | 0.098 | 0.086 | 0.197 | 0.155 | 0.149 | 0.228 | 0.145 | 0.239 | 0.142 | 0.217 | 0.302 | 0.221 | 0.225 | 0.411 | N/A | N/A | N/A | N/A | N/A | N/A | 0.161 | 0.291 |
| name | 0.052 | 0.041 | 0.059 | 0.052 | 0.046 | 0.041 | 0.153 | 0.239 | 0.151 | 0.160 | 0.151 | 0.270 | 0.263 | 0.263 | 0.194 | 0.396 | N/A | N/A | N/A | N/A | N/A | N/A | 0.146 | 0.291 |

## Responded (non-empty)

### Exact Match %

| Field | base-datasetA-hybrid | base-datasetA-standard | base-datasetB-hybrid-letterhead-detect | base-datasetB-hybrid | base-datasetB-standard-letterhead-detect | base-datasetB-standard | v1-datasetA-hybrid | v1-datasetA-standard | v1-datasetB-hybrid-letterhead-detect | v1-datasetB-hybrid-letterhead-explicit | v1-datasetB-hybrid | v1-datasetB-standard-letterhead-detect | v1-datasetB-standard-letterhead-explicit | v1-datasetB-standard | v2-datasetA-hybrid | v2-datasetA-standard | v2-datasetB-hybrid-letterhead-detect | v2-datasetB-hybrid-letterhead-explicit | v2-datasetB-hybrid | v2-datasetB-standard-letterhead-detect | v2-datasetB-standard-letterhead-explicit | v2-datasetB-standard | v3-datasetA-hybrid | v3-datasetA-standard |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 89.3% | 90.7% | 88.0% | 89.3% | 92.0% | 90.7% | 77.3% | 61.3% | 77.3% | 76.0% | 77.3% | 57.3% | 57.3% | 57.3% | 73.3% | 48.6% | N/A | N/A | N/A | N/A | N/A | N/A | 78.7% | 50.7% |
| dateOfBirth | 97.0% | 97.0% | 97.0% | 97.0% | 95.5% | 97.0% | 77.6% | 76.1% | 76.1% | 76.1% | 76.1% | 74.6% | 74.6% | 71.6% | 59.7% | 62.1% | N/A | N/A | N/A | N/A | N/A | N/A | 67.2% | 74.6% |
| gender | 100.0% | 98.6% | 100.0% | 100.0% | 98.6% | 98.6% | 97.3% | 97.3% | 95.9% | 95.9% | 95.9% | 95.9% | 98.6% | 98.6% | 93.2% | 87.5% | N/A | N/A | N/A | N/A | N/A | N/A | 97.3% | 95.9% |
| aadharNumber | 69.7% | 70.7% | 71.0% | 69.7% | 78.7% | 70.7% | 90.8% | 93.4% | 92.1% | 92.1% | 92.1% | 94.7% | 94.7% | 94.7% | 34.2% | 39.2% | N/A | N/A | N/A | N/A | N/A | N/A | 82.9% | 92.1% |
| address | 53.7% | 47.0% | 51.5% | 53.7% | 42.2% | 47.0% | 43.3% | 32.8% | 40.3% | 38.8% | 40.3% | 23.9% | 23.9% | 28.4% | 35.8% | 18.5% | N/A | N/A | N/A | N/A | N/A | N/A | 40.3% | 20.9% |
| pincode | 96.9% | 96.9% | 96.9% | 96.9% | 91.9% | 96.9% | 90.8% | 80.0% | 90.8% | 81.5% | 90.8% | 83.1% | 73.8% | 83.1% | 89.2% | 69.8% | N/A | N/A | N/A | N/A | N/A | N/A | 90.8% | 80.0% |
| mobileNumber | 87.9% | 63.6% | 84.8% | 87.9% | 54.5% | 63.6% | 81.8% | 30.3% | 78.8% | 63.6% | 81.8% | 33.3% | 33.3% | 33.3% | 78.8% | 12.5% | N/A | N/A | N/A | N/A | N/A | N/A | 81.8% | 24.2% |

### Char Similarity

| Field | base-datasetA-hybrid | base-datasetA-standard | base-datasetB-hybrid-letterhead-detect | base-datasetB-hybrid | base-datasetB-standard-letterhead-detect | base-datasetB-standard | v1-datasetA-hybrid | v1-datasetA-standard | v1-datasetB-hybrid-letterhead-detect | v1-datasetB-hybrid-letterhead-explicit | v1-datasetB-hybrid | v1-datasetB-standard-letterhead-detect | v1-datasetB-standard-letterhead-explicit | v1-datasetB-standard | v2-datasetA-hybrid | v2-datasetA-standard | v2-datasetB-hybrid-letterhead-detect | v2-datasetB-hybrid-letterhead-explicit | v2-datasetB-hybrid | v2-datasetB-standard-letterhead-detect | v2-datasetB-standard-letterhead-explicit | v2-datasetB-standard | v3-datasetA-hybrid | v3-datasetA-standard |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| name | 0.981 | 0.984 | 0.980 | 0.981 | 0.972 | 0.984 | 0.936 | 0.888 | 0.944 | 0.942 | 0.944 | 0.895 | 0.899 | 0.899 | 0.906 | 0.812 | N/A | N/A | N/A | N/A | N/A | N/A | 0.937 | 0.889 |
| dateOfBirth | 0.996 | 0.996 | 0.996 | 0.996 | 0.981 | 0.996 | 0.963 | 0.963 | 0.954 | 0.954 | 0.954 | 0.951 | 0.951 | 0.948 | 0.713 | 0.804 | N/A | N/A | N/A | N/A | N/A | N/A | 0.826 | 0.940 |
| gender | 1.000 | 0.986 | 1.000 | 1.000 | 0.986 | 0.986 | 0.995 | 0.995 | 0.992 | 0.992 | 0.992 | 0.992 | 0.997 | 0.997 | 0.943 | 0.897 | N/A | N/A | N/A | N/A | N/A | N/A | 0.995 | 0.992 |
| aadharNumber | 0.826 | 0.818 | 0.819 | 0.826 | 0.867 | 0.818 | 0.953 | 0.968 | 0.962 | 0.962 | 0.962 | 0.977 | 0.977 | 0.977 | 0.600 | 0.654 | N/A | N/A | N/A | N/A | N/A | N/A | 0.856 | 0.950 |
| address | 0.970 | 0.935 | 0.972 | 0.970 | 0.903 | 0.935 | 0.944 | 0.898 | 0.946 | 0.833 | 0.951 | 0.908 | 0.825 | 0.907 | 0.907 | 0.773 | N/A | N/A | N/A | N/A | N/A | N/A | 0.929 | 0.866 |
| pincode | 0.995 | 0.982 | 0.995 | 0.995 | 0.933 | 0.982 | 0.964 | 0.949 | 0.974 | 0.862 | 0.977 | 0.946 | 0.854 | 0.941 | 0.944 | 0.855 | N/A | N/A | N/A | N/A | N/A | N/A | 0.956 | 0.926 |
| mobileNumber | 0.934 | 0.689 | 0.889 | 0.934 | 0.611 | 0.689 | 0.933 | 0.861 | 0.918 | 0.764 | 0.921 | 0.818 | 0.721 | 0.839 | 0.835 | 0.422 | N/A | N/A | N/A | N/A | N/A | N/A | 0.914 | 0.823 |

### WER  _(name, address only)_

| Field | base-datasetA-hybrid | base-datasetA-standard | base-datasetB-hybrid-letterhead-detect | base-datasetB-hybrid | base-datasetB-standard-letterhead-detect | base-datasetB-standard | v1-datasetA-hybrid | v1-datasetA-standard | v1-datasetB-hybrid-letterhead-detect | v1-datasetB-hybrid-letterhead-explicit | v1-datasetB-hybrid | v1-datasetB-standard-letterhead-detect | v1-datasetB-standard-letterhead-explicit | v1-datasetB-standard | v2-datasetA-hybrid | v2-datasetA-standard | v2-datasetB-hybrid-letterhead-detect | v2-datasetB-hybrid-letterhead-explicit | v2-datasetB-hybrid | v2-datasetB-standard-letterhead-detect | v2-datasetB-standard-letterhead-explicit | v2-datasetB-standard | v3-datasetA-hybrid | v3-datasetA-standard |
|-------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| address | 0.086 | 0.142 | 0.084 | 0.086 | 0.159 | 0.142 | 0.149 | 0.228 | 0.145 | 0.239 | 0.142 | 0.217 | 0.302 | 0.221 | 0.225 | 0.393 | N/A | N/A | N/A | N/A | N/A | N/A | 0.161 | 0.291 |
| name | 0.052 | 0.041 | 0.059 | 0.052 | 0.046 | 0.041 | 0.153 | 0.239 | 0.151 | 0.160 | 0.151 | 0.270 | 0.263 | 0.263 | 0.194 | 0.387 | N/A | N/A | N/A | N/A | N/A | N/A | 0.146 | 0.291 |
