#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        sqr_row = []
        for element in row:
            sqr_row.append(element ** 2)
        new_matrix.append(sqr_row)
    return new_matrix
