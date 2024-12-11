def get_mask_card_number(card_number: str) -> str | None:
    """Возвращает маcкированный номер карты клиента"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return None


def get_mask_account(account_number: str) -> str | None:
    """Возвращает маcкированный номер счета клиента"""

    return f"**{account_number[-4:]}"


print(get_mask_card_number("123456789012345"))
print(get_mask_account("1234567891236222"))
