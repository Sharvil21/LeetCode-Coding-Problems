--MySQL Solution
SELECT
*
FROM Users
WHERE email REGEXP "^[A-Za-z0-9]*@[A-Za-z]*.com"

--Another MySQL Solution using REGEXP and :word:
SELECT
*
FROM Users
WHERE email REGEXP "^[:word:]*@[A-Za-z]*.com"
