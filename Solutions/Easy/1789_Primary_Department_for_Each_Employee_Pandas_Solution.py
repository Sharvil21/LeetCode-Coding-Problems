#Pandas Solution
#Logic is to sort the values by employee id ascending the primary_flag descending
#Then drop the duplicates only keep first. and return the required columns
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee.sort_values(by=['employee_id','primary_flag'],ascending=[True,False],inplace=True)
    employee.drop_duplicates(subset=['employee_id'],keep='first',inplace=True)
    return employee[['employee_id','department_id']]
