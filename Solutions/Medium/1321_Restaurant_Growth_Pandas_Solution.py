#Pandas Solution
#First, create another dataframe which contains the values of total amount spent each day by customers
#Then, we have to create a column that gives the 7 day cumulative sum. We cannot use .cumsum() for this. WE have to use the .rolling() method. IT will have 2 arguments: windows = 7, and min_periods = 7. So that it takes the sum of the last 6 and the present value. And only those values will be considered if it has 7 rows before it
#Same for the average amount, which will be the moving average. We will specify the same arguments. Also need to round the average to 2 decimals
import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    daily_totals = customer.groupby('visited_on',as_index=False)['amount'].sum()
    daily_totals.sort_values('visited_on',inplace=True)
    daily_totals['total_amount'] = daily_totals.amount.rolling(window=7, min_periods=7).sum()
    daily_totals['average_amount'] = daily_totals.amount.rolling(window=7, min_periods=7).mean().round(2)
    return daily_totals.dropna()[['visited_on','total_amount','average_amount']].rename(columns={'total_amount':'amount'})
