--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
name
FROM Employee
WHERE 
id IN (SELECT managerId FROM Employee GROUP BY 1 HAVING COUNT(*) > 4 )

-- 2nd PostgreSQL solution
-- Write your PostgreSQL query statement below


WITH ManagerReports AS

(
    SELECT managerId , COUNT(managerId) AS managerReports
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
)

SELECT e.name
FROM Employee e 
INNER JOIN ManagerReports mr
ON e.id = mr.managerId
WHERE mr.managerReports >= 5; 
