#Pandas Solution
import pandas as pd
def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
	df = employee.groupby('managerId')['id'].count().to_frame('total_reports').reset_index()
