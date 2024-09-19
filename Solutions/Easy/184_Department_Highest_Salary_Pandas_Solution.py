#Pandas Solution
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId',right_on='id',how='inner')
    df['rnk'] = df.groupby('name_y')['salary'].rank(method='dense',ascending=False)
