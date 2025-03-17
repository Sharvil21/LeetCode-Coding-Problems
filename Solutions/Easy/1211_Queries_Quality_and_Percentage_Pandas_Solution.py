#Pandas Solution
#First , create a column called quality that takes the ratio of rating and position
#For Leetcode Testcases, we have to add 1e-10 to the quality column as otherwise the rounding upto 2 digits doesn't work for the given testcases
# Then create another column for poor query percentage by using .apply method and a lambda function
#Lastly, group by the query_name, and use .agg method to aggregate the means for the two columns we want.

import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating']/queries['position'] + 1e-10
    queries['poor_quality_percentage'] = queries['rating'].apply(lambda x:100 if x<3 else 0)
    return queries.groupby('query_name').agg(quality=('quality','mean'),poor_query_percentage = ('poor_quality_percentage','mean')).round(2).reset_index()
