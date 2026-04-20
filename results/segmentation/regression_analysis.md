# Segmentation Regression Analysis — 5-Experiment Comparison

*1981 pages evaluated across all experiments*


## 1. Aggregate Metrics Overview

| Experiment | Accuracy | F1 | Precision | Recall | TP | FP | FN | TN | Parse Fail |
|---|---|---|---|---|---|---|---|---|---|
| Exp1: Baseline | 0.9248 | 0.5873 | 0.5436 | 0.6386 | 106 | 89 | 60 | 1726 | 0 |
| Exp2: LoRA w10 | 0.9399 | 0.6667 | 0.6284 | 0.7099 | 115 | 68 | 47 | 1747 | 4 |
| Exp3: LoRA+hint | 0.9631 | 0.7821 | 0.7751 | 0.7892 | 131 | 38 | 35 | 1777 | 0 |
| Exp4: Prompt v1 | 0.9626 | 0.7744 | 0.7840 | 0.7651 | 127 | 35 | 39 | 1780 | 0 |
| Exp5: Prompt v1+w5 | 0.9606 | 0.7674 | 0.7697 | 0.7651 | 127 | 38 | 39 | 1776 | 1 |

## 2. Pairwise Regression Analysis


### 2.1 Exp1: Baseline -> Exp2: LoRA w10

**Net: +30** (77 improvements, 47 regressions, 1857 unchanged)


#### REGRESSIONS (47 pages worse)


**correct->FP** (38 pages):

- **gstr_form**: 14 -- hallucinated new document starts on continuation pages
  - `gstr_form/2111c5ef_p10.png`
  - `gstr_form/2111c5ef_p13.png`
  - `gstr_form/2111c5ef_p16.png`
  - *...and 11 more*
- **cibil_commercial**: 6 -- hallucinated new document starts on continuation pages
  - `cibil_commercial/81cde9d4_p2.png`
  - `cibil_commercial/81cde9d4_p3.png`
  - `cibil_commercial/81cde9d4_p4.png`
  - *...and 3 more*
- **gst_accumn_report**: 4 -- hallucinated new document starts on continuation pages
  - `gst_accumn_report/94467b2b_p2.png`
  - `gst_accumn_report/94467b2b_p3.png`
  - `gst_accumn_report/94467b2b_p4.png`
  - *...and 1 more*
- **property_ownership_docs**: 4 -- hallucinated new document starts on continuation pages
  - `property_ownership_docs/2073d3f1_p3.png`
  - `property_ownership_docs/2073d3f1_p5.png`
  - `property_ownership_docs/2073d3f1_p7.png`
  - *...and 1 more*
- **gst_certificate**: 3 -- hallucinated new document starts on continuation pages
  - `gst_certificate/54d5e066_p2.png`
  - `gst_certificate/54d5e066_p3.png`
  - `gst_certificate/9d59e01a_p4.png`
- **title_search_report**: 2 -- hallucinated new document starts on continuation pages
  - `title_search_report/281fe059_p2.png`
  - `title_search_report/46458baa_p2.png`
- **form_16**: 1 -- hallucinated new document starts on continuation pages
  - `form_16/aa90c7cf_p2.png`
- **income_sheet**: 1 -- hallucinated new document starts on continuation pages
  - `income_sheet/f9a663d9_p2.png`
- **notes_to_accounts**: 1 -- hallucinated new document starts on continuation pages
  - `notes_to_accounts/098a7bf8_p73.png`
- **tax_challan**: 1 -- hallucinated new document starts on continuation pages
  - `tax_challan/318a930f_p2.png`
- **village_form_7_12**: 1 -- hallucinated new document starts on continuation pages
  - `village_form_7_12/6532ec6d_p2.png`

**correct->FN** (9 pages):

- **aadhar_card**: 2 -- missed actual document boundaries
  - `aadhar_card/975f2f4f_p1.png`
  - `aadhar_card/dcbd172c_p1.png`
- **bank_cheque**: 1 -- missed actual document boundaries
  - `bank_cheque/e07ec6df_p1.png`
- **combined_pnl_bs**: 1 -- missed actual document boundaries
  - `combined_pnl_bs/8fd75ba1_p1.png`
- **form_16**: 1 -- missed actual document boundaries
  - `form_16/c77162f9_p1.png`
- **form_26AS**: 1 -- missed actual document boundaries
  - `form_26AS/f9bb7ab3_p1.png`
- **pan_card**: 1 -- missed actual document boundaries
  - `pan_card/2bcc3f6c_p1.png`
- **rent_agreement**: 1 -- missed actual document boundaries
  - `rent_agreement/c2914140_p1.png`
- **schedules_and_annexures**: 1 -- missed actual document boundaries
  - `schedules_and_annexures/098a7bf8_p28.png`

#### IMPROVEMENTS (77 pages fixed)


**FP->correct** (59 pages):

- **municipal_mutation_record**: 10 -- stopped hallucinating starts (false positives removed)
  - `municipal_mutation_record/24c2a5be_p26.png`
  - `municipal_mutation_record/24c2a5be_p38.png`
  - `municipal_mutation_record/24c2a5be_p39.png`
  - *...and 7 more*
- **gstr_form**: 7 -- stopped hallucinating starts (false positives removed)
  - `gstr_form/098a7bf8_p10.png`
  - `gstr_form/2111c5ef_p22.png`
  - `gstr_form/2111c5ef_p27.png`
  - *...and 4 more*
- **title_search_report**: 7 -- stopped hallucinating starts (false positives removed)
  - `title_search_report/281fe059_p10.png`
  - `title_search_report/281fe059_p11.png`
  - `title_search_report/281fe059_p12.png`
  - *...and 4 more*
- **cibil_individual**: 5 -- stopped hallucinating starts (false positives removed)
  - `cibil_individual/c98fea39_p2.png`
  - `cibil_individual/c98fea39_p3.png`
  - `cibil_individual/c98fea39_p4.png`
  - *...and 2 more*
- **village_form_7_12**: 5 -- stopped hallucinating starts (false positives removed)
  - `village_form_7_12/24c2a5be_p13.png`
  - `village_form_7_12/24c2a5be_p14.png`
  - `village_form_7_12/24c2a5be_p15.png`
  - *...and 2 more*
- **loan_sanction_letter**: 4 -- stopped hallucinating starts (false positives removed)
  - `loan_sanction_letter/82eb960b_p2.png`
  - `loan_sanction_letter/82eb960b_p3.png`
  - `loan_sanction_letter/82eb960b_p4.png`
  - *...and 1 more*
- **property_ownership_docs**: 4 -- stopped hallucinating starts (false positives removed)
  - `property_ownership_docs/2073d3f1_p47.png`
  - `property_ownership_docs/2073d3f1_p54.png`
  - `property_ownership_docs/2073d3f1_p56.png`
  - *...and 1 more*
- **bank_statement_of_account_SOA**: 3 -- stopped hallucinating starts (false positives removed)
  - `bank_statement_of_account_SOA/bed2fed3_p3.png`
  - `bank_statement_of_account_SOA/bed2fed3_p4.png`
  - `bank_statement_of_account_SOA/bed2fed3_p5.png`
