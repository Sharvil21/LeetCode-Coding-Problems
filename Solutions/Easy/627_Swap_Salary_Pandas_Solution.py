#Pandas Solution
#First solution: Using .replace method on the column
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'].replace({'f':'m','m':'f'},inplace=True)
    return salary

#Another Pandas Solution
#Using .replace method directly
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    return salary.replace({'f':'m','m':'f'})

#Using if else condition
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = ['m' if x=='f' else 'f' for x in salary.sex]
    return salary
    
