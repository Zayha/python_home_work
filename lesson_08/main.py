import data_processing
from view_mod import show_menu as sm
import controller


def main():
    data_processing.check_on_start()
    flag = '*'
    while flag == '*':
        sm()
        flag = controller.controller(input("Select menu number: "))


if __name__ == '__main__':
    main()
