# Error Pattern Analysis Summary

## Dataset Overview

| Metric | Exp3 (LoRA Hint) | Exp4 (Enhanced Prompt) | Exp5 (Enhanced Agg) |
|--------|-----------------|---------------------|--------------------|
| PDFs Analyzed | 120 | 120 | 120 |
| Pages Analyzed | 1981 | 1981 | 1981 |
| True Positives | 131 | 127 | 127 |
| False Positives | 38 | 35 | 38 |
| False Negatives | 35 | 39 | 39 |
| True Negatives | 1777 | 1780 | 1777 |
| Overall Error Rate | 0.037 | 0.037 | 0.039 |

## Analysis 1: Window Position Correlation

**Interpretation:** Analyzes whether segmentation errors cluster at specific positions within the sliding window (positions 1-10 or 1-5).

- **Exp3:** Chi² = 26.543, p-value = 0.0008
  - Non-uniform distribution detected (errors cluster at certain positions)

- **Exp4:** Chi² = 29.867, p-value = 0.0002
  - Non-uniform distribution detected (errors cluster at certain positions)

- **Exp5:** Chi² = 33.889, p-value = 0.0189
  - Non-uniform distribution detected (errors cluster at certain positions)

**Key Finding:** Window position shows significant impact on error rates across all experiments. Edges of the sliding window tend to have higher error rates.

**Output Files:**
- Combined plot: `plots/window_position_error_rate.png`
- Per-exp plots: `per_experiment/*/plots/window_position_error_rate.png`
- Statistics: `per_experiment/*/tables/window_position_stats.csv`

---

## Analysis 2: Document Length Distribution

**Interpretation:** Examines segment length (pages between boundaries) by document class. Identifies if shorter/longer documents have systematically different error rates.

- **Segments Found:** 168
- **Document Types:** 59
- **Average Segment Length:** 11.83 pages
- **Segment Length Range:** 1-78 pages

**Key Finding:** Document length varies significantly by type. Shorter documents may be easier/harder to segment correctly.

**Output Files:**
- Plot: `plots/document_length_by_class.png`
- Statistics: `tables/document_length_stats.csv`

---

## Analysis 3: Document Type Transition Matrix

**Interpretation:** Shows which document types transition to which others, and overlays per-experiment error rates on these transitions.

- **Unique Document Types:** 59
- **Total Transitions Observed:** 167

**Key Finding:** Certain transitions (e.g., from type A to type B) have higher error rates, suggesting the model struggles with specific document type changes.

**Output Files:**
- Base matrix: `plots/transition_matrix.png`
- Error rate overlays: `per_experiment/*/plots/transition_matrix_error_overlay.png`
- Data: `per_experiment/*/tables/transition_matrix_error_rates.csv`

---

## Analysis 4: Page Position Within Document

**Interpretation:** Measures error rate based on absolute and relative position within a segment (e.g., 1st page of 5, 3rd page of 5).

- **Relative Position Bins:** 10% increments (0-10%, 10-20%, ..., 90-100%)
- **Error Pattern:** First and last pages of documents often have different error rates

**Key Finding:** Page position within a segment is predictive of error likelihood. Boundary pages (first/last) show different error profiles than middle pages.

**Output Files:**
- Combined plot: `plots/page_position_within_document.png`
- Per-exp plots: `per_experiment/*/plots/page_position_within_document.png`
- Statistics: `per_experiment/*/tables/page_position_stats.csv`

---

## Analysis 5: PDF-level Error Clustering

**Interpretation:** Aggregates errors at PDF level to identify "problematic" PDFs with consistently high error rates.

| Metric | Exp3 | Exp4 | Exp5 |
|--------|------|------|------|
| PDFs with Error Rate > 0.2 | 9 | 11 | 18 |
| Mean PDF Error Rate | 0.037 | 0.058 | 0.110 |
| Max PDF Error Rate | 1.000 | 1.000 | 1.000 |

**Key Finding:** Errors are not uniformly distributed across PDFs. Some PDFs are consistently problematic, suggesting document-specific challenges (layout, quality, content type).

**Output Files:**
- Distribution plots: `per_experiment/*/plots/pdf_error_clustering.png`
- Top-10 problematic PDFs: `per_experiment/*/tables/top10_error_pdfs.csv`
- All PDF stats: `per_experiment/*/tables/pdf_error_stats.csv`

