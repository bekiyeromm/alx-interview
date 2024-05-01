#!/usr/bin/python3
"""
a module that determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    findfewest number of coins to get total
    Args:
        coins:- a list of coins
        tatal:- tatal coin value
    Return:
        -on success: -Minimum number of coins needed to make change
        -0: if if total <= 0
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    sum = 0
    count = 0
    for i in range(len(coins)):
        while sum < total and coins[i] <= total - sum:
            sum += coins[i]
            count += 1
            if sum == total:
                return count
    return -1
