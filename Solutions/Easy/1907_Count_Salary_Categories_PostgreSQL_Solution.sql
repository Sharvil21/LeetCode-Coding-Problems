--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
'Low Salary' AS category, SUM(CASE WHEN income < 20000 THEN 1 ELSE 0 END) AS accounts_count
FROM Accounts
UNION ALL
SELECT
'Average Salary' AS category, SUM(CASE WHEN income BETWEEN 20000 AND 50000 THEN 1 ELSE 0 END) AS accounts_count
FROM Accounts
UNION ALL
SELECT
'High Salary' AS category, SUM(CASE WHEN income > 50000 THEN 1 ELSE 0 END) AS accounts_count
FROM Accounts

--2nd PostgreSQL Solution
WITH cte1 AS (SELECT account_id,
CASE WHEN income < 20000 THEN 'Low Salary'
WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
WHEN income > 50000 THEN 'High Salary' END AS category
FROM Accounts
UNION SELECT NULL, 'Low Salary'
UNION SELECT NULL, 'Average Salary'
UNION SELECT NULL, 'High Salary'
)
