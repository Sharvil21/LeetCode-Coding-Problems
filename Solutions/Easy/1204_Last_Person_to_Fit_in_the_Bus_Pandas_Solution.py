#Pandas Solution
#Create a column which gives the cumulative sum/rolling sum of weight
#We can use the .cumsum() method for this
#Then only get the last row where the cumulative sum <=1000
import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn',inplace=True)
    queue['weight_till_this_turn'] = queue['weight'].cumsum()
    return queue.loc[queue['weight_till_this_turn']<=1000,'person_name'].tail(1).to_frame('person_name')
