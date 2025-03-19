#Pandas Solution
#Simple Approach:
#Drop the duplicates first. This will remove all the numbers which don't appear once. Remember to have the argument keep = False.
# Then get the max value of the resulting dataset and return it
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    return my_numbers.drop_duplicates(keep=False).max().to_frame('num')
