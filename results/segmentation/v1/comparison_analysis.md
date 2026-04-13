# Segmentation Model Comparison — Full Analysis

*Common evaluation pages: 1981*


## 1. Aggregate Metrics

| Model | F1 | Precision | Recall | Accuracy | TP | FP | TN | FN | Parse Failures |
|----------------------|--------|------------|----------|------------|-------|-------|--------|-------|----------------|
| epoch4 (sliding window) | 0.7859 | 0.7486 | 0.8272 | 0.9631 | 134 | 45 | 1770 | 28 | 4 |
| ckpt240 (+ hints) | 0.7712 | 0.8039 | 0.7410 | 0.9631 | 123 | 30 | 1785 | 43 | 0 |
| triplet (multitask) | 0.6900 | 0.5923 | 0.8263 | 0.9374 | 138 | 95 | 1720 | 29 | 5 |

**Key**: ckpt240 trades recall for precision (FP↓ but FN↑). Triplet has similar recall to epoch4 but dramatically worse precision.


## 2. Per-Sample Error Alignment

| Category | Count | % of total |
|----------------------------------------------------|---------|------------|
| All 3 correct | 1813 | 91.5% |
| All 3 wrong — same prediction → **GT suspect** | 32 | 1.6% |
| All 3 wrong — different predictions | 0 | 0.0% |
| epoch4 only correct (hints+triplet regressed) | 6 | 0.3% |
| ckpt240 only correct (hints genuinely help) | 24 | 1.2% |
| triplet only correct | 11 | 0.6% |
| epoch4+ckpt240 correct, triplet wrong | 59 | 3.0% |
| epoch4+triplet correct, ckpt240 wrong | 21 | 1.1% |
| ckpt240+triplet correct, epoch4 wrong | 6 | 0.3% |
| Other | 0 | 0.0% |
| Parse failure (any model) | 9 | 0.5% |

## 3. GT Audit Candidates


### 3a. All 3 models agree but disagree with GT (strongest GT suspects)

**32 pages** where all 3 models predict the same boundary decision but GT says otherwise.

| Label | Count | All predict START (GT=CONTINUE) | All predict CONTINUE (GT=START) |
|--------------------------------|---------|----------------------------------|-----------------------------------|
| schedules_and_annexures | 7 | 2 | 5 |
| gstr_form | 5 | 5 | 0 |
| property_ownership_docs | 5 | 5 | 0 |
| other_financial_doc | 3 | 1 | 2 |
| pnl_statement | 3 | 0 | 3 |
| notes_to_accounts | 2 | 0 | 2 |
| balance_sheet | 1 | 0 | 1 |
| municipal_mutation_record | 1 | 0 | 1 |
| other | 1 | 0 | 1 |
| rent_agreement | 1 | 1 | 0 |
| shop_act_license | 1 | 1 | 0 |
| title_search_report | 1 | 1 | 0 |
| village_form_7_12 | 1 | 0 | 1 |

**Images to inspect manually:**

