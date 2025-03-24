#Pandas Solution
#First, merge the two tables
#Then, I preferred to create a new column tat shows the Month and Year only for the order date of that row
#Then filter out only those rows which are in Feb 2020
#All that's left is to group by, then take the sum and use the .loc[] to return the required columns
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = products.merge(orders,on='product_id',how='inner')
    df['month_year'] = df['order_date'].dt.strftime("%Y-%m")
    df2 = df.loc[df['month_year'] == "2020-02"].groupby(['product_id','product_name'],as_index=False).agg(unit=('unit','sum'))
    return df2.loc[df2['unit']>=100,['product_name','unit']]
