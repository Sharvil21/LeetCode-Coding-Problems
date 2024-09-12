--MySQL Solution
--Write your MySQL query statement below
SELECT
DISTINCT author_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY 1 ASC;

--PostgreSQL Solution
-- Write your PostgreSQL query statement below
SELECT
DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id;
