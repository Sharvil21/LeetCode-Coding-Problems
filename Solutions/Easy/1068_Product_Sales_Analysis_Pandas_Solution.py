#Pandas Solution
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df= sales.merge(product,on='product_id',how='inner')
    return df[['product_name','year','price']]

#Another Pandas Solution - 1 liner, beats 99%
import pandas as pd

def sales_analysis(sales: pd.DataFrame, 
                   product: pd.DataFrame) -> pd.DataFrame:

    return pd.merge(sales, product).iloc[:,[5,2,4]]
