menu = [
    'Show Base',
    'Add an entry to the phone book',
    'Delete a record from the phone book(not ready)',
    'Export DB to CSV',
    'Export DB to txt',
    'Import DB from CSV',
    'Import DB from txt',
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