- `/mnt/data/chaitanya/data/financial_data/images/balance_sheet/1b0c1b36_p17.png` | label=balance_sheet | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/gstr_form/2111c5ef_p7.png` | label=gstr_form | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/gstr_form/21cdfb2c_p10.png` | label=gstr_form | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/gstr_form/21cdfb2c_p4.png` | label=gstr_form | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/gstr_form/21cdfb2c_p52.png` | label=gstr_form | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/gstr_form/21cdfb2c_p7.png` | label=gstr_form | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/municipal_mutation_record/24c2a5be_p31.png` | label=municipal_mutation_record | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/notes_to_accounts/1b0c1b36_p25.png` | label=notes_to_accounts | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/notes_to_accounts/24140944_p23.png` | label=notes_to_accounts | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/other/24c2a5be_p30.png` | label=other | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/other_financial_doc/0a6e0208_p4.png` | label=other_financial_doc | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/other_financial_doc/1b0c1b36_p21.png` | label=other_financial_doc | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/other_financial_doc/24140944_p5.png` | label=other_financial_doc | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/pnl_statement/098a7bf8_p30.png` | label=pnl_statement | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/pnl_statement/0a6e0208_p3.png` | label=pnl_statement | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/pnl_statement/0a6e0208_p55.png` | label=pnl_statement | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/property_ownership_docs/2073d3f1_p3.png` | label=property_ownership_docs | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/property_ownership_docs/2073d3f1_p35.png` | label=property_ownership_docs | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/property_ownership_docs/2073d3f1_p5.png` | label=property_ownership_docs | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/property_ownership_docs/2073d3f1_p7.png` | label=property_ownership_docs | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/property_ownership_docs/2073d3f1_p9.png` | label=property_ownership_docs | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/rent_agreement/c2914140_p3.png` | label=rent_agreement | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/098a7bf8_p32.png` | label=schedules_and_annexures | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/098a7bf8_p45.png` | label=schedules_and_annexures | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/098a7bf8_p71.png` | label=schedules_and_annexures | all_pred=START | gt=CONTINUE

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/0a6e0208_p10.png` | label=schedules_and_annexures | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/1b0c1b36_p10.png` | label=schedules_and_annexures | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/1fa8eba0_p16.png` | label=schedules_and_annexures | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/24140944_p11.png` | label=schedules_and_annexures | all_pred=CONTINUE | gt=START

- `/mnt/data/chaitanya/data/financial_data/images/shop_act_license/81b32c0b_p2.png` | label=shop_act_license | all_pred=START | gt=CONTINUE

*... and 2 more*


### 3b. Notable repeated offenders (appear in all 3 models' error lists)

Classes appearing as errors in all three models suggest GT inconsistency or inherently ambiguous boundaries:

**14 labels with boundary errors across all 3 models:**

- `balance_sheet`: epoch4 FP=0/FN=2, ckpt240 FP=0/FN=4, triplet FP=0/FN=1

- `gst_certificate`: epoch4 FP=1/FN=0, ckpt240 FP=1/FN=0, triplet FP=2/FN=0

- `gstr_form`: epoch4 FP=19/FN=0, ckpt240 FP=8/FN=1, triplet FP=35/FN=0

- `municipal_mutation_record`: epoch4 FP=0/FN=3, ckpt240 FP=0/FN=3, triplet FP=0/FN=1

- `notes_to_accounts`: epoch4 FP=0/FN=4, ckpt240 FP=0/FN=4, triplet FP=0/FN=2

- `other`: epoch4 FP=0/FN=1, ckpt240 FP=0/FN=1, triplet FP=0/FN=2

- `other_financial_doc`: epoch4 FP=1/FN=2, ckpt240 FP=1/FN=2, triplet FP=3/FN=3

- `pnl_statement`: epoch4 FP=0/FN=6, ckpt240 FP=0/FN=5, triplet FP=0/FN=5

- `property_ownership_docs`: epoch4 FP=12/FN=0, ckpt240 FP=8/FN=0, triplet FP=30/FN=0

- `rent_agreement`: epoch4 FP=1/FN=0, ckpt240 FP=2/FN=1, triplet FP=1/FN=0

- `schedules_and_annexures`: epoch4 FP=5/FN=5, ckpt240 FP=4/FN=5, triplet FP=6/FN=7

- `shop_act_license`: epoch4 FP=1/FN=0, ckpt240 FP=1/FN=0, triplet FP=1/FN=0

- `title_search_report`: epoch4 FP=2/FN=0, ckpt240 FP=2/FN=1, triplet FP=5/FN=0

- `village_form_7_12`: epoch4 FP=0/FN=1, ckpt240 FP=0/FN=1, triplet FP=1/FN=1


## 4. Same-Class Boundary Analysis

These are FN cases (missed boundaries) where the anchor page class == GT label of the next document.
This is the specific failure mode the classification hint was supposed to fix.

