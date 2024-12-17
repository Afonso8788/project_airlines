def airlines_mentioned(data):
    counts = {}
    for row in data:
        counts[row['airline']] = counts.get(row['airline'],0) + 1
        return counts
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