#Pandas Solution
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df= sales.merge(product,on='product_id',how='inner')
    return df[['product_name','year','price']]

#Another Pandas Solution, 1 Line & beats 99%
import pandas as pd

def sales_analysis(sales: pd.DataFrame, 
                   product: pd.DataFrame) -> pd.DataFrame:

    return pd.merge(sales, product).iloc[:,[5,2,4]]

#3rd Pandas Solution - Straightforward merge, then select the 3 columns directly
