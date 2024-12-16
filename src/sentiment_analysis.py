def count_tweets_per_sentiment(data):
    return data['airline_sentiment'].value_counts().to_dict()
def calculate_percentual_sentiments(data):
    total = len(data)
    counting = count_tweets_per_sentiment(data)
    return {sentiment: (counting / total) * 100 for sentiment, counting in counting.items()}
def company_most_positive_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'positive':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return max(counts, key=counts.get)
def company_least_positive_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'positive':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return min(counts, key=counts.get)
def company_most_neutral_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'neutral':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return max(counts, key=counts.get)
def company_least_neutral_tweets(data):
    neutral = data[data['airline_sentiment'] == 'neutral']
    return neutral['airline'].value_counts().idxmin()
def number_retweets_per_sentiments(data):
    return data.groupby('airline_sentiment')['retweet_count'].max().to_dict()
def media_retweets_per_sentiments(data):
    return data.groupby('airline_sentiment')['retweet_count'].mean().to_dict()
