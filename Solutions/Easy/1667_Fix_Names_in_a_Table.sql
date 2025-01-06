--MySQL Solution
SELECT
user_id, CONCAT(UPPER(SUBSTRING(name,1,1)), LOWER(SUBSTRING(name,2))) AS name
FROM Users
ORDER BY user_id;

--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
user_id, UPPER(SUBSTR(name,1,1)) || LOWER(SUBSTR(name,2)) AS name
FROM Users
ORDER BY user_id
