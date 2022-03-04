import openpyxl
import random


def create_excel(vals: list):
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    index = 0
    for row in range(1, int(pow(len(vals), 0.5)) + 1):
        for column in range(1, int(pow(len(vals), 0.5)) + 1):
            sheet.cell(row=row, column=column).value = vals[index]
            index += 1
    wb.save("table_nxn.xlsx")


# Full probability (sum of all probabilities) must be equal 1
# Probability calculates the following way:
# 1. Count number of unique values and theirs amount
# 2. Calculate probability of exact value
def calculate_probabilities():
    pass


if __name__ == '__main__':
    n = int(input("Enter size of table: "))
    value_min = 1
    value_max = 30
    values = list()
    for i in range(pow(n, 2)):
        values.append(random.randint(value_min, value_max))
    create_excel(values)
