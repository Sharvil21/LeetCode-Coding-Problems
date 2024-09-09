#Solution using Pandas
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country = world.query("area >= 3000000 or population >= 25000000")
    return big_country[['name','population','area']]

#Second Solution
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]
