# Project_airlines

Análise e visualização de tweets sobre companhias aéreas.

---

## Visão Geral

Este projeto permite analisar tweets relacionados a companhias aéreas, fornecendo insights como:
- Sentimentos mais frequentes (positivos, negativos, neutros).
- Companhias com mais reclamações ou elogios.
- Estatísticas detalhadas, como retweets e razões para reclamações.
- Uma lista das companhias aéreas.
- Empresa com mais e menos tweets negativos,positivos e neutros.
- O numero total de tweets por companhia.
- Estatísticas relativamente aos sentimentos.
- Estatíscas relativamente aos tweets numa determinada data.
- Top 10 de regiões e nomes com mais tweets.

---

## Instalação

### Pré-requisitos
Certifique-se de ter pelo menos o **Python 3.8+** instalado.

Clone o repositório:
```bash
git clone https://github.com/ubi-datasciencelabs-students/IACD_Prog_20242025_Grupo9
cd (Um lugar do teu computador à tua escolha)

## Explicações :

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
Para o usuário saber das diferentes companhias disponiveis .
Exemplo de uso : airlines_list(data) "Onde o data é arquivo onde queres verificar as companhias"

company_most_negative_tweets (data)
Objetivo : Procura e coloca a companhia com o numero total de tweets negativos.
Uso :
O usuário saber da companhia com o maior numero de críticas já recebidas .
Exemplo de uso : company_most_negative_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_least_negative_tweets (data)
Objetivo : Procura e coloca a companhia com a menor quantidade de tweets negativos.
Uso :
O usuário saber da companhia com o menor numero de críticas já recebidas .
Exemplo de uso : company_least_negative_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_most_positive_tweets (data)
Objetivo : Procura e coloca a companhia com o numero total de tweets positivos.
Uso :
O usuário saber da companhia com o maior numero de elogios já recebidos .
Exemplo de uso : company_most_positive_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_least_positive_tweets (data)
Objetivo : Procura e coloca a companhia com a menor quantidade de tweets positivos.
Uso :
O usuário saber da companhia com o menor numero de elogios já recebidos .
Exemplo de uso : company_least_positive_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_most_neutral_tweets (data)
Objetivo : Procura e coloca a companhia com o numero total de tweets neutros.
Uso :
O usuário saber da companhia com o maior numero de tweets neutros já recebidos .
Exemplo de uso : company_most_neutral_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

company_least_neutral_tweets (data)
Objetivo : Procura e coloca a companhia com a menor quantidade de tweets neutros.
Uso :
O usuário saber da companhia com o menor numero de tweets neutros já recebidos .
Exemplo de uso : company_least_neutral_tweets (data) "Onde o data é arquivo onde queres verificar as companhias"

most_tweets_day(data)
Objetivo : Procura e coloca o dia com maior numero de tweets.
Uso :
O usuário saber qual é o maior numero de tweets num dia.
Exemplo de uso : most_tweets_day(data) "Onde o data é arquivo onde queres verificar as companhias"

tweets_per_month(data , year , month)

Objetivo : Procura e coloca o numero de tweets num mes e ano dependendo da escolha do usuario.
Uso :
O usuário ver quantos tweets foram dados num determinado mês e ano.
Exemplo de uso : tweets_per_month(data , year , month) "Onde o data é arquivo onde queres verificar as companhias e o year e month são definidos pelo cliente "
