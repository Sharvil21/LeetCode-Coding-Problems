#Pandas Solution
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    person.drop_duplicates('email',inplace=True)

#Here, we sort the values first in place, to check for test cases that have disordered ids, then drop the duplicates using the .drop_duplicates() method in-place
