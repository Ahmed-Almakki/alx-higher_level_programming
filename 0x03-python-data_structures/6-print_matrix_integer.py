#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    for i in range(row):
        count = 0
        for j in matrix[i]:
            if count != len(matrix[i]) - 1:
                print(j, end=" ")
            else:
                print(j)
            count += 1
