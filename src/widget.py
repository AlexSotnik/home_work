def mask_account_card(card_number: str) -> str:
    """Возвращает тип карты или счет, и замаскированный номер"""
    if "Счет" in card_number:
        number = f" **{card_number[-4:]}"
        type_card = "Счет"
    else:
        number = f"{card_number[-16:-12]} {card_number[-12:-10]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
        type_card = f"{card_number[0:len(card_number)-16]}"
    return f"{type_card}{number}"


def get_date(date_time: str) -> str:
    """Возвращает дату ДД.ММ.ГГ"""
    return f"{date_time[8:10]}.{date_time[5:7]}.{date_time[0:4]}"


# print(mask_account_card("Счет 12345678901234567890"))
# print(get_data("2018-07-11T02:26:18.671407"))
