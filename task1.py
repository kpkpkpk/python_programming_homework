import MyMatrix
import MyMatrixImproved
import numpy as np
import time


def get_current_time_milliseconds():
    return round(time.time() * 1000)


def square_matrix():
    squared_matrix = np.matmul(MyMatrixImproved.matrix, MyMatrixImproved.matrix)
    # squared_matrix = np.matmul(MyMatrix.matrix, MyMatrix.matrix)
    print(squared_matrix)


def transpose_matrix():
    transposed_matrix = np.array(MyMatrix.matrix)
    transposed_matrix.transpose()
    print(transposed_matrix)


def find_determinant():
    determinant = np.linalg.det(MyMatrix.matrix)
    print(int(np.rint(determinant)))


if __name__ == "__main__":
    MyMatrixImproved.main()
    # MyMatrix.main()
    # matrix = MyMatrix.matrix
    matrix = MyMatrixImproved.matrix

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
            print("Determinant: ")
            find_determinant()
            end_timer = get_current_time_milliseconds()
            print("Time of running: " + str((end_timer - start_timer)))
        elif option == "0":
            exit(0)
        else:
            print("Enter a number 1, 2 or 3.")
