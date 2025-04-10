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
#Same steps as first solution
#Difference will be in the last steps
#Instead of specifying the names of columns, we specify the indexes using iloc
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    df = employee.merge(bonus, how = 'left', on = 'empId')

    return df[(df.bonus < 1000)|(df.bonus.isnull())].iloc[:,[1,4]]
    
