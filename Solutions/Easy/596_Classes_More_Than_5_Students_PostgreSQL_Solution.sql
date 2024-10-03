--PostgreSQL Solution
WITH cte AS (SELECT
class, COUNT(student) AS cnt
FROM Courses
GROUP BY 1)
SELECT class FROM cte WHERE cnt >=5

