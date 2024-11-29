#Pandas Solution 
#First Join the two tables usiong .merge()
#Sort the values just in case
#Then create a column called rnk. The logic here is to rank the rows partitioned by each product_id for every year. Dense rank will be used, and the first year be will ranked 1.
#Then filter out those rows only where the rnk value is 1
#Finally return the desired columns, don't forget to rename them
