#Pandas Solution
#Merge the two tables first using a left join using .merge() method
#Group the df then by customer_id based on the number of unique products they bought. (Designated by the product_key column)
#Then get the total unique products in the products table
#Lastly, compare the two values. We need to get the customer_id where the total_products_bought by each customer id is the same as the total number of unique products in the products df
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = customer.merge(product,on='product_key',how='left')
    df2 = df.groupby('customer_id').agg(total_products_bought=('product_key','nunique')).reset_index()
    return df2.loc[df2['total_products_bought']==product['product_key'].nunique(),'customer_id'].to_frame('customer_id')
