#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [216]
print(validUTF8(data))
print("-----\n")

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))
print("-----\n")

data = [229, 139, 171, 256]
print(validUTF8(data))
