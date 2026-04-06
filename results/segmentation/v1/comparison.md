# Doc Classification Benchmark Results
_Generated: 2026-04-04 20:58_

## Summary

| Run | Total | Errors | Parse Failures | Valid |
|-----|------:|-------:|---------------:|------:|
| qwen35_9b-segmentation-lora-upsampled-epoch3 | 1981 | 0 | 4 | 1977 |
| qwen35_9b-segmentation-lora-upsampled-epoch4 | 1981 | 0 | 4 | 1977 |
| qwen35_9b-segmentation-lora-upsampled-epoch5 | 1981 | 0 | 0 | 1981 |
| qwen35_9b-segmentation-lora-w10-checkpoint-138-merged | 1981 | 0 | 0 | 1981 |
| qwen35_9b-segmentation-lora-w10-checkpoint-46-merged | 1981 | 0 | 0 | 1981 |
| qwen35_9b-segmentation-lora-w10-checkpoint-92-merged | 1981 | 0 | 0 | 1981 |
| qwen35_9b_base | 2336 | 1 | 179 | 2156 |
| qwen35_9b_segmentation_sliding | 1981 | 0 | 533 | 1448 |
| qwen35_9b_segmentation_sliding_enhanced | 1981 | 0 | 0 | 1981 |
| qwen35_9b_segmentation_sliding_parsing_fix | 1981 | 0 | 0 | 1981 |
| qwen35_9b_wholefile_robust | 1456 | 0 | 278 | 1178 |
| qwen35_9b_wholefile_twopass | 1456 | 32 | 278 | 1146 |

## is_start_page (binary)

| Run | Accuracy | Precision | Recall | F1 | TP | FP | TN | FN |
|-----|:--------:|:---------:|:------:|:--:|---:|---:|---:|---:|
| qwen35_9b-segmentation-lora-upsampled-epoch3 | 0.955 | 0.6872 | 0.8272 | 0.7507 | 134 | 61 | 1754 | 28 |
| qwen35_9b-segmentation-lora-upsampled-epoch4 | 0.9631 | 0.7486 | 0.8272 | 0.7859 | 134 | 45 | 1770 | 28 |
| qwen35_9b-segmentation-lora-upsampled-epoch5 | 0.9631 | 0.7751 | 0.7892 | 0.7821 | 131 | 38 | 1777 | 35 |
| qwen35_9b-segmentation-lora-w10-checkpoint-138-merged | 0.9418 | 0.6284 | 0.7099 | 0.6667 | 115 | 68 | 1747 | 47 |
| qwen35_9b-segmentation-lora-w10-checkpoint-46-merged | 0.9233 | 0.5321 | 0.6988 | 0.6042 | 116 | 102 | 1713 | 50 |
| qwen35_9b-segmentation-lora-w10-checkpoint-92-merged | 0.9404 | 0.6412 | 0.6566 | 0.6488 | 109 | 61 | 1754 | 57 |
| qwen35_9b_base | 0.4281 | 0.3825 | 0.9987 | 0.5531 | 763 | 1232 | 160 | 1 |
| qwen35_9b_segmentation_sliding | 0.9254 | 0.5792 | 0.8357 | 0.6842 | 117 | 85 | 1223 | 23 |
| qwen35_9b_segmentation_sliding_enhanced | 0.9202 | 0.5208 | 0.6024 | 0.5586 | 100 | 92 | 1723 | 66 |
| qwen35_9b_segmentation_sliding_parsing_fix | 0.9248 | 0.5436 | 0.6386 | 0.5873 | 106 | 89 | 1726 | 60 |
| qwen35_9b_wholefile_robust | 0.9745 | 0.9543 | 0.8995 | 0.9261 | 188 | 9 | 960 | 21 |
| qwen35_9b_wholefile_twopass | 0.9738 | 0.9541 | 0.899 | 0.9257 | 187 | 9 | 929 | 21 |

## Label Accuracy (start pages only)

| Run | Overall Accuracy | Correct | Total |
|-----|:----------------:|--------:|------:|
| qwen35_9b-segmentation-lora-upsampled-epoch3 | - | - | - |
| qwen35_9b-segmentation-lora-upsampled-epoch4 | - | - | - |
| qwen35_9b-segmentation-lora-upsampled-epoch5 | - | - | - |
| qwen35_9b-segmentation-lora-w10-checkpoint-138-merged | - | - | - |
| qwen35_9b-segmentation-lora-w10-checkpoint-46-merged | - | - | - |
| qwen35_9b-segmentation-lora-w10-checkpoint-92-merged | - | - | - |
| qwen35_9b_base | 0.7225 | 552 | 764 |
| qwen35_9b_segmentation_sliding | - | - | - |
| qwen35_9b_segmentation_sliding_enhanced | - | - | - |
| qwen35_9b_segmentation_sliding_parsing_fix | - | - | - |
| qwen35_9b_wholefile_robust | 0.6699 | 140 | 209 |
| qwen35_9b_wholefile_twopass | 0.4471 | 93 | 208 |

