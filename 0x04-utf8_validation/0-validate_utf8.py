#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    1. Convert the elements in the data set to binary.
    2. Check for the first few numbers after if they are 1 or 0.
        if 0 then it's a one byte code point.
        if 10 then it's a continuation.
        if 110...
    3. In the previous check if a binary number starts with
    more than two ones then I should check the next ones
    to validate the data.
    """
    continuation_check = 0
    one_byte = True
    for num in data:
        binary_rep = f"{num:08b}"
        binary_rep = binary_rep[len(binary_rep)-8:]
        one_byte = binary_rep[0] == "0"
        two_byte = binary_rep[:3] == "110"
        three_byte = binary_rep[:4] == "1110"
        four_byte = binary_rep[:5] == "11110"
        continuation = binary_rep[:2] == "10"
        if continuation and continuation_check == 0:
            return False
        if continuation_check > 0 and not continuation:
            return False
        if one_byte:
            continuation_check = 0
        elif two_byte:
            continuation_check = 1
        elif three_byte:
            continuation_check = 2
        elif four_byte:
            continuation_check = 3
        elif continuation and continuation_check > 0:
            continuation_check -= 1
        else:
            return False
    if continuation_check > 0:
        return False
    return True