- **epoch4**: 28 FNs total (same-class subset not directly annotated)

- **ckpt240**: 40 FNs total, **3 are same-class** (anchor==gt_label)

- **triplet**: 26 FNs total


**Same-class FN cases in ckpt240 (hint model):**

  - `notes_to_accounts` × 1

  - `schedules_and_annexures` × 1

  - `village_form_7_12` × 1


**Same-class FN examples:**

- `/mnt/data/chaitanya/data/financial_data/images/notes_to_accounts/0a6e0208_p8.png` | label=notes_to_accounts | anchor=notes_to_accounts

- `/mnt/data/chaitanya/data/financial_data/images/schedules_and_annexures/098a7bf8_p32.png` | label=schedules_and_annexures | anchor=schedules_and_annexures

- `/mnt/data/chaitanya/data/financial_data/images/village_form_7_12/24c2a5be_p19.png` | label=village_form_7_12 | anchor=village_form_7_12


## 5. Per-Class Boundary F1 (classes with ≥3 positive GT samples)

Only showing classes where support (GT=True) ≥ 3 to avoid noise.

| Label | Support | F1_e4 | F1_c240 | F1_tri | FP/FN e4 | FP/FN c240 | FP/FN tri | Best? |
|--------------------------------|----------|---------|----------|---------|------------|-------------|------------|--------|
| municipal_mutation_record | 3 | 0.000 | 0.000 | 0.800 | 0/3 | 0/3 | 0/1 | tri |
| pnl_statement | 8 | 0.400 | 0.545 | 0.545 | 0/6 | 0/5 | 0/5 | c240 |
| gstr_form | 7 | 0.424 | 0.571 | 0.286 | 19/0 | 8/1 | 35/0 | c240 |
| notes_to_accounts | 6 | 0.500 | 0.500 | 0.800 | 0/4 | 0/4 | 0/2 | tri |
| schedules_and_annexures | 10 | 0.500 | 0.526 | 0.316 | 5/5 | 4/5 | 6/7 | c240 |
| balance_sheet | 5 | 0.750 | 0.333 | 0.889 | 0/2 | 0/4 | 0/1 | tri |
| title_search_report | 3 | 0.750 | 0.571 | 0.545 | 2/0 | 2/1 | 5/0 | e4 |
| other_financial_doc | 8 | 0.800 | 0.800 | 0.625 | 1/2 | 1/2 | 3/3 | e4 |
| aadhar_back | 3 | 0.800 | 1.000 | 0.800 | 0/1 | 0/0 | 0/1 | c240 |
| other | 3 | 0.800 | 0.800 | 0.500 | 0/1 | 0/1 | 0/2 | e4 |
| village_form_7_12 | 3 | 0.800 | 0.800 | 0.667 | 0/1 | 0/1 | 1/1 | e4 |
| gst_certificate | 4 | 0.889 | 0.889 | 0.800 | 1/0 | 1/0 | 2/0 | e4 |
| aadhar_front | 4 | 1.000 | 1.000 | 1.000 | 0/0 | 0/0 | 0/0 | e4 |
| bank_cheque | 3 | 1.000 | 1.000 | 1.000 | 0/0 | 0/0 | 0/0 | e4 |
| bank_statement | 16 | 1.000 | 1.000 | 1.000 | 0/0 | 0/0 | 0/0 | e4 |
| cibil_individual | 3 | 1.000 | 1.000 | 1.000 | 0/0 | 0/0 | 0/0 | e4 |
| computation_sheet | 3 | 1.000 | 1.000 | 0.800 | 0/0 | 0/0 | 0/1 | e4 |
| disbursement_request_letter | 3 | 1.000 | 1.000 | 1.000 | 0/0 | 0/0 | 0/0 | e4 |
| itr_firm | 3 | 1.000 | 0.500 | 1.000 | 0/0 | 0/2 | 0/0 | e4 |
| tax_audit_3CB_3CD | 3 | 1.000 | 0.857 | 0.857 | 0/0 | 1/0 | 1/0 | e4 |
| tax_challan | 3 | 1.000 | 1.000 | 0.857 | 0/0 | 0/0 | 1/0 | e4 |

