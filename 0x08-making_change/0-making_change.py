#!/usr/bin/python3
"""
The change making challenge using dynamic programming.
"""


def makeChange(coins, total):
    """
    Returns the minimum amount of coins needed to meet total.
    Steps:
        - Get the least coins starting from the least amount
        with the value of least coin.
        - Amount - coin = newAmount
        - is newAmount in cachedData if not then it's the 1st.
        - else least coins of newAmount plus one.
        - Do that for every coin and get the least.
    """
    # Bottom up approach.
    if total <= 0:
        return 0
    if len(coins) == 0:
        return -1
    if total < min(coins):
        return -1
    minCoinsPerTotal = {}
    for amount in range(min(coins), total+1):
        minCoinsPerTotal[amount] = total+1
        for coin in coins:
            newAmount = amount - coin
            if newAmount < 0:
                continue
            if newAmount not in minCoinsPerTotal and newAmount == 0:
                minCoinsPerTotal[amount] = 1
            elif newAmount not in minCoinsPerTotal and newAmount > 0:
                pass
            elif (minCoinsPerTotal[newAmount] + 1) < minCoinsPerTotal[amount]:
                minCoinsPerTotal[amount] = minCoinsPerTotal[newAmount] + 1
    res = -1 if minCoinsPerTotal[total] >= total+1 else minCoinsPerTotal[total]
    return res
