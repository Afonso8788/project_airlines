from src.data_reading import (path_arquive_csv)
from src.logs import (configurate_logs,
                      register_event,
                      register_error)

from src.airline_analysis import (company_most_negative_tweets,
    company_least_negative_tweets,
    airlines_list,
    total_companies,
    negative_reasons,
    tweet_statistics,
    sentiment_distribution_airline,
    top_10_names,
    top_10_region,
    least_10_region,
    calculate_top_10_region,
    calculate_least_10_region,
    count_tweets_per_sentiment,
    calculate_percentual_sentiments,
    company_most_positive_tweets,
    media_retweets_per_sentiments,
    company_least_positive_tweets,
    number_retweets_per_sentiments,
    company_most_neutral_tweets,
    company_least_neutral_tweets,
    most_tweets_day,
    tweets_per_month)
path = r'C:\Programming\CodePython\Moodles\Tweets.csv'
data = path_arquive_csv(path)

print(tweets_per_month(data, 2015, 2))