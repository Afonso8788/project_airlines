#Identificar o número de tweets por sentimento
def count_tweets_per_sentiment(data):
    counts = {}
    for row in data:
        counts[row['airline_sentiment']] = counts.get(row['airline_sentiment'], 0) + 1
    return counts

#Identificar a percentagem de tweets por sentimento
def calculate_percentual_sentiments(data):
    total = len(data)
    counting = count_tweets_per_sentiment(data)
    return {sentiment: (counting / total) * 100 for sentiment, counting in counting.items()}

#Identificar a companhia aérea com mais tweets positivos
def company_most_positive_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'positive':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return max(counts, key=counts.get)

#Identificar a companhia aérea com menos tweets positivos
def company_least_positive_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'positive':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return min(counts, key=counts.get)

#Identificar a companhia aérea com mais tweets neutros
def company_most_neutral_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'neutral':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return max(counts, key=counts.get)

#Identificar a companhia aérea com menos tweets neutros
def company_least_neutral_tweets(data):
    counts = {}
    for row in data:
        if row['airline_sentiment'] == 'negative':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return min(counts, key=counts.get)

#Identificar o número de retweets por sentimento
def number_retweets_per_sentiments(data):
    counts = {}
    for row in data:
        sentiment = row['airline_sentiment']
        retweets = int(row['retweet_count'])
        counts[sentiment] = max(counts.get(sentiment, 0), retweets)
    return counts

#Identificar a média de retweets por sentimento
def media_retweets_per_sentiments(data):
    total = len(data)
    counting = number_retweets_per_sentiments(data)
    return {sentiment: (counting / total) * 100 for sentiment, counting in counting.items()}

#Identificar as razões negativas
def negative_reasons(data):
    counts = {}
    for row in data:
        reason = row['negativereason']
        if reason:
            counts [reason] = counts.get(reason,0) + 1
    return counts

#Identificar os diferentes dados estatisticos
def tweet_statistics(data):
    lengths = [len(row['text']) for row in data]
    return {
        'min_length': max(lengths),
        'max_length': min(lengths),
        'average_length': sum(lengths)/len(lengths),
        'total_length' : sum(lengths),
        'median_length' : sorted(lengths)[len(lengths) // 2]
    }

#Distribuir sentimentos por companhia
def sentiment_distribution_airline(data):
    counts = {}
    for row in data:
        key = (row['airline'], row['airline_sentiment'])
        counts[key] = counts.get(key, 0) + 1
    return counts

#Identificar os 10 nomes com mais tweets
def top_10_names(data):
    counts = {}
    for row in data:
        counts[row['name']] = counts.get(row['name'], 0) + 1
    return dict(sorted(counts.items(), key=lambda x: -x[1])[:10])

#Identificar as 10 regiões com mais tweets
def top_10_region(data):
    counts = {}
    for row in data:
        counts[row['user_timezone']] = counts.get(row['user_timezone'], 0) + 1
    return dict(sorted(counts.items(), key=lambda x: -x[1])[:10])

#Identificar as 10 regiões com menos tweets
def least_10_region(data):
    counts = {}
    for row in data:
        counts[row['user_timezone']] = counts.get(row['user_timezone'], 0) + 1
    return dict(sorted(counts.items(), key=lambda x: x[1])[:10])

#Identificar as percentagens das 10 regiões com mais tweets
def calculate_top_10_region(data):
    total = len(data)
    counting = top_10_region(data)
    return {datas: (counting / total) * 100 for datas, counting in counting.items()}

#Identificar as percentagens das 10 regiões com menos tweets
def calculate_least_10_region(data):
    total = len(data)
    counting = least_10_region(data)
    return {datas: (counting / total) * 100 for datas, counting in counting.items()}
def airlines_list(data):
    return list(set(row['airline'] for row in data))

#Identificar a companhia aérea com mais tweets negativos
def company_most_negative_tweets(data):
    counts ={}
    for row in data:
        if row['airline_sentiment'] == 'negative':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return max(counts, key=counts.get)

#Identificar a companhia aérea com menos tweets negativos
def company_least_negative_tweets(data):
    counts ={}
    for row in data:
        if row['airline_sentiment'] == 'negative':
            counts[row['airline']] = counts.get(row['airline'], 0) + 1
    return min(counts, key=counts.get)

#Identificar o número de companhias
def total_companies(data):
    counts = {}
    for row in data:
        counts [row['airline']] = counts.get(row['airline'],0)+1
    return counts

#Identificar o dia com mais tweets
def most_tweets_day(data):
    counts = {}
    for row in data:
        date = row["tweet_created"].split(' ')[0]
        counts[date] = counts.get(date,0) + 1
    return max(counts,key= counts.get)

#Identificar o determinado número de tweets num determinado mês
def tweets_per_month(data , year , month):
    count = 0
    for row in data:
        date = row['tweet_created'].split(' ')[0]
        y, m , _ = map (int , date.split('-'))
        if y == year and m == month :
            count +=1
    return count