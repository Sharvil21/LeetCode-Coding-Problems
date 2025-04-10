#Pandas Solution
#First Sort the values by player_id and the event_date just for precaution
#Then create a new column which shows the immediate next login date for each player. Can be done using .shift() method and group by each player_id
#Then create another column which shows the difference between the next login date and the actual event date
#Drop the duplicate values. There will be testcases where the difference will be 1 for same player id. So keep='first' in the drop_duplicates() method
#Then count the number of rows in the resulting df, and then count unique players. Then get the ratio
#return the output as a dataframe
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['player_id','event_date'],inplace=True)
    activity['next_login_date'] = activity.groupby('player_id')['event_date'].shift(-1)
    activity['date_diff'] = (activity['next_login_date'] - activity['event_date']).dt.days
    activity.drop_duplicates(subset=['player_id'],keep='first',inplace=True)
    value = len(activity[activity['date_diff']==1])/activity['player_id'].nunique()
    return pd.DataFrame({'fraction':[value]}).round(2)
#
