from model import *
from view_mod import show_menu as sm
from view_mod import show_base as sb
from data_processing import *
from controller import *


def main():
    # sm()
    # sb(read_db())
    # add_to_db(get_data_from_console())
    flag = '*'
    while flag == '*':
        sm()
        flag = controller(input("Select menu number: "))


if __name__ == '__main__':
    main()
