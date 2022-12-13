from data_processing import get_data_from_console
from export_data import export_to_csv
from model import read_db, add_to_db
from view_mod import show_base as sb


def controller(number):
    match number:
        case '0':
            sb(read_db())
            return "*"
        case '1':
            add_to_db(get_data_from_console())
            return "*"
        case '2':
            return "*"
        case '3':
            export_to_csv()
            return "*"
        case '4':
            return "*"
        case '5':
            return "*"
        case '6':
            return "*"
        case '7':
            return "-"
