#Pandas Solution
#First, get the min order date. In Pandas, .transform('min') will have to be used so that we get first_order_date in all rows of the dataframe
#Then create another columns called condition_satisfied. Assign them values of 1 or 0 based on whether first_order_date is the same as the customer_pref_delivery_date
#NOw all we have to do is get the sum of the condition_satisfied column and the number of unique customers using .nunique() method
#Lastly, we have to create a dataframe so as to return the output
