--MySQL Solution
--First, use SUM() OVER() window function to get the cumulative sum for each turn
--Put that in a cte
--Then select only that person name when ordering the cumulative weight in descending order & the cumulative weight is <=1000
--Lastly, only return 1 row, which will be done by LIMIT 1

# Write your MySQL query statement below
WITH cte AS (SELECT
*,
SUM(weight) OVER(ORDER BY turn ASC) AS weight_till_this_turn
FROM Queue)

SELECT
person_name
FROM cte
WHERE weight_till_this_turn <= 1000
ORDER BY weight_till_this_turn DESC
LIMIT 1
