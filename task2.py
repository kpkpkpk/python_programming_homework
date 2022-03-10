import random


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

    print(approximation(a))
