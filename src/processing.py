start_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(orig_list: list, state: str) -> list:
    """Возвращает тот или иной словаль в зависимости от статуса 'state'"""
    new_list_executed = []
    for i in orig_list:
        if i.get("state") == state:
            new_list_executed.append(i)
    return new_list_executed


def sort_by_date(sorsed_of_date: list, revers: bool = True) -> list:
    """Сортирует словарь по датам"""
    new_list = sorted(sorsed_of_date, key=lambda d: d.get("date"), reverse=revers)
    return new_list


# print(filter_by_state(start_list))
# print(sort_by_date(start_list))
