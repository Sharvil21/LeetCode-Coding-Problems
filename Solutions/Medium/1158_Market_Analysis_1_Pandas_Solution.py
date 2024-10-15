#Pandas Solution
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    df1 = users.merge(orders,left_on='user_id',right_on='buyer_id', how='left')
    df1['order_in_2019'] = df1['order_date'].dt.year == 2019
    return df1.groupby(['user_id','join_date']).agg(orders_in_2019=('order_in_2019','sum')).reset_index().rename(columns={'user_id':'buyer_id'})

#2nd Pandas SOlution
