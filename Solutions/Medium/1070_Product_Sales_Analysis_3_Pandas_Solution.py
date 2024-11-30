#Pandas Solution 
#First Join the two tables usiong .merge()
#Sort the values just in case
#Then create a column called rnk. The logic here is to rank the rows partitioned by each product_id for every year. Dense rank will be used, and the first year be will ranked 1.
#Then filter out those rows only where the rnk value is 1
#Finally return the desired columns, don't forget to rename them
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product,on='product_id',how='inner')
    df.sort_values(by=['product_id','year'],inplace=True)
    df['rnk'] = df.groupby('product_id')['year'].rank(method='dense',ascending=True)
    return df.loc[df['rnk']==1,['product_id','year','quantity','price']].rename(columns={'year':'first_year'})

#Another Pandas Solution
#This time, we use .transform() method 
#Merge the two dataframes first.
