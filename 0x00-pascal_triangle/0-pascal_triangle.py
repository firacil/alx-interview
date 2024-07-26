#!/usr/bin/python3
"""script to solve pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns list of list of integers representing
    the pascal triangles of a number
    """
    triangle = []

    # return (triangle if n <= 0)
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        templ = [1]
        for j in range(len(triangle[i - 1]) - 1):
            curr = triangle[i - 1]
            templ.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        templ.append(1)
        triangle.append(templ)
    # return (triangle)
    return triangle
