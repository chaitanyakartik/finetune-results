# Aadhaar Holdout Dataset Benchmark Report

**Generated:** 2026-04-20 11:40:30

## Executive Summary

- **Total Documents:** 25
- **With Ground Truth:** 12
- **GT Comparisons:** 12

### Overall Accuracy
- **Average:** 66.7%
- **Median:** 71.4%
- **Std Dev:** 17.6%
- **Range:** 14.3% – 85.7%

### Field-Level Accuracy
- **Correct Fields:** 56/84 (66.7%)

## Field-wise Analysis

| Field | Exact Match | Char Sim | CER | WER |
|-------|-------------|----------|-----|-----|
| Name | 91.7% (11/12) | 0.940 | 0.115 | 0.083 |
| Dateofbirth | 91.7% (11/12) | 0.983 | 0.017 | — |
| Gender | 83.3% (10/12) | 0.900 | 0.111 | — |
| Aadharnumber | 91.7% (11/12) | 0.972 | 0.028 | — |
| Address | 0.0% (0/12) | 0.759 | 0.329 | 0.344 |
| Pincode | 91.7% (11/12) | 0.958 | 0.069 | — |
| Mobilenumber | 16.7% (2/12) | 0.167 | 0.833 | — |

## Document-by-Document Results

### ⚠ file-4.jpg
- **Accuracy:** 86% (6/7)
- **Pages:** 1
- **Wrong Fields:** address

### ✗ file-19.pdf
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-2.jpg
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-20.pdf
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-21.jpg
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-22.jpg
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-23.pdf
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-24.pdf
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-25.pdf
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ file-7.pdf
- **Accuracy:** 71% (5/7)
- **Pages:** 2
- **Wrong Fields:** address, mobileNumber

### ✗ file-13.jpg
- **Accuracy:** 57% (4/7)
- **Pages:** 1
- **Wrong Fields:** gender, address, mobileNumber

### ✗ file-1.pdf
- **Accuracy:** 14% (1/7)
- **Pages:** 1
- **Wrong Fields:** name, dateOfBirth, gender, aadharNumber, address, pincode

## Documents Without Ground Truth

- file-10.pdf
- file-11.pdf
- file-12.pdf
- file-14.jpg
- file-15.jpg
- file-16.pdf
- file-17.pdf
- file-18.pdf
- file-3.jpg
- file-5.jpg
- file-6.jpg
- file-8.pdf
- file-9.pdf
