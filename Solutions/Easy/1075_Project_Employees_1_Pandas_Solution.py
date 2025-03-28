#Pandas Solution
#Step 1 : Merge the two tables using Inner JOIN
#Step 2: Group by project_id
#Step 3:use the .mean() method to get the avg experience years
#Step 4: rename the columns and return the output
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee,on='employee_id',how='inner')
    return df.groupby('project_id')['experience_years'].mean().round(2).reset_index().rename(columns={'experience_years':'average_years'})

#Another Pandas Solution - clean code, uses .rename() method
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
  # merge DataFrames 'project' and 'employee' 
  df = pd.merge(project, employee, how='left', on='employee_id')

  # group by 'project_id' and find the mean of the 'experience_years'
  result = df.groupby('project_id')['experience_years'].mean().round(2).rename('average_years').reset_index()

  return result

