#Pandas Solution
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df1 = product.merge(sales,on='product_id',how='inner')
    unrequired = df1.query("sale_date < '2019-01-01' or sale_date > '2019-03-31'")['product_id']
    return df1.query("product_id not in @unrequired")[['product_id','product_name']].drop_duplicates()

#2nd Pandas Solution
