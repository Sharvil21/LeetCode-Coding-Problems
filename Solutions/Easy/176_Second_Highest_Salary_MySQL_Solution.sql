--MySQL Solution Using Dense_RANK
SELECT (SELECT
DISTINCT Salary  
FROM Employee
ORDER BY Salary DESC
LIMIT 1
OFFSET 1
)
AS SecondHighestSalary;

--2nd solutio
