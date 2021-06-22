import pandas as pd
from pandas.core.indexes.base import Index

SCAN_BEFORE = '/home/robby/projects/scrape-report/scan-report/scanbefore-report_scan_21062021T082729.html'
REMEDIATION = '/home/robby/projects/scrape-report/scan-report/remediation-report_scan_21062021T091729.html'
ROLLBACK = '/home/robby/projects/scrape-report/scan-report/rollback-report_scan_21062021T094803.html' 

df_scan_before_rule = pd.read_html(SCAN_BEFORE)
df_scan_before_result = pd.read_html(SCAN_BEFORE)
df_remediation_result = pd.read_html(REMEDIATION)
df_rollback_result = pd.read_html(ROLLBACK)
series_scan_before_rule = df_scan_before_rule[1]['Rule']
series_scan_before_result = df_scan_before_result[1]['Result']
series_remediation_result = df_remediation_result[1]['Result']
series_rollback_result =  df_rollback_result[1]['Result']
combined = pd.concat([series_scan_before_rule, series_scan_before_result, series_remediation_result, series_rollback_result], axis=1).to_csv('combined.csv', index=False)