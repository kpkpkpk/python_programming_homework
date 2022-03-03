import time


def get_current_time_milliseconds():
    return round(time.time() * 1000)


def square_matrix():
    if rows == columns:
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*matrix)] for X_row in matrix]
        print("Matrix squared:")
        print_matrix(result)
    else:
        print("The matrix cannot be squared. Number of rows must be equal number of columns.")


def transpose_matrix():
    result = map(list, zip(*matrix))
    print("Matrix transposed: ")
    for r in result:
        print(r)


def get_cofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


def find_determinant(mat):
    if len(mat) == 2:
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
    my_sum = 0
    for current_column in range(len(mat)):
        sign = (-1) ** current_column
        sub_det = find_determinant(get_cofactor(mat, 0, current_column))
        my_sum += (sign * mat[0][current_column] * sub_det)
    return my_sum


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
            print("Determinant: " + str(find_determinant(matrix)))
            end_timer = get_current_time_milliseconds()
            print("Time of running: " + str((end_timer - start_timer)))
        elif option == "0":
            return
        else:
            print("Enter a number 1, 2 or 3.")


rows = 0
columns = 0
matrix = []
