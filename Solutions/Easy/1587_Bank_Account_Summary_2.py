#Solution using pandas .query() method as well as merge() and groupby()
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return (transactions
            .groupby('account')[['amount']].sum()
            .join(users.set_index('account'))
            .query('amount > 10000')
            [['name', 'amount']].rename(columns={'amount': 'balance'}))
