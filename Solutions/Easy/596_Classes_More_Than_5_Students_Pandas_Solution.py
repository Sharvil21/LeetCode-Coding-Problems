#Pandas Solution
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().to_frame('Total_Students').reset_index()
    return df.query("Total_Students >= 5")[['class']]

#Another Pandas Solution
import pandas as pd
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().to_frame('Total Students').reset_index()
    return df.loc[df['Total Students']>= 5,['class']]
