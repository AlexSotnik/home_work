import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.fixture()
def card_number():
    return "1234567890123456"


@pytest.fixture()
def account_number():
    return "1234567891236222"


def test_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_mask_card_number_insufficient_quantity():
    assert get_mask_card_number("12435678765") == None


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**6222"
