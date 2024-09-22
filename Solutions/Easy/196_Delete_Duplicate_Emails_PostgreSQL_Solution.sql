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
