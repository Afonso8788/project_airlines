import csv
import pandas as pd
def path_arquive_csv(path_arquive, use_pandas=True):
    try:
        if use_pandas:
            data = pd.read_csv(path_arquive)
            print(f"Arquivo '{path_arquive}' carregado com sucesso usando pandas!")
            return data
        else:
            with open(path_arquive, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            print(f"Arquivo '{path_arquive}' carregado com sucesso usando csv!")
            return data
    except FileNotFoundError:
        print(f"Erro: Arquivo '{path_arquive}' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
    return None
path = r'C:\Programming\CodePython\Moodles\Tweets.csv'
datas = path_arquive_csv(path, use_pandas=True)
if datas is not None:
    if isinstance(datas, pd.DataFrame):
        print(datas.head())
    else:
        print(datas[:5])