#Pandas Solution
#Create a new column called rank. Use the groupby() and rank methods to rank the employee and department based on their salary
#Then filter out those rows where the rank value is < 4
#Then select only those rows required in the output
#rename the columns at last and return the output
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department,left_on='departmentId',right_on='id',how='inner')
    df['rank'] = df.groupby(['departmentId','name_y'])['salary'].rank(method='dense',ascending=False)
    return df.loc[df['rank']<4,['name_y','name_x','salary']].rename(columns={'name_x':'Employee','name_y':'Department','salary':'Salary'})
