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

### Função principal



def main():
    logger = configurate_logs("logs/app.log")
    path = r'C:\Programming\CodePython\Moodles\Tweets.csv'
    data = path_arquive_csv(path)
    if data is None:
        register_error(logger, "Erro ao carregar os dados.")
        return
    register_event(logger, "Dados carregados com sucesso.")
    steps = [
        {"Descrição": "Listar companhias aéreas", "função": airlines_list, "args": [data]},
        {"Descrição": "Empresa com mais tweets negativos", "função": company_most_negative_tweets, "args": [data]},
        {"Descrição": "Empresa com menos tweets negativos", "função": company_least_negative_tweets,
         "args": [data]},
        {"Descrição": "Total de tweets por companhia", "função": total_companies, "args": [data]},
        {"Descrição": "Contagem de tweets por sentimento", "função": count_tweets_per_sentiment, "args": [data]},
        {"Descrição": "Percentual de tweets por sentimento", "função": calculate_percentual_sentiments,
         "args": [data]},
        {"Descrição": "Empresa com mais tweets positivos", "função": company_most_positive_tweets, "args": [data]},
        {"Descrição": "Empresa com menos tweets positivos", "função": company_least_positive_tweets,
         "args": [data]},
        {"Descrição": "Empresa com mais tweets neutros", "função": company_most_neutral_tweets, "args": [data]},
        {"Descrição": "Empresa com menos tweets neutros", "função": company_least_neutral_tweets, "args": [data]},
        {"Descrição": "Número de retweets por sentimento", "função": number_retweets_per_sentiments,
         "args": [data]},
        {"Descrição": "Média de retweets por sentimento", "função": media_retweets_per_sentiments, "args": [data]},
        {"Descrição": "Dia com mais tweets", "função": most_tweets_day, "args": [data]},
        {"Descrição": "Número de tweets em um mês específico", "função": tweets_per_month, "args": [data, 2015, 2]},
        {"Descrição": "Razões negativas dos tweets", "função": negative_reasons, "args": [data]},
        {"Descrição": "Estatísticas dos tweets", "função": tweet_statistics, "args": [data]},
        {"Descrição": "Distribuição de sentimentos por companhia", "função": sentiment_distribution_airline,
         "args": [data]},
        {"Descrição": "Top 10 nomes mais frequentes", "função": top_10_names, "args": [data]},
        {"Descrição": "Top 10 regiões com mais tweets", "função": top_10_region, "args": [data]},
        {"Descrição": "Top 10 regiões com menos tweets", "função": least_10_region, "args": [data]},
        {"Descrição": "Percentagem das 10 regiões mais frequentes", "função": calculate_top_10_region,
         "args": [data]},
        {"Descrição": "Percentagem das 10 regiões menos frequentes", "função": calculate_least_10_region,
         "args": [data]}
    ]
    assert tweets_per_month(data, 2015, 2) == 14640
    assert most_tweets_day (data) == "2015-02-22"
    assert company_most_negative_tweets (data) == "United"
    assert company_least_negative_tweets(data) == "Virgin America"
    assert company_most_neutral_tweets(data) == "Delta"
    assert company_least_neutral_tweets(data) == "Virgin America"
    assert company_most_positive_tweets(data) == "Southwest"
    assert company_least_positive_tweets(data) == "Virgin America"
    for step in steps:
        print(step["Descrição"] + ":")
        print(step["função"](*step["args"]))
    return steps

try:
    if __name__ == "__main__":
        main()
except FileNotFoundError as e:
        print("Erro: Arquivo não encontrado:", e)
except Exception as e:
    print("Erro inesperado:", e)