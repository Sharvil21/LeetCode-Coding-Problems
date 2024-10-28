#Pandas Solution using .groupby() method
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df2 = person.groupby(by='email')['email'].count().to_frame('cnt')
    df3 = df2.loc[df2['cnt']>1].reset_index().rename(columns={'email':'Email'})
    return df3[['Email']]


#Another Pandas Solution using  using value_counts() method
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person['email'].value_counts().reset_index().rename(columns={'email':'Email'})
    return df.loc[df['count']>1,'Email'].to_frame()