- **rent_agreement**: 3 -- stopped hallucinating starts (false positives removed)
  - `rent_agreement/924a2cf0_p2.png`
  - `rent_agreement/924a2cf0_p3.png`
  - `rent_agreement/c2914140_p2.png`
- **schedules_and_annexures**: 3 -- stopped hallucinating starts (false positives removed)
  - `schedules_and_annexures/098a7bf8_p52.png`
  - `schedules_and_annexures/0a79758a_p37.png`
  - `schedules_and_annexures/d9bd812e_p3.png`
- **form_16**: 2 -- stopped hallucinating starts (false positives removed)
  - `form_16/c77162f9_p2.png`
  - `form_16/c77162f9_p3.png`
- **property_revenue_docs**: 2 -- stopped hallucinating starts (false positives removed)
  - `property_revenue_docs/24c2a5be_p22.png`
  - `property_revenue_docs/24c2a5be_p28.png`
- **combined_pnl_bs**: 1 -- stopped hallucinating starts (false positives removed)
  - `combined_pnl_bs/8fd75ba1_p2.png`
- **computation_sheet**: 1 -- stopped hallucinating starts (false positives removed)
  - `computation_sheet/c904d624_p2.png`
- **property_technical_report**: 1 -- stopped hallucinating starts (false positives removed)
  - `property_technical_report/60fa6d30_p10.png`
- **web_search_report**: 1 -- stopped hallucinating starts (false positives removed)
  - `web_search_report/8e337cda_p2.png`

**FN->correct** (18 pages):

- **balance_sheet**: 2 -- now detects previously missed boundaries
  - `balance_sheet/098a7bf8_p29.png`
  - `balance_sheet/1fa8eba0_p12.png`
- **disbursement_request_letter**: 2 -- now detects previously missed boundaries
  - `disbursement_request_letter/6abcb450_p1.png`
  - `disbursement_request_letter/cbf02ff7_p1.png`
- **NACH_form**: 1 -- now detects previously missed boundaries
  - `NACH_form/c1927f9f_p1.png`
- **gst_certificate**: 1 -- now detects previously missed boundaries
  - `gst_certificate/54d5e066_p1.png`
- **gstr_form**: 1 -- now detects previously missed boundaries
  - `gstr_form/8a19b172_p1.png`
- **income_sheet**: 1 -- now detects previously missed boundaries
  - `income_sheet/f9a663d9_p1.png`
- **itr_individual**: 1 -- now detects previously missed boundaries
  - `itr_individual/098a7bf8_p11.png`
- **notes_to_accounts**: 1 -- now detects previously missed boundaries
  - `notes_to_accounts/098a7bf8_p72.png`
- **other_financial_doc**: 1 -- now detects previously missed boundaries
  - `other_financial_doc/24140944_p17.png`
- **professional_license**: 1 -- now detects previously missed boundaries
  - `professional_license/c226e76f_p1.png`
- **property_technical_report**: 1 -- now detects previously missed boundaries
  - `property_technical_report/60fa6d30_p1.png`
- **shop_act_license**: 1 -- now detects previously missed boundaries
  - `shop_act_license/6380151d_p1.png`
- **tax_audit_3CB_3CD**: 1 -- now detects previously missed boundaries
  - `tax_audit_3CB_3CD/098a7bf8_p13.png`
- **udyam_certificate**: 1 -- now detects previously missed boundaries
  - `udyam_certificate/bdf1baa7_p1.png`
- **village_form_7_12**: 1 -- now detects previously missed boundaries
  - `village_form_7_12/6532ec6d_p1.png`
- **voter_id_front**: 1 -- now detects previously missed boundaries
  - `voter_id_front/ac4e2c76_p1.png`

### 2.2 Exp2: LoRA w10 -> Exp3: LoRA+hint

**Net: +46** (70 improvements, 24 regressions, 1887 unchanged)


#### REGRESSIONS (24 pages worse)


**correct->FP** (24 pages):

- **gstr_form**: 10 -- hallucinated new document starts on continuation pages
  - `gstr_form/098a7bf8_p10.png`
  - `gstr_form/2111c5ef_p6.png`
  - `gstr_form/21cdfb2c_p19.png`
  - *...and 7 more*
- **property_ownership_docs**: 8 -- hallucinated new document starts on continuation pages
  - `property_ownership_docs/2073d3f1_p11.png`
  - `property_ownership_docs/2073d3f1_p13.png`
  - `property_ownership_docs/2073d3f1_p35.png`
  - *...and 5 more*
- **schedules_and_annexures**: 3 -- hallucinated new document starts on continuation pages
  - `schedules_and_annexures/098a7bf8_p71.png`
  - `schedules_and_annexures/0a79758a_p37.png`
  - `schedules_and_annexures/0a79758a_p67.png`
- **combined_pnl_bs**: 1 -- hallucinated new document starts on continuation pages
  - `combined_pnl_bs/8fd75ba1_p2.png`
- **other_financial_doc**: 1 -- hallucinated new document starts on continuation pages
  - `other_financial_doc/24140944_p5.png`
- **rent_agreement**: 1 -- hallucinated new document starts on continuation pages
  - `rent_agreement/c2914140_p3.png`

#### IMPROVEMENTS (70 pages fixed)


**FP->correct** (54 pages):

- **gstr_form**: 10 -- stopped hallucinating starts (false positives removed)
  - `gstr_form/2111c5ef_p10.png`
  - `gstr_form/2111c5ef_p13.png`
  - `gstr_form/2111c5ef_p16.png`
  - *...and 7 more*
- **cibil_commercial**: 8 -- stopped hallucinating starts (false positives removed)
  - `cibil_commercial/1a877007_p2.png`
  - `cibil_commercial/1a877007_p3.png`
  - `cibil_commercial/81cde9d4_p2.png`
  - *...and 5 more*
- **tax_audit_3CB_3CD**: 6 -- stopped hallucinating starts (false positives removed)
  - `tax_audit_3CB_3CD/5145f0c5_p2.png`
  - `tax_audit_3CB_3CD/5145f0c5_p3.png`
  - `tax_audit_3CB_3CD/5145f0c5_p4.png`
  - *...and 3 more*
- **application_form**: 4 -- stopped hallucinating starts (false positives removed)
  - `application_form/a6ba2c62_p2.png`
  - `application_form/a6ba2c62_p3.png`
  - `application_form/a6ba2c62_p4.png`
  - *...and 1 more*
- **gst_accumn_report**: 4 -- stopped hallucinating starts (false positives removed)
  - `gst_accumn_report/94467b2b_p2.png`
  - `gst_accumn_report/94467b2b_p3.png`
  - `gst_accumn_report/94467b2b_p4.png`
  - *...and 1 more*
- **gst_certificate**: 4 -- stopped hallucinating starts (false positives removed)
  - `gst_certificate/54d5e066_p2.png`
  - `gst_certificate/54d5e066_p3.png`
  - `gst_certificate/9d59e01a_p4.png`
  - *...and 1 more*
