import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    filemode="w",
                    )
logger = logging.getLogger('masks')


def get_mask_card_number(card_number: str) -> str | None:
    """Возвращает маcкированный номер карты клиента"""
    if card_number.isdigit() and len(card_number) == 16:
        logger.info(f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}")
        return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return None


def get_mask_account(account_number: str) -> str | None:
    """Возвращает маcкированный номер счета клиента"""
    logger.info(f"**{account_number[-4:]}")
    return f"**{account_number[-4:]}"


print(get_mask_card_number("1234567890123455"))
print(get_mask_account("1234567891236222"))
