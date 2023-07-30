#!/usr/bin/python3
""" This is a valid UTF-8 encoding. """

def validUTF8(data):
    """
    Encode UTF-8
    """

    n_bytes = 0

    for num in data:
        bin_repr = format(num, '#010b')[-8:]
        if n_bytes == 0:
            for bit in bin_repr:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_repr[0] == '1' and bin_repr[1] == '0'):
                return False
        n_bytes -= 1

    return n_bytes == 0
