#Pandas Solution
import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].min().to_frame('first_login').reset_index()

#Second Pandas Solution (Using .agg() method)
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id').agg(first_login=('event_date','min')).reset_index()
