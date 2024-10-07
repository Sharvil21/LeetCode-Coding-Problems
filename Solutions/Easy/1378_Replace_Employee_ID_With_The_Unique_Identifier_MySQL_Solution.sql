--MySQL Solution
SELECT
unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI
USING(id)

--Second MySQL Solution
SELECT EmployeeUNI.unique_id, Employees.name FROM Employees LEFT JOIN EmployeeUNI ON EmployeeUNI.id = Employees.id
