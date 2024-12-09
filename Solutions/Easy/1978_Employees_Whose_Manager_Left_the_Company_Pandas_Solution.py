#Pandas Solution
#Logic is that we need to find the manager_id which does not exist in the employee_id column
#We can use .loc[] and .isin() method to make it work
#So basically, we filter out saying give us the rows where manager_id is not in employee_id column and also the manager_id is not null and also where the salary is <30000
#Lastly, sort the values by employee_id
import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[(~employees['manager_id'].isin(employees['employee_id'])) & (~employees['manager_id'].isna()) & (employees['salary'] <30000),'employee_id'].to_frame('employee_id').sort_values('employee_id')
