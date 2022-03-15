import openpyxl
import random

pr = 1


def create_excel_table(vals: list):
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    index = 0
    for row in range(1, int(pow(len(vals), 0.5)) + 1):
        for column in range(1, int(pow(len(vals), 0.5)) + 1):
            sheet.cell(row=row, column=column).value = vals[index]
            index += 1
    wb.save("table_nxn.xlsx")


def get_x(pair: dict):
    for x in list(pair.keys()):
        return x


def get_p(pair: dict):
    # print(f'Pair: {pair}')
    global pr
    if 1 >= pr >= 0:
        for p in list(pair.values()):
            pr -= p
            return p
    else:
        exit("ERROR - probability cannot be less 0")


# https://allcalc.ru/node/685
# https://www.matburo.ru/tvart_sub.php?p=art_mo
def find_mathematical_expectation(probability: list):
    sum_ = 0
    for index in range(len(probability)):
        x = get_x(probability[index])
        p = get_p(probability[index])
        sum_ += x * p
    print(f"Mathematical expectation is : {sum_}")
    global pr
    pr = 1
    find_dispersion(probability)


# https://allcalc.ru/node/1836
# https://www.matburo.ru/tvart_sub.php?p=art_disp
def find_dispersion(probability: list):
    sum1 = 0
    sum2 = 0
    for index in range(len(probability)):
        x = get_x(probability[index])
        p = get_p(probability[index])
        sum1 += pow(x, 2) * p
        sum2 += x * p
    result = sum1 - pow(sum2, 2)
    print(f"Dispersion is : {result}")
    global pr
    pr = 1


# Full probability (sum of all probabilities) must be equal 1
# Probability calculates the following way:
# 1. Count number of unique values and theirs amount
# 2. Calculate probability of exact value
def calculate_probabilities(vals, length: int):
    probability_1_element = 1 / length
    probability = list()
    for el in range(len(vals)):
        ks = vals[el].keys()
        vs = vals[el].values()
        for k in ks:
            for v in vs:
                p = probability_1_element * v
                probability.append({k: p})
    find_mathematical_expectation(probability)


def collector(vals: list):
    dictionary_with_count = {}
    count = 1

    for element in vals:
        if element in dictionary_with_count:
            dictionary_with_count[element] += 1
        else:
            dictionary_with_count[element] = count

    keys = list(dictionary_with_count.keys())
    values1 = list(dictionary_with_count.values())
    number_and_amounts = list()

    sum_ = 0
    for el in range(len(dictionary_with_count)):
        number_and_amounts.append({keys[el]: values1[el]})
        sum_ += values1[el]
    calculate_probabilities(number_and_amounts, sum_)


if __name__ == '__main__':
    n = int(input("Enter size of table: "))
    value_min = 1
    value_max = 30
    values_all = list()
    values_rows = list()
    for i in range(pow(n, 2)):
        values_all.append(random.randint(value_min, value_max))
        if i % 3 != 0 or i == 0:
            values_rows.append(values_all[i])
        else:
            values_rows.clear()
            values_rows.append(values_all[i])
        if len(values_rows) == 3:
            print(values_rows)
            collector(values_rows)
    print(f"Values are: {values_all}")
    create_excel_table(values_all)
