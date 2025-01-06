--MySQL Solution
SELECT
user_id, CONCAT(UPPER(SUBSTRING(name,1,1)), LOWER(SUBSTRING(name,2))) AS name
FROM Users;

--PostgreSQL Solution
