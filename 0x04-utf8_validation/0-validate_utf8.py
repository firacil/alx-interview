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
        lead_mask = 1 << 7

        if num_bytes == 0:
            while lead_mask & num:
                num_bytes += 1
                lead_mask = lead_mask >> 1

            # if byte is not a multi-byte sequence,
            # move to next byte
            if num_bytes == 0:
                continue

            # if number of continuation byte is not
            # b/n 2 and 4, the sequence is invalid
            if num_bytes == 1 or num_bytes > 4:
                return False

        # if we are expecting continuation bytes
        else:
            # check that the byte starts with a "10"
            # prefix and not a "11" prefix
            if not (num & mask1 and not (num & mask2)):
                return False

        # decrement the expected number of continuation bytes
        num_bytes -= 1

    # if we have processed all bytes and are not expecting
    # another continuation bytes, sequence is valid
    if num_bytes == 0:
        return True
    else:
        return False
