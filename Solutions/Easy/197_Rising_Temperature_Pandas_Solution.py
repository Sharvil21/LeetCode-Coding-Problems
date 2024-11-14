#Pandas Solution
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate',inplace=True)
    weather['previous_temperature'] = weather['temperature'].shift(1)
    return weather.query("temperature > previous_temperature").reset_index()[['id']]
