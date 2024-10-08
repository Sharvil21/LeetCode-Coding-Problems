#Pandas Solution
import pandas as pd
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni,on='id',how='left')
    return df.replace(float('nan'),None)[['name','unique_id']]


