#Pandas Solution using .merge(). Basically do a LEFT JOIN, then group by user_id and name, then take the sum. Rename the columns. Then sort by the 2 values
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(rides,left_on='id',right_on='user_id',how='left').fillna(0)
    df2 = df.groupby(['user_id','name'])['distance'].sum().reset_index()
    return df2[['name','distance']].rename(columns={'distance':'travelled_distance'}).sort_values(['travelled_distance','name'],ascending=[False,True])

#Another Pandas Solution
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    
    df = rides.groupby( ['user_id'])['distance'].sum().reset_index(name='travelled_distance' )

    df = pd.merge( users, df, how='left', left_on='id', right_on='user_id')

    df['travelled_distance'] = df['travelled_distance'].fillna(0)

    df.sort_values( by=['travelled_distance','name'], ascending=[False,True], inplace=True )

    return df[['name','travelled_distance']]
