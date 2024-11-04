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
# Write your MySQL query statement below
with v as (
    select user_id, sum(distance) as distance
    from Rides
    group by user_id
)

select name, ifnull(distance, 0) as travelled_distance
from Users u
left join v on u.id = v.user_id
order by travelled_distance desc, name
