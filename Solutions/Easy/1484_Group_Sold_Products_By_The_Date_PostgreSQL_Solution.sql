--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
sell_date, COUNT(DISTINCT product) AS num_sold,
STRING_AGG(DISTINCT product,',') AS products
FROM Activities
GROUP BY 1
ORDER BY 1