- **rent_agreement**: 3 -- stopped hallucinating starts (false positives removed)
  - `rent_agreement/2eafc895_p2.png`
  - `rent_agreement/2eafc895_p3.png`
  - `rent_agreement/2eafc895_p4.png`
- **passport_front**: 2 -- stopped hallucinating starts (false positives removed)
  - `passport_front/1769e413_p2.png`
  - `passport_front/433fb825_p2.png`
- **title_search_report**: 2 -- stopped hallucinating starts (false positives removed)
  - `title_search_report/281fe059_p2.png`
  - `title_search_report/46458baa_p2.png`
- **certificate_of_incorporation**: 1 -- stopped hallucinating starts (false positives removed)
  - `certificate_of_incorporation/48d93ca6_p2.png`
- **cibil_individual**: 1 -- stopped hallucinating starts (false positives removed)
  - `cibil_individual/42212c9f_p2.png`
- **email**: 1 -- stopped hallucinating starts (false positives removed)
  - `email/93fb415e_p2.png`
- **emi_repayment_schedule**: 1 -- stopped hallucinating starts (false positives removed)
  - `emi_repayment_schedule/ad0ee082_p2.png`
- **form_16**: 1 -- stopped hallucinating starts (false positives removed)
  - `form_16/aa90c7cf_p2.png`
- **non_agriculture_order**: 1 -- stopped hallucinating starts (false positives removed)
  - `non_agriculture_order/390a03d7_p2.png`
- **notes_to_accounts**: 1 -- stopped hallucinating starts (false positives removed)
  - `notes_to_accounts/098a7bf8_p73.png`
- **property_ownership_docs**: 1 -- stopped hallucinating starts (false positives removed)
  - `property_ownership_docs/2073d3f1_p49.png`
- **schedules_and_annexures**: 1 -- stopped hallucinating starts (false positives removed)
  - `schedules_and_annexures/098a7bf8_p46.png`
- **tax_challan**: 1 -- stopped hallucinating starts (false positives removed)
  - `tax_challan/318a930f_p2.png`
- **village_form_7_12**: 1 -- stopped hallucinating starts (false positives removed)
  - `village_form_7_12/6532ec6d_p2.png`

**FN->correct** (16 pages):

- **aadhar_card**: 2 -- now detects previously missed boundaries
  - `aadhar_card/975f2f4f_p1.png`
  - `aadhar_card/dcbd172c_p1.png`
- **other_financial_doc**: 2 -- now detects previously missed boundaries
  - `other_financial_doc/098a7bf8_p12.png`
  - `other_financial_doc/24140944_p4.png`
- **schedules_and_annexures**: 2 -- now detects previously missed boundaries
  - `schedules_and_annexures/098a7bf8_p28.png`
  - `schedules_and_annexures/0a79758a_p8.png`
- **aadhar_front**: 1 -- now detects previously missed boundaries
  - `aadhar_front/f806d42d_p1.png`
- **bank_cheque**: 1 -- now detects previously missed boundaries
  - `bank_cheque/e07ec6df_p1.png`
- **combined_pnl_bs**: 1 -- now detects previously missed boundaries
  - `combined_pnl_bs/8fd75ba1_p1.png`
- **field_investigation_report**: 1 -- now detects previously missed boundaries
  - `field_investigation_report/4692549c_p1.png`
- **gstr_form**: 1 -- now detects previously missed boundaries
  - `gstr_form/1ba357cb_p1.png`
- **itr_firm**: 1 -- now detects previously missed boundaries
  - `itr_firm/24140944_p2.png`
- **pan_card**: 1 -- now detects previously missed boundaries
  - `pan_card/2bcc3f6c_p1.png`
- **rent_agreement**: 1 -- now detects previously missed boundaries
  - `rent_agreement/c2914140_p1.png`
- **udyam_certificate**: 1 -- now detects previously missed boundaries
  - `udyam_certificate/c92dc212_p1.png`
- **web_search_report**: 1 -- now detects previously missed boundaries
  - `web_search_report/499351f8_p1.png`

### 2.3 Exp3: LoRA+hint -> Exp4: Prompt v1

**Net: -1** (17 improvements, 18 regressions, 1946 unchanged)


#### REGRESSIONS (18 pages worse)


**correct->FP** (10 pages):

- **schedules_and_annexures**: 2 -- hallucinated new document starts on continuation pages
  - `schedules_and_annexures/098a7bf8_p57.png`
  - `schedules_and_annexures/d9bd812e_p2.png`
- **certificate_of_incorporation**: 1 -- hallucinated new document starts on continuation pages
  - `certificate_of_incorporation/c070a7c3_p2.png`
- **gstr_form**: 1 -- hallucinated new document starts on continuation pages
  - `gstr_form/21cdfb2c_p43.png`
- **non_agriculture_order**: 1 -- hallucinated new document starts on continuation pages
  - `non_agriculture_order/37a7a3ab_p6.png`
- **rent_agreement**: 1 -- hallucinated new document starts on continuation pages
  - `rent_agreement/924a2cf0_p2.png`
- **tax_audit_3CA_3CD**: 1 -- hallucinated new document starts on continuation pages
  - `tax_audit_3CA_3CD/24140944_p41.png`
- **tax_audit_3CB_3CD**: 1 -- hallucinated new document starts on continuation pages
  - `tax_audit_3CB_3CD/d7814402_p14.png`
- **tax_challan**: 1 -- hallucinated new document starts on continuation pages
  - `tax_challan/318a930f_p2.png`
- **title_search_report**: 1 -- hallucinated new document starts on continuation pages
  - `title_search_report/49ad5a7a_p5.png`

**correct->FN** (8 pages):

- **balance_sheet**: 1 -- missed actual document boundaries
  - `balance_sheet/1fa8eba0_p12.png`
- **certificate_of_incorporation**: 1 -- missed actual document boundaries
  - `certificate_of_incorporation/c070a7c3_p1.png`
- **combined_pnl_bs**: 1 -- missed actual document boundaries
  - `combined_pnl_bs/8fd75ba1_p1.png`
- **itr_firm**: 1 -- missed actual document boundaries
  - `itr_firm/a74a84ed_p1.png`
- **rent_agreement**: 1 -- missed actual document boundaries
  - `rent_agreement/924a2cf0_p1.png`
- **schedules_and_annexures**: 1 -- missed actual document boundaries
  - `schedules_and_annexures/d9bd812e_p1.png`
- **tax_audit_3CA_3CD**: 1 -- missed actual document boundaries
  - `tax_audit_3CA_3CD/24140944_p40.png`
- **web_search_report**: 1 -- missed actual document boundaries
  - `web_search_report/499351f8_p1.png`

#### IMPROVEMENTS (17 pages fixed)


**FP->correct** (13 pages):

- **property_ownership_docs**: 7 -- stopped hallucinating starts (false positives removed)
  - `property_ownership_docs/2073d3f1_p11.png`
  - `property_ownership_docs/2073d3f1_p13.png`
  - `property_ownership_docs/2073d3f1_p36.png`
  - *...and 4 more*
