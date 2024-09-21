--MySQL Solution
WITH cte AS (
    SELECT
b.id
FROM Person a
JOIN Person b
ON a.email = b.email AND a.id < b.id)

DELETE FROM PERSON
WHERE id IN (SELECT * FROM cte)

-- Second MySQL Solution
delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;


