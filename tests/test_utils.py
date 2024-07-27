import os
import pytest
from unittest.mock import patch
from src.utils import open_json_file, transaction_amount_in_rub, convert_to_rub
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


@pytest.fixture
def get_path():
    return '../data/operations.json'


@pytest.fixture
def get_wrong_path():
    return 'nothing'


@pytest.fixture
def get_bad_file():
    return '../data/wrong_operations.json'


def test_open_json_file_dictionary(get_path):
    assert open_json_file(get_path)[1] == {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }


def test_open_json_file(get_wrong_path):
    assert open_json_file(get_wrong_path) == []


def test_get_transactions_dictionary(get_bad_file):
    assert open_json_file(get_bad_file) == []


@pytest.fixture
def transactions():
    return open_json_file('../data/operations.json')


@pytest.fixture
def rub_transaction_number():
    return 587085106


def test_transaction_amount_in_rub(transactions, rub_transaction_number):
    assert transaction_amount_in_rub(transactions, rub_transaction_number) == "48223.05"


@patch('requests.get')
def test_convert_to_rub(mock_get):
    headers = {"apikey": api_key}
    mock_get.return_value.json.return_value = ({'result': 60})
    assert convert_to_rub({'amount': '20', 'currency': 'USD'}) == 60
    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=20',
                                     headers=headers)
