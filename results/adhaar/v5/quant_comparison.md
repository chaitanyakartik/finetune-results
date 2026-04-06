# Quantization Sweep — Results

_Generated: 2026-04-02 10:44_

| Variant | p50 ms | p95 ms | req/s | name | dateOfBi | gender | aadharNu | address | pincode | mobileNu |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BF16 (baseline) | 8962.6 | 49937.7 | 0.451 | 95.9 | 100.0 | 100.0 | 98.8 | 62.1 | 100.0 | 97.0 |
| BnB INT8 | — | — | — | — | — | — | — | — | — | — |
| BnB NF4 (4-bit) | — | — | — | — | — | — | — | — | — | — |
| AWQ INT4 | — | — | — | — | — | — | — | — | — | — |

## Accuracy Gate (critical fields: aadharNumber, dateOfBirth)

Drop >3% on either field fails the gate.

- **BnB INT8**: PASS (no critical drop)
- **BnB NF4 (4-bit)**: PASS (no critical drop)