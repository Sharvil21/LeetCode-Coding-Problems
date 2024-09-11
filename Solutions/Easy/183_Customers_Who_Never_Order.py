#Solution:
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders,left_on='id',right_on='customerId',how='left')
    return df.query('id_y.isna()')['name'].to_frame().rename(columns={'name':'Customers'})
