#Pandas Solution using .diff() method. First sort the dataframe by machine_id, process_id then the timestamp. Then group by machine_id and process_id, and use the .diff() method on the timestamp values to get the difference. Then drop the na values in place. Then lastly, group by again by the machine_id and get the mean.
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=['machine_id','process_id','timestamp'],inplace=True)
    activity['processing_time'] = activity.groupby(['machine_id','process_id'])['timestamp'].diff()
    df = activity[['machine_id','processing_time']]
    df.dropna(inplace=True)
    return df.groupby('machine_id')['processing_time'].mean().round(3).reset_index()
