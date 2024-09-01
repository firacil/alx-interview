#!/usr/bin/python3
"""N queens on nxn solved"""
import sys


def solutions(row, column):
    sol = [[]]
    for queen in range(row):
        sol = place_queen(queen, column, sol)
    return sol


def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for i in range(column):
            if safe(queen, i, array):
                safe_position.append(array + [i])
    return safe_position


def safe(q, x, array):
    if x in array:
        return(False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return(n)


def n_queens():
    n = init()
    # start solutions
    my_solutions = solutions(n, n)
    # print solutions
    for array in my_solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == "__main__":
    n_queens()
