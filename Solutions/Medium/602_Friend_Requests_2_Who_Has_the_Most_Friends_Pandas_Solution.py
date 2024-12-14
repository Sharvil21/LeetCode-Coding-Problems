#Pandas Solution
#Simple approach is to do a 'union' between the requester_id and accepter_id column
#If both values are in a single column, then we can just group by and get the count
#This will directly tell use how many friends each user_id has
#In Pandas, Union can be done by using .concat() method. Here, we are creating a new dataframe with just one column that contains the values in both the columns
