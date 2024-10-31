#Pandas Solution
import pandas as pd
import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.loc[users['email'].str.contains('^[A-Za-z0-9_]*@[A-Za-z]*.com')]
