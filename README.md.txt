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