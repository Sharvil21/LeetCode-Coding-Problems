--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
*
FROM Users
WHERE
email ~ '^[A-Za-z0-9_]*@[A-Za-z]*.com$'

--Another PostgreSQL Solution
