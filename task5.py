import random, openpyxl
import matplotlib.pyplot as plt

# количество координат
n = 5


# МНК и создание графика
def create_dots_and_line_on_graph(x_values: list, y_values: list):
    sum_of_x_mul_y = 0
    sum_of_x = 0
    sum_of_x_pow_two = 0
    sum_of_y = 0
    a = 0
    b = 0
    for j in range(len(x_values)):
        sum_of_x_mul_y += x_values[j] * y_values[j]
        sum_of_x += x_values[j]
        sum_of_y += y_values[j]
        sum_of_x_pow_two += x_values[j] ** 2
    # Вычисляем наш коэфф a и b
    a = (n * sum_of_x_mul_y - sum_of_x * sum_of_y) / (n * sum_of_x_pow_two - sum_of_x ** 2)
    b = (sum_of_y - a * sum_of_x) / n
    mkn_y = list()
    # Выводим график
    for j in range(len(x_values)):
        plt.scatter(x_values[j], y_values[j])
        y = a * x_values[j] + b
        mkn_y.append(y)
    plt.plot(x_values, mkn_y)
    plt.show()


# работа с библиотекой для создания excel файла
def create_excel(x_values: list, y_values: list):
    # создаем нашу рабочую область
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    iter = 0
    for i in range(1, len(x_values)):
        # записываем наши координаты в формате x y
        sheet.cell(row=i, column=1).value = x_values[iter]
        sheet.cell(row=i, column=2).value = y_values[iter]
        iter += 1
    wb.save("coordinates_table.xlsx")


if __name__ == '__main__':
    print("Введите диапазон значений координат в формате: min max ")
    coordinate_value_min, coordinate_value_max = map(float, input().split())
    x_coordinates = list()
    y_coordinates = list()
    # Заполянем наши листы коориданатами
    for i in range(n):
        x_coordinates.append(random.uniform(coordinate_value_min, coordinate_value_max))
        y_coordinates.append(random.uniform(coordinate_value_min, coordinate_value_max))
    create_excel(x_coordinates, y_coordinates)
    # test_x = [1, 2, 3, 4, 5]
    # test_y = [1.1, 3.8, 6.5, 10.2, 13.1]
    create_dots_and_line_on_graph(x_coordinates, y_coordinates)
