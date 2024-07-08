import pytest

from src.processing import filter_by_state, sort_by_date, start_list


@pytest.fixture
def test_start_list():
    return [start_list, "EXECUTED"]


def test_filter_by_state(test_start_list):
    assert filter_by_state(start_list, state=test_start_list)


def test_filter_by_state_1():
    assert filter_by_state(start_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_sort():
    assert sort_by_date(start_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]