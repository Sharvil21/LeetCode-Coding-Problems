#Pandas Solution using .merge() method (Basically self join)
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee,left_on='managerId',right_on='id',how='inner')
    return df.loc[df['salary_x']>df['salary_y'],'name_x'].to_frame('Employee')
