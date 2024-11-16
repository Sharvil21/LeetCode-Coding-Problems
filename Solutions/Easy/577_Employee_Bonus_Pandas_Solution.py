#Pandas Solution: 
#Step 1: Merge the tables using a left Join
#Step 2: Filter out the row where bonus is <1000 Or where the bonus column is null
#For null values, we have to use .isna() method, and not '== None' as this won't work
#Use .loc tnd specify the name, bonus columns to get the desired output

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
     df = employee.merge(bonus,on='empId', how = 'left')
     return df.loc[(df['bonus'] < 1000) | (df['bonus'].isna()),['name','bonus']]

#Another Pandas Solution
