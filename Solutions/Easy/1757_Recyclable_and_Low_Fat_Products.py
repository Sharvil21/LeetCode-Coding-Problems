#First Solution
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.query("low_fats == 'Y' and recyclable == 'Y'")['product_id'].to_frame()

#Second Solution
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    #df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    #return df[['product_id']]
    return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'),['product_id']]
