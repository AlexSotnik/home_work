from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    и выводит результат в файл или консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = (
                    f"{func.__name__} вызывается с помощью аргументов: {args}, kwargs:{kwargs}. Результат: {result}"
                )
            except Exception as e:
                log_message = f"{func.__name__} ошибка {e}. Входящие:{args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
                    print(log_message)
            else:
                print(log_message)

        return wrapper

    return decorator


@log(filename="test_log.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
