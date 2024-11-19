--MySQL Solution
SELECT
*
FROM
Cinema
WHERE id%2 != 0 AND description NOT LIKE "%boring%"
ORDER BY rating DESC;

--Another MYSQL Solution
--This time use <> instead of NOT LIKE in the WHERE clause

SELECT * FROM Cinema WHERE MOD( id, 2) = 1 AND 
description <> 'boring' ORDER BY rating DESC
