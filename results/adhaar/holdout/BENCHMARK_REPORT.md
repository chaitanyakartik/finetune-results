# Aadhaar Holdout Dataset Benchmark Report

**Generated:** 2026-04-18 13:06:04

## Executive Summary

- **Total Documents:** 25
- **With Ground Truth:** 12
- **GT Comparisons:** 12

### Overall Accuracy
- **Average:** 65.5%
- **Median:** 71.4%
- **Std Dev:** 14.2%
- **Range:** 28.6% – 85.7%

### Field-Level Accuracy
- **Correct Fields:** 55/84 (65.5%)

## Field-wise Analysis

| Field | Exact Match | Char Sim | CER | WER |
|-------|-------------|----------|-----|-----|
| Name | 83.3% (10/12) | 0.929 | 0.131 | 0.125 |
| Dateofbirth | 75.0% (9/12) | 0.875 | 0.133 | — |
| Gender | 100.0% (12/12) | 1.000 | 0.000 | — |
| Aadharnumber | 91.7% (11/12) | 0.972 | 0.028 | — |
| Address | 0.0% (0/12) | 0.764 | 0.315 | 0.348 |
| Pincode | 91.7% (11/12) | 0.917 | 0.083 | — |
| Mobilenumber | 16.7% (2/12) | 0.167 | 0.833 | — |

## Document-by-Document Results

### ⚠ file-4.jpg
- **Accuracy:** 86% (6/7)
- **Pages:** 1
- **Wrong Fields:** address

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
- **Wrong Fields:** dateOfBirth, address, mobileNumber

### ✗ file-19.pdf
- **Accuracy:** 57% (4/7)
- **Pages:** 1
- **Wrong Fields:** dateOfBirth, address, mobileNumber

### ✗ file-24.pdf
- **Accuracy:** 57% (4/7)
- **Pages:** 1
- **Wrong Fields:** name, address, mobileNumber

### ✗ file-1.pdf
- **Accuracy:** 29% (2/7)
- **Pages:** 1
- **Wrong Fields:** name, dateOfBirth, aadharNumber, address, pincode

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
