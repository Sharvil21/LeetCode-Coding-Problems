--MySQL Solution
SELECT
employee_id, CASE WHEN employee_id%2!=0 AND SUBSTRING(name,1,1)!='M' THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY 1;

--PostgreSQL Solution
SELECT
employee_id, CASE WHEN employee_id%2!=0 AND SUBSTRING(name,1,1)!='M' THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY 1;
