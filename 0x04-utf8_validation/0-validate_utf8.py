#!/usr/bin/python3

def validUTF8(data):
    num_bytes = 0

    for byte in data:
        if num_bytes_expected == 0:
            if (byte & 0b10000000) == 0:
                continue
            elif (byte & 0b11100000) == 0b11000000:
                num_bytes_expected = 1
            elif (byte & 0b11110000) == 0b11100000:
                num_bytes_expected = 2
            elif (byte & 0b11111000) == 0b11110000:
                num_bytes_expected = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            num_bytes_expected -= 1
    
    return num_bytes_expected == 0