- **combined_pnl_bs**: 1 -- stopped hallucinating starts (false positives removed)
  - `combined_pnl_bs/8fd75ba1_p2.png`
- **gstr_form**: 1 -- stopped hallucinating starts (false positives removed)
  - `gstr_form/2111c5ef_p7.png`
- **income_sheet**: 1 -- stopped hallucinating starts (false positives removed)
  - `income_sheet/f9a663d9_p2.png`
- **rent_agreement**: 1 -- stopped hallucinating starts (false positives removed)
  - `rent_agreement/c2914140_p3.png`
- **schedules_and_annexures**: 1 -- stopped hallucinating starts (false positives removed)
  - `schedules_and_annexures/0a79758a_p67.png`
- **tax_audit_3CA_3CD**: 1 -- stopped hallucinating starts (false positives removed)
  - `tax_audit_3CA_3CD/24140944_p61.png`

**FN->correct** (4 pages):

- **pnl_statement**: 2 -- now detects previously missed boundaries
  - `pnl_statement/1fa8eba0_p13.png`
  - `pnl_statement/24140944_p21.png`
- **balance_sheet**: 1 -- now detects previously missed boundaries
  - `balance_sheet/1b0c1b36_p17.png`
- **form_26AS**: 1 -- now detects previously missed boundaries
  - `form_26AS/f9bb7ab3_p1.png`

### 2.4 Exp4: Prompt v1 -> Exp5: Prompt v1+w5

**Net: -4** (39 improvements, 43 regressions, 1899 unchanged)


#### REGRESSIONS (43 pages worse)


**correct->FP** (26 pages):

- **gstr_form**: 8 -- hallucinated new document starts on continuation pages
  - `gstr_form/2111c5ef_p19.png`
  - `gstr_form/2111c5ef_p28.png`
  - `gstr_form/2111c5ef_p31.png`
  - *...and 5 more*
- **title_search_report**: 3 -- hallucinated new document starts on continuation pages
  - `title_search_report/281fe059_p15.png`
  - `title_search_report/281fe059_p2.png`
  - `title_search_report/46458baa_p2.png`
- **property_ownership_docs**: 2 -- hallucinated new document starts on continuation pages
  - `property_ownership_docs/2073d3f1_p37.png`
  - `property_ownership_docs/2073d3f1_p50.png`
- **application_form**: 1 -- hallucinated new document starts on continuation pages
  - `application_form/a6ba2c62_p9.png`
- **combined_pnl_bs**: 1 -- hallucinated new document starts on continuation pages
  - `combined_pnl_bs/8fd75ba1_p2.png`
- **email_conversation**: 1 -- hallucinated new document starts on continuation pages
  - `email_conversation/28315416_p2.png`
- **form_26AS**: 1 -- hallucinated new document starts on continuation pages
  - `form_26AS/f9bb7ab3_p2.png`
- **gst_accumn_report**: 1 -- hallucinated new document starts on continuation pages
  - `gst_accumn_report/94467b2b_p2.png`
- **gst_certificate**: 1 -- hallucinated new document starts on continuation pages
  - `gst_certificate/9d59e01a_p4.png`
- **loan_sanction_letter**: 1 -- hallucinated new document starts on continuation pages
  - `loan_sanction_letter/82eb960b_p2.png`
- **notes_to_accounts**: 1 -- hallucinated new document starts on continuation pages
  - `notes_to_accounts/24140944_p28.png`
- **other_financial_doc**: 1 -- hallucinated new document starts on continuation pages
  - `other_financial_doc/1b0c1b36_p8.png`
- **passport_front**: 1 -- hallucinated new document starts on continuation pages
  - `passport_front/433fb825_p2.png`
- **schedules_and_annexures**: 1 -- hallucinated new document starts on continuation pages
  - `schedules_and_annexures/098a7bf8_p47.png`
- **tax_audit_3CB_3CD**: 1 -- hallucinated new document starts on continuation pages
  - `tax_audit_3CB_3CD/098a7bf8_p15.png`
- **web_search_report**: 1 -- hallucinated new document starts on continuation pages
  - `web_search_report/499351f8_p2.png`

**correct->FN** (16 pages):

- **gstr_form**: 2 -- missed actual document boundaries
  - `gstr_form/1ba357cb_p1.png`
  - `gstr_form/ef099877_p1.png`
- **other_financial_doc**: 2 -- missed actual document boundaries
  - `other_financial_doc/098a7bf8_p12.png`
  - `other_financial_doc/24140944_p4.png`
- **schedules_and_annexures**: 2 -- missed actual document boundaries
  - `schedules_and_annexures/0a79758a_p8.png`
  - `schedules_and_annexures/96522712_p1.png`
- **NACH_form**: 1 -- missed actual document boundaries
  - `NACH_form/c1927f9f_p1.png`
- **aadhar_back**: 1 -- missed actual document boundaries
  - `aadhar_back/baa671cd_p1.png`
- **bank_cheque**: 1 -- missed actual document boundaries
  - `bank_cheque/e07ec6df_p1.png`
- **bank_statement**: 1 -- missed actual document boundaries
  - `bank_statement/b91b0c92_p1.png`
- **cibil_individual**: 1 -- missed actual document boundaries
  - `cibil_individual/42212c9f_p1.png`
- **field_investigation_report**: 1 -- missed actual document boundaries
  - `field_investigation_report/4692549c_p1.png`
- **notes_to_accounts**: 1 -- missed actual document boundaries
  - `notes_to_accounts/098a7bf8_p72.png`
- **passport_front**: 1 -- missed actual document boundaries
  - `passport_front/433fb825_p1.png`
- **pnl_statement**: 1 -- missed actual document boundaries
  - `pnl_statement/24140944_p21.png`
- **title_search_report**: 1 -- missed actual document boundaries
  - `title_search_report/49ad5a7a_p1.png`

**correct->parse_fail** (1 pages):

- **certificate_of_incorporation**: 1 -- output became unparseable
  - `certificate_of_incorporation/48d93ca6_p2.png`

#### IMPROVEMENTS (39 pages fixed)


**FP->correct** (23 pages):

- **gstr_form**: 11 -- stopped hallucinating starts (false positives removed)
  - `gstr_form/098a7bf8_p10.png`
  - `gstr_form/2111c5ef_p6.png`
  - `gstr_form/21cdfb2c_p10.png`
  - *...and 8 more*
- **property_ownership_docs**: 4 -- stopped hallucinating starts (false positives removed)
  - `property_ownership_docs/2073d3f1_p35.png`
  - `property_ownership_docs/2073d3f1_p5.png`
  - `property_ownership_docs/2073d3f1_p7.png`
  - *...and 1 more*
- **schedules_and_annexures**: 2 -- stopped hallucinating starts (false positives removed)
  - `schedules_and_annexures/098a7bf8_p71.png`
  - `schedules_and_annexures/d9bd812e_p2.png`
