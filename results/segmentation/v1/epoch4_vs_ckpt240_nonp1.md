# epoch4 vs ckpt240 — Non-Trivial Boundary Comparison

> **p1 pages excluded** (first page of every packet is always START by definition — including them inflates metrics).
> This shows how each model actually performs on the hard problem: detecting boundaries *mid-packet*.

---

## Overall (non-p1 pages only)

| Model | F1 | Precision | Recall | TP | FP | TN | FN |
|---|---|---|---|---|---|---|---|
| epoch4 (sliding window) | **0.5590** | 0.5000 | **0.6338** | 45 | 45 | 1770 | 26 |
| ckpt240 (+ hints) | 0.5417 | **0.5652** | 0.5200 | 39 | **30** | 1785 | 36 |

**Key trade-off**: ckpt240 cuts FPs by 33% (45→30) but increases FNs by 38% (26→36). Net result: both models are nearly identical at ~0.54–0.56 F1 on real mid-packet boundaries.

The headline F1 of ~0.78 reported in earlier benchmarks was heavily inflated by trivially correct p1 predictions (~89–90 free TPs per model).

---

## Per-Class Breakdown (non-p1 only)

Only labels with any boundary activity (TP+FP+FN > 0) shown.
`sup` = number of true positive boundaries (GT=True) in the non-p1 test set.

| Label | sup | e4 F1 | e4 TP | e4 FP | e4 TN | e4 FN | c240 F1 | c240 TP | c240 FP | c240 TN | c240 FN | Winner |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gstr_form | 1 | 0.095 | 1 | 19 | 105 | 0 | **0.200** | 1 | 8 | 116 | 0 | c240 ✓ |
| property_ownership_docs | 0 | 0.000 | 0 | 12 | 47 | 0 | 0.000 | 0 | **8** | 51 | 0 | tie (both fail) |
| pnl_statement | 6 | 0.000 | 0 | 0 | 10 | 6 | **0.286** | 1 | 0 | 10 | 5 | c240 ✓ |
| schedules_and_annexures | 9 | 0.444 | 4 | 5 | 172 | 5 | **0.471** | 4 | 4 | 173 | 5 | c240 ✓ |
| municipal_mutation_record | 3 | 0.000 | 0 | 0 | 21 | 3 | 0.000 | 0 | 0 | 21 | 4 | tie (both fail) |
| notes_to_accounts | 5 | 0.333 | 1 | 0 | 70 | 4 | 0.333 | 1 | 0 | 70 | 4 | tie |
| balance_sheet | 5 | **0.750** | 3 | 0 | 1 | 2 | 0.333 | 1 | 0 | 1 | 4 | e4 ✓ |
| itr_firm | 2 | **1.000** | 2 | 0 | 0 | 0 | 0.667 | 1 | 0 | 0 | 1 | e4 ✓ |
| other_financial_doc | 6 | 0.727 | 4 | 1 | 25 | 2 | 0.727 | 4 | 1 | 25 | 2 | tie |
| title_search_report | 2 | **0.667** | 2 | 2 | 25 | 0 | 0.400 | 1 | 2 | 25 | 1 | e4 ✓ |
| tax_audit_3CA_3CD | 1 | **0.667** | 1 | 1 | 20 | 0 | 0.000 | 0 | 1 | 20 | 1 | e4 ✓ |
| rent_agreement | 1 | **0.667** | 1 | 1 | 8 | 0 | 0.000 | 0 | 2 | 7 | 1 | e4 ✓ |
| village_form_7_12 | 1 | 0.000 | 0 | 0 | 18 | 1 | 0.000 | 0 | 0 | 18 | 2 | tie (both fail) |
| form_26AS | 2 | 0.667 | 1 | 0 | 6 | 1 | **1.000** | 2 | 0 | 6 | 0 | c240 ✓ |
| aadhar_back | 1 | 0.000 | 0 | 0 | 0 | 1 | **1.000** | 1 | 0 | 0 | 0 | c240 ✓ |
| cibil_commercial | 1 | 0.667 | 1 | 1 | 10 | 0 | **1.000** | 1 | 0 | 11 | 0 | c240 ✓ |
| tax_audit_3CB_3CD | 2 | **1.000** | 2 | 0 | 40 | 0 | 0.800 | 2 | 1 | 39 | 0 | e4 ✓ |
| gst_certificate | 0 | 0.000 | 0 | 1 | 7 | 0 | 0.000 | 0 | 1 | 7 | 0 | tie |
| other | 2 | 0.667 | 1 | 0 | 6 | 1 | 0.667 | 1 | 0 | 6 | 1 | tie |
| certificate_of_incorporation | 1 | **1.000** | 1 | 0 | 20 | 0 | 0.000 | 0 | 1 | 19 | 1 | e4 ✓ |
| bank_statement_of_account_SOA | 1 | **1.000** | 1 | 0 | 9 | 0 | 0.000 | 0 | 0 | 9 | 1 | e4 ✓ |
| form_16 | 1 | **1.000** | 1 | 0 | 3 | 0 | 0.000 | 0 | 0 | 3 | 1 | e4 ✓ |

---

## Win/Loss Summary

| | Count | Labels |
|---|---|---|
| **epoch4 wins** | 9 | `balance_sheet`, `itr_firm`, `title_search_report`, `tax_audit_3CA_3CD`, `rent_agreement`, `tax_audit_3CB_3CD`, `certificate_of_incorporation`, `bank_statement_of_account_SOA`, `form_16` |
| **ckpt240 wins** | 5 | `gstr_form`, `pnl_statement`, `schedules_and_annexures`, `form_26AS`, `aadhar_back`, `cibil_commercial` |
| **Both fail (0 F1)** | 3 | `property_ownership_docs`, `municipal_mutation_record`, `village_form_7_12` |
| **Tie** | rest | |

---

## Key Observations

### Where hints genuinely help
- **`gstr_form`**: FPs halved (19→8). Single biggest improvement. Hint correctly suppresses false boundaries in multi-page GSTR packets.
- **`pnl_statement`**: epoch4 gets 0/6 (complete failure); ckpt240 gets 1/6. Marginal but real.
- **`schedules_and_annexures`**: FPs reduced 5→4; F1 barely improves. Noisy class for both.

### Where hints hurt
- **`balance_sheet`**: epoch4 3/5 correct; ckpt240 drops to 1/5. Hint biases toward CONTINUE on visually similar financial statement pages.
- **`itr_firm`**, **`form_16`**, **`certificate_of_incorporation`**, **`bank_statement_of_account_SOA`**: epoch4 perfect (1.0), ckpt240 completely fails (0.0). These are new regressions from the hint.

### Complete failures (both models)
- **`property_ownership_docs`**: 12 and 8 FPs respectively, 0 TPs. All errors are FPs — the model consistently hallucinates new boundaries within a single multi-page property doc packet. Strong GT suspect.
- **`municipal_mutation_record`**: 0 TPs for both, all FNs. Model never detects boundaries for this class.
- **`village_form_7_12`**: 0 TPs, both fail. Likely same-class boundary issue (2 packets of this class back-to-back).

### GT quality flags
Classes where both models agree (same FP/FN pattern) but still fail → likely GT errors:
- `property_ownership_docs`: packet `2073d3f1` — 5 pages all models predict START, GT=CONTINUE. Inspect this packet.
- `pnl_statement`: packet `0a6e0208` pages p3, p30, p55 — all models miss these boundaries.

---

*Generated 2026-04-06. Excludes p1 pages (first page of each packet = always START by definition).*
