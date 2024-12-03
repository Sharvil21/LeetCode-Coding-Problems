#Pandas Solution
import pandas as pd
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee.sort_values(by=['employee_id','primary_flag'],ascending=[True,False],inplace=True)
    employee.drop_duplicates(subset=['employee_id'],keep='first',inplace=True)
    return employee[['employee_id','department_id']]
