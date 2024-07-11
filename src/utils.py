import json





def open_json_file(my_file: str) -> list:
    try:
        with open(my_file, 'r', encoding='utf-8') as f:
            try:
                file_operation = json.load(f)
                if file_operation == []:
                    return []
            except json.decoder.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return file_operation

# if __name__ == '__main__':
#     my_file = "../data/operations.json"
#     fun = open_json_file(my_file)
#     print(fun)
