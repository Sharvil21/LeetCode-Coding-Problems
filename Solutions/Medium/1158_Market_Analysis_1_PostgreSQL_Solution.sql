--PostgreSQL Solution
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT
*
FROM 
USERS u
LEFT JOIN Orders o ON u.user_id = o.buyer_id
)

SELECT
user_id AS buyer_id, join_date,
SUM(CASE WHEN EXTRACT(YEAR FROM order_date) = 2019 THEN 1 ELSE 0 END) AS orders_in_2019
FROM cte
GROUP BY 1,2
ORDER By 1

