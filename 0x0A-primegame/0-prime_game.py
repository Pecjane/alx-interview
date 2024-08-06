#!/usr/bin/python3
"""
The prime game.
"""


def getPrimeNumbersUptoLimit(limit):
    """
    Get prime numbers in the limit range, including the limit.
    """
    isPrime = True
    primeList = []
    for number in range(2, limit + 1):
        for primeNumber in primeList:
            if number % primeNumber == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(number)
        isPrime = True
    return primeList


def isWinner(rounds, nums):
    """
    Gets a winner in a certain round.
    """
    game = nums[0: rounds]
    Maria = 0
    Ben = 0
    for number in game:
        checker = len(getPrimeNumbersUptoLimit(number))
        if checker % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria == Ben:
        return None
    return 'Maria' if Maria > Ben else 'Ben'
