# https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Finfodoski.ru%2Fimages%2Fdetailed%2F9%2F155__15001000.jpg&f=1&nofb=1
# https://ru.wikipedia.org/wiki/Периодическая_система_химических_элементов
from decimal import Decimal


class Element:
    def __init__(self, number, period, group, name, atomic_mass):  # may be need more
        self.number = number
        self.period = period
        self.group = group
        self.name = name
        self.atomic_mass = atomic_mass

    def __str__(self):
        return "Element: number=" + str(self.number) \
               + ", period=" + str(self.period) \
               + ", group=" + str(self.group) \
               + ", name=" + str(self.name) \
               + ", atomic_mass=" + str(self.atomic_mass)


def fill_data():
    return [Element(1, 1, 7, "Водород", 1.00794),
            Element(39, 5, 3, "Иттрий", 88.906),
            Element(3, 2, 1, "Литий", 6.941),
            Element(5, 2, 3, "Бор", 10.811),
            Element(6, 2, 4, "Углерод", 12.011),
            Element(36, 4, 8, "Криптон", 83.80),
            Element(28, 4, 8, "Никель", 58.70),
            Element(16, 3, 6, "Сера", 32.066),
            Element(14, 3, 4, "Кремний", 28.086),
            Element(25, 4, 7, "Марганец", 54.938),
            Element(49, 5, 3, "Индий", 114.82),
            Element(85, 6, 7, "Астат", 209.99),
            Element(47, 5, 1, "Серебро", 107.868),
            Element(79, 6, 1, "Золото", 196.967),
            Element(50, 5, 4, "Олово", 118.71),
            Element(4, 2, 2, "Берилий", 9.0122)]


def check_input(result):
    if result == "да":
        return True
    elif result == "нет":
        return False
    else:
        exit("ERROR - Введите \'да\' или \'нет\'")


def is_number_even(el):
    if number_is_even:
        if el.number % 2 == 0:
            return True
    elif el.number % 2 != 0:
        return True


def is_period_even(el):
    if period_is_even:
        if el.period % 2 == 0:
            return True
    elif el.period % 2 != 0:
        return True


def is_group_even(el):
    if group_is_even:
        if el.group % 2 == 0:
            return True
    elif el.group % 2 != 0:
        return True


def is_name_longer_4(el):
    if name_longer_4:
        if len(el.name) > 4:
            return True
    elif len(el.name) <= 4:
        return True


def has_atomic_mass_9(el):
    if atomic_mass_has_9:
        if str(el.atomic_mass).__contains__('9'):
            return True
    elif not str(el.atomic_mass).__contains__('9'):
        return True


def is_atomic_mass_longer_decimal_2(el):
    if atomic_mass_longer_decimal_2:
        if len(str(Decimal(str(el.atomic_mass)) % int(el.atomic_mass))) > 4:
            return True
    elif len(str(Decimal(str(el.atomic_mass)) % int(el.atomic_mass))) <= 4:
        return True


def is_atomic_mass_longer_integer_2(el):
    if atomic_mass_longer_integer_2:
        if len(str(int(el.atomic_mass))) > 2:
            return True
    elif len(str(int(el.atomic_mass))) <= 2:
        return True


def has_name_letters(el):
    if name_has_y:
        if str(el.name).__contains__('й') or str(el.name).__contains__('ь'):
            return True
    elif not str(el.name).__contains__('й') and not str(el.name).__contains__('ь'):
        return True


def get_answer():
    for el in elements:
        if has_atomic_mass_9(el) \
                and is_name_longer_4(el) \
                and has_name_letters(el) \
                and is_period_even(el) \
                and is_number_even(el) \
                and is_atomic_mass_longer_decimal_2(el) \
                and is_atomic_mass_longer_integer_2(el) \
                and is_group_even(el):
            print(el)


elements = fill_data()
number_is_even = check_input(input("Порядковый номер четный - "))
period_is_even = check_input(input("Период четный - "))
group_is_even = check_input(input("Группа четная - "))
name_longer_4 = check_input(input("Название элемента длиннее 4 символов (5 и более) - "))
name_has_y = check_input(input("Название элемента имеет букву й или ь - "))
atomic_mass_has_9 = check_input(input("В относительной атомной массе есть 9 - "))
atomic_mass_longer_decimal_2 = check_input(input("Дробная часть атомной массы длинее 2 символов (3 и более) - "))
atomic_mass_longer_integer_2 = check_input(input("Целая часть атомной массы длинее 2 символов (3 и более) - "))

get_answer()
