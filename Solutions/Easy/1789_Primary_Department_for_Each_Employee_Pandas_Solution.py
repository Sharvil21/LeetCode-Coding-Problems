#Pandas Solution
#Logic is to sort the values by employee id ascending the primary_flag descending
#Then drop the duplicates only keep first. and return the required columns
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee.sort_values(by=['employee_id','primary_flag'],ascending=[True,False],inplace=True)
    employee.drop_duplicates(subset=['employee_id'],keep='first',inplace=True)
    return employee[['employee_id','department_id']]

#One Liner Solution
#Similar solution as previous, but in this, we remove the inplace=True argument from both methods, and use both the methods in the same line 
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    
    return employee.sort_values(by=['employee_id','primary_flag'],ascending=[True,False]).drop_duplicates(subset=['employee_id'],keep='first')[['employee_id','department_id']]
