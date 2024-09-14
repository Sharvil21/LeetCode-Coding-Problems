#Solution
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['tweet_length'] = tweets['content'].str.len()
    return tweets.query("tweet_length > 15")['tweet_id'].to_frame()
