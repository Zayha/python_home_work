import csv
import json
from prettytable import PrettyTable


def read_db(path='db.json'):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def add_to_db(data, path='db.json'):
    new_data = read_db()
    new_data.append(data)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file)


def del_from_db(uid, path='db.json'):
    uid = int(uid)
    data = read_db()
    counter = 0
    del_position = len(data) + 1
    for i in data:
        if i['uid'] == uid:
            del_position = counter
        counter += 1
    try:
        data.pop(del_position)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file)
        return f'Сотрудник с ID = {uid} удален из базы данных'
    except IndexError:
        return f'Сотрудник с ID = {uid} в базе не найден'



