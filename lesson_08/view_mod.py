from model import read_db

menu = [
    'Найти сотрудника',
    'Выборка сотруднов по должности',
    'Найти сотрудника по зп',
    'Добавить сотрудника',
    'Удалить сотрудника',
    'Обновить данные сотрудника',
    'Экспорт данных в JSON',
    'Экспорт в CSV',
    'Exit'
]


def show_menu(menu=menu):
    for i in range(len(menu)):
        print(f'[{i}] - {menu[i]}')


def show_base(data):
    counter = 0
    for i in data:
        print('-' * 20)
        for k in i:
            print(f'{k}: {i[k]}')
        print("*" * 20)
        counter += 1


def show_person(uid):
    uid = int(uid)
    data = read_db()
    for i in data:
        if i['uid'] == uid:
            for k in i:
                print(f'{k}: {i[k]}')


# 'employees_position': ep}
def show_employees_position():
    data = read_db()
    empl_pos = []
    for i in data:
        empl_pos.append(i['employees_position'])
    empl_pos = list(set(empl_pos))
    for k in empl_pos:
        print(f'Должность: {k}')
        for i in data:
            if i['employees_position'] == k:
                print(f'     Name: {i["first_name"]} {i["last_name"]}, ID: {i["uid"]}')
    return '<<<<<<=========>>>>>>'


def show_employees_by_salary(minimum, maximum):
    data = read_db()
    for i in data:
        if minimum <= int(i['minimum_income']) <= maximum or minimum <= int(i['maximum_income']) <= maximum:
            print(f'     Name: {i["first_name"]} {i["last_name"]}, ID: {i["uid"]}, ZP: {i["minimum_income"]} - '
                  f'{i["maximum_income"]}')