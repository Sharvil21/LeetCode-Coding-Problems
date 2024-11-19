#Pandas Solution
#Step 1: Merge signups and confirmations on user_id using a left join
#Step 2 : use .fillna(0) method to fill NaN values
#Step 3: Filter only the confirmed messages then group by user_id and then count the occurrences
#Step 4: Group by user_id and count all messages (df_total).
#Step 5: Merge df_total and df_confirmations to combine total and confirmed messages.
#Step 6: Fill NaN values with 0 after merging using .fillna() method again
#Step 7: Rename the columns, calculate the confirmation_rate by creating a new column and taking the division of the two required columns
#Step 8: Return the final DataFrame with user_id and confirmation_rate, then use the .round() function with argument as 2 to round the value to 2 decimal placesimport pandas as pd

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = signups.merge(confirmations,on='user_id',how='left')
    df.fillna(0,inplace=True)
    df_confirmations = df[df['action']=='confirmed'].groupby('user_id')['action'].count().reset_index()
    df_total = df.groupby('user_id')['action'].count().reset_index()
    finaldf= df_total.merge(df_confirmations,on='user_id',how='left').fillna(0).rename(columns={'action_x':'total_messages','action_y':'confirmation_messages'})
    finaldf['confirmation_rate'] =finaldf['confirmation_messages']/finaldf['total_messages']
    return finaldf[['user_id','confirmation_rate']].round(2)


#Another Pandas Solution using lambda function
