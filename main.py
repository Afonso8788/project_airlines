from src.data_reading import path_arquive_csv
from src.sentiment_analysis import (
    count_tweets_per_sentiment,
    calculate_percentual_sentiments,
    company_most_positive_tweets,
    media_retweets_per_sentiments,
    company_least_positive_tweets,
    number_retweets_per_sentiments,
    company_most_neutral_tweets,
    company_least_neutral_tweets)
from src.logs import configurate_logs, register_event, register_error
from src.tweet_analysis import (airlines_mentioned,
                                negative_reasons,
                                tweet_statistics,
                                sentiment_distribution_airline,
                                top_10_names,
                                top_10_region,
                                least_10_region,
                                calculate_top_10_region,
                                calculate_least_10_region)
from src.airlines_analysis import (company_most_negative_tweets,
    company_least_negative_tweets,
    airlines_list,
    total_companies,
    tweets_per_company)
from src.temporal_processing import (most_tweets_day,
                                     tweets_per_month)

def main():
    logger = configurate_logs("logs/app.log")
    path = r'C:\Programming\CodePython\Moodles\Tweets.csv'
    data = path_arquive_csv(path)
    if data is None:
        register_error(logger, "Erro ao carregar os dados.")
        return
    register_event(logger, "Dados carregados com sucesso.")
    # Listar companhias aéreas
    print("Companhias aéreas disponíveis:")
    print(airlines_list(data))
    # Empresa com mais tweets negativos
    print("Empresa com mais tweets negativos:")
    print(company_most_negative_tweets(data))
    # Empresa com menos tweets negativos
    print("Empresa com menos tweets negativos:")
    print(company_least_negative_tweets(data))
    # Total de companhias e seus tweets
    print("Total de tweets por companhia:")
    print(total_companies(data))
    # Número de tweets de uma companhia específica
    company = "United"
    print(f"Número de tweets da companhia {company}:")
    print(tweets_per_company(data, company))
    # Contagem de tweets por sentimento
    print("Contagem de tweets por sentimento:")
    print(count_tweets_per_sentiment(data))
    # Percentagem de sentimentos
    print("Percentual de tweets por sentimento:")
    print(calculate_percentual_sentiments(data))
    # Empresa com mais tweets positivos
    print("Empresa com mais tweets positivos:")
    print(company_most_positive_tweets(data))
    # Empresa com menos tweets positivos
    print("Empresa com menos tweets positivos:")
    print(company_least_positive_tweets(data))
    # Empresa com mais tweets neutros
    print("Empresa com mais tweets neutros:")
    print(company_most_neutral_tweets(data))
    # Empresa com menos tweets neutros
    print("Empresa com menos tweets neutros:")
    print(company_least_neutral_tweets(data))
    # Número de retweets por sentimento
    print("Número de retweets por sentimento:")
    print(number_retweets_per_sentiments(data))
    # Média de retweets por sentimento
    print("Média de retweets por sentimento:")
    print(media_retweets_per_sentiments(data))
    # Dia com mais tweets
    print("Dia com mais tweets:")
    print(most_tweets_day(data))
    # Número de tweets em um mês específico
    year, month = 2015, 2
    print(f"Número de tweets em {month}/{year}:")
    print(tweets_per_month(data, year, month))
    # Companhias mencionadas
    print("Companhias mencionadas:")
    print(airlines_mentioned(data))
    # Razões negativas dos tweets
    print("Razões negativas dos tweets:")
    print(negative_reasons(data))
    # Estatísticas dos tweets
    print("Estatísticas dos tweets:")
    print(tweet_statistics(data))
    # Distribuição de sentimentos por companhia
    print("Distribuição de sentimentos por companhia:")
    print(sentiment_distribution_airline(data))
    # Top 10 nomes mais frequentes
    print("Top 10 nomes mais frequentes:")
    print(top_10_names(data))
    # Top 10 regiões com mais tweets
    print("Top 10 regiões com mais tweets:")
    print(top_10_region(data))
    # Top 10 regiões com menos tweets
    print("Top 10 regiões com menos tweets")
    print(least_10_region(data))
    # Percentagem das 10 regiões mais frequentes
    print("Percentagem das 10 regiões mais frequentes:")
    print(calculate_top_10_region(data))
    # Percentagem das 10 regiões menos frequentes
    print("Percentagem das 10 regiões menos frequentes")
    print(calculate_least_10_region(data))

if __name__ == "__main__":
    main()