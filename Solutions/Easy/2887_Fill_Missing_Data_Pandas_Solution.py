#Pandas Solution
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.loc[products['quantity'].isna(),'quantity'] = 0
    return products


#Another Pandas Solution using .fillna() method
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

