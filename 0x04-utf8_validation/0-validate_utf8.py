#!/usr/bin/python3
"""
UTF-8 Validation module

This module provides a function to validate whether a given list of integers
represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list): A list of integers representing bytes (0 <= integer <= 255).

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes_expected = 0

    for byte in data:
        # Validate the byte range
        if byte < 0 or byte > 255:
            return False

        # Mask to get the last 8 bits of the byte
        byte = byte & 0xFF

        if num_bytes_expected == 0:
            # Count the number of leading 1's in the byte
            if (byte >> 5) == 0b110:
                num_bytes_expected = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_expected = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_expected = 3
            elif (byte >> 7) != 0:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes_expected -= 1

    return num_bytes_expected == 0