- **certificate_of_incorporation**: 1 -- stopped hallucinating starts (false positives removed)
  - `certificate_of_incorporation/c070a7c3_p2.png`
- **non_agriculture_order**: 1 -- stopped hallucinating starts (false positives removed)
  - `non_agriculture_order/37a7a3ab_p6.png`
- **other_financial_doc**: 1 -- stopped hallucinating starts (false positives removed)
  - `other_financial_doc/24140944_p5.png`
- **tax_audit_3CA_3CD**: 1 -- stopped hallucinating starts (false positives removed)
  - `tax_audit_3CA_3CD/24140944_p41.png`
- **tax_audit_3CB_3CD**: 1 -- stopped hallucinating starts (false positives removed)
  - `tax_audit_3CB_3CD/d7814402_p14.png`
- **title_search_report**: 1 -- stopped hallucinating starts (false positives removed)
  - `title_search_report/49ad5a7a_p5.png`

**FN->correct** (16 pages):

- **balance_sheet**: 2 -- now detects previously missed boundaries
  - `balance_sheet/1fa8eba0_p12.png`
  - `balance_sheet/24140944_p20.png`
- **notes_to_accounts**: 2 -- now detects previously missed boundaries
  - `notes_to_accounts/0a6e0208_p8.png`
  - `notes_to_accounts/1b0c1b36_p25.png`
- **schedules_and_annexures**: 2 -- now detects previously missed boundaries
  - `schedules_and_annexures/24140944_p11.png`
  - `schedules_and_annexures/d9bd812e_p1.png`
- **aadhar_front**: 1 -- now detects previously missed boundaries
  - `aadhar_front/24c2a5be_p51.png`
- **certificate_of_incorporation**: 1 -- now detects previously missed boundaries
  - `certificate_of_incorporation/c070a7c3_p1.png`
- **combined_pnl_bs**: 1 -- now detects previously missed boundaries
  - `combined_pnl_bs/8fd75ba1_p1.png`
- **form_16**: 1 -- now detects previously missed boundaries
  - `form_16/c77162f9_p1.png`
- **itr_firm**: 1 -- now detects previously missed boundaries
  - `itr_firm/a74a84ed_p1.png`
- **other**: 1 -- now detects previously missed boundaries
  - `other/24c2a5be_p52.png`
- **other_financial_doc**: 1 -- now detects previously missed boundaries
  - `other_financial_doc/1b0c1b36_p21.png`
- **pnl_statement**: 1 -- now detects previously missed boundaries
  - `pnl_statement/1b0c1b36_p19.png`
- **tax_audit_3CA_3CD**: 1 -- now detects previously missed boundaries
  - `tax_audit_3CA_3CD/24140944_p40.png`
- **web_search_report**: 1 -- now detects previously missed boundaries
  - `web_search_report/499351f8_p1.png`

## 3. Cross-Model Alignment (All 5 Experiments)


### 3.1 Universal Successes

**1730 pages** all 5 experiments get correct.


### 3.2 Universal Failures (GT Suspects)

**26 pages** all 5 experiments get wrong.


**Strong GT suspects** (26 pages — all 5 models agree on prediction, disagree with GT):

| Label | Count | GT | All predict | Example pages |
|---|---|---|---|---|
| schedules_and_annexures | 5 | START | CONTINUE | `schedules_and_annexures/098a7bf8_p32.png`, `schedules_and_annexures/098a7bf8_p45.png`, `schedules_and_annexures/0a6e0208_p10.png` |
| municipal_mutation_record | 4 | START | CONTINUE | `municipal_mutation_record/24c2a5be_p17.png`, `municipal_mutation_record/24c2a5be_p25.png`, `municipal_mutation_record/24c2a5be_p29.png` |
| pnl_statement | 3 | START | CONTINUE | `pnl_statement/098a7bf8_p30.png`, `pnl_statement/0a6e0208_p3.png`, `pnl_statement/0a6e0208_p55.png` |
| gstr_form | 2 | CONTINUE | START | `gstr_form/21cdfb2c_p4.png`, `gstr_form/21cdfb2c_p7.png` |
| notes_to_accounts | 2 | START | CONTINUE | `notes_to_accounts/0a79758a_p78.png`, `notes_to_accounts/24140944_p23.png` |
| property_revenue_docs | 2 | START | CONTINUE | `property_revenue_docs/24c2a5be_p21.png`, `property_revenue_docs/24c2a5be_p27.png` |
| village_form_7_12 | 2 | START | CONTINUE | `village_form_7_12/24c2a5be_p19.png`, `village_form_7_12/24c2a5be_p23.png` |
| balance_sheet | 1 | START | CONTINUE | `balance_sheet/0a6e0208_p2.png` |
| computation_sheet | 1 | START | CONTINUE | `computation_sheet/24140944_p3.png` |
| other | 1 | START | CONTINUE | `other/24c2a5be_p30.png` |
| other_financial_doc | 1 | START | CONTINUE | `other_financial_doc/0a6e0208_p4.png` |
| photograph | 1 | START | CONTINUE | `photograph/871d16e9_p1.png` |
| shop_act_license | 1 | CONTINUE | START | `shop_act_license/81b32c0b_p2.png` |

### 3.3 Most Volatile Pages (flip >= 2 times)

**93 pages** flip between correct/incorrect 2+ times across experiments.

