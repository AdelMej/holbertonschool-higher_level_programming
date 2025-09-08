#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for rows in matrix:
        cols_list = []
        for cols in rows:
            cols_list.append(cols**2)
        new_matrix.append(cols_list)

    return new_matrix
