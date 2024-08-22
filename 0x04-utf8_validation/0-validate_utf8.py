#!/usr/bin/python3
"""
    a method that determines if a given data set
    represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """determines if a given data set represents
    a valid UTF-8 encoding.
    """
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # convert to the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # determine the number of bytes in uft-8 char
            if (byte & mask1) == 0:
                # 1-byte char (0xxxxxxx)
                continue
            elif (byte & mask1) and (byte & mask2) == 0:
                # invalid leading byte (shoul not be 10xxxxxx)
                return False
            elif (byte & mask1) and (byte & (mask1 >> 1)):
                # 2-byte charchter (110xxxxx)
                num_bytes = 1
            elif (byte & mask1) and (byte & (mask1 >> 2)):
                # 3-byte charchter (1110xxxx)
                num_bytes = 2
            elif (byte & mask1) and (byte & (mask1 >> 3)):
                # 4-byte charcter (11110xxx)
                num_bytes = 3
            else:
                return False
        else:
            # continuation bytes (10xxxxxx)
            if not (byte & mask1) or (byte & mask2):
                return False
            num_bytes -= 1

    # if there leftover bytes to process the encoding is invalid
    return num_bytes == 0
