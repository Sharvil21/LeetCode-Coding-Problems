--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI USING(id)
