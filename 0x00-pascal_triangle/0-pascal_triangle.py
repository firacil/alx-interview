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
    for i in range(n):
        templ = []

        for j in range(i+1):
            if j == 0 or j == 1:
                templ.append(1)
            else:
                templ.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(templ)
    # return (triangle)
    return triangle
