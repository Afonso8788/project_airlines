import pandas as pd
def most_tweets_day(dataframe):
    dataframe['tweet_created'] = pd.to_datetime(dataframe['tweet_created'])
    return dataframe['tweet_created'].dt.date.value_counts().idxmax()

def tweets_per_month(dataframe, year, month):
    dataframe['tweet_created'] = pd.to_datetime(dataframe['tweet_created'])
    return dataframe[(dataframe['tweet_created'].dt.year == year) & (dataframe['tweet_created'].dt.month == month)].shape[0]

