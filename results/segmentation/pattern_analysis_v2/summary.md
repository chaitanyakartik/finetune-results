# Window Position Error Analysis - Summary Report

## Overview
This analysis examines how model errors (False Positives and False Negatives) are distributed across window positions for three segmentation experiments. The data is analyzed using the `anchor_page_num` field and window position derived from file naming patterns.

**Key Insight:** Window position refers to a page's location within a sliding window during inference (position 1-10 for w10, 1-5 for w5).

---

## Chi-Square Goodness-of-Fit Test Results

The chi-square test evaluates whether errors are uniformly distributed across window positions (H0: uniform distribution, H1: non-uniform distribution).

### Exp3 (w10): qwen35_9b-segmentation-lora-upsampled-epoch5
- **χ² statistic:** 17.7143
- **p-value:** 0.038637
- **Degrees of freedom:** 9 (positions with data)
- **Conclusion:** **Statistically significant** (p < 0.05). Errors are **NOT uniformly distributed** across positions. Distribution is significantly non-uniform.

### Exp4 (w10): segg_sliding_enhanced_upsampled
- **χ² statistic:** 25.1892
- **p-value:** 0.002769
- **Degrees of freedom:** 10
- **Conclusion:** **Highly statistically significant** (p < 0.01). Errors are **NOT uniformly distributed** across positions. Distribution is significantly non-uniform.

### Exp5 (w5): segg_w5_no_headers
- **χ² statistic:** 30.0779
- **p-value:** 0.000005
- **Degrees of freedom:** 5
- **Conclusion:** **Highly statistically significant** (p < 0.001). Errors are **NOT uniformly distributed** across positions. Distribution is significantly non-uniform.

---

## Position with Highest Error Rate per Experiment

| Experiment | Window Size | Highest Error Rate | Position | Error Count |
|------------|-------------|-------------------|----------|-------------|
| Exp3 (w10) | 10          | 0.0714 (7.14%)    | 10 (last) | 12 errors out of 168 pages |
| Exp4 (w10) | 10          | 0.0609 (6.09%)    | 10 (last) | 12 errors out of 197 pages |
| Exp5 (w5)  | 5           | 0.0609 (6.09%)    | 3 (middle) | 30 errors out of 493 pages |

---

## Edge Clustering Hypothesis: Supported

### Findings:

#### Exp3 (w10):
- **Position 1 (anchor):** 0.0106 (1.06%) - Very low error rate
- **Positions 2-9:** Range from 0.016 to 0.061 (1.6%-6.1%)
- **Position 10 (end):** 0.0714 (7.14%) - **Highest error rate**
- **Edge clustering:** YES. Position 10 shows markedly higher error concentration (7.14%), with position 1 also very low.

#### Exp4 (w10):
- **Position 1 (anchor):** 0.0000 (0%) - No errors in 42 pages
- **Positions 2-9:** Range from 0.019 to 0.058 (1.9%-5.8%)
- **Position 10 (end):** 0.0609 (6.09%) - **Highest error rate**
- **Edge clustering:** YES. Position 10 shows elevated error concentration (6.09%), position 1 has zero errors.

#### Exp5 (w5):
- **Position 1 (anchor):** 0.0000 (0%) - No errors in 41 pages
- **Position 2:** 0.0319 (3.19%)
- **Position 3 (middle):** 0.0609 (6.09%) - **Highest error rate** (NOT at edge)
- **Position 4:** 0.0378 (3.78%)
- **Position 5 (end):** 0.0278 (2.78%)
- **Edge clustering:** **PARTIAL/WEAK**. Error peak is at position 3 (middle), not at edges. Position 1 has zero errors, but position 5 (end) has lower error rate than positions 2-4.

---

## Comparison: w10 vs w5 Window Sizes

### W10 Experiments (Exp3 & Exp4):
- Both w10 experiments show **consistent edge clustering** at position 10
- Error distribution: **Pos1 < Pos2-9 < Pos10**
- Pattern is consistent across two independent models
- Position 10 (end of window) consistently has the highest error rate

### W5 Experiment (Exp5):
- **Different pattern:** Error peak at position 3 (middle), not at edges
- Position 1 and 5 (edges) have relatively low error rates
- Suggests that window size affects error distribution pattern
- Possibly more challenging middle positions in smaller windows
- Smaller window may have different optical/contextual challenges

### Interpretation:
The w10 experiments show strong **end-of-window bias** (position 10), suggesting that pages at the end of the 10-page window may be harder to classify (possibly due to context limitations, fewer future context windows, or inherent document boundaries). The w5 experiment, however, shows a **middle-position weakness** (position 3), which may indicate different segmentation challenges in smaller windows or different training dynamics.

---

## Statistical Summary Table

