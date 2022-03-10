import random
import numpy as np


def reverse(arr: list):
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        if count == 1 and (arr[i] is not None):
            x2, y2 = i, arr[i]
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            for j in range(x1, len(arr)):
                if arr[j] is None:
                    arr[j] = k * j + b
            break
        if arr[i] is not None:
            x1, y1 = i, arr[i]
            count += 1


def recover_by_correlation(row, data_values):
    deleted_value = []
    for i in range(len(row[0])):
        if row[0][i] is None:
            deleted_value.append(i)
    for i in range(len(row[1])):
        for j in deleted_value:
            if data_values[row[1][i][0][j]] is not None:
                row[0][j] = data_values[row[1][i][0][j]]
                deleted_value.remove(j)


def correlation(list_of_v: list):
    data_values = []
    while len(list_of_v) > 0:
        # создаем лист даты, чтобы хранить в нем ряд и коэффы наиб корр.рядов
        data_values.append([list_of_v.pop(), []])

    for i in range(len(data_values)):
        for j in range(len(data_values)):
            if i != j:
                data_values[i][1].append([np.corrcoef(np.array(data_values[i][0]).min(), np.array(data_values[j][0])), j])
        data_values[i][1].sort()

    for value in data_values:
        recover_by_correlation(value, data_values)
    return data_values

def approximation(array: list):
    saved_coord = list()
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    count = 0
    for i in array:
        saved_coord += i
    print(saved_coord)
    for i in range(len(saved_coord)):
        if count == 1 and (saved_coord[i] is not None):
            x2, y2 = i, saved_coord[i]
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            for j in range(x1 + 1, x2, 1):
                if saved_coord[j] is None:
                    saved_coord[j] = k * j + b
            count = 0
        if saved_coord[i] is not None:
            x1, y1 = i, saved_coord[i]
            count += 1
    print(saved_coord)
    # проходим второй раз чтобы заполнить другие ячейки
    for i in range(len(saved_coord)):
        if count == 1 and (saved_coord[i] is not None):
            x2, y2 = i, saved_coord[i]
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
            for j in range(x1, -1, -1):
                if saved_coord[j] is None:
                    saved_coord[j] = k * j + b
            break
        if saved_coord[i] is not None:
            x1, y1 = i, saved_coord[i]
            count += 1
    # проходим третий чтобы восстановить конец
    reverse(saved_coord)
    return saved_coord


if __name__ == '__main__':
    n = int(input())
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(1, 30)
    count = 0
    while count != 10:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        if a[i][j] is not None:
            a[i][j] = None
            count += 1
    print(correlation(a))
    # print(approximation(a))
