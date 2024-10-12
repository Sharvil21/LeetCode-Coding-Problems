#Pandas Solution
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId')['id'].count().to_frame('total_reports').reset_index()
    managers = df.loc[df['total_reports']>=5,'managerId']
    return employee.query("id in @managers")['name'].to_frame('name')

#Pandas Solution
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    return employee[ employee.id.isin(employee.groupby('managerId', as_index=0).count().query('id > 4')['managerId']) ][['name']] 
