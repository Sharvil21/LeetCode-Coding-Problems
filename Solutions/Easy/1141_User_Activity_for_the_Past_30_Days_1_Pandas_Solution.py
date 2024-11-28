#Pandas Solution
#Step 1: Get only the rows which staisfy the condition of falling within 30 days of 2019-07-27
#For this, use the pd.to_datetime() function or pd.Timedelta(days=30) methods
#Then group by the activity_date, then get the no. of unique users for each day using .nunique() method
