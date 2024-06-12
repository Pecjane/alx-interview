#!/usr/bin/python3
"""
Minimum operations.
"""
import math


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    The only operations allowed are 'copy all' and 'paste'.
    Note:
        If number is divisible by any number (> 1) below its square root
        then it's not prime.
    """
    if n <= 1:
        return 0

    number_of_operations = 0
    isPrime = False

    while isPrime is False:
        isPrime = True
        for number in range(2, int(math.sqrt(n)) + 1):
            if n % number == 0:
                isPrime = False
                n = n // number
                number_of_operations += number
                break
    number_of_operations += n
    return number_of_operations
