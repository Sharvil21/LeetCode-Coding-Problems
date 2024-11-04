--MySQL Solution using left join and CASE WHEN
WITH cte AS (SELECT
u.id AS id, u.name AS name, SUM(CASE WHEN r.distance IS NOT NULL THEN r.distance ELSE 0 END) AS travelled_distance
FROM
Users u LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY 1,2
ORDER BY 2 DESC, 1 ASC)
SELECT
name, travelled_distance
FROM cte
ORDER BY travelled_distance DESC, name ASC

--Another MYSQL Solution