| Page | Label | GT | Pattern (1-2-3-4-5) | Flips |
|---|---|---|---|---|
| `combined_pnl_bs/8fd75ba1_p1.png` | combined_pnl_bs | START | YNYNY | 4 |
| `combined_pnl_bs/8fd75ba1_p2.png` | combined_pnl_bs | CONT | NYNYN | 4 |
| `balance_sheet/1fa8eba0_p12.png` | balance_sheet | START | NYYNY | 3 |
| `bank_cheque/e07ec6df_p1.png` | bank_cheque | START | YNYYN | 3 |
| `gst_accumn_report/94467b2b_p2.png` | gst_accumn_report | CONT | YNYYN | 3 |
| `gst_certificate/9d59e01a_p4.png` | gst_certificate | CONT | YNYYN | 3 |
| `gstr_form/098a7bf8_p10.png` | gstr_form | CONT | NYNNY | 3 |
| `gstr_form/2111c5ef_p6.png` | gstr_form | CONT | NYNNY | 3 |
| `gstr_form/2111c5ef_p7.png` | gstr_form | CONT | YNNYN | 3 |
| `property_ownership_docs/2073d3f1_p37.png` | property_ownership_docs | CONT | YYNYN | 3 |
| `property_ownership_docs/2073d3f1_p56.png` | property_ownership_docs | CONT | NYNYY | 3 |
| `tax_challan/318a930f_p2.png` | tax_challan | CONT | YNYNN | 3 |
| `title_search_report/281fe059_p2.png` | title_search_report | CONT | YNYYN | 3 |
| `title_search_report/46458baa_p2.png` | title_search_report | CONT | YNYYN | 3 |
| `web_search_report/499351f8_p1.png` | web_search_report | START | NNYNY | 3 |
| `NACH_form/c1927f9f_p1.png` | NACH_form | START | NYYYN | 2 |
| `aadhar_card/975f2f4f_p1.png` | aadhar_card | START | YNYYY | 2 |
| `aadhar_card/dcbd172c_p1.png` | aadhar_card | START | YNYYY | 2 |
| `certificate_of_incorporation/48d93ca6_p2.png` | certificate_of_incorporation | CONT | NNYYN | 2 |
| `certificate_of_incorporation/c070a7c3_p1.png` | certificate_of_incorporation | START | YYYNY | 2 |
| `certificate_of_incorporation/c070a7c3_p2.png` | certificate_of_incorporation | CONT | YYYNY | 2 |
| `cibil_commercial/81cde9d4_p2.png` | cibil_commercial | CONT | YNYYY | 2 |
| `cibil_commercial/81cde9d4_p3.png` | cibil_commercial | CONT | YNYYY | 2 |
| `cibil_commercial/81cde9d4_p4.png` | cibil_commercial | CONT | YNYYY | 2 |
| `cibil_commercial/81cde9d4_p5.png` | cibil_commercial | CONT | YNYYY | 2 |
| `cibil_commercial/81cde9d4_p6.png` | cibil_commercial | CONT | YNYYY | 2 |
| `cibil_commercial/81cde9d4_p7.png` | cibil_commercial | CONT | YNYYY | 2 |
| `field_investigation_report/4692549c_p1.png` | field_investigation_report | START | NNYYN | 2 |
| `form_16/aa90c7cf_p2.png` | form_16 | CONT | YNYYY | 2 |
| `form_16/c77162f9_p1.png` | form_16 | START | YNNNY | 2 |
| `form_26AS/f9bb7ab3_p1.png` | form_26AS | START | YNNYY | 2 |
| `gst_accumn_report/94467b2b_p3.png` | gst_accumn_report | CONT | YNYYY | 2 |
| `gst_accumn_report/94467b2b_p4.png` | gst_accumn_report | CONT | YNYYY | 2 |
| `gst_accumn_report/94467b2b_p5.png` | gst_accumn_report | CONT | YNYYY | 2 |
| `gst_certificate/54d5e066_p2.png` | gst_certificate | CONT | YNYYY | 2 |
| `gst_certificate/54d5e066_p3.png` | gst_certificate | CONT | YNYYY | 2 |
| `gstr_form/1ba357cb_p1.png` | gstr_form | START | NNYYN | 2 |
| `gstr_form/2111c5ef_p10.png` | gstr_form | CONT | YNYYY | 2 |
| `gstr_form/2111c5ef_p13.png` | gstr_form | CONT | YNYYY | 2 |
| `gstr_form/2111c5ef_p16.png` | gstr_form | CONT | YNYYY | 2 |

*...and 53 more volatile pages*


## 4. Per-Class Trajectory


### 4.1 Full Trajectory Table (classes with support >= 2)

| Class | Support | Total | F1_baseline | FP_baseline | FN_baseline | F1_lora_w10 | FP_lora_w10 | FN_lora_w10 | F1_lora_hint | FP_lora_hint | FN_lora_hint | F1_prompt_v1 | FP_prompt_v1 | FN_prompt_v1 | F1_prompt_w5 | FP_prompt_w5 | FN_prompt_w5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| aadhar_card | 2 | 2 | 1.000 | 0 | 0 | 0.000 | 0 | 2 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| udyam_certificate | 2 | 6 | 0.000 | 0 | 2 | 0.667 | 0 | 1 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| balance_sheet | 5 | 6 | 0.000 | 0 | 5 | 0.571 | 0 | 3 | 0.571 | 0 | 3 | 0.571 | 0 | 3 | 0.889 | 0 | 1 |
| cibil_commercial | 2 | 13 | 0.667 | 2 | 0 | 0.333 | 8 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| tax_audit_3CB_3CD | 3 | 43 | 0.364 | 6 | 1 | 0.500 | 6 | 0 | 1.000 | 0 | 0 | 0.857 | 1 | 0 | 0.857 | 1 | 0 |
| title_search_report | 3 | 30 | 0.462 | 7 | 0 | 0.750 | 2 | 0 | 1.000 | 0 | 0 | 0.857 | 1 | 0 | 0.500 | 3 | 1 |
| certificate_of_incorporation | 2 | 22 | 0.800 | 1 | 0 | 0.800 | 1 | 0 | 1.000 | 0 | 0 | 0.500 | 1 | 1 | 0.800 | 1 | 0 |
| cibil_individual | 3 | 18 | 0.500 | 6 | 0 | 0.857 | 1 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.800 | 0 | 1 |
| disbursement_request_letter | 3 | 3 | 0.500 | 0 | 2 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| form_16 | 2 | 5 | 0.667 | 2 | 0 | 0.500 | 1 | 1 | 0.667 | 0 | 1 | 0.667 | 0 | 1 | 1.000 | 0 | 0 |
| passport_front | 2 | 4 | 0.667 | 2 | 0 | 0.667 | 2 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.500 | 1 | 1 |
| web_search_report | 2 | 6 | 0.500 | 1 | 1 | 0.667 | 0 | 1 | 1.000 | 0 | 0 | 0.667 | 0 | 1 | 0.800 | 1 | 0 |
| village_form_7_12 | 4 | 22 | 0.200 | 5 | 3 | 0.571 | 1 | 2 | 0.667 | 0 | 2 | 0.667 | 0 | 2 | 0.667 | 0 | 2 |
| bank_statement_of_account_SOA | 2 | 11 | 0.571 | 3 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| rent_agreement | 3 | 12 | 0.500 | 6 | 0 | 0.500 | 3 | 1 | 0.857 | 1 | 0 | 0.667 | 1 | 1 | 0.667 | 1 | 1 |
| aadhar_front | 4 | 4 | 0.667 | 0 | 2 | 0.667 | 0 | 2 | 0.857 | 0 | 1 | 0.857 | 0 | 1 | 1.000 | 0 | 0 |
| field_investigation_report | 2 | 3 | 0.667 | 0 | 1 | 0.667 | 0 | 1 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.667 | 0 | 1 |
| form_26AS | 2 | 8 | 1.000 | 0 | 0 | 0.667 | 0 | 1 | 0.667 | 0 | 1 | 1.000 | 0 | 0 | 0.800 | 1 | 0 |
| gst_certificate | 4 | 12 | 0.750 | 1 | 1 | 0.667 | 4 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.889 | 1 | 0 |
| income_sheet | 2 | 6 | 0.667 | 0 | 1 | 0.800 | 1 | 0 | 0.800 | 1 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| itr_individual | 2 | 2 | 0.667 | 0 | 1 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| professional_license | 2 | 2 | 0.667 | 0 | 1 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| notes_to_accounts | 6 | 76 | 0.286 | 0 | 5 | 0.444 | 1 | 4 | 0.500 | 0 | 4 | 0.500 | 0 | 4 | 0.600 | 1 | 3 |
| other | 3 | 9 | 0.500 | 0 | 2 | 0.500 | 0 | 2 | 0.500 | 0 | 2 | 0.500 | 0 | 2 | 0.800 | 0 | 1 |
| shop_act_license | 2 | 3 | 0.500 | 1 | 1 | 0.800 | 1 | 0 | 0.800 | 1 | 0 | 0.800 | 1 | 0 | 0.800 | 1 | 0 |
| pnl_statement | 8 | 18 | 0.400 | 0 | 6 | 0.400 | 0 | 6 | 0.400 | 0 | 6 | 0.667 | 0 | 4 | 0.667 | 0 | 4 |
| other_financial_doc | 8 | 34 | 0.545 | 0 | 5 | 0.667 | 0 | 4 | 0.800 | 1 | 2 | 0.800 | 1 | 2 | 0.714 | 1 | 3 |
| aadhar_back | 3 | 3 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.800 | 0 | 1 |
| bank_cheque | 3 | 6 | 1.000 | 0 | 0 | 0.800 | 0 | 1 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.800 | 0 | 1 |
| email | 2 | 4 | 0.800 | 1 | 0 | 0.800 | 1 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| itr_firm | 3 | 3 | 0.800 | 0 | 1 | 0.800 | 0 | 1 | 1.000 | 0 | 0 | 0.800 | 0 | 1 | 1.000 | 0 | 0 |
| non_agriculture_order | 2 | 8 | 0.800 | 1 | 0 | 0.800 | 1 | 0 | 1.000 | 0 | 0 | 0.800 | 1 | 0 | 1.000 | 0 | 0 |
| tax_challan | 3 | 4 | 1.000 | 0 | 0 | 0.857 | 1 | 0 | 1.000 | 0 | 0 | 0.857 | 1 | 0 | 0.857 | 1 | 0 |
| combined_pnl_bs | 2 | 3 | 0.800 | 1 | 0 | 0.667 | 0 | 1 | 0.800 | 1 | 0 | 0.667 | 0 | 1 | 0.800 | 1 | 0 |
| computation_sheet | 3 | 5 | 0.667 | 1 | 1 | 0.800 | 0 | 1 | 0.800 | 0 | 1 | 0.800 | 0 | 1 | 0.800 | 0 | 1 |
| schedules_and_annexures | 10 | 187 | 0.421 | 5 | 6 | 0.400 | 2 | 7 | 0.526 | 4 | 5 | 0.421 | 5 | 6 | 0.444 | 4 | 6 |
| gstr_form | 7 | 131 | 0.476 | 9 | 2 | 0.414 | 16 | 1 | 0.467 | 16 | 0 | 0.467 | 16 | 0 | 0.400 | 13 | 2 |
| bank_statement | 16 | 921 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 0.968 | 0 | 1 |
| form_60 | 2 | 2 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| itr_individual_full | 2 | 149 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 | 1.000 | 0 | 0 |
| municipal_mutation_record | 4 | 25 | 0.000 | 10 | 4 | 0.000 | 0 | 4 | 0.000 | 0 | 4 | 0.000 | 0 | 4 | 0.000 | 0 | 4 |
| property_revenue_docs | 2 | 4 | 0.000 | 2 | 2 | 0.000 | 0 | 2 | 0.000 | 0 | 2 | 0.000 | 0 | 2 | 0.000 | 0 | 2 |

