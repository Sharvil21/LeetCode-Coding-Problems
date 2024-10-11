#Pandas Solution
import pandas as pd

df = employee.groupby('managerId')['id'].count().to_frame('total_reports').reset_index()
