#Solution
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
     return views.query("author_id == viewer_id")['author_id'].sort_values().drop_duplicates().to_frame().rename(columns={'author_id':'id'})
