import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
api_key = os.getenv("API_KEY")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)
logger = logging.getLogger("utils")


def open_json_file(my_file: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Принимаю json-файл со сиписком транзакций")
        with open(my_file, "r", encoding="utf-8") as f:
            try:
                logger.info("Файл получен")
                file_operation = json.load(f)
                if file_operation == []:
                    return []
            except json.JSONDecodeError:
                logger.error("Decode error")
                return []
    except FileNotFoundError:
        logger.error("File was not found")
        return []
    return file_operation


def convert_to_rub(transaction_convert: dict) -> Any:
    """Принимает значение в долларах или евро, обращается к внешнему API и возвращает конвертацию в рубли"""
    amount = transaction_convert["amount"]
    currency = transaction_convert["currency"]
    try:
        if currency == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
        elif currency == "EUR":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
            headers = {"apikey": api_key}
            response = requests.get(url, headers=headers)
            json_result = response.json()
            rub_amount = json_result["result"]
            return rub_amount
    except RequestException:
        return 0


def transaction_amount_in_rub(transactions: list, transaction_id: int) -> Any:
    """Принимает транзакцию и возвращает сумму в рублях, если операция не в рублях, конвертирует"""
    logger.info("Получаю сумму транзакции")
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                logger.info(f"Сумма транзакции: {rub_amount}")
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                if rub_amount != 0:
                    logger.info(f"Сумма транзакции: {rub_amount}")
                    return rub_amount
                else:
                    logger.error("Конвертация не может быть выполнена")
                    return "Конвертация не может быть выполнена"
    else:
        logger.info("Транзакция не найдена")
        return "Транзакция не найдена"


if __name__ == "__main__":
    transactions = open_json_file("../data/operations.json")
    print(transaction_amount_in_rub(transactions, 179194306))