### 4.2 Biggest Winners (F1 improved baseline -> latest)

- **udyam_certificate**: F1 0.000 -> 1.000 (+1.000), FP +0, FN -2
- **balance_sheet**: F1 0.000 -> 0.889 (+0.889), FP +0, FN -4
- **disbursement_request_letter**: F1 0.500 -> 1.000 (+0.500), FP +0, FN -2
- **tax_audit_3CB_3CD**: F1 0.364 -> 0.857 (+0.494), FP -5, FN -1
- **village_form_7_12**: F1 0.200 -> 0.667 (+0.467), FP -5, FN -1
- **bank_statement_of_account_SOA**: F1 0.571 -> 1.000 (+0.429), FP -3, FN +0
- **cibil_commercial**: F1 0.667 -> 1.000 (+0.333), FP -2, FN +0
- **form_16**: F1 0.667 -> 1.000 (+0.333), FP -2, FN +0
- **aadhar_front**: F1 0.667 -> 1.000 (+0.333), FP +0, FN -2
- **income_sheet**: F1 0.667 -> 1.000 (+0.333), FP +0, FN -1
- **itr_individual**: F1 0.667 -> 1.000 (+0.333), FP +0, FN -1
- **professional_license**: F1 0.667 -> 1.000 (+0.333), FP +0, FN -1
- **notes_to_accounts**: F1 0.286 -> 0.600 (+0.314), FP +1, FN -2
- **cibil_individual**: F1 0.500 -> 0.800 (+0.300), FP -6, FN +1
- **web_search_report**: F1 0.500 -> 0.800 (+0.300), FP +0, FN -1
- **other**: F1 0.500 -> 0.800 (+0.300), FP +0, FN -1
- **shop_act_license**: F1 0.500 -> 0.800 (+0.300), FP +0, FN -1
- **pnl_statement**: F1 0.400 -> 0.667 (+0.267), FP +0, FN -2
- **email**: F1 0.800 -> 1.000 (+0.200), FP -1, FN +0
- **itr_firm**: F1 0.800 -> 1.000 (+0.200), FP +0, FN -1
- **non_agriculture_order**: F1 0.800 -> 1.000 (+0.200), FP -1, FN +0
- **other_financial_doc**: F1 0.545 -> 0.714 (+0.169), FP +1, FN -2
- **rent_agreement**: F1 0.500 -> 0.667 (+0.167), FP -5, FN +1
- **gst_certificate**: F1 0.750 -> 0.889 (+0.139), FP +0, FN -1
- **computation_sheet**: F1 0.667 -> 0.800 (+0.133), FP -1, FN +0

### 4.3 Biggest Losers (F1 regressed baseline -> latest)

- **form_26AS**: F1 1.000 -> 0.800 (-0.200), FP +1, FN +0
- **aadhar_back**: F1 1.000 -> 0.800 (-0.200), FP +0, FN +1
- **bank_cheque**: F1 1.000 -> 0.800 (-0.200), FP +0, FN +1
- **passport_front**: F1 0.667 -> 0.500 (-0.167), FP -1, FN +1
- **tax_challan**: F1 1.000 -> 0.857 (-0.143), FP +1, FN +0
- **gstr_form**: F1 0.476 -> 0.400 (-0.076), FP +4, FN +0

### 4.4 Stubbornly Wrong (F1 < 0.5 in latest, support >= 2)

- **schedules_and_annexures**: F1=0.444 (support=10, total pages=187, errors in latest=10)
- **municipal_mutation_record**: F1=0.000 (support=4, total pages=25, errors in latest=4)
- **property_revenue_docs**: F1=0.000 (support=2, total pages=4, errors in latest=2)

## 5. Cumulative Regression Tracker

Tracks pages that were correct in baseline but broke at some point and never recovered.

