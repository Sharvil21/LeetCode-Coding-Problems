--MySQL Solution
--First, write a SELECT query to get the name of the review that has the highest reviews
--This can be done by using COUNT() function along with group by. Order by this value DESCENDING and the name ASCENDING. Put this query in a CTE
--Then, in another CTE, get the Average ratings for all movies by JOINing the movies table with MovieRating Table
-- Use the AVG() function to get the ratings. Don't forget to use WHERE clause to filter only those rows where the created_at is in FEB 2020. Sort the values.
--Also, for both CTEs make sure to add LIMIT 1 as it causes problems when used in a UNION
-- Then, first write a select query to get the name from the first CTE then UNION ALL then another select query to get the movie name from second CTE
WITH cte1 AS (SELECT
user_id, name, COUNT(movie_id) AS total_reviews
FROM 
Users JOIN MovieRating USING(user_id)
GROUP BY 1,2
ORDER BY COUNT(movie_id) DESC, name ASC LIMIT 1),
cte2 AS (
    SELECT title, movie_id, AVG(rating) AS average_rating
    FROM Movies JOIN MovieRating USING(movie_id)
    WHERE EXTRACT(YEAR FROM created_at) = 2020 AND EXTRACT(MONTH FROM created_at) = 2
    GROUP BY 1,2
    ORDER BY 3 DESC, 1 ASC
    LIMIT 1
)

SELECT
name AS results
FROM cte1
UNION ALL
SELECT
title
FROM cte2
