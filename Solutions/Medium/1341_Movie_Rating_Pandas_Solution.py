#Pandas Solution
#For first output,merge the users table and movie_rating table on user_id
#Then simply group by the 'name', and find the count of movie_id, reset the index, then sort by the total ratings Descending and the name ascending (so that they are sorted lexicographically)
#Then store the value of the highest movie rater inside a variable using .iloc method
#For second output, merge the movie_rating table with movies table
#Then, use .loc to filter out those rows where the crreated at date is only in feb 2020
