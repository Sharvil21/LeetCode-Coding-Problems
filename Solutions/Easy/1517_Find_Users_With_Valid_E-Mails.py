#Solution
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.loc[users['mail'].str.match("^[A-Za-z][\w\.\-]*@leetcode\.com$")]


#S
