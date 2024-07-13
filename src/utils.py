import json
import os
import requests
from typing import Any
from dotenv import load_dotenv
from requests import RequestException

load_dotenv()
api_key = os.getenv("API_KEY")


def open_json_file(my_file: str) -> Any:
    try:
        with open(my_file, 'r', encoding='utf-8') as f:
            try:
                file_operation = json.load(f)
                if file_operation == []:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return file_operation


def convert_to_rub(transaction_convert: dict) -> Any:
    amount = transaction_convert["amount"]
    currency = transaction_convert["currency"]
    """Принимает значение в долларах или евро, обращается к внешнему API и возвращает конвертацию в рубли"""
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
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                if rub_amount != 0:
                    return rub_amount
                else:
                   return "Конвертация не может быть выполнена"
    else:
        return "Транзакция не найдена"


if __name__ == "__main__":
    transactions = open_json_file("../data/operations.json")
    print(transaction_amount_in_rub(transactions, 179194306))
