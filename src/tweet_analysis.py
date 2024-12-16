def airlines_mentioned(data):
    return data['airline'].value_counts().to_dict()
def negative_reasons(data):
    return data['negativereason'].value_counts().to_dict()
def tweet_statistics(data):
    tweet_lengths = data['text'].apply(len)
    return {
        'min_length': tweet_lengths.min(),
        'max_length': tweet_lengths.max(),
        'average_length': tweet_lengths.mean(),
        'total_length' : tweet_lengths.sum(),
        'median_length' : tweet_lengths.median()
    }
def sentiment_distribution_airline(data):
    return data.groupby('airline')['airline_sentiment'].value_counts(normalize=True).to_dict()
def top_10_names(data):
    return data['name'].value_counts()[:10].to_dict()
def top_10_region(data):
    return data['user_timezone'].value_counts()[:10].to_dict()
def least_10_region(data):
    return data['user_timezone'].value_counts()[10:].to_dict()
def calculate_top_10_region(data):
    total = len(data)
    counting = top_10_region(data)
    return {datas: (counting / total) * 100 for datas, counting in counting.items()}
def calculate_least_10_region(data):
    total = len(data)
    counting = least_10_region(data)
    return {datas: (counting / total) * 100 for datas, counting in counting.items()}