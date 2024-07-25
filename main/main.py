from typing import Any
from src.open_csv_file import get_csv_data_dict
from src.open_excel_file import get_xlsx_data_dict
from src.utils import open_json_file
from src.processing import filter_by_state, sort_by_date

print('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла''')

user_input = input()


while True:
    if user_input == '1':
        print('Для обработки выбран JSON-файл')
        break
    elif user_input == '2':
        print('Для обработки выбран csv-файл')
        break
    elif user_input == '3':
        print('Для обработки выбран excel-файл')
        break
    else:
        print( "Вы не выбрали файл. Выберите необходимый файл: "
        "\n1. Получить информацию о транзакциях из JSON-файла "
        "\n2. Получить информацию о транзакциях из CSV-файла "
        "\n3. Получить информацию о транзакциях из XLSX-файла")
        user_input = input()

def user_input_choice(user_input: str) -> Any:
    if user_input == "1":
        choice = open_json_file("../data/operations.json")
    elif user_input == "2":
        choice = get_csv_data_dict("../data/transactions.csv")
    else:
        choice = get_xlsx_data_dict("../data/transactions_excel.xlsx")

    return choice


open_file = user_input_choice(user_input)

print('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
user_input_2 = input()

while True:
    if user_input_2.upper() == 'EXECUTED':
        print('Операции отфильтрованы по статусу "EXECUTED"')
        break
    elif user_input_2.upper() == 'CANCELED':
        print('Операции отфильтрованы по статусу "CANCELED"')
        break
    elif user_input_2.upper() == 'PENDING':
        print('Операции отфильтрованы по статусу "PENDING"')
        break
    else:
        print(f'Статус операции {user_input_2} недоступен.')
        print('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
        user_input_2 = input()

filter_out = filter_by_state(open_file, user_input_2)

print('''Отсортировать операции по дате? yes/no''')
user_input_3 = input().lower()

print('''Отсортировать по возрастанию или по убыванию? ascending/descending''')
user_input_4 = input()
# while True:
#     if user_input_3 != "yes" and user_input_3 != "no":
#         print('''Отсортировать операции по дате? yes/no''')
#         user_input_3 = input()
#     else:
#         print('''Отсортировать по возрастанию или по убыванию? ascending/descending''')
#         user_input_4 = input()
#         while True:
#             if user_input_4.lower() != "ascending" and user_input_4.lower() != "descending":
#                 print('''Отсортировать по возрастанию или по убыванию? ascending/descending''')
#                 user_input_4 = input()
#             else:
#                 break
#         break

def sort_of_date(user_input_4):
    if user_input_4.lower() == "ascending":
        filter_date = sort_by_date(filter_out)
    elif user_input_4.lower() == "descending":
        filter_date = sort_by_date(filter_out, False)

    return filter_date


filter_out_1 = sort_of_date(user_input_4)
print(filter_out_1)
"""
print('''Выводить только рублевые тразакции? yes/no''')
user_input_5 = input()

while True:
    if user_input_5.lower() != "yes" and user_input_5.lower() != "no":
        print('''Выводить только рублевые тразакции? yes/no''')
        user_input_5 = input()
    elif user_input_5 == "yes":
        filter_RUB =
    else:
        break

"""