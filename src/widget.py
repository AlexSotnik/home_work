def mask_account_card(card_number: str) -> str:
    """Возвращает тип карты или счет, и замаскированный номер"""
    if card_number in "Счет":
        number = f"**{card_number[-4:]}"
        type_card = "Счет"
    else:
        number = f"{card_number[-16:-13]} {card_number[-12:-10]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
        type_card = f"{card_number[0:len(card_number)-16]}"
    return f"{type_card}  {number}"

def get_data(date_time: str) -> str:
    """Возвращает дату ДД.ММ.ГГ"""
    return f"{date_time[8:10]}.{date_time[5:7]}.{date_time[0:4]}"

