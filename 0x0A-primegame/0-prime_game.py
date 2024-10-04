#!/usr/bin/python3
""" Modle for prime game"""


def isWinner(x, nums):
    """checks for the winner"""
    if not nums or x < 1:
        return None
    maxi = max(nums)

    my_filter = [True for _ in range(max(maxi + 1, 2))]
    for i in range(2, int(pow(maxi, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, maxi + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y
    pl1 = 0
    for x in nums:
        pl1 += my_filter[x] % 2 == 1
    if pl1 * 2 == len(nums):
        return None
    if pl1 * 2 > len(nums):
        return "Maria"
    return "Ben"
