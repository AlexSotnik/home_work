# Домашнее задание 10.1
## Добавлен модуль processing, в нем две функции filter_by_state, sort_by_date
filter_by_state фильтрует по пункту state, sort_by_date сортирует по дате.
Добавлены тесты для модулей masks, widget, processing

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/AlexSotnik/home_work/pull/2
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте приложение в PyCharm.

## Тестирование

Установить библиотеку

pytest-cov:
```
poetry add --group dev pytest-cov
```
Команды, чтобы запустить тесты с оценкой покрытия:

    pytest --cov — при активированном виртуальном окружении.

    poetry run pytest --cov — через poetry.

    pytest --cov=src --cov-report=html — чтобы сгенерировать отчет о покрытии в HTML-формате, где
    src — пакет c модулями, которые тестируем

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).