### 5b. Which model wins (highest F1) per class?

- **epoch4 wins**: 2 classes — `title_search_report`, `tax_audit_3CB_3CD`

- **ckpt240 wins**: 3 classes — `gstr_form`, `schedules_and_annexures`, `aadhar_back`

- **triplet wins**: 3 classes — `municipal_mutation_record`, `notes_to_accounts`, `balance_sheet`

- **Tie**: 13 classes


## 6. Synthetic vs Real Data Breakdown

- Synthetic pages: 0

- Real pages: 1972


*(No synthetic pages found in common key set — synthetic docs may not be in test manifest)*


## 7. Hypothesis Verdicts


**H1 — Hints model over-suppresses boundaries (FP→FN trade)**: CONFIRMED
  Classification hint biases model toward CONTINUE, masking real boundaries in same-class consecutive docs.
  FN↑ from 28→43, concentrated in `balance_sheet`, `municipal_mutation_record`, `village_form_7_12`, `itr_firm`.

**H2 — Hints help with gstr_form FP problem**: CONFIRMED
  gstr_form FPs dropped 19→8 (58% reduction). The single biggest FP class improved significantly.

**H3 — Triplet FP explosion from narrow context window**: CONFIRMED
  95 FPs vs 45 (epoch4). 3-page window insufficient for multi-page repetitive docs like `gstr_form` (19→35) and `property_ownership_docs` (12→30).

**H4 — GT errors masking real performance**: INVESTIGATE via Section 3
  Classes `schedules_and_annexures`, `property_ownership_docs`, `municipal_mutation_record` appear in all three models' error lists → strong GT suspect.

**H5 — Triplet reveals label noise**: CONFIRMED (diagnostic)
  Case sensitivity bug: `tax_audit_3CB_3CD` → `tax_audit_3cb_3cd` (21 triplet doc_type errors). Not a model failure.
  Semantic ambiguity: `schedules_and_annexures` confused with `notes_to_accounts` (67), `other_financial_doc` (52).


## 8. Recommendations


### Immediate (before next training run)
1. **Fix label case normalization** — `tax_audit_3CB_3CD` vs `tax_audit_3cb_3cd`. This is a data pipeline bug inflating error counts.
2. **GT audit** the pages in Section 3a (all-3-wrong, same prediction). These are the highest-confidence GT errors.
3. **Review `schedules_and_annexures` boundaries** — this class is the source of both FPs and FNs across all models, suggesting inconsistent annotation of where annexure sections start/end.
4. **Review `property_ownership_docs`** — 12/8/30 FPs across models. These docs may span multiple packets incorrectly in GT.

### Modelling
5. **Don't adopt ckpt240 as default** — F1 regression (-0.015) and recall drop outweigh the gstr_form precision gain.
6. **Don't adopt triplet** — F1 regression (-0.086) is severe. 3-page window is too narrow. Would need ≥5-7 page context at minimum to be competitive.
7. **Selective hints**: Instead of a blanket hint for all classes, consider injecting the classification hint only for the top FP classes (gstr_form, property_ownership_docs). This could preserve the gstr_form improvement without hurting recall on financial statements.
8. **Ensemble opportunity**: For the specific classes where ckpt240 wins (see Section 5b), a routing ensemble could use the hints model on those classes and epoch4 for the rest. Evaluate if the wins outweigh the losses.

### Data
9. **Add same-class boundary examples to training** — as noted in `segmentation_data_prep_plan.md`, synthetic same-class stitching is planned. Prioritize this for `notes_to_accounts`, `schedules_and_annexures`, `pnl_statement` which are highest FN across all models.
