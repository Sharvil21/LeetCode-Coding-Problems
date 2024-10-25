--MySQL Solution
--Write your MySQL Query Statement Below
WITH cte AS (SELECT
email, COUNT(email) AS total_emails
FROM Person
GROUP BY 1
HAVING COUNT(email) > 1)

SELECT email AS Email
FROM cte
