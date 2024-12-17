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
def tweets_per_company(data, company):
    return [row for row in data if row['airline'] == company]
