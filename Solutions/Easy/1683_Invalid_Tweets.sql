--MySQL Solution
# Write your MySQL query statement below
SELECT
tweet_id
FROM Tweets
WHERE LENGTH(content) > 15

-- MySQL Solution with CHAR_LENGTH
# Write your MySQL query statement below
SELECT
tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15
