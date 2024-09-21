--MySQL Solution
SELECT
b.id
FROM Person a
JOIN Person b
ON a.email = b.email AND a.id < b.id)
