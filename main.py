# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.e_configuration import get_electron_configuration, print_e_configuration, generate_terms, generate_general_term


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_number():
    print("Введите целое число больше нуля")
    try:
        a = int(input())
        if a <= 0:
            return get_number()
        else:
            return a
    except ValueError:
        return get_number()


if __name__ == '__main__':
    current_cap, s, conf = get_electron_configuration(get_number())
    print_e_configuration(conf, s)
    terms = generate_terms(s, conf[-1][1])
    generate_general_term(terms)
    # a, b, c = get_electron_configuration(116)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
