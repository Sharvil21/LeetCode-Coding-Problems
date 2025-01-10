--PostgreSQL Solution
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH cte AS (SELECT
    *, DENSE_RANK() OVER(ORDER BY Employee.salary DESC) AS rnk
    FROM Employee)
    SELECT
    DISTINCT cte.salary
    FROM cte WHERE rnk = n
    
      
  );
END;
$$ LANGUAGE plpgsql;
