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

# Função para testar a escolha do utilizador
def test_function_choice(code):
    logger = configurate_logs("logs/app.log")
    if code is None:
        register_error(logger, "Erro ao carregar os dados.")
        return
    register_event(logger, "Dados carregados com sucesso.")
    while True:
        print("Escolha uma das opções abaixo para testar:")
        options = [
            "1 - Contar o número de tweets por sentimento",
            "2 - Calcular a percentagem de tweets por sentimento",
            "3 - Companhia aérea com mais tweets positivos",
            "4 - Companhia aérea com menos tweets positivos",
            "5 - Companhia aérea com mais tweets neutros",
            "6 - Companhia aérea com menos tweets neutros",
            "7 - Número de retweets por sentimento",
            "8 - Média de retweets por sentimento",
            "9 - Razões negativas dos tweets",
            "10 - Estatísticas dos tweets",
            "11 - Distribuição de sentimentos por companhia aérea",
            "12 - Top 10 nomes com mais tweets",
            "13 - Top 10 regiões com mais tweets",
            "14 - Top 10 regiões com menos tweets",
            "15 - Percentagens das 10 regiões com mais tweets",
            "16 - Percentagens das 10 regiões com menos tweets",
            "17 - Lista de companhias aéreas",
            "18 - Companhia aérea com mais tweets negativos",
            "19 - Companhia aérea com menos tweets negativos",
            "20 - Número total de companhias aéreas",
            "21 - Dia com mais tweets",
            "22 - Número de tweets em determinado mês",
            "23 - Sair"
        ]

        for option in options:
            print(option)

        choice = int(input("Escolha uma opção (1-23): "))

        if choice == 1:
            print(count_tweets_per_sentiment(data))
        elif choice == 2:
            print(calculate_percentual_sentiments(data))
        elif choice == 3:
            print(company_most_positive_tweets(data))
        elif choice == 4:
            print(company_least_positive_tweets(data))
        elif choice == 5:
            print(company_most_neutral_tweets(data))
        elif choice == 6:
            print(company_least_neutral_tweets(data))
        elif choice == 7:
            print(number_retweets_per_sentiments(data))
        elif choice == 8:
            print(media_retweets_per_sentiments(data))
        elif choice == 9:
            print(negative_reasons(data))
        elif choice == 10:
            print(tweet_statistics(data))
        elif choice == 11:
            print(sentiment_distribution_airline(data))
        elif choice == 12:
            print(top_10_names(data))
        elif choice == 13:
            print(top_10_region(data))
        elif choice == 14:
            print(least_10_region(data))
        elif choice == 15:
            print(calculate_top_10_region(data))
        elif choice == 16:
            print(calculate_least_10_region(data))
        elif choice == 17:
            print(airlines_list(data))
        elif choice == 18:
            print(company_most_negative_tweets(data))
        elif choice == 19:
            print(company_least_negative_tweets(data))
        elif choice == 20:
            print(total_companies(data))
        elif choice == 21:
            print(most_tweets_day(data))
        elif choice == 22:
            year = int(input("Digite o ano: "))
            month = int(input("Digite o mês: "))
            print(tweets_per_month(data, year, month))
        elif choice == 23:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

test_function_choice(data)