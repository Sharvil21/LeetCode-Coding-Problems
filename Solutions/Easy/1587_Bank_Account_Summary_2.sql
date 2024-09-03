-- Write your PostgreSQL query statement below
SELECT
name,
SUM(amount) AS balance
FROM Users JOIN Transactions USING(account)
GROUP BY 1
HAVING SUM(amount) > 10000

