#Pandas Solution
#Join the two tables using .merge() method first. Then use .groupby() method to group by customer_id, then use .agg() method for convenience. Take the 'count'. rename the columns and return the output.
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions,on='visit_id',how='left')
    op = df.query("transaction_id.isna()").groupby('customer_id').agg(count_no_trans=('customer_id','count'))
    return op.reset_index().sort_values(by='count_no_trans',ascending=False)

#
