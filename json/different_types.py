import json


def process_data(data):
    data_type = type(data)
    if data_type == str:
        return data + '!'
    elif data_type == int:
        return data + 1
    elif data_type == bool:
        return not data
    elif data_type == list:
        return data + data
    elif data_type == dict:
        data.update(newkey=None)
        return data
    else:
        pass

total_list = []


with open('data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for symb in data:
        total_list.append(total_list(symb))

    print(total_list)


