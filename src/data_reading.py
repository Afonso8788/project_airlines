import csv
import logging
import os

def path_arquive_csv(path_arquive):
        with open(path_arquive, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        print(f"Arquivo '{path_arquive}' carregado com sucesso usando csv!")
        return data

