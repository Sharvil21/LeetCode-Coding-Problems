#First solution using CTE
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT customer_number, COUNT(order_number) AS total_orders
FROM Orders
GROUP BY 1
ORDER BY 2 DESC)
SELECT customer_number FROM cte LIMIT 1

#Second solution using CTE & Dense Rank Window Function
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT
customer_number, DENSE_RANK() OVER(ORDER BY COUNT(order_number) DESC) as rnk
FROM Orders
GROUP BY 1)

SELECT customer_number FROM cte WHERE rnk = 1;
