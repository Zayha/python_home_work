from data_processing import get_data_from_console, back_new_id, export_to_json_file, export_to_csv
# from export_data import export_to_csv, export_to_txt
from model import read_db, add_to_db, del_from_db
from view_mod import show_base as sb, show_person, show_employees_position, show_employees_by_salary


def controller(number):
    match number:
        case '0':
            sb(read_db())
            return "*"
        case '1':
            print(show_employees_position())
            return "*"
        case '2':
            mies = int(input("Укажите минимальную зарплату: "))
            maes = int(input("Укажите максимальную зарплату: "))
            show_employees_by_salary(mies, maes)
            return "*"
        case '3':
            add_to_db(get_data_from_console())
            return "*"
        case '4':
            del_id = input("Укажите ID сотрудника, запись которого необходимо удалить из базы: ")
            print(del_from_db(del_id))
            return "*"
        case '5':
            edit_id = input("Укажите ID сотрудника, запись которого необходимо изменить в базе: ")
            show_person(edit_id)
            del_from_db(edit_id)
            add_to_db(get_data_from_console('e', edit_id))
            print(f'Запись сотрудника с ID {edit_id} изменена!')
            return "*"
        case '6':
            print(export_to_json_file())
            return "*"
        case '7':
            print(export_to_csv())
            return "*"
        case '8':
            return "-"
