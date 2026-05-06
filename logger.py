import logging
from datetime import datetime

logging.basicConfig(
    filename='logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

class Logger:
    @staticmethod
    def registrar_info(mensaje):
        logging.info(mensaje)

    @staticmethod
    def registrar_error(mensaje):
        logging.error(mensaje)