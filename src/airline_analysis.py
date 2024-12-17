def count_tweets_per_sentiment(data):
    counts = {}
    for row in data:
        counts[row['airline_sentiment']] = counts.get(row['airline_sentiment'], 0) + 1
    return counts
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
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'negative':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return min(counts, key=counts.get)
def number_retweets_per_sentiments(data):
    counts = {}
    for row in data:
        sentiment = row['airline_sentiment']
        retweets = int(row['retweet_count'])
        counts[sentiment] = max(counts.get(sentiment, 0), retweets)
    return counts
def media_retweets_per_sentiments(data):
    total = len(data)
    counting = number_retweets_per_sentiments(data)
    return {sentiment: (counting / total) * 100 for sentiment, counting in counting.items()}
import logging
import os
def configurate_logs(arquive_name="app.log"):
    directory_logs = os.path.dirname(arquive_name)
    if directory_logs and not os.path.exists(directory_logs):
        os.makedirs(directory_logs)
    logging.basicConfig(
        filename=arquive_name,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger()
    logger.info("Sistema de logs configurado.")
    return logger
def register_event(logger, message):
    logger.info(message)
def register_error(logger, message):
    logger.error(message)
def negative_reasons(data):
    counts = {}
    for row in data:
        reason = row['negativereason']
        if reason:
            counts [reason] = counts.get(reason,0) + 1
    return counts
def tweet_statistics(data):
    lengths = [len(row['text']) for row in data]
    return {
        'min_length': max(lengths),
        'max_length': min(lengths),
        'average_length': sum(lengths)/len(lengths),
        'total_length' : sum(lengths),
        'median_length' : sorted(lengths)[len(lengths) // 2]
    }
def sentiment_distribution_airline(data):
    counts = {}
    for row in data:
        key = (row['airline'], row['airline_sentiment'])
        counts[key] = counts.get(key, 0) + 1
    return counts
def top_10_names(data):
    counts = {}
    for row in data:
        counts[row['name']] = counts.get(row['name'], 0) + 1
    return dict(sorted(counts.items(), key=lambda x: -x[1])[:10])
def top_10_region(data):
    counts = {}
    for row in data:
        counts[row['user_timezone']] = counts.get(row['user_timezone'], 0) + 1
    return dict(sorted(counts.items(), key=lambda x: -x[1])[:10])
def least_10_region(data):
    counts = {}
    for row in data:
        counts[row['user_timezone']] = counts.get(row['user_timezone'], 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1])[:10])
def calculate_top_10_region(data):
    total = len(data)
    counting = top_10_region(data)
    return {datas: (counting / total) * 100 for datas, counting in counting.items()}
def calculate_least_10_region(data):
    total = len(data)
    counting = least_10_region(data)
    return {datas: (counting / total) * 100 for datas, counting in counting.items()}
def airlines_list(data):
    return list(set(row['airline'] for row in data))

def company_most_negative_tweets(data):
    counts ={}
    for row in data:
        if row['airline_sentiment'] == 'negative':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return max(counts, key=counts.get)

def company_least_negative_tweets(data):
    counts ={}
    for row in data:
        if row['airline_sentiment'] == 'negative':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return min(counts, key=counts.get)

def total_companies(data):
    counts = {}
    for row in data:
        counts[row['airline']] = counts.get(row['airline'],0)+1
    return counts

def most_tweets_day(data):
    counts = {}
    for row in data:
        date = row["tweet_created"].split(' ')[0]
        counts[date] = counts.get(date,0) + 1
    return max(counts,key= counts.get)
def tweets_per_month(data , year , month):
    count = 0
    for row in data:
        date = row['tweet_created'].split(' ')[0]
        y, m , _ = map (int , date.split('-'))
        if y == year and m == month :
            count +=1
    return count