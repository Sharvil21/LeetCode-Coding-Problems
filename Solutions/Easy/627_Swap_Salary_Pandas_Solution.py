#Pandas Solution
#First solution: Using .replace mnethod
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'].replace({'f':'m','m':'f'},inplace=True)
    return salary

#Another Pandas Solution
#
