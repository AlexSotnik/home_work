import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def card_number():
    return "1234567890123456"


@pytest.fixture()
def account_number():
    return "1234567891236222"


def test_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_mask_card_number_insufficient_quantity():
    assert get_mask_card_number("12345678") is None


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**6222"