### Exp3 (w10)
```
Position | Total Pages | FP | FN | Total Errors | Error Rate | FP Rate | FN Rate
---------|-------------|----|----|--------------|------------|---------|----------
1        | 94          | 0  | 1  | 1            | 0.0106     | 0.0000  | 0.0106
2        | 228         | 5  | 4  | 9            | 0.0395     | 0.0219  | 0.0175
3        | 207         | 2  | 7  | 9            | 0.0435     | 0.0097  | 0.0338
4        | 199         | 7  | 3  | 10           | 0.0503     | 0.0352  | 0.0151
5        | 195         | 3  | 3  | 6            | 0.0308     | 0.0154  | 0.0154
6        | 187         | 1  | 2  | 3            | 0.0160     | 0.0053  | 0.0107
7        | 180         | 7  | 4  | 11           | 0.0611     | 0.0389  | 0.0222
8        | 173         | 2  | 3  | 5            | 0.0289     | 0.0116  | 0.0173
9        | 170         | 3  | 1  | 4            | 0.0235     | 0.0176  | 0.0059
10       | 168         | 7  | 5  | 12           | 0.0714     | 0.0417  | 0.0298
```

### Exp4 (w10)
```
Position | Total Pages | FP | FN | Total Errors | Error Rate | FP Rate | FN Rate
---------|-------------|----|----|--------------|------------|---------|----------
1        | 42          | 0  | 0  | 0            | 0.0000     | 0.0000  | 0.0000
2        | 234         | 3  | 4  | 7            | 0.0299     | 0.0128  | 0.0171
3        | 230         | 2  | 10 | 12           | 0.0522     | 0.0087  | 0.0435
4        | 226         | 9  | 4  | 13           | 0.0575     | 0.0398  | 0.0177
5        | 223         | 3  | 3  | 6            | 0.0269     | 0.0135  | 0.0135
6        | 216         | 1  | 3  | 4            | 0.0185     | 0.0046  | 0.0139
7        | 208         | 6  | 6  | 12           | 0.0577     | 0.0288  | 0.0288
8        | 204         | 2  | 2  | 4            | 0.0196     | 0.0098  | 0.0098
9        | 201         | 3  | 1  | 4            | 0.0199     | 0.0149  | 0.0050
10       | 197         | 6  | 6  | 12           | 0.0609     | 0.0305  | 0.0305
```

### Exp5 (w5)
```
Position | Total Pages | FP | FN | Total Errors | Error Rate | FP Rate | FN Rate
---------|-------------|----|----|--------------|------------|---------|----------
1        | 41          | 0  | 0  | 0            | 0.0000     | 0.0000  | 0.0000
2        | 502         | 4  | 12 | 16           | 0.0319     | 0.0080  | 0.0239
3        | 493         | 19 | 11 | 30           | 0.0609     | 0.0385  | 0.0223
4        | 477         | 9  | 9  | 18           | 0.0378     | 0.0189  | 0.0189
5        | 467         | 6  | 7  | 13           | 0.0278     | 0.0128  | 0.0150
```

---

## Key Insights and Recommendations

1. **Non-uniform Distribution Confirmed:** All three experiments show statistically significant non-uniform error distributions (p < 0.05). Window position strongly impacts model performance.

2. **W10 End-of-Window Effect:** Both w10 experiments (Exp3 & Exp4) show higher error rates at position 10, suggesting:
   - End-of-window context limitations
   - Possible document boundary effects
   - Pages at end of window may have less "future context" for prediction
   
3. **W5 Middle-Position Weakness:** Exp5 shows error concentration at position 3 (middle), different from w10 pattern. This may indicate:
   - Different segmentation challenges in smaller windows
   - Potentially stronger anchor effects in position 1
   - Position 3 may lack sufficient context from both sides

4. **Position 1 (Anchor) Consistency:** 
   - Exp3: Low error (1.06%)
   - Exp4: Zero errors (0%)
   - Exp5: Zero errors (0%)
   - The anchor page shows strong predictions across all experiments

5. **Optimization Opportunities:**
   - For w10 models: Focus on improving position 10 accuracy (7.14% error rate)
   - For w5 models: Focus on improving position 3 accuracy (6.09% error rate)
   - Consider context augmentation strategies to improve non-anchor positions
   - Analyze whether errors correlate with document-level position (beginning/middle/end of actual document)

---

## Files Generated

### Tables (CSV):
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/tables/exp3_window_position_stats.csv`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/tables/exp4_window_position_stats.csv`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/tables/exp5_window_position_stats.csv`

### Plots (PNG):
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/plots/exp3_window_position_error_rate.png`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/plots/exp4_window_position_error_rate.png`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/plots/exp5_window_position_error_rate.png`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/plots/window_position_error_rate_combined.png`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/plots/all_experiments_error_rates.png`
- `/mnt/data/chaitanya/ocr-finetuning/finetune-results/results/segmentation/pattern_analysis_v2/plots/all_experiments_fp_fn_rates.png`

---

## Conclusion

The analysis conclusively demonstrates that window position has a **statistically significant impact** on model performance across all three experiments. The w10 experiments show a consistent **end-of-window bias**, while the w5 experiment shows **middle-position weakness**. These patterns suggest that improving model robustness across all window positions should be a focus for further optimization, particularly at high-error positions (position 10 for w10, position 3 for w5).
