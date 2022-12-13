from data_processing import get_data_from_console
from export_data import export_to_csv, export_to_txt
from model import read_db, add_to_db, import_from_csv, import_from_txt
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
            export_to_txt()
            return "*"
        case '5':
            import_from_csv()
            return "*"
        case '6':
            import_from_txt()
            return "*"
        case '7':
            return "-"
