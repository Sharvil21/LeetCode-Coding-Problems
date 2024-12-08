#Pandas Solution
#First, sort the values by product_id and change_date ascending. This will ensure that all testcases will pass with ease
#Then, get only those rows for product_id where the change date is <= 2019-08-16
#Drop the duplicates and keep only the last value.
#Create another dataframe from the original (sorted one obviously) and drop the duplicates. This is for the test cases where the product_id change_date is always graeter than 2019-08-16.
import pandas as pd
