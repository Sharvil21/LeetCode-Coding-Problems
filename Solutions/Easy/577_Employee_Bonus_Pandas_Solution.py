#Pandas Solution: 
#Step 1: Merge the tables using a left Join
#Step 2: Filter out the row where bonus is <1000 Or where the bonus column is null
#For null values, we have to use .isna() method, and not '== None' as this won't work
