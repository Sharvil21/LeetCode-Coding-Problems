#Pandas Solution
#First, get the min order date. In Pandas, .transform('min') will have to be used so that we get first_order_date in all rows of the dataframe
#Then create another columns called condition_satisfied. Assign them values of 1 or 0 based on whether first_order_date is the same as the customer_pref_delivery_date
#NOw all we have to do is get the sum of the condition_satisfied column and the number of unique customers using .nunique() method
#Lastly, we have to create a dataframe so as to return the output
#Since we're passing only scalar value in the dataframe we have to specify the index

import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['first_order_date'] = delivery.groupby('customer_id')['order_date'].transform('min')
    delivery['condition_satisfied'] = delivery.apply(lambda x:1 if x['customer_pref_delivery_date'] == x['first_order_date'] else 0, axis = 1)
    value = (delivery['condition_satisfied'].sum())/(delivery['customer_id'].nunique())
    return pd.DataFrame({'immediate_percentage':100*value},index=[0]).round(2)

#
