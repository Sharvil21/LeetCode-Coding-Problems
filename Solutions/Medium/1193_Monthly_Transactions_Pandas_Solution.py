#Pandas Solution
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.year.astype(str) + '-' + transactions['trans_date'].dt.month.astype(str).str.zfill(2)
    
    transactions['approved_total_count'] = transactions['state'].apply(lambda x:1 if x == 'approved' else 0)
    transactions['approved_total_amount'] = transactions.apply(lambda x:x['amount'] if x['state'] == 'approved' else 0,axis = 1)
    return transactions.groupby(['month','country'],dropna=False).agg(trans_count=('id','count'),approved_count=('approved_total_count','sum'),trans_total_amount=('amount','sum'),approved_total_amount=('approved_total_amount','sum')).reset_index()

#Another Pandas Solution
#This time, using .dt.strftime("%Y-%m") to get the month column 
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime("%Y-%m")
    transactions['approved_total_count'] = transactions['state'].apply(lambda x:1 if x == 'approved' else 0)
    transactions['approved_total_amount'] = transactions.apply(lambda x:x['amount'] if x['state'] == 'approved' else 0,axis = 1)
    return transactions.groupby(['month','country'],dropna=False).agg(trans_count=('id','count'),approved_count=('approved_total_count','sum'),trans_total_amount=('amount','sum'),approved_total_amount=('approved_total_amount','sum')).reset_index()


#Third Pandas Solution using numpy np.where
import pandas as pd
import numpy as np

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['approved'] = np.where(transactions['state'] == 'approved', transactions['amount'], np.nan)
    transactions['month'] = transactions['trans_date'].dt.strftime("%Y-%m")
    return transactions.groupby(['month', 'country']).agg(
        trans_count=('state', 'count'),
        approved_count=('approved', 'count'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('approved', 'sum')
    ).reset_index()
    