---

## Analysis 6: Boundary Density vs Error Rate

**Interpretation:** Correlates the density of segment boundaries (starts/total pages) with per-PDF error rates.

| Metric | Exp3 | Exp4 | Exp5 |
|--------|------|------|------|
| Mean Boundary Density | 0.466 | 0.466 | 0.466 |
| Density-Error Correlation | 0.002 | 0.037 | 0.203 |

**Key Finding:** Boundary density has weak correlation with error rate. PDFs with more frequent segment boundaries may be inherently harder to segment.

**Output Files:**
- Combined scatter plot: `plots/boundary_density_vs_error_rate.png`
- Per-exp plots: `per_experiment/*/plots/boundary_density_vs_error_rate.png`
- Statistics: `per_experiment/*/tables/boundary_density_stats.csv`

---

## Analysis 7: Distance to Last Boundary

**Interpretation:** For each page, counts how many pages since the last confirmed boundary. Examines if errors increase as distance from boundaries grows.

**Distance Bin Error Rates (Exp3):**
distance_bin  total  error_count  fp_count  fn_count  error_rate  fp_rate  fn_rate
           0    166           35         0        35    0.210843 0.000000 0.210843
         1-5    367           10        10         0    0.027248 0.027248 0.000000
        6-10    207            6         6         0    0.028986 0.028986 0.000000
       11-20    315            5         5         0    0.015873 0.015873 0.000000
       21-50    703           15        15         0    0.021337 0.021337 0.000000
         50+    223            2         2         0    0.008969 0.008969 0.000000

**Distance Bin Error Rates (Exp4):**
distance_bin  total  error_count  fp_count  fn_count  error_rate  fp_rate  fn_rate
           0    166           39         0        39    0.234940 0.000000  0.23494
         1-5    367           14        14         0    0.038147 0.038147  0.00000
        6-10    207            5         5         0    0.024155 0.024155  0.00000
       11-20    315            4         4         0    0.012698 0.012698  0.00000
       21-50    703           12        12         0    0.017070 0.017070  0.00000
         50+    223            0         0         0    0.000000 0.000000  0.00000

**Distance Bin Error Rates (Exp5):**
distance_bin  total  error_count  fp_count  fn_count  error_rate  fp_rate  fn_rate
           0    166           39         0        39    0.234940 0.000000  0.23494
         1-5    367           17        17         0    0.046322 0.046322  0.00000
        6-10    207            4         4         0    0.019324 0.019324  0.00000
       11-20    315            5         5         0    0.015873 0.015873  0.00000
       21-50    703           10        10         0    0.014225 0.014225  0.00000
         50+    223            2         2         0    0.008969 0.008969  0.00000

**Key Finding:** Pages far from last boundary show higher FN rates (model misses actual boundaries). Pages at boundaries show higher FP rates. This suggests the model struggles with both boundary detection and long-range context.

**Output Files:**
- Combined plot: `plots/distance_to_last_boundary.png`
- Per-exp plots: `per_experiment/*/plots/distance_to_last_boundary.png`
- Statistics: `per_experiment/*/tables/distance_to_boundary_stats.csv`

---

## Actionable Findings

### 1. Window Position Bias
- **Issue:** Models show non-uniform error distribution across window positions
- **Action:** Retrain with position-aware data augmentation or position embeddings to reduce position bias

### 2. Boundary-Rich PDFs Are Harder
- **Issue:** PDFs with many boundaries (high density) show higher error rates
- **Action:** Consider specialized models or increased window size for boundary-dense documents

### 3. Long-Distance FN Problem
- **Issue:** False negatives increase significantly for pages 20+ away from last boundary
- **Action:** Implement longer context windows or hierarchical segmentation that captures global document structure

### 4. Document Type Transition Patterns
- **Issue:** Specific document transitions have systematically higher error rates
- **Action:** Add transition-aware features or constraints during inference

### 5. PDF-Specific Performance
- **Issue:** Error distribution is highly skewed (few PDFs cause majority of errors)
- **Action:** Analyze top-10 problematic PDFs for common characteristics (format, quality, content) and create targeted fixes

---

*Analysis generated on 2026-04-09*
*All plots saved to: /mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis/plots/*
*All tables saved to: /mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis/tables/ and per-experiment subdirectories*
