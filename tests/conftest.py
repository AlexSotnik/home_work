import pytest
from src.processing import filter_by_state, sort_by_date, start_list
from src.generators import transactions


@pytest.fixture
def test_transactions():
    return transactions

@pytest.fixture
def test_start_list():
    return [start_list, "EXECUTED"]


@pytest.fixture
def an_empty_dictionary():
    return 'nothing'