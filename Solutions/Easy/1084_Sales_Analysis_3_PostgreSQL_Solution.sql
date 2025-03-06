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


--Another postgreSQL Solution
SELECT Product.product_id, Product.product_name FROM Product 
JOIN Sales 
ON Product.product_id = Sales.product_id 
GROUP BY Sales.product_id 
HAVING MIN(Sales.sale_date) >= "2019-01-01" AND MAX(Sales.sale_date) <= "2019-03-31";
