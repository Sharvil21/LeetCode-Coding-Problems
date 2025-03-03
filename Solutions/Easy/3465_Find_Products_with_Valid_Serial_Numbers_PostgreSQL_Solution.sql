--PostgreSQL solution
-- Write your PostgreSQL query statement below
SELECT
*
FROM products
WHERE description ~* '\mSN[0-9]{4}\-[0-9]{4}\M'
ORDER BY 1 ASC;
