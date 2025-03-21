#Pandas Solution
#For first output,merge the users table and movie_rating table on user_id
#Then simply group by the 'name', and find the count of movie_id, reset the index, then sort by the total ratings Descending and the name ascending (so that they are sorted lexicographically)
#Then store the value of the highest movie rater inside a variable using .iloc method
#For second output, merge the movie_rating table with movies table
#Then, use .loc to filter out those rows where the crreated at date is only in feb 2020
#then again use groupby, get the mean of rating, reset the index and sort the values
#Store the movie name in another variable
#Lastly, create a new Dataframe as required in the output and pass the 2 variables as values

import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    df1 = users.merge(movie_rating,on='user_id',how='inner')
    movie_rater = df1.groupby(['name']).agg(total_rating=('movie_id','count')).reset_index().sort_values(['total_rating','name'],ascending=[False,True])['name'].iloc[0]

    df2 = movies.merge(movie_rating,on='movie_id',how='inner') 
    op2 = df2.loc[(df2['created_at'] > pd.to_datetime('2020-01-31')) & (df2['created_at'] < pd.to_datetime('2020-03-01'))].groupby(['movie_id','title']).agg(average_rating=('rating','mean')).reset_index().sort_values(by=['average_rating','title'],ascending=[False,True])
    movie_name = op2.title.iloc[0]
    return pd.DataFrame({'results':[movie_rater,movie_name]})
