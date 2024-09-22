--PostgreSQL Solution:
WITH cte AS (
    SELECT
b.id
FROM Person a
JOIN Person b
ON a.email = b.email AND a.id < b.id)

DELETE FROM PERSON
WHERE id IN (SELECT * FROM cte)

--2nd PostgreSQL Solution
-- Write your PostgreSQL query statement below
WITH cte AS (SELECT
min(id) AS id, email
FROM Person
GROUP BY email)

DELETE
FROM Person
WHERE id NOT IN (SELECT id FROM cte)
