#Pandas Solution
import pandas as pd

    return weather.query("temperature > previous_temperature").reset_index()[['id']]
