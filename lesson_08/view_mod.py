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
        print(f'Record number in DB: {counter}')
        for k in i:
            print(f'{k}: {i[k]}')
        print("*" * 20)
        counter += 1
