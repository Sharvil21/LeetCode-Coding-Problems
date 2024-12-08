#Pandas Solution
#First, sort the values by product_id and change_date ascending. This will ensure that all testcases will pass with ease
#Then, get only those rows for product_id where the change date is <= 2019-08-16
#Drop the duplicates and keep only the last value.
#Create another dataframe from the original (sorted one obviously) and drop the duplicates. This is for the test cases where the product_id change_date is always graeter than 2019-08-16.
#Do a Left JOIN with the first data frame and the second one on product_id
#The changed_price will be NaN for the dates which don't exist before the required date
#use the .fillna() method to fill those NaN values as 10.
#Return the desired columns after renaming them
import pandas as pd
