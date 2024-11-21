#Pandas Solution
#Step 1 : Merge the two tables using Inner JOIN
#Step 2: Group by project_id
#Step 3:use the .mean() method to get the avg experience years
#Step 4: rename the columns and return the output
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee,on='employee_id',how='inner')
    return df.groupby('project_id')['experience_years'].mean().round(2).reset_index().rename(columns={'experience_years':'average_years'})

#
