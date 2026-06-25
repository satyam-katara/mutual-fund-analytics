-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Average Monthly NAV
SELECT strftime('%Y-%m', date) AS Month,
AVG(nav) AS Avg_NAV
FROM fact_nav
GROUP BY Month;

-- 4. Transactions by State
SELECT state,
COUNT(*) AS Total_Transactions
FROM fact_transactions
GROUP BY state
ORDER BY Total_Transactions DESC;

-- 5. Expense Ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Total AUM by Fund House
SELECT fund_house,
SUM(aum_crore)
FROM fact_aum
GROUP BY fund_house;

-- 7. Average 3-Year Return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 8. Total SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- 9. Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 10. Top 10 NAV Values
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;