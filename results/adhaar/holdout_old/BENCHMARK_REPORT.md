# Aadhaar Holdout Dataset Benchmark Report

**Generated:** 2026-04-16 16:34:50

## Executive Summary

- **Total Documents:** 24
- **With Ground Truth:** 10
- **GT Comparisons:** 10

### Overall Accuracy
- **Average:** 48.6%
- **Median:** 57.1%
- **Std Dev:** 31.7%
- **Range:** 0.0% - 85.7%

### Field-Level Accuracy
- **Correct Fields:** 34/70 (48.6%)

## Field-wise Analysis

| Field | Exact Match | Char Sim | CER | WER |
|-------|-------------|----------|-----|-----|
| Name | 70.0% (7/10) | 0.797 | 0.310 | 0.300 |
| Dateofbirth | 50.0% (5/10) | 0.790 | 0.210 | — |
| Gender | 80.0% (8/10) | 0.960 | 0.100 | — |
| Aadharnumber | 60.0% (6/10) | 0.870 | 0.158 | — |
| Address | 0.0% (0/10) | 0.605 | 0.486 | 0.606 |
| Pincode | 70.0% (7/10) | 0.833 | 0.217 | — |
| Mobilenumber | 10.0% (1/10) | 0.100 | 0.900 | — |

## Document-by-Document Results

### ⚠ A2301020216_Co-Borrower2_AdhaarXML_vkyc
- **Accuracy:** 86% (6/7)
- **Pages:** 1
- **Wrong Fields:** address

### ✗ A2301020157_app_adhaar
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ A2306060349 KYC CoApplicant 1 - Job Card issued by NREGA
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ Address Document Proof of possesion of Aadhar card
- **Accuracy:** 71% (5/7)
- **Pages:** 1
- **Wrong Fields:** address, mobileNumber

### ✗ A2301050052 Applicant Address Proof - Proof of possession of Aadhaar
- **Accuracy:** 57% (4/7)
- **Pages:** 2
- **Wrong Fields:** aadharNumber, address, mobileNumber

### ✗ A2306060180_app_adhaar
- **Accuracy:** 57% (4/7)
- **Pages:** 1
- **Wrong Fields:** dateOfBirth, address, mobileNumber

### ✗ A2306060349 Identity Document CoApplicant 2 Proof of possesion of Aadhar card
- **Accuracy:** 57% (4/7)
- **Pages:** 1
- **Wrong Fields:** dateOfBirth, address, mobileNumber

### ✗ Identity Document CoApplicant 2 Proof of possesion of Aadhar card
- **Accuracy:** 14% (1/7)
- **Pages:** 1
- **Wrong Fields:** name, dateOfBirth, aadharNumber, address, pincode, mobileNumber

### ✗ Identity Document CoApplicant 1 Proof of possesion of Aadhar card
- **Accuracy:** 0% (0/7)
- **Pages:** 1
- **Wrong Fields:** name, dateOfBirth, gender, aadharNumber, address, pincode, mobileNumber

### ✗ Identity Document Proof of possesion of Aadhar card
- **Accuracy:** 0% (0/7)
- **Pages:** 1
- **Wrong Fields:** name, dateOfBirth, gender, aadharNumber, address, pincode, mobileNumber

## Documents Without Ground Truth

- A2301020157 FATHER ADHAR (1)
- A2301020157_co2_adhaar
- A2301020216_co1_adhaar
- A2301020216_co2_adhaar
- A2301050052 Coapplicant 1 Address Proof - Proof of possession of Aadhaar
- A2301050052 Coapplicant 2 Address Proof - Proof of possession of Aadhaar
- A2306060180 Identity Document CoApplicant 1 Proof of possesion of Aadhar card
- A2306060180 Identity Document CoApplicant 2 Proof of possesion of Aadhar card
- A2306060180 Identity Document Proof of possesion of Aadhar card
- A2306060180_co1_adhaar
- A2306060180_co2_adhaar
- A2306060268 Identity Document CoApplicant 1 Proof of possesion of Aadhar card
- A2306060268 Identity Document CoApplicant 2 Proof of possesion of Aadhar card
- A2306060268 Identity Document CoApplicant 3 Proof of possesion of Aadhar card

## Inference Statistics
