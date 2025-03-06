--PostgreSQL Solution
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT
product_id,
product_name
FROM Product JOIN Sales USING(product_id)
WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31')

SELECT 
DISTINCT product_id, product_name
FROM Product
JOIN Sales USING(product_id)
WHERE product_id NOT IN (SELECT product_id FROM cte)
