--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
name
FROM Employee
WHERE 
id IN (SELECT managerId FROM Employee GROUP BY 1 HAVING COUNT(*) > 4 )
