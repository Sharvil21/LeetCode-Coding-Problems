#Pandas Solution using .rank() Dense Rank Method
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee['rankk'] = employee['salary'].rank(method='dense', ascending=False)
    if employee['salary'].drop_duplicates().shape[0] < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    return employee.loc[employee['rankk']==N,'salary'].drop_duplicates().to_frame(f'getNthHighestSalary({N})')

#
