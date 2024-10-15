#Pandas Solution
#Created the dataframe, then created another column that checks if the order date is in 2019 as boolean. Then just need to use .sum() onto that column while grouping by
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df1 = users.merge(orders,left_on='user_id',right_on='buyer_id', how='left')
    df1['order_in_2019'] = df1['order_date'].dt.year == 2019
    return df1.groupby(['user_id','join_date']).agg(orders_in_2019=('order_in_2019','sum')).reset_index().rename(columns={'user_id':'buyer_id'})

#2nd Pandas Solution
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[orders['order_date'].dt.year==2019]
    orders_agg = orders_2019.groupby('buyer_id')['order_id'].size().reset_index(name='orders_in_2019')
    df = users.merge(orders_agg, left_on='user_id', right_on='buyer_id', how='left').fillna(0)
    df.drop(columns=['buyer_id', 'favorite_brand'], inplace=True)
    df.rename(columns={'user_id': 'buyer_id'}, inplace=True)
    return df
