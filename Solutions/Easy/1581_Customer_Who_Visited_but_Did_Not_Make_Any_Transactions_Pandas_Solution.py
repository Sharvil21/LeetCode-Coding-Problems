#Pandas Solution
#Join the two tables using .merge() method first. Then use .groupby() method to group by customer_id, then use .agg() method for convenience. Take the 'count'. rename the columns and return the output.
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions,on='visit_id',how='left')
    op = df.query("transaction_id.isna()").groupby('customer_id').agg(count_no_trans=('customer_id','count'))
    return op.reset_index().sort_values(by='count_no_trans',ascending=False)

#Another Pandas Solution
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    df = visits.merge(transactions, how='left')

    df = df[df['transaction_id'].isna()].groupby(['customer_id'], as_index=False).agg(count_no_trans=('visit_id', 'nunique'))

    return df

#3rd Pandas Solution with detailed
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    #Left joining visits and transactions dataframe on visit_id
    merge_df = pd.merge(visits, transactions, on='visit_id', how='left')
    # filtering only null value columns in merged dataframe
    merge_df = merge_df[merge_df['transaction_id'].isna()]
    # grouping data based on customer-id and count the no of visits, use rest_index() to maintained both grouped data
    merge_df = merge_df.groupby(['customer_id'])['visit_id'].count().reset_index()
    # rename the column visit_id to count_no_trans and return result
    return merge_df.rename({'visit_id':'count_no_trans'},axis = 1) 
