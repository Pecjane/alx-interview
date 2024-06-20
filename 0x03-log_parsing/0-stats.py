#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys
import re


def print_data(fSize, statusCodes):
    """
    Prints the data after every 10 lines or keyboard interrupt.
    """
    print(f"File size: {fSize}")
    for key, value in statusCodes.items():
        if value != 0:
            print(f"{key}: {value}")


if __name__ == "__main__":
    lines = 0
    total_file_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    regex1 = r'(\d+.){3}\d+\s?-\s?\[(\d{4}-\d{2}-\d{2} '
    regex2 = r'\d{2}:\d{2}:\d{2}.\d{6})\] '
    regex3 = r'"GET /projects/260 HTTP/1.1" \d{3} \d+'
    regex = regex1 + regex2 + regex3
    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            if not re.search(regex, line):
                continue
            lines += 1
            split_line = line.split(' ')
            file_size = int(split_line[-1])
            status_code = split_line[-2]
            total_file_size += file_size
            status_codes[status_code] += 1
            if lines % 10 == 0:
                print_data(total_file_size, status_codes)
    except KeyboardInterrupt:
        print_data(total_file_size, status_codes)
    finally:
        print_data(total_file_size, status_codes)
