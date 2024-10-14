--MySQL Solution
WITH cte AS (SELECT
SalesPerson.name
FROM SalesPerson
LEFT JOIN Orders USING(sales_id)
LEFT JOIN Company USING(com_id)
WHERE Company.name = "RED")

SELECT
name
FROM SalesPerson
WHERE name NOT IN (SELECT * FROM CTE)
