# Project_airlines

Análise e visualização de tweets sobre companhias aéreas.

---

## Visão Geral

Este projeto permite analisar tweets relacionados a companhias aéreas, fornecendo insights como:
- Sentimentos mais frequentes (positivos, negativos, neutros).
- Companhias com mais reclamações ou elogios.
- Estatísticas detalhadas, como retweets e razões para reclamações.
- Uma lista das companhias aéreas.
- Empresa com mais e menos tweets negativos, positivos e neutros.
- O numero total de tweets por companhia.
- Estatísticas relativamente aos sentimentos.
- Estatísticas relativamente aos tweets numa determinada data.
- Top 10 de regiões e nomes com mais tweets.

---

## Instalação

### Pré-requisitos
Certifique-se de ter pelo menos o **Python 3.8+** instalado.

Clone o repositório:
```bash
git clone https://github.com/ubi-datasciencelabs-students/IACD_Prog_20242025_Grupo9
cd (Um lugar do teu computador à tua escolha)

## Explicações das funções :

path_arquive_csv(path)

Objetivo: Carrega os dados de um arquivo CSV no caminho especificado (path).
Uso:
Recebe o caminho do arquivo como argumento e retorna os dados carregados como uma lista de dicionários. Cada dicionário representa um tweet.

configurate_logs(log_file)

Objetivo: Configura o sistema de logs.
Uso:
Recebe um caminho de arquivo (log_file) onde os logs serão gravados. O arquivo de log registra tanto eventos quanto erros.
Exemplo de uso: configurate_logs("logs/app.log").

register_event(logger, message)

Objetivo: Registra um evento no arquivo de log.
Uso:
Recebe o objeto logger (gerado pela função configurate_logs) e uma mensagem (message) descrevendo o evento.
Exemplo de uso: register_event(logger, "Dados carregados com sucesso.").

register_error(logger, message)

Objetivo: Registra um erro no arquivo de log.
Uso:
Recebe o objeto logger e uma mensagem (message) descrevendo o erro.
Exemplo de uso: register_error(logger, "Erro ao carregar os dados.").

airlines_list (data)
Objetivo : Procura e coloca os diferentes nomes das diferentes companhias.
Uso :
Para o usuário saber das diferentes companhias disponíveis .
Exemplo de uso : airlines_list(data) "Onde o data é arquivo onde queres verificar as companhias"

company_most_negative_tweets (data)
Objetivo : Procura e coloca a companhia com o numero total de tweets negativos.
Uso :
O utilizador saber da companhia com o maior numero de críticas já recebidas .
Exemplo de uso : company_most_negative_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_least_negative_tweets (data)
Objetivo : Procura e coloca a companhia com a menor quantidade de tweets negativos.
Uso :
O utilizador saber da companhia com o menor numero de críticas já recebidas .
Exemplo de uso : company_least_negative_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_most_positive_tweets (data)
Objetivo : Procura e coloca a companhia com o numero total de tweets positivos.
Uso :
O utilizador saber da companhia com o maior numero de elogios já recebidos .
Exemplo de uso : company_most_positive_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_least_positive_tweets (data)
Objetivo : Procura e coloca a companhia com a menor quantidade de tweets positivos.
Uso :
O utilizador saber da companhia com o menor numero de elogios já recebidos .
Exemplo de uso : company_least_positive_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_most_neutral_tweets (data)
Objetivo : Procura e coloca a companhia com o numero total de tweets neutros.
Uso :
O utilizador saber da companhia com o maior numero de tweets neutros já recebidos .
Exemplo de uso : company_most_neutral_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_least_neutral_tweets (data)
Objetivo : Procura e coloca a companhia com a menor quantidade de tweets neutros.
Uso :
O utilizador saber da companhia com o menor numero de tweets neutros já recebidos .
Exemplo de uso : company_least_neutral_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

most_tweets_day(data)
Objetivo : Procura e coloca o dia com maior numero de tweets.
Uso :
O usuário saber qual é o maior numero de tweets num dia.
Exemplo de uso : most_tweets_day(data) "Onde o data é arquivo onde queres verificar as companhias"

tweets_per_month(data , year , month)

Objetivo : Procura e coloca o numero de tweets num mes e ano dependendo da escolha do usuário.
Uso :
O utilizador ver quantos tweets foram dados num determinado mês e ano.
Exemplo de uso : tweets_per_month(data , year , month) "Onde o data é arquivo onde queres verificar as companhias e o year e month são definidos pelo cliente "

tweet_statistics(data)

Objetivo : Colocar os diferentes dados estatísticos sobre os tweets.
Uso :
O utilizador saber sobre as estatisticas como o maior e menor comprimentos , média , mediana e total .
Exemplo de uso : tweet_statistics(data) "Onde o data é arquivo onde queres verificar as companhias"

sentiment_distribution_airline (data)

Objetivo : Avaliar os sentimentos por companhia.
Uso :
O utilizador saber sobre a avaliação de outros usuários sobre os sentimentos por companhia.
Exemplo de uso : sentiment_distribution_airline(data) "Onde o data é arquivo onde queres verificar as companhias"

count_tweets_per_sentiment(data)

Objetivo : Avaliar os sentimentos.
Uso :
O utilizador saber sobre a avaliação de outros utilizadores sobre os sentimentos.
Exemplo de uso : count_tweets_per_sentiment(data) "Onde o data é arquivo onde queres verificar as companhias"

calculate_percentual_sentiments(data)

Objetivo : Avaliar os sentimentos por pecentagens.
Uso :
O utilizador saber através do count_tweets_per_sentiment sobre a percentagem da avaliação de outros utilizadores sobre os sentimentos.
Exemplo de uso : calculate_percentual_sentiments(data) "Onde o data é arquivo onde queres verificar as companhias"

top_10_names(data)

Objetivo : Buscar os 10 usuários com mais tweets.
Uso :
O utilizador ver através quem o nome dos usuários com mais tweets .
Exemplo de uso : top_10_names(data) "Onde o data é arquivo onde queres verificar as companhias"

top_10_region (data)

Objetivo : Buscar as 10 regiões com mais tweets.
Uso :
O utilizador saber quais são as regiões pelo mundo que mais comentam.
Exemplo de uso : top_10_region(data) "Onde o data é arquivo onde queres verificar as companhias"

least_10_region (data)

Objetivo : Buscar as 10 regiões com menos tweets.
Uso :
O utilizador saber quais são as regiões pelo mundo que menos comentam.
Exemplo de uso : least_10_region(data) "Onde o data é arquivo onde queres verificar as companhias"

calculate_top_10_region (data)

Objetivo : Buscar as 10 regiões com mais percentagens de tweets .
Uso :
O utilizador saber através do top_10_region quais são as regiões pelo mundo que mais comentam.
Exemplo de uso : top_10_region(data) "Onde o data é arquivo onde queres verificar as companhias"

calculate_least_10_region (data)

Objetivo : Buscar as 10 regiões com menos percentagens de tweets.
Uso :
O utilizador saber através do least_10_region quais são as regiões pelo mundo que menos comentam.
Exemplo de uso : least_10_region(data) "Onde o data é arquivo onde queres verificar as companhias"

negative_reasons(data)

Objetivo : Buscar as criticas relativamente às companhias .
Uso :
O utilizador saber sobre a maior parte das criticas dos populares relativamente às companhias.
Exemplo de uso : negative_reasons(data) "Onde o data é arquivo onde queres verificar as companhias"

number_retweets_per_sentiments(data)

Objetivo : Buscar o numero de retweets por sentimento .
Uso :
O utilizador saber sobre o numero de sentimentos relativamente aos retweets .
Exemplo de uso : number_retweets_per_sentiments(data) "Onde o data é arquivo onde queres verificar as companhias"

media_retweets_per_sentiments(data)

Objetivo : Buscar a percentagem de retweets por sentimento .
Uso :
O utilizador saber através do number_retweets_per_sentiments sobre a percentagem de sentimentos relativamente aos retweets .
Exemplo de uso : media_retweets_per_sentiments(data) "Onde o data é arquivo onde queres verificar as companhias"