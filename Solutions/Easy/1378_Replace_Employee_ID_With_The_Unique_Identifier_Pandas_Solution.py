#Pandas Solution
import pandas as pd
def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(employee_uni,on='id',how='left')
    return df.replace(float('nan'),None)[['name','unique_id']]

#2nd Pandas solution (Without using .replace() method. NaN is considered as Null in the test cases)
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(employee_uni, on='id', how='left')
    
    # Return the result table with the 'unique_id' column
    result = merged[['unique_id','name']]
    
    return result