### Per-Class Label Accuracy

| Label | qwen35_9b-segmentation-lora-upsampled-epoch3 | qwen35_9b-segmentation-lora-upsampled-epoch4 | qwen35_9b-segmentation-lora-upsampled-epoch5 | qwen35_9b-segmentation-lora-w10-checkpoint-138-merged | qwen35_9b-segmentation-lora-w10-checkpoint-46-merged | qwen35_9b-segmentation-lora-w10-checkpoint-92-merged | qwen35_9b_base | qwen35_9b_segmentation_sliding | qwen35_9b_segmentation_sliding_enhanced | qwen35_9b_segmentation_sliding_parsing_fix | qwen35_9b_wholefile_robust | qwen35_9b_wholefile_twopass |
|-------|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| NACH_form | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| aadhar_back | - | - | - | - | - | - | 0.474 | - | - | - | 0.333 | 0.000 |
| aadhar_card | - | - | - | - | - | - | 0.900 | - | - | - | 0.750 | 0.250 |
| aadhar_front | - | - | - | - | - | - | 0.842 | - | - | - | 0.600 | 0.000 |
| aadhar_udyog | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| accumn_monitor_alerts | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| agreement_to_sale_cancellation | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| application_form | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 0.400 |
| balance_sheet | - | - | - | - | - | - | 1.000 | - | - | - | 0.600 | 0.400 |
| bank_cheque | - | - | - | - | - | - | 0.714 | - | - | - | - | - |
| bank_signature_verification | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| bank_statement | - | - | - | - | - | - | 1.000 | - | - | - | 0.800 | 0.200 |
| bank_statement_of_account_SOA | - | - | - | - | - | - | 0.500 | - | - | - | 0.000 | 0.000 |
| builder_allotment_letter | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| building_use_permission | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| ca_certificate | - | - | - | - | - | - | 0.286 | - | - | - | 0.800 | 0.800 |
| cersai_asset_search_report | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| certificate_of_incorporation | - | - | - | - | - | - | 0.923 | - | - | - | 1.000 | 1.000 |
| cibil_commercial | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 0.000 |
| cibil_individual | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 0.200 |
| combined_pnl_bs | - | - | - | - | - | - | 0.692 | - | - | - | 0.750 | 0.500 |
| commencement_letter_rajachitthi | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| computation_sheet | - | - | - | - | - | - | 0.800 | - | - | - | 0.667 | 0.500 |
| death_certificate | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| debt_sheet | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| deed_of_hypothecation | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| development_agreement | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| disbursement_memo | - | - | - | - | - | - | 0.833 | - | - | - | - | - |
| disbursement_request_letter | - | - | - | - | - | - | 1.000 | - | - | - | 0.000 | 0.000 |
| driving_license | - | - | - | - | - | - | 0.857 | - | - | - | 1.000 | 0.000 |
| dual_demographic_undertaking | - | - | - | - | - | - | 0.857 | - | - | - | - | - |
| electricity_bill | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| email | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| email_conversation | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| emi_repayment_schedule | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| employee_id_card | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| encumbrance_certificate | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| experience_letter | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| field_investigation_report | - | - | - | - | - | - | 0.556 | - | - | - | - | - |
| field_visit_photograph | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| foreclosure_letter | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| form_16 | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| form_26AS | - | - | - | - | - | - | 1.000 | - | - | - | 0.500 | 0.167 |
| form_60 | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| form_AIS | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| gas_bill | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| general_power_of_attorney | - | - | - | - | - | - | 0.667 | - | - | - | - | - |
| gift_deed_docs | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| gst_accumn_report | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| gst_certificate | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| gst_registration | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| gstr_form | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| income_sheet | - | - | - | - | - | - | 0.778 | - | - | - | 0.800 | 0.800 |
| invoice_quotation_bill | - | - | - | - | - | - | 0.875 | - | - | - | - | - |
| itr_firm | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| itr_firm_full | - | - | - | - | - | - | 0.000 | - | - | - | 0.500 | 0.500 |
| itr_individual | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| itr_individual_full | - | - | - | - | - | - | 0.000 | - | - | - | 0.400 | 0.400 |
| key_facts_statement | - | - | - | - | - | - | 0.667 | - | - | - | 1.000 | 0.000 |
| legal_heir_certificate | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| loan_end_use_letter | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| loan_exposure_summary | - | - | - | - | - | - | 0.222 | - | - | - | 0.000 | 0.000 |
| loan_lod_letter | - | - | - | - | - | - | 0.444 | - | - | - | - | - |
| loan_sanction_letter | - | - | - | - | - | - | 0.667 | - | - | - | 0.333 | 0.000 |
| memorandum_deposit_title_deeds | - | - | - | - | - | - | 0.500 | - | - | - | - | - |
| memorandum_of_association | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| municipal_mutation_record | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| na_conversion_affidavit | - | - | - | - | - | - | 0.250 | - | - | - | - | - |
| noc_financial_institution_docs | - | - | - | - | - | - | 0.400 | - | - | - | - | - |
| non_agriculture_order | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| notes_to_accounts | - | - | - | - | - | - | 1.000 | - | - | - | 0.500 | 0.500 |
| other | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| other_financial_doc | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| other_property_docs | - | - | - | - | - | - | 0.125 | - | - | - | 0.000 | 0.000 |
| pan_card | - | - | - | - | - | - | 0.900 | - | - | - | 0.800 | 0.000 |
| partnership_deed | - | - | - | - | - | - | 0.333 | - | - | - | 1.000 | 1.000 |
| passport | - | - | - | - | - | - | 0.333 | - | - | - | - | - |
| passport_back | - | - | - | - | - | - | 0.750 | - | - | - | - | - |
| passport_front | - | - | - | - | - | - | 0.750 | - | - | - | 1.000 | 0.000 |
| payment_receipt | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| pension_card | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| phone_bill | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| photograph | - | - | - | - | - | - | 0.950 | - | - | - | 0.750 | 0.750 |
| pnl_statement | - | - | - | - | - | - | 0.500 | - | - | - | 0.600 | 0.600 |
| professional_license | - | - | - | - | - | - | 0.533 | - | - | - | 0.500 | 0.000 |
| property_builder_docs | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| property_development_authority_docs | - | - | - | - | - | - | 0.400 | - | - | - | - | - |
| property_ownership_docs | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| property_revenue_docs | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| property_tax_receipts | - | - | - | - | - | - | 0.667 | - | - | - | - | - |
| property_tax_receipts_docs | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| property_technical_report | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 0.000 |
| ration_card | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| rent_agreement | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 0.000 |
| salary_slip | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| sale_agreement_docs | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| sale_deed_docs | - | - | - | - | - | - | 0.333 | - | - | - | 0.000 | 0.000 |
| sanctioned_layout_plan | - | - | - | - | - | - | 0.750 | - | - | - | - | - |
| schedules_and_annexures | - | - | - | - | - | - | 1.000 | - | - | - | 0.800 | 0.400 |
| shop_act_license | - | - | - | - | - | - | 0.938 | - | - | - | 1.000 | 1.000 |
| society_registration | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| tax_audit_3CA_3CD | - | - | - | - | - | - | 1.000 | - | - | - | 0.800 | 0.600 |
| tax_audit_3CB_3CD | - | - | - | - | - | - | 0.333 | - | - | - | 0.600 | 0.400 |
| tax_challan | - | - | - | - | - | - | 1.000 | - | - | - | 0.600 | 0.600 |
| title_search_report | - | - | - | - | - | - | 0.667 | - | - | - | - | - |
| trade_license | - | - | - | - | - | - | 0.400 | - | - | - | 1.000 | 1.000 |
| trust_deed | - | - | - | - | - | - | 0.000 | - | - | - | - | - |
| uae_resident_id | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| udyam_certificate | - | - | - | - | - | - | 1.000 | - | - | - | 1.000 | 1.000 |
| unclassified | - | - | - | - | - | - | 0.000 | - | - | - | 0.000 | 0.000 |
| upi_transaction_statement | - | - | - | - | - | - | 0.750 | - | - | - | - | - |
| vehicle_info | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| vehicle_insurance_policy | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| vetting_report | - | - | - | - | - | - | 0.667 | - | - | - | - | - |
| village_form_7_12 | - | - | - | - | - | - | 0.750 | - | - | - | - | - |
| voter_id | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
| voter_id_back | - | - | - | - | - | - | 0.500 | - | - | - | - | - |
| voter_id_front | - | - | - | - | - | - | 0.900 | - | - | - | 0.750 | 0.250 |
| web_search_report | - | - | - | - | - | - | 0.600 | - | - | - | - | - |
| wholesale_cam | - | - | - | - | - | - | 1.000 | - | - | - | - | - |
