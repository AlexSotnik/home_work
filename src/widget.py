def mask_account_card(card_number: str) -> str:
    """Возвращает тип карты или счет, и замаскированный номер"""
    if card_number in "Счет":
        number = f"**{card_number[-4:]}"
        type_card = "Счет"
    else:
        number = f"{card_number[-16:-13]} {card_number[-12:-10]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
        type_card = f"{card_number[0:len(card_number)-16]}"
    return f"{type_card}  {number}"



