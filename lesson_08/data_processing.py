import json
import os.path

import pandas as pd

import model


def get_data_from_console(uid_flag='a', in_uid='*'):
    if uid_flag == 'a' or uid_flag == 'e':
        if uid_flag == 'a':
            uid = back_new_id()
        if uid_flag == 'e':
            uid = int(in_uid)
    else:
        uid = back_new_id()
    fn = input("Enter first name: ")
    ln = input("Enter last name: ")
    ph = input("Enter phone number: ")
    co = input("Enter comment: ")
    bd = input("Date of birth: ")
    wg_min = input('Minimum salary: ')
    wg_max = input("Maximum salary: ")
    ep = input("Employee's position: ")
    return {"uid": uid, "first_name": fn, "last_name": ln, "phone": ph, "comment": co, 'date_of_birth': bd,
            'minimum_income': wg_min, 'maximum_income': wg_max, 'employees_position': ep}


def back_new_id():
    data = model.read_db()
    uid_lst = []
    for i in data:
        uid_lst.append(i['uid'])
    uid_lst_max = max(list(set(uid_lst)))
    return int(uid_lst_max) + 1


def export_to_json_file(path='out/base.json'):
    data = model.read_db()
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    return f'Файл JSON выгружен в {path}'


def export_to_csv(path='db.json', csv_file_name='out/base.csv'):
    pd.set_option('display.max_columns', 50)
    df = pd.read_json(path)
    df.to_csv(csv_file_name)
    return f'Файл CSV выгружен в {csv_file_name}'


def check_on_start():
    dir_path = 'out'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    json_bd_file = 'db.json'
    if os.path.exists(json_bd_file):
        print('Json DB file available')
    else:
        with open(json_bd_file, 'w') as f:
            data = []
            json.dump(data, f)


