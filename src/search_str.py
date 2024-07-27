import re
from typing import Dict, List


def search_by_string(dictionaries: List[Dict], user_string: str) -> List[Dict]:
    """Принимеает список словарей и строку поиска, возвращает список словарей, у которых в описании есть эта строка"""
    new_dict_list = []
    for dictionary in dictionaries:
        text = dictionary["description"]
        needed = re.findall(user_string, text, flags=re.IGNORECASE)
        if needed:
            new_dict_list.append(dictionary)
    return new_dict_list
