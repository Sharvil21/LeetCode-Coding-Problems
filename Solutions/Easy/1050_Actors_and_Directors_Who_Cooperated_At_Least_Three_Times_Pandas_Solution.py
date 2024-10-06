#Pandas Solution
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id'])['timestamp'].count().to_frame('total_collabs').reset_index()
    return df.loc[df['total_collabs']>2,['actor_id','director_id']]

#Another Pandas Solution
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id','director_id']).agg(cnt=('timestamp','count')).reset_index()
    return df.loc[df['cnt']>2,['actor_id','director_id']]
