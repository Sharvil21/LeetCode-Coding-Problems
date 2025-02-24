#Solution using .pivot() method of Pandas
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month',columns='city',values='temperature')
