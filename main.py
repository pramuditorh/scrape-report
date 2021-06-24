import pandas as pd

SCAN_BEFORE = '/home/robby/projects/scrape-report/scan-report/scanbefore-report_scan_21062021T082729.html'
REMEDIATION = '/home/robby/projects/scrape-report/scan-report/remediation-report_scan_21062021T091729.html'
ROLLBACK = '/home/robby/projects/scrape-report/scan-report/rollback-report_scan_21062021T094803.html' 

df_scan_before_report = pd.read_html(SCAN_BEFORE)
df_remediation_report = pd.read_html(REMEDIATION)
df_rollback_report = pd.read_html(ROLLBACK)
series_scan_before_rule = df_scan_before_report[1]['Rule']
series_scan_before_skipped_rule = df_scan_before_report[2]['Rule']
series_remediation_rule = df_remediation_report[1]['Rule']
series_remediation_skipped_rule = df_remediation_report[2]['Rule']
series_rollback_rule = df_remediation_report[1]['Rule']
series_rollback_skipped_rule = df_remediation_report[2]['Rule']
series_scan_before_result = df_scan_before_report[1]['Result']
series_remediation_result = df_remediation_report[1]['Result']
series_rollback_result =  df_rollback_report[1]['Result']
combined = pd.concat([series_scan_before_rule, series_scan_before_result, 
   series_remediation_result, series_rollback_result], axis=1).to_csv('combined.csv', index=False)

#print(series_remediation_rule.to_string(index=False))