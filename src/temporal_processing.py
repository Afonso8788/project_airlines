def most_tweets_day(data):
    counts = {}
    for row in data:
        date = row["tweet_created"].split('')[0]
        counts[date] = counts.get (date,0) + 1
        return max(counts,key= counts.get)
def tweets_per_month(data , year , month):
    count = 0
    for row in data:
        date = row['tweet_created'].split('')[0]
        y, m , _ = map (int , date.split('-'))
        if y == year and m == month :
            count +=1
    return count

