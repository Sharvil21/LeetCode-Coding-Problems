--PostgreSQL Solution
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT
DISTINCT salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
FROM Employee)

SELECT
(SELECT salary
FROM cte
WHERE rnk = 2)
AS SecondHighestSalary

--Second Postgresql Solution
-- Write your PostgreSQL query statement below
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT
DISTINCT salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS rnk
FROM Employee)

SELECT salary AS SecondHighestSalary FROM cte WHERE rnk = 2
UNION
SELECT NULL
LIMIT 1;

