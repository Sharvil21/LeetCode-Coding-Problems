--MySQL Solution
SELECT
*
FROM Users
WHERE email REGEXP "^[A-Za-z0-9]*@[A-Za-z]*.com"

--
