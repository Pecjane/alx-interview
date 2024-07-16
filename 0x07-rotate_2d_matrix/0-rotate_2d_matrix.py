#!/usr/bin/python3
"""
Has rotate_2d_matrix function.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix 90 degrees clockwise.
    Tranpose then reverse.
    """
    iterator = zip(*matrix)
    l_matrix = len(matrix[0])
    matrix.clear()
    for index in range(l_matrix):
        matrix.insert(index, list(next(iterator)))

    for index in range(len(matrix)):
        matrix[index].reverse()
