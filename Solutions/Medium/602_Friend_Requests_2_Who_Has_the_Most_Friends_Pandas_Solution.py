#Pandas Solution
#Simple approach is to do a 'union' between the requester_id and accepter_id column
#If both values are in a single column, then we can just group by and get the count
#This will directly tell use how many friends each user_id has
#In Pandas, Union can be done by using .concat() method. Here, we are creating a new dataframe with just one column that contains the values in both the columns
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([request_accepted['requester_id'],request_accepted['accepter_id']]).reset_index(drop=True)
    df = pd.DataFrame(df,columns=['user_id'])
    return df.groupby('user_id').agg(total_friends=('user_id','count')).reset_index().sort_values('total_friends',ascending=False)[['user_id','total_friends']].iloc[[0]].rename(columns={'user_id':'id','total_friends':'num'})
