import csv
import logging
import os

def path_arquive_csv(path_arquive):
        with open(path_arquive, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        print(f"Arquivo '{path_arquive}' carregado com sucesso usando csv!")
        return data

def configurate_logs(arquive_name="app.log"):
    directory_logs = os.path.dirname(arquive_name)
    if directory_logs and not os.path.exists(directory_logs):
        os.makedirs(directory_logs)
    logging.basicConfig(
        filename=arquive_name,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logger = logging.getLogger()
    logger.info("Sistema de logs configurado.")
    return logger
def register_event(logger, message):
    logger.info(message)
def register_error(logger, message):
    logger.error(message)