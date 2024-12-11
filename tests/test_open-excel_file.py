import pytest
from src.open_excel_file import get_xlsx_data_dict


@pytest.fixture
def get_path():
    return '../data/transactions_excel.xlsx'


@pytest.fixture
def get_bad_file():
    return '../data/no_transactions.xlsx'


def test_open_csv_file_dictionary(get_path):
    assert get_xlsx_data_dict(get_path)[1] == {
        'id': 3598919.0, 'state': 'EXECUTED',
        'date': '2020-12-06T23:00:58Z', 'operationAmount':
            {'amount': 29740.0, 'currency':
                {'name': 'Peso', 'code': 'COP'}
             },
        'description': 'Перевод с карты на карту',
        'from': 'Discover 3172601889670065',
        'to': 'Discover 0720428384694643'
    }


def test_get_transactions_dictionary(get_bad_file):
    assert get_xlsx_data_dict(get_bad_file) == [{}]
