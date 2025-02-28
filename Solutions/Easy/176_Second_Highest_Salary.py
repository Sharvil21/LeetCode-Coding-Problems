#Pandas Solution using .rank() method
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee['salary'].drop_duplicates().shape[0] < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    
    employee['rnk'] = employee['salary'].rank(method='dense',ascending=False)
    return employee.query("rnk == 2")['salary'].drop_duplicates().to_frame("SecondHighestSalary")
