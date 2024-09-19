#!/usr/bin/python3
"""
module for fewest number of coins solution
"""


def makeChange(coins, total):
    """ fewest number of coins needed to find total"""
    if total <= 0:
        return 0

    # sort coins in descending
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        tempo = total // coin
        change += tempo
        total -= (tempo * coin)
    if total != 0:
        return -1
    return change
