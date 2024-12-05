#Pandas Solution
#We have to filter out the rows which contain the same number 3 times
#For this, we can use .shift() method

import pandas as pd
import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    return logs.loc[(logs['num']==logs['num'].shift(-1)) & (logs['num'] == logs['num'].shift(-2)),'num'].drop_duplicates(keep='first').to_frame('ConsecutiveNums')
