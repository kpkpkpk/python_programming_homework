import time


def get_current_time_milliseconds():
    return round(time.time() * 1000)


def square_matrix():
    result = [[0] * columns for _ in range(rows)]
    matrix2 = matrix.copy()
    if rows == columns:
        for row in range(rows):
            for column in range(columns):
                for k in range(rows):
                    result[row][column] += matrix[row][k] * matrix2[k][column]
        print("Matrix squared:")
        print_matrix(result)
    else:
        print("The matrix cannot be squared. Number of rows must be equal number of columns.")


def transpose_matrix():
    result = [[0] * rows for _ in range(columns)]
    for row in range(rows):
        for column in range(columns):
            result[column][row] = matrix[row][column]
    print("Matrix transposed:")
    print_matrix(result)


def find_determinant(m, mul):
    width = len(m)
    if width == 1:
        return mul * m[0][0]
    elif columns == rows:
        sign = -1
        answer = 0
        for el1 in range(width):
            buf = []
            for el2 in range(1, width):
                buff = []
                for k in range(width):
                    if k != el1:
                        buff.append(m[el2][k])
                buf.append(buff)
            sign *= -1
            answer = answer + mul * find_determinant(buf, sign * m[0][el1])
    else:
        return "Determinate can be found only for matrix, where number of rows equals number of columns."
    return answer


def print_matrix(m):
    for row in range(len(m)):
        for column in range(len(m[0])):
            print(m[row][column], end=" ")
        print()


def main():
    global rows
    global columns
    global matrix

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix = []
    print("Enter entries line by line:")

    for i in range(rows):
        entries_in_a_row = []
        for j in range(columns):
            entries_in_a_row.append(int(input()))
        matrix.append(entries_in_a_row)

    while True:
        print("""
Type a number of option:
1. Square matrix.
2. Transpose matrix.
3. Find determinant.
0. Exit.""")
        option = input()
        if option == "1":
            start_timer = get_current_time_milliseconds()
            square_matrix()
            end_timer = get_current_time_milliseconds()
            print("Time of running: " + str((end_timer - start_timer)))
        elif option == "2":
            start_timer = get_current_time_milliseconds()
            transpose_matrix()
            end_timer = get_current_time_milliseconds()
            print("Time of running: " + str((end_timer - start_timer)))
        elif option == "3":
            start_timer = get_current_time_milliseconds()
            print("Determinant: " + str(find_determinant(matrix, 1)))
            end_timer = get_current_time_milliseconds()
            print("Time of running: " + str((end_timer - start_timer)))
        elif option == "0":
            return
        else:
            print("Enter a number 1, 2 or 3.")


rows = 0
columns = 0
matrix = []
