#Pandas Solution
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId',right_on='id',how='inner')
    df['rnk'] = df.groupby('name_y')['salary'].rank(method='dense',ascending=False)
    return df.query('rnk == 1')[['name_y','name_x','salary']].rename(columns={'name_y':'Department','name_x':'Employee','salary':'Salary'})






