#!/usr/bin/python3
"""calculates the fewest number of operations needed
to result in exactly n H characters in the file
"""


def minOperations(n):
    """
        method to calculate fewest operation
    """
    minim = 2
    total = 0
    while n > 1:
        while n % minim == 0:
            total += minim
            n /= minim
        minim += 1
    return total