- **Baseline correct, Latest wrong (net regressions)**: 37 pages
- **Baseline wrong, Latest correct (net improvements)**: 108 pages
- **Net change**: +71 pages


### 5.1 Regressions from Baseline (correct in Exp1, wrong in Exp5)


**gstr_form** (12 regressions: 11 now FP, 1 now FN):
- `gstr_form/2111c5ef_p31.png` [YYYYN] -> FP
- `gstr_form/2111c5ef_p40.png` [YYYYN] -> FP
- `gstr_form/21cdfb2c_p31.png` [YYNNN] -> FP
- `gstr_form/2111c5ef_p43.png` [YYYYN] -> FP
- `gstr_form/2111c5ef_p7.png` [YNNYN] -> FP
- `gstr_form/21cdfb2c_p19.png` [YYNNN] -> FP
- `gstr_form/ef099877_p1.png` [YYYYN] -> FN
- `gstr_form/2111c5ef_p19.png` [YYYYN] -> FP
- `gstr_form/2111c5ef_p28.png` [YYYYN] -> FP
- `gstr_form/21cdfb2c_p43.png` [YYYNN] -> FP
- `gstr_form/2111c5ef_p55.png` [YYYYN] -> FP
- `gstr_form/2111c5ef_p52.png` [YYYYN] -> FP

**property_ownership_docs** (3 regressions: 3 now FP):
- `property_ownership_docs/2073d3f1_p50.png` [YYYYN] -> FP
- `property_ownership_docs/2073d3f1_p37.png` [YYNYN] -> FP
- `property_ownership_docs/2073d3f1_p3.png` [YNNNN] -> FP

**title_search_report** (3 regressions: 2 now FP, 1 now FN):
- `title_search_report/281fe059_p2.png` [YNYYN] -> FP
- `title_search_report/49ad5a7a_p1.png` [YYYYN] -> FN
- `title_search_report/46458baa_p2.png` [YNYYN] -> FP

**schedules_and_annexures** (3 regressions: 2 now FP, 1 now FN):
- `schedules_and_annexures/96522712_p1.png` [YYYYN] -> FN
- `schedules_and_annexures/098a7bf8_p57.png` [YYYNN] -> FP
- `schedules_and_annexures/098a7bf8_p47.png` [YYYYN] -> FP

**form_26AS** (1 regressions: 1 now FP):
- `form_26AS/f9bb7ab3_p2.png` [YYYYN] -> FP

**bank_cheque** (1 regressions: 1 now FN):
- `bank_cheque/e07ec6df_p1.png` [YNYYN] -> FN

**gst_certificate** (1 regressions: 1 now FP):
- `gst_certificate/9d59e01a_p4.png` [YNYYN] -> FP

**email_conversation** (1 regressions: 1 now FP):
- `email_conversation/28315416_p2.png` [YYYYN] -> FP

**web_search_report** (1 regressions: 1 now FP):
- `web_search_report/499351f8_p2.png` [YYYYN] -> FP

**application_form** (1 regressions: 1 now FP):
- `application_form/a6ba2c62_p9.png` [YYYYN] -> FP

**tax_audit_3CB_3CD** (1 regressions: 1 now FP):
- `tax_audit_3CB_3CD/098a7bf8_p15.png` [YYYYN] -> FP

**rent_agreement** (1 regressions: 1 now FN):
- `rent_agreement/924a2cf0_p1.png` [YYYNN] -> FN

**cibil_individual** (1 regressions: 1 now FN):
- `cibil_individual/42212c9f_p1.png` [YYYYN] -> FN

**tax_challan** (1 regressions: 1 now FP):
- `tax_challan/318a930f_p2.png` [YNYNN] -> FP

**passport_front** (1 regressions: 1 now FN):
- `passport_front/433fb825_p1.png` [YYYYN] -> FN

**other_financial_doc** (1 regressions: 1 now FP):
- `other_financial_doc/1b0c1b36_p8.png` [YYYYN] -> FP

**bank_statement** (1 regressions: 1 now FN):
- `bank_statement/b91b0c92_p1.png` [YYYYN] -> FN

**notes_to_accounts** (1 regressions: 1 now FP):
- `notes_to_accounts/24140944_p28.png` [YYYYN] -> FP

**aadhar_back** (1 regressions: 1 now FN):
- `aadhar_back/baa671cd_p1.png` [YYYYN] -> FN

**gst_accumn_report** (1 regressions: 1 now FP):
- `gst_accumn_report/94467b2b_p2.png` [YNYYN] -> FP

### 5.2 Net Improvements (wrong in Exp1, correct in Exp5)

- **municipal_mutation_record**: 10 fixed (10 were FP)
- **gstr_form**: 8 fixed (7 were FP, 1 were FN)
- **tax_audit_3CB_3CD**: 7 fixed (6 were FP, 1 were FN)
- **cibil_individual**: 6 fixed (6 were FP)
- **title_search_report**: 6 fixed (6 were FP)
- **village_form_7_12**: 6 fixed (5 were FP, 1 were FN)
- **rent_agreement**: 5 fixed (5 were FP)
- **property_ownership_docs**: 5 fixed (5 were FP)
- **balance_sheet**: 4 fixed (4 were FN)
- **application_form**: 4 fixed (4 were FP)
- **schedules_and_annexures**: 4 fixed (3 were FP, 1 were FN)
- **loan_sanction_letter**: 3 fixed (3 were FP)
- **bank_statement_of_account_SOA**: 3 fixed (3 were FP)
- **gst_certificate**: 2 fixed (1 were FP, 1 were FN)
- **other_financial_doc**: 2 fixed (2 were FN)
- **pnl_statement**: 2 fixed (2 were FN)
- **cibil_commercial**: 2 fixed (2 were FP)
- **property_technical_report**: 2 fixed (1 were FP, 1 were FN)
- **aadhar_front**: 2 fixed (2 were FN)
- **notes_to_accounts**: 2 fixed (2 were FN)
- **web_search_report**: 2 fixed (1 were FP, 1 were FN)
- **disbursement_request_letter**: 2 fixed (2 were FN)
- **form_16**: 2 fixed (2 were FP)
- **property_revenue_docs**: 2 fixed (2 were FP)
- **udyam_certificate**: 2 fixed (2 were FN)
- **shop_act_license**: 1 fixed (1 were FN)
- **itr_individual**: 1 fixed (1 were FN)
- **passport_front**: 1 fixed (1 were FP)
- **itr_firm**: 1 fixed (1 were FN)
- **computation_sheet**: 1 fixed (1 were FP)
- **voter_id_front**: 1 fixed (1 were FN)
- **emi_repayment_schedule**: 1 fixed (1 were FP)
- **professional_license**: 1 fixed (1 were FN)
- **non_agriculture_order**: 1 fixed (1 were FP)
- **other**: 1 fixed (1 were FN)
- **tax_audit_3CA_3CD**: 1 fixed (1 were FP)
- **income_sheet**: 1 fixed (1 were FN)
- **email**: 1 fixed (1 were FP)