from src.e_configuration import get_electron_configuration, print_e_configuration, generate_terms, generate_general_term

symbols = ["H", "He", "Li", "Be", "B",
           "C", "N", "O", "F", "Ne", "Na",
           "Mg", "Al", "Si", "P", "S", "Cl",
           "Ar", "K", "Ca", "Sc", "Ti", "V",
           "Cr", "Mn", "Fe", "Co", "Ni", "Cu",
           "Zn", "Ga", "Ge", "As", "Se", "Br",
           "Kr", "Rb", "Sr", "Y", "Zr", "Nb",
           "Mo", "Tc", "Ru", "Rh", "Pd", "Ag",
           "Cd", "In", "Sn", "Sb", "Te", "I",
           "Xe", "Cs", "Ba", "La", "Ce", "Pr",
           "Nd", "Pm", "Sm", "Eu", "Gd", "Tb",
           "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
           "Hf", "Ta", "W", "Re", "Os", "Ir",
           "Pt", "Au", "Hg", "Tl", "Pb", "Bi",
           "Po", "At", "Rn", "Fr", "Ra", "Ac",
           "Th", "Pa", "U", "Np", "Pu", "Am",
           "Cm", "Bk", "Cf", "Es", "Fm", "Md",
           "No", "Lr", "Rf", "Db", "Sg", "Bh",
           "Hs", "Mt", "Ds", "Rg", "Uub"]


def get_number():
    print("Введите целое число больше нуля или символ:", end=" ")
    input_ = input()
    print()
    try:
        a = int(input_)
        if a <= 0:
            print("Атомное число должно быть больше нуля")
            return get_number()
        else:
            if a == 24 or a == 29:
                print("Конфигурация неправильная, атом является исключением")
            return a
    except ValueError:
        var = input_.lower()
        for i in range(len(symbols)):
            if var == symbols[i].lower():
                if i == 23 or i == 28:
                    print("Конфигурация неправильная, атом является исключением")
                return i + 1
        print("Такого символа не существует")
        return get_number()


if __name__ == '__main__':
    while True:
        current_cap, s, conf = get_electron_configuration(get_number())
        print_e_configuration(conf, s)
        terms = generate_terms(s, conf[-1][1])
        generate_general_term(terms)
