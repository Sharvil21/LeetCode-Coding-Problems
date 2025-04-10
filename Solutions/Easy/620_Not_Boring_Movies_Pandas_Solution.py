#Pandas Solution
# use .query method, and then filter ids where id%2 != 0 and description != boring

import pandas as pd

def not_boring_moveis(cinema: pd.DataFrame) -> pd.DataFrame:
	return cinema.query("id%2 != 0 and description != 'boring'").sort_values(by="rating",ascending = False)

#Another Pandas Solution using str.contains() method

def not_boring_moveis(cinema: pd.DataFrame) -> pd.DataFrame:
	return cinema.query("id%2 != 0 and description.str.contains('boring')").sort_values(by="rating",ascending = False)

