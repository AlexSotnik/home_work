import os

from typing import Any


def count_file_and_dir(directory: Any) -> Any:
    """Счетчик файлов и директорий в получиной/текущей директории"""
    count = {}
    count_file = 0
    count_dir = 0
    if os.path.isdir(directory) is True:
        for file in os.scandir(directory):
            if file.is_file() is True:
                count_file += 1
            elif file.is_dir() is True:
                count_dir += 1
    else:
        for file in os.scandir("D:/Progekt/home_work/src"):
            if file.is_file() is True:
                count_file += 1
            elif file.is_dir() is True:
                count_dir += 1
    count = {"file": count_file, "folders": count_dir}
    return count


print(count_file_and_dir("D:/Progekt/home_work"))
