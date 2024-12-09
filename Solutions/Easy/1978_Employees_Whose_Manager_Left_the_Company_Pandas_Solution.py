#Pandas Solution
#Logic is that we need to find the manager_id which does not exist in the employee_id column
#We can use .loc[] and .isin() method to make it work
#So basically, we filter out saying give us the rows where manager_id is not in employee_id column and also the manager_id is not null and also where the salary is <30000
