#!/usr/bin/env python3
"""
module for validating UTF-8
"""


def validUTF8(data):
    """
    method that determines if a given data set represents a valid
        UTF-8 encoding
    Args:
        data - a list of integers
    """
    def countLeadingOnes(byte):
        """
        Count the number of consecutive 1s in the most significant bit
        """
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    i = 0
    while i < len(data):
        num_bytes = 1

        """ Determine the number of bytes for the current character"""
        leading_ones = countLeadingOnes(data[i])
        if leading_ones == 1 or leading_ones > 4:
            return False
        elif leading_ones > 1:
            num_bytes = leading_ones

        """Check if there are enough bytes in the data"""
        if i + num_bytes > len(data):
            return False

        """Check that the following bytes start with '10'"""
        for j in range(i + 1, i + num_bytes):
            if data[j] >> 6 != 0b10:
                return False

        """Move to the next character"""
        i += num_bytes

    return True
