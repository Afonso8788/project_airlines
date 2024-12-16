def most_tweets_day(data):
    counts = {}
    for row in data:
        date = row["tweet created"].split('')[0]
        counts[date] = counts.get (date,0) + 1
        return max(counts,key= counts.get)
