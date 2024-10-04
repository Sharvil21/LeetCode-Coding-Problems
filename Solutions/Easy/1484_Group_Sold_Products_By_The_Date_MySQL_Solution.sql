--MySQL Solution (Have to use the GROUP_CONCAT() Function to get the desired 3rd column)
SELECT
sell_date,
COUNT(DISTINCT product) AS num_sold,
GROUP_CONCAT(DISTINCT product ORDER BY product ASC) AS products
FROM Activities
GROUP BY 1;


