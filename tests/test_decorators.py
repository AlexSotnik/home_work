import pytest
from src.decorators import log


def test_log_correct(capsys):
    # Проверка корректного выполнения функции
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y


    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function вызывается с помощью аргументов: (1, 2), kwargs:{}. Результат: 3\n" in captured.out


def test_log_different_types_str(capsys):
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y

    try:
        my_function("a", "b")
    except TypeError as e:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
