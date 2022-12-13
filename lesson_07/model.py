import csv
import json
import pandas as pd


def read_db(path='db.json'):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def add_to_db(data, path='db.json'):
    new_data = read_db()
    new_data.append(data)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file)


def import_from_txt(path='txt_base.txt'):
    with open(path) as txt_file:
        lines = txt_file.readlines()
        print(lines)
    data = {}
    for i in range(0, len(lines), 5):
        data['first_name'] = str(lines[i]).replace('\n', '')
        data['last_name'] = str(lines[i + 1]).replace('\n', '')
        data['phone'] = str(lines[i + 2]).replace('\n', '')
        data['comment'] = str(lines[i + 3]).replace('\n', '')
        add_to_db(data)
        data.clear()


def import_from_csv(path='csv_base.csv', base='db.json'):
    with open(path) as csv_file:
        data = {}
        lst = list(csv.DictReader(csv_file))
        for i in lst:
            data['first_name'] = i['first_name']
            data['last_name'] = i['last_name']
            data['phone'] = i['phone']
            data['comment'] = i['comment']
            add_to_db(data)
            data.clear()

    # add_to_db(df.to_json)