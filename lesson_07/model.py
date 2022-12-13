import json


def read_db(path='db.json'):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def add_to_db(data, path='db.json'):
    new_data = read_db()
    new_data.append(data)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file)
