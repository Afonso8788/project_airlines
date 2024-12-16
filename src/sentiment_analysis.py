def count_tweets_per_sentiment(data):
    return data['airline_sentiment'].value_counts().to_dict()
def calculate_percentual_sentiments(data):
    total = len(data)
    counting = count_tweets_per_sentiment(data)
    return {sentiment: (counting / total) * 100 for sentiment, counting in counting.items()}
def company_most_positive_tweets(data):
    positive = data[data['airline_sentiment'] == 'positive']
    return positive['airline'].value_counts().idxmax()
def company_least_positive_tweets(data):
    positive = data[data['airline_sentiment'] == 'positive']
    return positive['airline'].value_counts().idxmin()
def company_most_neutral_tweets(data):
    neutral = data[data['airline_sentiment'] == 'neutral']
    return neutral['airline'].value_counts().idxmax()
def company_least_neutral_tweets(data):
    neutral = data[data['airline_sentiment'] == 'neutral']
    return neutral['airline'].value_counts().idxmin()
def number_retweets_per_sentiments(data):
    return data.groupby('airline_sentiment')['retweet_count'].max().to_dict()
def media_retweets_per_sentiments(data):
    return data.groupby('airline_sentiment')['retweet_count'].mean().to_dict()
