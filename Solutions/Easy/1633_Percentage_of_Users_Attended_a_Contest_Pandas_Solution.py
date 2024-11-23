#Pandas Solution
#First merge the two dataframes
#Then get the total no. of participants independently in a different variable
#Group the merged DF by contest id and count the total users for each contest
#Create a new column called 'percentage' to get the percentage. The values will be 100* total_registered participants divided by the total participants
#Lastly, use the .round method then also the .sort_values method and return the 2 columns.
import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(register,on='user_id',how='inner')
    total_participants = users['user_id'].nunique()
    df2 = df.groupby('contest_id')['user_id'].count().reset_index().rename(columns={'user_id':'total_registered'})
    df2['percentage'] = 100*df2['total_registered']/total_participants
    return df2[['contest_id','percentage']].round(2).sort_values(by=['percentage','contest_id'],ascending=[False,True])
    
