#!/usr/bin/python3
"""module to rotate 2d matrix"""


def transpose(matrix, n):
    """_summary_"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """_summary_"""
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """_summary_"""
    n = len(matrix)
    # print(n)

    """matrix demo
    1 2 3
    4 5 6
    7 8 9
    """

    # transpose matrix
    """
    1 4 7
    2 5 8
    3 6 9
    """

    transpose(matrix, n)

    # reverse mx
    """
    7 4 1
    8 5 2
    9 6 3
    """
    reverse_matrix(matrix)

    return matrix
