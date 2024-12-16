def airlines_list(data):
    return data['airline'].unique()

def company_most_negative_tweets(data):
    negative = data[data['airline_sentiment'] == 'negative']
    return negative['airline'].value_counts().idxmax()

def company_least_negative_tweets(data):
    negative = data[data['airline_sentiment'] == 'negative']
    return negative['airline'].value_counts().idxmin()

def total_companies(data):
    return data['airline'].value_counts().to_dict()

def tweets_per_company(dataframe, company):
    return dataframe[dataframe['airline'] == company]
