#Pandas Solution
#First , create a column called quality that takes the ratio of rating and position
#For Leetcode Testcases, we have to add 1e-10 to the quality column as otherwise the rounding upto 2 digits doesn't work for the given testcases
# Then create another column for poor query percentage by using .apply method and a lambda function
