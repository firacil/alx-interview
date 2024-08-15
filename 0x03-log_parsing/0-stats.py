#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics:
    Input format: <IP Address> - [<date>] "GET /projects/260
    HTTP/1.1" <status code> <file size> (if the format is
    not this one, the line must be skipped)

    After every 10 lines and/or a keyboard interruption
    (CTRL + C), print these statistics from the beginning:

        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        Number of lines by status code
"""

import sys

# store count of all status code in dict
stat_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
             '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0


try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # check if the stat code revieve exist in dict stat_code
            # and then increment its count
            if status_code in stat_code.keys():
                stat_code[status_code] += 1

            # update the total size
            total_size += file_size

            # update count of lines
            count += 1

        if count == 10:
            count = 0  # restart count
            print('File size: {}'.format(total_size))

            # print status code counts
            for key, val in sorted(stat_code.items()):
                if val != 0:
                    print('{}: {}'.format(key, val))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, val in sorted(stat_code.items()):
        if val != 0:
            print('{}: {}'.format(key, val))
