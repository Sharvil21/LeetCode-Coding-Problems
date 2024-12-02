#Pandas Solution
#Merge the two tables first using a left join using .merge() method
#Group the df then by customer_id based on the number of unique products they bought. (Designated by the product_key column)
#Then get the total unique products in the products table
#Lastly, compare the two values. We need to get the customer_id where the total_products_bought by each customer id is the same as the total number of unique products in the products df
