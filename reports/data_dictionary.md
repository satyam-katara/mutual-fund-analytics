# Data Dictionary

## dim_fund

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| scheme_name | TEXT | Scheme Name |
| fund_house | TEXT | Mutual Fund House |
| category | TEXT | Equity/Debt |
| plan | TEXT | Regular/Direct |

## fact_nav

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Fund Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| amount_inr | REAL | Investment Amount |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |