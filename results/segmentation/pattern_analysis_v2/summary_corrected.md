# Window Position Error Analysis (Corrected)
## Methodology
For each experiment, pages are assigned to windows based on their position within their document:
- Pages within a document are indexed 0, 1, 2, ... (document-absolute)
- Windows are formed with stride and window_size as specified
- Within-window position = (document-absolute index) - (window start) + 1

## Exp3 (w10, stride=9)
**Configuration:** Window size=10, Stride=9

**Overall Statistics:**
- Total pages: 1981
- Total errors: 73
- FP errors: 38
- FN errors: 35
- Overall error rate: 3.69%

**Error Rate by Position:**

| Position | FP | FN | Total Errors | Total Pages | Error Rate |
|----------|----|----|--------------|-------------|------------|
| 1 | 7 | 8 | 15 | 300 | 5.00% |
| 2 | 5 | 4 | 9 | 257 | 3.50% |
| 3 | 3 | 7 | 10 | 230 | 4.35% |
| 4 | 7 | 3 | 10 | 218 | 4.59% |
| 5 | 3 | 3 | 6 | 211 | 2.84% |
| 6 | 1 | 2 | 3 | 203 | 1.48% |
| 7 | 7 | 4 | 11 | 192 | 5.73% |
| 8 | 2 | 3 | 5 | 187 | 2.67% |
| 9 | 3 | 1 | 4 | 183 | 2.19% |

**Chi-square Test (Uniform Distribution):**
- Chi-square statistic: 9.0881
- P-value: 0.3349
- Null hypothesis (uniform): Not rejected (alpha=0.05)

**Key Findings:**
- Highest error rate: Position 7 (5.73%)
- Lowest error rate: Position 6 (1.48%)

---

## Exp4 (w10, stride=9)
**Configuration:** Window size=10, Stride=9

**Overall Statistics:**
- Total pages: 1981
- Total errors: 74
- FP errors: 35
- FN errors: 39
- Overall error rate: 3.74%

**Error Rate by Position:**

| Position | FP | FN | Total Errors | Total Pages | Error Rate |
|----------|----|----|--------------|-------------|------------|
| 1 | 6 | 13 | 19 | 300 | 6.33% |
| 2 | 5 | 4 | 9 | 257 | 3.50% |
| 3 | 2 | 6 | 8 | 230 | 3.48% |
| 4 | 5 | 4 | 9 | 218 | 4.13% |
| 5 | 4 | 4 | 8 | 211 | 3.79% |
| 6 | 2 | 2 | 4 | 203 | 1.97% |
| 7 | 6 | 3 | 9 | 192 | 4.69% |
| 8 | 2 | 2 | 4 | 187 | 2.14% |
| 9 | 3 | 1 | 4 | 183 | 2.19% |

**Chi-square Test (Uniform Distribution):**
- Chi-square statistic: 10.2014
- P-value: 0.2512
- Null hypothesis (uniform): Not rejected (alpha=0.05)

**Key Findings:**
- Highest error rate: Position 1 (6.33%)
- Lowest error rate: Position 6 (1.97%)

---

## Exp5 (w5, stride=4)
**Configuration:** Window size=5, Stride=4

**Overall Statistics:**
- Total pages: 1980
- Total errors: 77
- FP errors: 38
- FN errors: 39
- Overall error rate: 3.89%

**Error Rate by Position:**

| Position | FP | FN | Total Errors | Total Pages | Error Rate |
|----------|----|----|--------------|-------------|------------|
| 1 | 5 | 18 | 23 | 559 | 4.11% |
| 2 | 13 | 6 | 19 | 497 | 3.82% |
| 3 | 13 | 9 | 22 | 480 | 4.58% |
| 4 | 7 | 6 | 13 | 444 | 2.93% |

**Chi-square Test (Uniform Distribution):**
- Chi-square statistic: 1.7283
- P-value: 0.6307
- Null hypothesis (uniform): Not rejected (alpha=0.05)

**Key Findings:**
- Highest error rate: Position 3 (4.58%)
- Lowest error rate: Position 4 (2.93%)

---

## Cross-Experiment Comparison

### Window Edge Analysis
Comparing error rates at window edges:

**Exp3 (w10, stride=9):**
  - Position 1: 5.00%
  - Position 2: 3.50%
  - Position 9: 2.19%

**Exp4 (w10, stride=9):**
  - Position 1: 6.33%
  - Position 2: 3.50%
  - Position 9: 2.19%

**Exp5 (w5, stride=4):**
  - Position 1: 4.11%
  - Position 2: 3.82%
  - Position 4: 2.93%

